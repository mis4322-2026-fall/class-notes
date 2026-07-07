from django.db import models


class Customer(models.Model):
    customer_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.customer_code} - {self.name}"


class Project(models.Model):
    project_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=120)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="open")

    def __str__(self):
        return f"{self.project_code} - {self.name}"


class WorkItem(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    owner = models.CharField(max_length=80)
    is_done = models.BooleanField(default=False)
