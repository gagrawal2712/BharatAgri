from django.db import models
from datetime import datetime

class Crop(models.Model):
    name = models.CharField(max_length=255, null=False)
    feature1 = models.CharField(max_length=255)
    feature2 = models.BooleanField()
    feature3 = models.DecimalField(max_digits=19, decimal_places=10, null=False)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = 'crop'

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = datetime.now()
        self.updated_at = datetime.now()
        return super(Categories, self).save(*args, **kwargs)
