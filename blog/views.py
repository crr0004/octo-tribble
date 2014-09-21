from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import HttpResponse, HttpReponseRedirect

from blog.models import *

# Create your views here.
def index(request):
	return HttpResponse("Hello world! :D. You're at the index")

def view(request, post_id):
	return HttpResponse("Hello! :). You're viewing " + post_id)