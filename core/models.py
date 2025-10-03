from django.db import models
from django.contrib.auth.models import User



class Gift(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='gifts/', blank=True, null=True)
    is_reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Presente'
        verbose_name_plural = 'Presentes'


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)
    reserved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} reservou {self.gift.name}"
    
    class Meta:
        verbose_name = 'Reserva'
        verbose_name_plural = 'Reservas'


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=150)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
