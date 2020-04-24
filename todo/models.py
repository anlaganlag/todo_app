from django.db import models

class TodoItem(models.Model):
    content =models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    last_edit=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.content


class BinItem(models.Model):
    content =models.TextField()
    delete_time=models.DateTimeField()
    def __str__(self):
        return self.content

class DoneItem(models.Model):
    content =models.TextField()
    done_time=models.DateTimeField()
    def __str__(self):
        return self.content


