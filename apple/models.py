from django.db import models


class dept(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=20)


class workers(models.Model):
    def __str__(self):
        return self.name
    dept = models.ForeignKey(dept)
    name = models.TextField()
    birthday = models.DateTimeField()
    boss = models.CharField(max_length=20)
