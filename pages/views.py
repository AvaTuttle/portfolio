from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import send_mail
from  django.template.loader import render_to_string

# Create your views here.
def my_first_view(request):
    return render(request, "base.html")

def about_view(request):
    return render(request, "pages/about_me.html")

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            #name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]

            #message_body = f"This is an email from your portfolio.\nName: {name}\nEmail: {email}\m{message}"
            message_body = render_to_string("content/email.html", request.POST)

            send_mail(
                "Portfolio email",
                message,
                email,
                ["tnt8me@gmail.com"],
                html_message=message_body
            )
    else:
        form = ContactForm()

    return render(request, "pages/contact.html", {"form": form})