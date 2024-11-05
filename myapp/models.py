# models.py
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    mobile1 = models.CharField(max_length=15, blank=True)
    noofpeople = models.IntegerField()
    oldorinf = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.user.username


from django.db import models

class UserMessage(models.Model):
    from_number = models.CharField(max_length=20)  # Store the sender's phone number
    to_number = models.CharField(max_length=20)  # Store the recipient's phone number
    body = models.TextField()  # Store the content of the message
    date_received = models.DateTimeField(auto_now_add=True)  # Store the timestamp of when the message was received

    def __str__(self):
        return f"Message from {self.from_number} at {self.date_received}: {self.body}"

# models.py
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

# models.py
from django.db import models
from django.contrib.auth.models import User

class MedicalPurpose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)  # Ensure this line is present
    address = models.TextField(null=True)  # Allow null values if desired
    purpose = models.CharField(max_length=255, default="Medical Purpose")

    def __str__(self):
        return f"{self.username} - {self.purpose}"
    
class FoodPurpose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)  # Ensure this line is present
    address = models.TextField(null=True)  # Allow null values if desired
    purpose = models.CharField(max_length=255, default="Food Purpose")

    def __str__(self):
        return f"{self.username} - {self.purpose}"
    

class ImmediatePurpose(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)  # Ensure this line is present
    address = models.TextField(null=True)  # Allow null values if desired
    purpose = models.CharField(max_length=255, default="Immediate Purpose")

    def __str__(self):
        return f"{self.username} - {self.purpose}"
from django.db import models



class FailMsg(models.Model):
    name = models.CharField(max_length=100)  # Store the user's name
    phone = models.CharField(max_length=15)  # Store the failed phone number
    error_message = models.TextField()  # Store the error message returned from the Twilio API
    address = models.CharField(max_length=255, blank=True, null=True)  # Store the address (optional)
    timestamp = models.DateTimeField(auto_now_add=True)  # Store when the failure happened

    def __str__(self):
        return f"Failed to send to {self.name} ({self.phone}) at {self.address}: {self.error_message}"
