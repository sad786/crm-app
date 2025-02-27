from django.db import models

# Create your models here.

from django.db import models

class Customer(models.Model):
    """
    Represents a customer in the CRM system.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Interaction(models.Model):
    """
    Represents an interaction with a customer (e.g., a call, meeting, or email).
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=50, choices=[
        ('phone', 'Phone Call'),
        ('email', 'Email'),
        ('meeting', 'In-Person Meeting'),
    ])
    notes = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.interaction_type} with {self.customer.name} on {self.date}"

class Note(models.Model):
    """
    Represents a note about a customer.
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Note for {self.customer.name} on {self.created_at}"
