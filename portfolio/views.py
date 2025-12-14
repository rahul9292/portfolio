from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from. models import ContactMessage

# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message = request.POST.get('message')
        contact =ContactMessage(name=name,email=email,message=message)
        contact.save()
        messages.success(request, "Your message has been sent successfully!")

        return redirect('home')



    return render(request,'home.html')
