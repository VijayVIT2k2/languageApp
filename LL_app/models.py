from django.db import models

# Create your models here.
class ChatMessage(models.Model):
    content = models.TextField()

    def __str__(self):
        return str(self.content)