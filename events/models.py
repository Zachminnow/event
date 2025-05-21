from django.db import models
from django.utils import timezone


# Create your models here.
class EventModel(models.Model):
    title = models.CharField(max_length=50)
    host = models.CharField(max_length=50)
    guest = models.CharField(max_length=50)
    description = models.TextField()
    venue = models.CharField(max_length=50)
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return self.title


class EventBook(models.Model):
    event = models.ForeignKey(EventModel, on_delete=models.CASCADE,
                              related_name='bookings', null=True)

    GENDER_CHOICES = [
        ('female', "Female"),
        ('male', "Male"),
        ('other', 'Other'),
    ]

    TICKET_CHOICES = [
        ('VVIP', 'VVIP'),
        ('VIP', 'VIP'),
        ('REGULAR', 'REGULAR'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    ticket_category = models.CharField(max_length=10, choices=TICKET_CHOICES)

    def __str__(self):
        return f"{self.last_name} - {self.event.title}"
