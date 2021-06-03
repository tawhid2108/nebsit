from django.db import models

class Client(models.Model):
    fullName = models.CharField('Full name',max_length=50)
    email = models.EmailField('Email address')
    phone = models.CharField('Phone number', max_length=20)
    message = models.TextField()

    def __str__(self):
        return self.fullName