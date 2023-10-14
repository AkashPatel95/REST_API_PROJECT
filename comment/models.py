from django.db import models

class Comment(models.Model):
    postId = models.IntegerField(default=0)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default='')
    email = models.EmailField(default='')
    body = models.TextField()

    def __str__(self):
        return self.name
