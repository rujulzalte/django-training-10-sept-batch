from django.contrib.auth.signals import user_logged_in #signal
from django.contrib.auth.models import User  #model send signals
from django.db.models.signals import pre_save
from django.dispatch import receiver

def login_success(sender,request,user,**kwargs):
    print("i am user logged in signal")
    print("semder",sender)
    print(f"user {user.username} logged in")
    print("request",request)
    print("kwargs",kwargs)
    # user.email
    # write a logic to inform user 
    # whenever he login into the system

user_logged_in.connect(login_success,sender=User)


@receiver(pre_save,sender=User)
def user_save(sender,instance,**kwargs):
    print("i am user save signal")
    print("sender",sender)
    print(f"user {instance.username} saved")
    print("kwargs",kwargs)
