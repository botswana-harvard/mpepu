from datetime import datetime

from django.contrib import messages

from lab_barcode.models import ZplTemplate
from label import Label


class ModelLabel(Label):
    """ Print a label building the template and context from the model."""
    def print_label(self, request, instance, copies=None, label_value=None):
        self.prepare_label_context(instance=instance)
        if not copies:
            copies = 1
            for field in instance._meta.fields:
                if field.attname == copies:
                    copies = instance.copies
                    break
        msg, success = super(ModelLabel, self).print_label(request.META.get('REMOTE_ADDR'),
                                                           copies,
                                                           label_value)
        if not success:
            messages.add_message(request, messages.ERROR, msg)
        else:
            messages.add_message(request, messages.SUCCESS, msg)

    def prepare_label_context(self, **kwargs):
        """ Add all the model fields to the template context.

        Users may override to set a label context that matches the template. """
        instance = kwargs.get('instance')
        for field in instance._meta.fields:
            if isinstance(getattr(instance, field.attname, field.attname), datetime):
                timestamp = getattr(instance, field.attname, field.attname).strftime('%Y-%m-%d %H:%M')
                self.label_context.update({field.attname: timestamp})
            else:
                self.label_context.update({field.attname: getattr(instance, field.attname, field.attname)})
        self.label_context.update({'barcode_value': instance.barcode_value()})
        self.is_prepared = True
        return self.label_context

    def get_template_prep(self):
        """Users may override."""
        try:
            template = ZplTemplate.objects.get(default=True)
        except:
            template = ZplTemplate()
            template.name = template
            template.default = True
            template.template = ('^XA\n'
                '^FO325,5^A0N,15,20^FD${item_count}/${item_count_total}^FS\n'
                '^FO320,20^BY1,3.0^BCN,50,N,N,N\n'
                '^BY^FD${barcode_value}^FS\n'
                '^FO320,80^A0N,15,20^FD${barcode_value}^FS\n'
                '^FO325,100^A0N,15,20^FD${panel} ${aliquot_type}^FS\n'
                '^FO325,152^A0N,20^FD${user_created}^FS\n'
                '^FO325,152^A0N,20^FD${created}^FS\n'
                '^XZ')

            """^XA
                ^FO325,15^A0N,15,20^FDBHHRL^FS
                '^FO310,30^BY2,3^BCN,75,N,N,N\n'
                ^BY^FD${barcode_value}^FS
                ^FO320,110^A0N,15,20^FD${barcode_value}^FS
                ^FO325,130^A0N,15,20^FDCD4^FS
                ^FO325,150^A0N,20^FD${created}^FS
                ^XZ"""
            template.save()
        return template
