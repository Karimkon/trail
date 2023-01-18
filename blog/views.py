from django.shortcuts import render, redirect

from blog.forms import GameparkForm, VisitorForm, PaymentForm, WardenForm, Wildlife_animalForm

from blog.models import Gamepark, Visitor, Payment,Warden,Wildlife_animal

from django.contrib.auth.forms import UserCreationForm 

from django.contrib.auth.decorators import login_required

from .utils import render_to_pdf

from django.http import HttpResponse

from django.contrib import messages

#render function is used to display the request or view to the user

def login(request):
    return render(request, 'registration/login.html')

@login_required
def index_view(request):
    return render(request, 'ase.html')

@login_required    
def indexx_view(request):
    return render(request, 'indexx.html')

@login_required
def blog_list_view(request):
    return render(request, 'blog_list.html')

@login_required   
def add_gamepark_view(request):
    message = ""
    if request.method == "POST":
        gamepark_form = GameparkForm(request.POST)

        if gamepark_form.is_valid():
            gamepark_form.save()

            message =  "Gamepark added succesfully"

        messages.success(request, message)
    gamepark_form = GameparkForm()

    gamepark= Gamepark.objects.all()
    
    context = {
        'form': gamepark_form,
        'message': message,
        'gameparks': gamepark,
    }
    return render(request, "add_gamepark.html", context)


def edit_gamepark_view(request,gamepark_id):
    message = ""
    gamepark = Gamepark.objects.get(id=gamepark_id)

    if request.method == "POST":

        gamepark_form = GameparkForm(request.POST,instance=gamepark)

        if gamepark_form.is_valid():
            gamepark_form.save()
            message = "Change made succesfully !" 
        else:
            message = "form is invalid !!"

        messages.success(request, message)

    else:
        gamepark_form = GameparkForm(instance=gamepark)
    context = {
        'form':gamepark_form,
        'gamepark':gamepark,
        'message': message
    }

    return render(request, 'edit_gamepark.html', context)

@login_required
def delete_gamepark_view(request,gamepark_id):
    gamepark = Gamepark.objects.get(id=gamepark_id) 
    gamepark.delete()
    return redirect(add_gamepark_view) 

@login_required
def add_visitor_view(request):
    message = ""
    if request.method == "POST":
        visitor_form = VisitorForm(request.POST)

        if visitor_form.is_valid():
            visitor_form.save()
            
            message = " Visitor saved successfully "

        messages.success(request, message)
    visitor_form = VisitorForm()
        
        
    visitor = Visitor.objects.all()
    
    context = {
        'form': visitor_form,
        'visitors': visitor,
        'message':message,
    }
    return render(request, "add_visitor.html", context)

def edit_visitor_view(request,visitor_id):
    message =""
    visitor = Visitor.objects.get(id=visitor_id)

    if request.method == "POST":

        visitor_form = VisitorForm(request.POST,instance=visitor)

        if visitor_form.is_valid():
            visitor_form.save()
            message = "Change made succesfully !" 
        else:
            message = "form is invalid !!"
        messages.success(request, message)

    else:
        visitor_form = VisitorForm(instance=visitor)
    context = {
        'form':visitor_form,
        'visitor':visitor,
        'message': message
    }

    return render(request, 'edit_visitor.html', context)

def delete_visitor_view(request,visitor_id):
    visitor = Visitor.objects.get(id=visitor_id) 
    visitor.delete()
    return redirect(add_visitor_view) 

def add_payment_view(request):
    message = ""
    if request.method == "POST":
        payment_form = PaymentForm(request.POST)

        if payment_form.is_valid():
            payment_form.save()
            message = "Payment added succesfully "
    else:
        payment_form = PaymentForm()
    messages.success(request, message)
        
    payment = Payment.objects.all()

    context = {
        'form': payment_form,
        'message': message,
        'payments': payment,
    }
    return render(request, "add_payment.html", context)

def edit_payment_view(request,payment_id):
    message = ""
    payment = Payment.objects.get(id=payment_id)

    if request.method == "POST":

        payment_form = PaymentForm(request.POST,instance=payment)

        if payment_form.is_valid():
            payment_form.save()
            message = "Change made succesfully !" 
        else:
            message = "form is invalid !!"
        
    else:
        payment_form = PaymentForm(instance=payment)

    messages.success(request, message)
    context = {
        'form':payment_form,
        'payment':payment,
        'message': message
    }

    return render(request, 'edit_payment.html', context)

def delete_payment_view(request,payment_id):
    payment = Payment.objects.get(id=payment_id) 
    payment.delete()
    return redirect(add_payment_view) 


def add_warden_view(request):
    message =""
    if request.method == "POST":
        warden_form = WardenForm(request.POST)

        if warden_form.is_valid():
            warden_form.save()
            message = "Warden Saved successfully"
    
    warden_form = WardenForm()
    
    warden = Warden.objects.all()
    
    messages.success(request, message)

    context = {
        'form': warden_form,
        'message': message,
        'wardens': warden,  
    }
    return render(request, "add_warden.html", context)

def edit_warden_view(request,warden_id):
    message =""
    warden = Warden.objects.get(id=warden_id)
    
    if request.method == "POST":
        warden_form = WardenForm(request.POST, instance=warden)
        
        if warden_form.is_valid():
            warden_form.save()
            message = "succesfuly changed warden"
        else:
            message = "declined"
    else:
        warden_form = WardenForm(instance=warden)

    messages.success(request,message)
        
    context = {
        'form': warden_form,
        'message': message,
        'warden':warden,
    }
    
    return render(request, 'edit_warden.html', context)

def delete_warden_view(request, warden_id):
    warden = Warden.objects.get(id=warden_id)
    warden.delete()
    return redirect(add_warden_view)
    
    

def add_wildlife_view(request):
    message = ""
    if request.method == "POST":
        wildlife_form = Wildlife_animalForm(request.POST)

        if wildlife_form.is_valid():
            wildlife_form.save()
            message = "succesfully added wildlife" 
    
    wildlife_form = Wildlife_animalForm()
    
    wildlife = Wildlife_animal.objects.all()
    messages.success(request, message)

    context = {
        'form': wildlife_form,
        'message': message,
        'wildlifes': wildlife,  
    }
    return render(request, "add_wildlife.html", context)

def edit_wildlife_view(request,wildlife_id):
    message = ""
    wildlife = Wildlife_animal.objects.get(id=wildlife_id)
    
    if request.method == "POST":
        wildlife_form = Wildlife_animalForm(request.POST, instance=wildlife)
        
        if wildlife_form.is_valid():
            wildlife_form.save()
            message = "succesfuly changed wildlife"
    
    wildlife_form = Wildlife_animalForm(instance=wildlife)

    messages.success(request,message)    
    context = {
        'form': wildlife_form,
        'message': message,
        'wildlife':wildlife,
    }
    
    return render(request, 'edit_wildlife.html', context)

def delete_wildlife_view(request, wildlife_id):
    wildlife = Wildlife_animal.objects.get(id=wildlife_id)
    wildlife.delete()
    messages.error(request, "Deleted")
    return redirect(add_wildlife_view)
    
def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message ="you have registered successful you can now login dear"           
        else:
            message="something went wrong !!!!"
    else:
        sign_up_form = UserCreationForm()

    context = {
        'form':sign_up_form
    }

    return render(request, 'registration/sign_up.html', context)

def gameparks_pdf(request):
    gameparks = Gamepark.objects.all()
    context ={
        "gameparks": gameparks,
    }
    pdf = render_to_pdf("gamepark_pdf.html", context)

    return HttpResponse(pdf, content_type="application/pdf" )