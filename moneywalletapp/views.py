# noinspection PyUnresolvedReferences
from django.shortcuts import render,redirect
# noinspection PyUnresolvedReferences
from .models import Customer
# noinspection PyUnresolvedReferences
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

def homepage(request):
    return render(request,'homepage.html')
def register(request):
    username1 = request.POST['username']
    first1=request.POST['First']
    Last1 = request.POST['Last']
    Email1 = request.POST['email']
    Mob1 = request.POST['Mob']
    Pass1 = request.POST['pwd']
    Cpass1=request.POST['cpwd']
    user = User.objects.create_user(username=username1, password=Pass1,email=Email1,first_name=first1,last_name=Last1)
    Cust=Customer(Custdetail=user,walletbalance=100.00)
    Cust.save()
    wb=Cust.walletbalance
    login(request,user)
    return render(request,'accounts.html',{'userid':first1,'wb':wb})


def logi(request):
    userid=request.POST['Username']
    passw=request.POST['pwdlogin']
    user = authenticate(username=userid, password=passw)
    if user:
        login(request, user)
    else:
        return HttpResponse("invalid details")
    if user.is_authenticated:
        u=User.objects.get(username=userid)
        c=Customer.objects.get(Custdetail=u)
        wb=c.walletbalance
        return render(request,'accounts.html',{'userid':userid,'wb':wb})
    else:
        return render(request, 'homepage.html')




def paynow(request):

        receive=request.GET['receiver']
        amount=int(request.GET['amt'])
        if amount<=0:
            return HttpResponse("Please Enter Valid amount")
        giver=Customer.objects.get(Custdetail=request.user)
        giver.walletbalance-=amount
        giver.save()
        print("hi")
        try:
             take=Customer.objects.get(Custdetail__username=receive)
             print(take.Custdetail)
             take.walletbalance+=amount
             take.save()
             print(take.walletbalance)
        except:
            giver.walletbalance += amount
            giver.save()
        finally:
            return redirect('./')



