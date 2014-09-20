from django.db import models

# Create your models here.
class Abstract(models.Model):
	body = models.TextField()

class Draft(models.Model):
	pass

class Paragraph(models.Model):
	title = models.CharField(max_length=400)
	body = models.TextField()
	post = models.ForeignKey('Post', blank=True, null=True)

class Post(models.Model):
	title = models.CharField(max_length=400)
	abstract = models.ForeignKey('Abstract')
	footer = models.TextField()
	date = models.DateTimeField()
	author = models.CharField(max_length=200)
	draft = models.ForeignKey('Draft', blank=True, null=True)

class Published(models.Model):
	post = models.ForeignKey('Post')

class Tag(models.Model):
	name = models.CharField(max_length=200)
	alias = models.ManyToManyField('self', blank=True, null=True)