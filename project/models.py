from django.db import models
from user.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    target = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    # donators = models.ManyToManyField(User, through='Donation')

    def __str__(self):
        return self.title


class Tag(models.Model):
    # project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.CharField(max_length=10)
    project = models.ManyToManyField(Project)

    def __str__(self):
        return self.tag


class Pic(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    # project = models.ManyToOneRel(Project,on_delete=models.CASCADE)
    pic = models.ImageField()

    def __str__(self):
        return self.pic


class Donation(models.Model):
    donator = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.amount


class Rate(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rate = models.IntegerField()

    def __str__(self):
        return self.rate


class ProjectReport(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    reporter = models.ForeignKey(User, on_delete=models.CASCADE)
    msg = models.CharField(max_length=100)

    def __str__(self):
        return self.msg
