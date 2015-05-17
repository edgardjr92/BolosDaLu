from django.template import RequestContext

__author__ = 'Edgard JR'
from django.shortcuts import render, render_to_response


def init(request):
    return render_to_response('about.html',RequestContext(request))