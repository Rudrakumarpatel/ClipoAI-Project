import datetime
import json
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from home.models import User, UserVideo,Video
import os
import google.generativeai as genai

# Create your views here.
def index(request):
  return render(request,'index.html')

def home(request):
  if(request.method == 'POST'):
        video_file = request.POST.get('video_file')
        #api-key of Gemini goolge
        API_KEY_AI = os.getenv("APIKEY")
        
        # Accessing environment variable
        genai.configure(api_key=API_KEY_AI)

        # Create a new conversation
        response = genai.chat(messages=f'{video_file} take this video file and give best one array json contain first description,title status (active or inactive) or date ')
        
        # Use regular expression to extract JSON data
        json_data = re.search(r'```json\n(.*?)\n```', response.last, re.DOTALL).group(1)

        # Parse the JSON data
        parsed_data = json.loads(json_data)
        
        data = json.loads(json.dumps(parsed_data, indent=2))
        
        description = data[0]['description']   
        title = data[0]['title']
        status = data[0]['status']
        # Parse date string to datetime object
        date = data[0]['date']
        
        # Create and save Video object
        video = Video(video_file=video_file, title=title, description=description, date=date, status=status)
        video.save()
  return render(request, 'home.html')

def login(request):
    if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = User.objects.filter(username=username).first()
        
        # Check if the user object exists and if the provided password is correct
        if user is not None:
        # Use Django's authenticate method to check if the password is correct
            passwordis = User.objects.filter(password=password).first()
            
            if passwordis is not None:
        # User exists and provided password is correct
        # authenticated_user contains the authenticated user object
              return redirect("home")
            else:
              # User exists but provided password is incorrect
              messages.info(request, "Please give correct password")      
        else:
        # User does not exist
          messages.info(request, "Username not exists please signup")      
    return render(request,"login.html")
  
  
def signup(request):
  if(request.method == "POST"):
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        
        user = User.objects.filter(username=username)
       
        if user.exists():
            messages.info(request, "Username already exists")
            return redirect('/signup')
        
        user = User(username=username,email=email, password=password)
        user.save()
        return redirect('home')
  return render(request,"signup.html")