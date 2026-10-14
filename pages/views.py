from django.shortcuts import render
from django.contrib import messages


def home(request):
    return render(request, "pages/home.html")


def about(request):
    return render(request, "pages/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if name and email and message:
            # Demo form: connect email sending here when you're ready.
            messages.success(request, "Thanks! Your message has been received in this demo.")
        else:
            messages.error(request, "Please complete every field.")

    return render(request, "pages/contact.html")


def projects(request):
    return render(request, "pages/projects.html")
