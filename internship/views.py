from django.shortcuts import render
from .models import Internship


def index(request):
    interns = Internship.objects.all()
    return render(request, 'index.html',
     {'interns':interns}
    )


def view_details(request):
    return render(request, 'view_details.html', {})

