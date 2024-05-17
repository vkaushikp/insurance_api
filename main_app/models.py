from django.db import models

# Create your models here.
class Project(models.Model):
    organization = models.CharField(max_length=100)
    github = models.CharField(max_length=100)
    repo = models.CharField(max_length=100)
    app = models.ForeignKey('App', on_delete=models.CASCADE)
    plan = models.ForeignKey('Plan', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class App(models.Model):
    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    framework = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Plan(models.Model):
    plan_type = models.CharField(max_length=100)
    storage = models.CharField(max_length=20)
    bandwidth = models.CharField(max_length=20)
    memory = models.CharField(max_length=20)
    cpu = models.CharField(max_length=20)
    monthly_cost = models.CharField(max_length=20)
    hourly_cost = models.CharField(max_length=20)
    database_type = models.CharField(max_length=20, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

