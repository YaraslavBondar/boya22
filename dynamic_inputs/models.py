from django.db import models
from django.urls import reverse


class DynamicInputsDatas(models.Model):
    
    data = models.JSONField()

    def get_absolute_url(self):
        return reverse('concrete', kwargs={'id': self.id})
