from django.shortcuts import render
from .forms import ContactForm
# Create your views here.
def my_first_view(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "pages/about_me.html")

def contact_view(request):
    form = ContactForm()
    return render(request, "pages/contact.html", {"form": form})
