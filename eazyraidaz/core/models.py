from django.db import models


class RiderApplication(models.Model):
    full_name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    location = models.CharField(max_length=200)
    has_license = models.BooleanField(default=False)
    has_smartphone = models.BooleanField(default=False)
    has_motorbike = models.BooleanField(default=False)
    message = models.TextField(blank=True)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')],
        default='pending'
    )

    def __str__(self):
        return f"{self.full_name} - {self.phone}"

    class Meta:
        ordering = ['-applied_at']
        verbose_name = 'Rider Application'
        verbose_name_plural = 'Rider Applications'


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"

    class Meta:
        ordering = ['-sent_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
