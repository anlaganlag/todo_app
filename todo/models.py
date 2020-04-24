from django.db import models

class TodoItem(models.Model):
    content =models.TextField()
    def __str__(self):
        return self.content


class BinItem(models.Model):
    content =models.TextField()
    delete_time=models.DateTimeField()
    def __str__(self):
        return self.content


