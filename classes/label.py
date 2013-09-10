import os
import subprocess
import threading
import tempfile
from datetime import datetime
from string import Template

from lab_barcode.models import ZplTemplate, LabelPrinter
from lab_barcode.exceptions import PrinterException


class Label(object):

    """ Prints a label based on a template and it's context.

    Call with kwargs or override prepare_label_context() before printing.
    If you override prepare_label_context(), you do not need
    to explicitly call it."""

    def __init__(self, *args, **kwargs):

        self.message = ''
        self.process = None
        self.printer_error = False
        self.file_name = None
        self.zpl_template = None
        self.label_printer = None
        self.label_count = 0
        self.label_count_total = 0
        self.barcode_value = '123456789'
        self.is_prepared = False
        self.label_context = {}
        self.default_template_string = ('^XA\n'
                '^FO325,5^A0N,15,20^FD${label_count}/${label_count_total}^FS\n'
                '^FO320,20^BY1,3.0^BCN,50,N,N,N\n'
                '^BY^FD${barcode_value}^FS\n'
                '^FO320,80^A0N,15,20^FD${barcode_value}^FS\n'
                '^FO325,152^A0N,20^FD${timestamp}^FS\n'
                '^XZ')

    def prepare_label_context(self, **kwargs):
        """ Users should override to define a label context that matches the template. """
        if kwargs:
            self.label_context.update(**kwargs)
        if not self.label_context:
            # set a default context
            self.label_context = {'barcode_value': self.barcode_value, }

    def prepare_label_template(self, template):
        """ Users may override to define the template. """
        if not self.zpl_template:
            self._set_label_template(template)
        return self.zpl_template

    def update_label_context(self, **kwargs):
        self.label_context.update(**kwargs)

    def print_label(self, remote_addr='127.0.0.1',
                    copies=None, label_value=None):
        """ Prints the label or throws an exception if the printer is not found. """
        print_success = False
        if not copies:
            copies = 1
        if self._set_label_printer(remote_addr):
            self.label_count_total = copies
            # reverse order so labels are in order top to bottom on a strip
            for i in range(copies, 0, -1):
                self.label_count = i
                self._prepare_label()
                if self._label_to_file():
                    # wrap the lpr process in a thread to allow for a timeout if printer not found.
                    # http://stackoverflow.com/questions/1191374/subprocess-with-timeout
                    timeout = 5
                    thread = threading.Thread(target=self._lpr)
                    thread.start()
                    thread.join(timeout)
                    if thread.is_alive():
                        self.process.terminate()
                        thread.join()
                    if self.process.returncode < 0:
                        # process timed out so throw an exception
                        self.message = ('Unable to connect to printer '
                                        '{0} ({1}){2}.'.format(unicode(self.label_printer),
                                                            self.process.returncode,remote_addr))
                        raise PrinterException(self.message)
                    else:
                        self.message = ('Successfully printed label \'{0}\' {1}/{2} to '
                                        '{3} from {4}'.format(label_value, (copies - i + 1), copies,
                                                     self.label_printer.cups_printer_name, remote_addr))
                    print_success = True
        return (self.message, print_success)

    def _lpr(self):
        """ Callback to run lpr in a thread. """
        self.process = subprocess.Popen(['lpr', '-P', self.label_printer.cups_printer_name, '-l',
                                        self.file_name, '-H', self.label_printer.cups_server_ip],
                                        shell=False)
        self.process.communicate()

    def get_template_prep(self):
        """ Gets or creates a label instance and returns it.

        Users may override, otherwise the `default` is returned
        from :method:`_set_label_template()`."""

        return None

    def _prepare_label(self):
        if not self.zpl_template:
            self._set_label_template(self.get_template_prep())
        if not self.label_context:
            self.prepare_label_context()
        self.label_context.update({'label_count': self.label_count,
                                   'label_count_total': self.label_count_total,
                                   'timestamp': datetime.today().strftime('%Y-%m-%d %H:%M')})

    def _set_label_template(self, template=None):
        """ Set zpl_template with a zpl_template name or an instance of ZplTemplate
        otherwise return the default template. """
        # use either the template name or the template instance
        if isinstance(template, ZplTemplate):
            self.zpl_template = template
        elif isinstance(template, basestring):
            zpl_templates = ZplTemplate.objects.filter(name=template)
            if zpl_templates:
                self.zpl_template = zpl_templates[0]
            else:
                raise ValueError('ZPL template \'%s\' does not exist. ' % template)
        else:
            # got neither template name nor a template objects but,
            # maybe one of the templates is flagged as default
            try:
                self.zpl_template = ZplTemplate.objects.get(default=True)
            except:
                # ... guess not
                raise ValueError('No valid zpl_template or zpl_template.name '
                                 'specified and a default template does not exist. '
                                 'Cannot continue.')

    def _label_to_file(self):
        """ Write the formatted label to a text file for the printer """
        self.file_name = None
        if self._format_label():
            try:
                tup = tempfile.mkstemp()
                self.file_name = tup[1]
                my_file = os.fdopen(tup[0], "w")
                my_file.write(self.formatted_label)
                my_file.close()
            except:
                self.message = ('Cannot print label. Unable to create/open temporary '
                                'file {0}.'.format(self.file_name))
                self.file_name = None
        return self.file_name

    def _set_label_printer(self, remote_addr):
        """ Set the label printer by remote_addr or default"""
        if LabelPrinter.objects.filter(client__ip=remote_addr):
            self.label_printer = LabelPrinter.objects.get(client__ip=remote_addr)
        if not self.label_printer:
            if LabelPrinter.objects.filter(default=True):
                self.label_printer = LabelPrinter.objects.get(default=True)
            # TODO(erikvw): ask cups/system for default printer
            else:
                self.message = ('Unable to determine the label printer for client {0}. '
                                'Set at one printer as the default printer. '
                                'See model LabelPrinter.'.format(remote_addr))
        return self.label_printer

    def _format_label(self):
        """ Format label with label context. """
        self.formatted_label = None
        if not self.zpl_template:
            self.message = ('Cannot print label. Formatted label has not been defined. '
                            'See model ZplTemplate.')
        else:
            if not self.label_context:
                raise TypeError('Cannot format label for printing. Label context not set. '
                                'Call prepare_label_context() first.')
            # convert old templates
            self.zpl_template.template = self.zpl_template.template.replace('%(', '${').replace(')s', '}')
            self.zpl_template.save()
            # safe_substitue
            self.formatted_label = self.zpl_template.template
            self.formatted_label = Template(self.zpl_template.template)
            self.formatted_label = self.formatted_label.safe_substitute(self.label_context)
        return self.formatted_label
