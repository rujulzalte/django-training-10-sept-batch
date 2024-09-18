from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import User
from .serializers import UserSerializer

# Create your views here.

# BusinessLogic/ Functionality


def homepage(request):
    # return HttpResponse("Hello World")
    return render(request, 'Login/homepage.html')


def index(request):
    return render(request, 'Login/index.html')


def all_user_data(request):
    # Fetch data from database and return it as a JSON response
    if request.method == 'GET':
        try:
            users = User.objects.all() #queryset
            serializer_data=UserSerializer(users,many=True)
            return JsonResponse(serializer_data.data,safe=False)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
  
