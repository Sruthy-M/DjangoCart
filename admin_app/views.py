# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import cards
from django.http import JsonResponse
from django.http import HttpResponse

# Create your views here.
def login(request):
    if request.user.is_authenticated:
        return redirect(home)    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username , password=password)

        if user is not None:
            auth.login(request,user)
            return JsonResponse('valid', safe=False)
        else:
            return JsonResponse('invalid', safe=False)
    else:
        return render(request,'index.html')
    
def signup(request):
    if request.user.is_authenticated:
        return redirect(home)
    if request.method == 'POST':
        
        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                return JsonResponse('usernamemismatch',safe=False)
                
                # return redirect('/')
            else: 
                user = User.objects.create_user(first_name=name,username=username,email=email,password = password1)
                user.save();
            messages.info(request, "User created successfully..")    
            return JsonResponse('valid', safe=False)       
        else:
            return JsonResponse('invalid', safe=False)
            # messages.info(request,"password not match")    
    else:    
        return render(request,'signup.html')

def home(request):
    obj1 = cards()
    obj1.img = 'https://b.zmtcdn.com/data/dish_photos/ed0/78894e7c88854f29b80493101f916ed0.jpg'
    obj1.item = 'Chicken Biriyani'
    obj1.desc = 'Top sellers Paramount, Nehdi and Zam Zam'
    obj1.price = 120
    
    obj2 = cards()
    obj2.img = 'https://i.ytimg.com/vi/HVi7xxQZDRQ/maxresdefault.jpg'
    obj2.item = 'Alfam'
    obj2.desc = 'Top sellers Nehdi , Buhari and Zam Zam'
    obj2.price = 240
    
    obj3 = cards()
    obj3.img = 'https://i.ytimg.com/vi/WBXgmNkyMz4/maxresdefault.jpg'
    obj3.item = 'Kuzhimanthi'
    obj3.desc = 'Top sellers Nehdi,Buhari and Rahmath '
    obj3.price = 150