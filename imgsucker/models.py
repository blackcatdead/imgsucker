from __future__ import unicode_literals

from django.db import models
from django.contrib.humanize.templatetags.humanize import naturalday, naturaltime
from django.utils import timezone
from datetime import datetime, timedelta

class Resolution(models.Model):
	id_resolution= models.AutoField(primary_key=True)
	resolution= models.CharField(max_length=100, null=False, default=None)

	ct= (
        (0, 'Desktop'),
        (1, 'Mobile'),
    )
	category= models.IntegerField(choices=ct, null=False, default=1)
	w= models.IntegerField(null=False, default=0)
	h= models.IntegerField(null=False, default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return '('+str(self.w)+'x'+str(self.h)+') - '+self.ct[self.category][1]+' - '+self.resolution



class Wallpaper(models.Model):
	id_wallpaper= models.AutoField(primary_key=True)
	wallpaper= models.ImageField(blank=True, null=True, upload_to='wallpaper')
	resolution= models.ForeignKey(Resolution, on_delete=models.SET_NULL,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	source = models.CharField(max_length=500, null=False, default=None)
	colors = models.CharField(max_length=100, null=False, default=None)
	uploader = models.CharField(max_length=100, null=False, default=None)
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)

	def __str__(self):
		return self.id_wallpaper

class Wallpaper_resoultion(models.Model):
	wallpaper= models.ForeignKey(Wallpaper, on_delete=models.SET_NULL,null=True)
	resolution= models.ForeignKey(Resolution, on_delete=models.SET_NULL,null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	st= (
        (0, 'Deactive'),
        (1, 'Active'),
    )
	status= models.IntegerField(choices=st, null=False, default=1)

class Tag(models.Model):
	id_tag= models.AutoField(primary_key=True)
	# sekolah= models.ForeignKey(Sekolah, on_delete=models.SET_NULL,null=True)
	tag= models.CharField(max_length=100, null=False, default=None)
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag

class Wallpaper_tag(models.Model):
	wallpaper= models.ForeignKey(Wallpaper, on_delete=models.SET_NULL,null=True)
	tag= models.ForeignKey(Tag, on_delete=models.SET_NULL,null=True)
