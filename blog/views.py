from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.views import generic
from django.http import *

from blog.models import *

# Create your views here.
def index(request):
	return render(request, 'blog/index.html', {"h": "<b>h"})

def view(request, post_id):
	return HttpResponse("Hello! :). You're viewing " + post_id)