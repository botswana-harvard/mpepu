from django.conf import settings
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required


@login_required
def index(request):

    warnings = {}

    return render_to_response('index.html', {
        'warnings': warnings,
        'comment': "",
        'warnings': warnings,
        'database': settings.DATABASES,
        'app_name': settings.APP_NAME,
    }, context_instance=RequestContext(request))
