from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lead
from .forms import LeadForm

def home(request):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, 'thankyou.html')  # Optional: redirect to a thank you page
    else:
        form = LeadForm()

    context = {
        'form': form
    }
    return render(request, 'home.html', context)

