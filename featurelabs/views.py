from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponseForbidden, Http404
from django.template import RequestContext
from django.utils.translation import ugettext, ugettext_lazy as _


from featureflipper.models import Feature


def index(request, *args, **kw):
    template_name = 'featurelabs/index.html'
    feature_list = [
        (feature, {
            'site': feature.enabled,
            'session': request.features[feature.name],
        })
        for feature in Feature.objects.all()
    ]
    template_context = {
        'feature_list': feature_list,
    }
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request),
    )