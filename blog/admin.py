from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Post)
admin.site.register(Abstract)
admin.site.register(Draft)
admin.site.register(Published)
admin.site.register(Tag)