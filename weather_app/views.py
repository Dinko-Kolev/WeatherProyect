import math
from django.shortcuts import render, redirect
import requests

from weather_app.forms import CityForm, CityDeleteForm
from weather_app.models import City
from weather_app.search_city.search_city_weather import search_city_weather


def index(request):
    form = CityForm()
    context = {
        'cities': search_city_weather(),
        'form': form,
    }

    return render(request, 'index.html', context)


def create(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CityForm()
        context = {
            'city': search_city_weather(),
            'form': form,
        }
        return render(request, 'index.html', context)


def delete(request, pk):
    city = City.objects.get(id=pk)
    form = CityDeleteForm(instance=city)
    if request.method == 'POST':
        city.delete()
        return redirect('index')
    context = {
        'pk': pk,
        'form': form,
    }
    return render(request, 'city_delete.html', context)
