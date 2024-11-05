

from django.contrib.auth import logout
from django.shortcuts import render,redirect
from .forms import SignupForm
from twilio.rest import Client
from django.conf import settings
from django.contrib.auth.models import User
def index(request):
    return render(request,"myapp/index.html")

def disaster_management(request):
    return render(request,"myapp/disaster.html")

def home(request):
    return render(request,"myapp/home.html")


def aboutus(request):
    return render(request,"myapp/aboutus.html")

def medical(request):
    return render(request,"myapp/medical.html")
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import SignupForm
from .models import UserProfile

from django.db import IntegrityError

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)

        if form.is_valid():
            user = form.save()

            # Capture cleaned data
            mobile = form.cleaned_data.get('mobile')
            mobile1 = form.cleaned_data.get('mobile1')
            noofpeople = form.cleaned_data.get('noofpeople')  # Capture noofpeople
            oldorinf = form.cleaned_data.get('oldorinf')
            address = form.cleaned_data.get('address')

            try:
                # Ensure unique UserProfile by using get_or_create
                UserProfile.objects.get_or_create(
                    user=user,
                    defaults={
                        'mobile': mobile,
                        'mobile1': mobile1,
                        'noofpeople': noofpeople or 0,  # Default to 0 if not provided
                        'oldorinf': oldorinf,
                        'address': address
                    }
                )

                # Log the user in
                login(request, user)
                return redirect("/")  # Redirect after signup
            except IntegrityError:
                # Handle the error here if the profile creation fails
                form.add_error(None, "User profile already exists or another error occurred.")
    else:
        form = SignupForm()

    return render(request, "myapp/signup.html", {
        "form": form
    })


def logout_view(request):
    logout(request)
    return redirect('/')  # Redirect to the homepage or another page after logout
# your_app/views.py
# your_app/views.py
from django.http import JsonResponse
from .models import UserProfile  # Ensure you import your UserProfile model
import requests
from requests.auth import HTTPBasicAuth

from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
import requests
from .models import FailMsg, UserProfile  # Import the FailMsg model

from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
import requests
from .models import FailMsg, UserProfile  # Import the FailMsg and UserProfile models

from django.http import JsonResponse
from requests.auth import HTTPBasicAuth
import requests
from .models import FailMsg, UserProfile  # Import the FailMsg and UserProfile models

def send_sms(request):
    # Twilio API credentials
    url = 'https://api.twilio.com/2010-04-01/Accounts/AC2ed487a768d2c36b03af48404149dc1c/Messages.json'
    auth = HTTPBasicAuth('AC2ed487a768d2c36b03af48404149dc1c', '2abb7fc620caeeeadd8306445dd174e1')

    message_body = "This is an emergency alert message."  # SMS message to send

    # Get all user profiles
    users = UserProfile.objects.all()
    print(f"Users found: {users.count()}")  # Debugging line

    successful_numbers = []
    failed_numbers = []

    for user_profile in users:
        to_number = user_profile.mobile  # User's primary mobile number
        user_name = user_profile.user.username  # Get the username from the related User model
        address = user_profile.address

        data = {
            'To': to_number,
            'From': '+12092990743',  # Your Twilio number
            'Body': message_body
        }

        response = requests.post(url, auth=auth, data=data)

        if response.status_code == 201:
            successful_numbers.append(to_number)
        else:
            error_message = response.json().get('message', 'Unknown error')
            failed_numbers.append({
                'phone': to_number,
                'name': user_name,
                'address': address,
                'error': error_message
            })

            # Save the failed message to the FailMsg table
            FailMsg.objects.create(
                name=user_name,
                phone=to_number,
                address=address,
                error_message=error_message
            )

    return JsonResponse({
        'status': 'complete',
        'success_count': len(successful_numbers),
        'failed_count': len(failed_numbers),
        'failed_numbers': failed_numbers,
    })

from django.http import JsonResponse
from .models import UserProfile  # Import your UserProfile model

def check_phone_numbers(request):
    users = UserProfile.objects.all()  # Get all user profiles
    phone_numbers = [user.mobile for user in users]  # Create a list of phone numbers

    return JsonResponse({
        'phone_numbers': phone_numbers,
        'count': len(phone_numbers),
    })



# views.py
# views.py
from django.shortcuts import render, redirect
from .models import MedicalPurpose, UserProfile,FoodPurpose,ImmediatePurpose

# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import MedicalPurpose, UserProfile

def medical_purpose_view(request):
    if request.method == "POST":
        # Fetch the user's profile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Get the address from the user's profile
        address = user_profile.address

        # Store the user's medical purpose interaction
        MedicalPurpose.objects.create(
            user=request.user,
            username=request.user.username,  # Use the username from the User model
            address=address,  # Use the address fetched from the user's profile
            purpose="Medical Purpose"
        )
        # Redirect after storing the data
        return redirect('/')  # Redirect to a thank you page or wherever you want

    return render(request, 'myapp/medical.html')

def food_purpose_view(request):
    if request.method == "POST":
        # Fetch the user's profile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Get the address from the user's profile
        address = user_profile.address

        # Store the user's medical purpose interaction
        FoodPurpose.objects.create(
            user=request.user,
            username=request.user.username,  # Use the username from the User model
            address=address,  # Use the address fetched from the user's profile
            purpose="Food Purpose"
        )
        # Redirect after storing the data
        return redirect('/')  # Redirect to a thank you page or wherever you want

    return render(request, 'myapp/food.html')

def immediate_purpose_view(request):
    if request.method == "POST":
        # Fetch the user's profile
        user_profile = get_object_or_404(UserProfile, user=request.user)

        # Get the address from the user's profile
        address = user_profile.address

        # Store the user's medical purpose interaction
        ImmediatePurpose.objects.create(
            user=request.user,
            username=request.user.username,  
            address=address,  
            purpose="Immediate Rescue Purpose"
        )
        # Redirect after storing the data
        return redirect('/')  # Redirect to a thank you page or wherever you want

    return render(request, 'myapp/immediate.html')


# views.py
from django.shortcuts import render
from .models import MedicalPurpose

def medical_purpose_list_view(request):
    # Query all records from the MedicalPurpose table
    medical_purposes = MedicalPurpose.objects.all()

    # Pass the data to the template
    return render(request, 'myapp/medicaltable.html', {
        'medical_purposes': medical_purposes
    })

def food_purpose_list_view(request):

    food_purposes = FoodPurpose.objects.all()

    # Pass the data to the template
    return render(request, 'myapp/foodtable.html', {
        'food_purposes': food_purposes
    })

def immediate_purpose_list_view(request):

    Immediate_purposes = ImmediatePurpose.objects.all()

    # Pass the data to the template
    return render(request, 'myapp/immediatetable.html', {
        'Immediate_purposes': Immediate_purposes
    })

def failmsg_list_view(request):

    msgs = FailMsg.objects.all()

    # Pass the data to the template
    return render(request, 'myapp/msgfailtable.html', {
        'msgs': msgs
    })



