from django.db import models

class Project(models.Model):
    STATUS_CHOICES = [
        ('Planning', 'Planning'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
