from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    address = models.TextField()
    phone = models.CharField(max_length=15)
    course = models.CharField(max_length=50, choices=[
        ('1', 'Basic (200,000 Naira)'),
        ('2', 'Intensive (300,000 Naira)'),
        ('3', 'Advanced (400,000 Naira)')
    ])
    mode_of_study = models.CharField(max_length=10, choices=[('Weekday', 'Weekday'), ('Weekend', 'Weekend')])
    gender = models.CharField(max_length=20, choices=[('Male', 'Male'), ('Female', 'Female'), ('Prefer not to say', 'Prefer not to say')])
    shirt_size = models.CharField(max_length=5, choices=[('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')])
    agree = models.BooleanField(default=False)
    date_registered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"
