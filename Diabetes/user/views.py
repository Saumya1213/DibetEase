from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import get_object_or_404


from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

import pickle
import numpy as np

from .models import *
from .forms import CreateUserForm
from .forms import CredUpdateForm
from .forms import AddHealthData




login_required(login_url='login')
def prediction(request):
    return render(request,'user/prediction.html')


login_required(login_url='login')
def result(request):
    loaded_model = pickle.load(open('user/saved_models/diabetes_model.sav', 'rb'))
    
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])
    val8 = float(request.GET['n8'])
    
    user_input = [val1,val2,val3,val4,val5,val6,val7,val8]
    
    prediction = loaded_model.predict([user_input])

    result1 = ""
    if prediction==[0]:
        result1 = "Negative"
    else:
        result1 = "Positive"
        
    glucose_level = user_input[1]  
    current_user = request.user
    health_data = HealthData(user=current_user, glucose_level=glucose_level, timestamp=timezone.now())
    health_data.save()
    
    return render(request,'user/prediction.html',{"result2":result1})


def signup(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account Created Successfully for '+user)
                return redirect('login')
                
        context = {'form':form}
        return render(request,'user/signup.html', context)
    


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('dashboard')
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.info(request,'Username OR Password is incorrect')
            
        context = {}
        return render(request, 'user/login.html',context)



def logoutUser(request):
    logout(request)
    return redirect('login')


login_required(login_url='login')
def history(request):
    current_user = request.user
    history_data = HealthData.objects.filter(user=current_user).order_by('-timestamp')
    context = {'history': history_data}
    return render(request, 'user/history.html', context)


login_required(login_url='login')
def dashboard(request, updated_info=None):
    user = request.user
    info_obj = Info.objects.get(user=user)  # Get the latest info object for the user
    context = {'user': user, 'updated_info': info_obj}
    return render(request, 'user/dashboard.html', context)
    


login_required(login_url='login')
def edit(request):
    user = request.user
    try:
        info_obj = Info.objects.get(user=user)  # Get the Info object for the user
        cred_form = CredUpdateForm(instance=info_obj)  # Initialize form with existing data
    except Info.DoesNotExist:
    # Handle case where no Info object exists (create a new one?)
        messages.warning(request, 'No user information found. Please try again.')
        cred_form = CredUpdateForm()  # Create an empty form in case of exception

    
    if request.method == 'POST':
        cred_form = CredUpdateForm(request.POST, instance=info_obj)

        if cred_form.is_valid():
            cred_form.save()
            messages.success(request, 'User information updated successfully for ' + cred_form.cleaned_data.get('name'))
            return redirect('dashboard_with_info', updated_info=info_obj)
            
    context = {'cred_form':cred_form}
    return render(request,'user/edit.html', context)


def home(request):
    return render(request, 'user/home.html') 
# Create your views here. 
