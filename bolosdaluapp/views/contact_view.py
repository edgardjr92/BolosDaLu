__author__ = 'Edgard JR'
from django.template import RequestContext
from django.shortcuts import render_to_response


def init(request):
    return render_to_response('contact.html',RequestContext(request))