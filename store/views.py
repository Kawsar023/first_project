from django.shortcuts import render, redirect
from store.models import Card
from store.forms import Contactform

# Create your views here.

def home(request):
    card = Card.objects.all().order_by('-id')
    fashion = Card.objects.filter(category__name = 'Fashion')

    

    context = {
        'card': card,
        'fashion' : fashion
    }

    return render(request, 'index.html',context)

def contact(request):
    form = Contactform(request.POST)

    if request.method == 'POST':
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('/')
        
    return render(request, 'contact.html', { 'form' : form})