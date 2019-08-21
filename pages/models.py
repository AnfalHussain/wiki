from django.db import models
from datatime import datatime

class Page(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	last_update = models.DateField(auto_now=True)

	def get_absolute_url(self):
		from django.urls import reverse
		return reverse('page-detail', args=[str(self.id)])
		# ("/pages/detail/%i/" % self.id)



