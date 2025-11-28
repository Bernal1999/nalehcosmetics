from django.shortcuts import render,get_object_or_404,redirect
from .models import Product,NewProducts
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

# Create your views here.

def index(request):
    products = Product.objects.all()
    newproducts = NewProducts.objects.all()
    return render (request,'index.html',{'products':products,'newproducts':newproducts})


def buy(request,product_id):
    products=get_object_or_404(Product,id=product_id)
    if request.method=="POST":
        products=Product.objects.all()
        
    return render (request,"buy.html",{"products":products})

def about(request):
    return render (request,"about.html")

def shop(request):    
    query = request.GET.get("q")  # get search term
    if query:
        products = Product.objects.filter(title__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'shop.html', {'products': products, 'query': query})


def search(request):
    query = request.GET.get("q")
    results = Product.objects.filter(title__icontains=query) if query else []
    return redirect('')
    return render(request,"search.html",{"results":results,"query":query})

def information(request):
    return render(request,'information.html')

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        subject = f"New Contact Form Submission from {name}"
        body = f"""
        You received a new message:

        Name: {name}
        Email: {email}
        Message: {message}
        """

        try:
            send_mail(subject, body, email, ["nalehcosmetics@gmail.com"])
            messages.success(request, "✅ Message sent successfully!")
        except:
            messages.error(request, "❌ Failed to send message. Please try again.")

        return redirect("contact")

    return render(request, "contact.html")

def upcoming_products(request):
    newproducts = NewProducts.objects.all()

    return render (request,'upcoming_products.html',{"newproducts":newproducts})

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("Kavin", "nalehcosmetics@gmail.com", "Kavin@123")
        return HttpResponse("✅ Superuser created!")
    return HttpResponse("ℹ️ Superuser already exists.")

def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")

        subject = f"New Feedback from {name}"
        body = f"""
        You received new feedback:

        Name: {name}
        Email: {email}
        Feedback: {feedback}
        """

        try:
            send_mail(
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
                ["nalehcosmetics@gmail.com"],     # Change to your receiving email
                headers={"Reply-To": email},
            )
            messages.success(request, "✅ Thank you! Your feedback has been sent.")
        except Exception as e:
            messages.error(request, f"❌ Failed to send feedback: {e}")

        return redirect("feedback")

    return render(request, "feedback.html")


