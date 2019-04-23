from django.db import models
from project.models import Project
from user.models import User


# Create your models here.

class Comment(models.Model):
    comment_body = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parent = models.ForeignKey("self", on_delete=models.CASCADE)


class CommentReport(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=100)
