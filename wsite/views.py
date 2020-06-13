from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'index.html', {})


def email(request, email):
    print("Email sending ...", email)

    send_mail(
        'Name',
        "Test email",
        email,
        ['john@codemy.com'],
        fail_silently=False,

    )

    return HttpResponse("Hello email sent..")


def about(request):
    return "G"


def patients(request):
    return "G"


def news(request):
    return "G"


def services(request):
    return "G"


def contect(request):
    return "G"


def team(request):
    return "G"


def private_policy(request):
    return "G"


def membership(request):
    return "G"
