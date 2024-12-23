from django.shortcuts import render
from .models import Tour, Schedule


# Create your views here.


def index(request):
    tours = Tour.objects.all()
    return render(request, 'tours/index.html', {'tours': tours})


def schedule(request):
    schedules = Schedule.objects.select_related('tour').all()
    return render(request, 'tours/schedule.html', {'schedules': schedules})


def admin(request):
    return render(request, 'admin')

