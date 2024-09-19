from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework_simplejwt.tokens import RefreshToken,AccessToken

# Create your views here.

def login_v(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST.get('password')

        user=authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            refresh=RefreshToken.for_user(user)
            access_token = AccessToken.for_user(user)
            return JsonResponse(
                {
                    "success": True,
                    "access_token":str(access_token),
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                    "username": user.username
                },status=200
            )
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        
    return render(request, 'JWT/login.html')