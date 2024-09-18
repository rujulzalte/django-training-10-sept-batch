from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import UserSerializer
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

# BusinessLogic/ Functionality


def homepage(request):
    # return HttpResponse("Hello World")
    return render(request, 'Login/homepage.html')


def index(request):
    return render(request, 'Login/index.html')


@csrf_exempt
def all_user_data(request):
    # Fetch data from database and return it as a JSON response
    if request.method == 'GET':
        try:
            users = User.objects.all() #queryset
            serializer_data=UserSerializer(users,many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
        
    if request.method == 'POST':
        input_data=json.loads(request.body)
        serializer_data=UserSerializer(data=input_data)

        if serializer_data.is_valid():
            serializer_data.save()
            return JsonResponse({
                'Message': 'User created successfully'
            },status=201)
  
@csrf_exempt
def single_user_data(request,pk):
    if request.method == 'GET':
        try:
            user = User.objects.get(id=pk)
            serializer_data=UserSerializer(user)
            return JsonResponse(serializer_data.data)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse({
                'Message': 'User deleted successfully'
            },status=204)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    if request.method == 'PUT':
        try: 
            user = User.objects.get(id=pk) 
            input_data=json.loads(request.body)
            serializer_data=UserSerializer(user,data=input_data)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    'Message': 'User updated successfully'
                },status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
           
    if request.method=='PATCH':
        try: 
            user = User.objects.get(id=pk) 
            input_data=json.loads(request.body)
            serializer_data=UserSerializer(user,data=input_data,partial=True)
            if serializer_data.is_valid():
                serializer_data.save()
                return JsonResponse({
                    'Message': 'User partially updated successfully'
                },status=200)
        except User.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)