from django.db import models


class Remark(models.Model):
    name = models.CharField(max_length=100)
    text = models.TextField(blank=False)  # the field cannot be blank

    def __str__(self):
        return self.name
