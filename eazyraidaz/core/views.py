from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RiderApplicationForm, ContactForm


def home(request):
    return render(request, 'core/home.html')


def join(request):
    if request.method == 'POST':
        form = RiderApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Application submitted! We'll contact you within 24 hours.")
            return redirect('join_success')
    else:
        form = RiderApplicationForm()
    return render(request, 'core/join.html', {'form': form})


def join_success(request):
    return render(request, 'core/join_success.html')


def services(request):
    return render(request, 'core/services.html', {'services_list': SERVICES_LIST})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent! We'll get back to you shortly.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'core/contact.html', {'form': form})


SERVICES_LIST = [
    {'icon': '🍕', 'name': 'Hot Meals', 'desc': 'Restaurant and home-cook deliveries from local spots in Nairobi — delivered hot and fast to your door.'},
    {'icon': '🛒', 'name': 'Groceries', 'desc': 'Supermarket and fresh-market grocery runs plus household essentials delivered same-day.'},
    {'icon': '📦', 'name': 'E-Commerce', 'desc': 'Packages and documents from online stores, offices, and warehouses across the city.'},
    {'icon': '💊', 'name': 'Pharmacy', 'desc': 'Urgent medication and medical supply deliveries — because health cannot wait.'},
    {'icon': '🏢', 'name': 'Corporate Courier', 'desc': 'Same-day document and parcel runs for offices, law firms, banks, and corporate clients.'},
    {'icon': '🎁', 'name': 'Gift Delivery', 'desc': 'Flowers, cakes, and surprises delivered on time for any occasion anywhere in Nairobi.'},
]
