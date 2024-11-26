import uuid

from django.db import models

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    company_name = models.CharField(max_length=255)
    position = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.phone_number

class Event(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    location = models.TextField()
    custom_link = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Report(models.Model):
    event = models.ForeignKey(Event, on_delete=models.SET_NULL, null=True)
    total_registrations = models.IntegerField(default=0)
    total_check_in = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qr_code = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.event.name + " " + self.user.name

class CheckIn(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.SET_NULL, null=True)
    check_in_time = models.DateTimeField()
    device = models.CharField(max_length=255)

class NameTag(models.Model):
    registration = models.ForeignKey(Registration, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.registration.user

class Email(models.Model):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

class SentMail(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE)
    registration = models.ForeignKey(Registration, on_delete=models.SET_NULL, null=True)
    sent_at = models.DateTimeField(auto_now_add=True)

    class STATUS(models.TextChoices):
        SENDING = 'SENDING',
        SENT = 'SENT',
        RECEIVED = 'RECEIVED',
        PENDING = 'PENDING',
        ERROR = 'ERROR',

    status = models.CharField(
        max_length=20,
        choices=STATUS.choices,
        default=STATUS.SENDING,
    )