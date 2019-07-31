from django.db import models

class Comment(models.Model):
    text = models.TextField()
    created = models.DateTimeField('date published', null=True)

    def __str__(self):
        return self.text