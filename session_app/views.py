from django.http import JsonResponse
from django.shortcuts import render
from .models import User
# Create your views here.

def login(request):
    if request.session.get('username'):
        return JsonResponse({"username": f"{request.session.get('username')} is already login"}, status=200)
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            user=User.objects.get(username=username)
            if user.password==password:
                request.session['username'] = username
                request.session.set_expiry(20)
                return JsonResponse({
                    'Message': 'Login successful'
                },status=200)
            else:
                return JsonResponse({'error': 'Invalid credentials'},status=401)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    return render(request,'session_app/login.html')