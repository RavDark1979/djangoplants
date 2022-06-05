from django.shortcuts import render

from .forms import PlantForm, PotForm, PlanForm, SupplierForm, LocationForm, SoilForm
from .models import Plant, Plan

# Create your views here.




def page(request):
    """main page view"""
    return render(request, 'main_page.html')





def all_plants(request):
    """view of all plants currently uploaded to the databse"""
    plants = Plant.objects.all()
    return render(request, 'plant_list.html', {'plants': plants})





def all_plans(request):
    """view of all plans currently uploaded to the databse"""
    plans = Plan.objects.all()
    return render(request, 'plan_list.html', {'plans': plans})




def add_plant(request):
    """view of form for adding plants to database"""
    form = PlantForm(request.POST or None, request.FILES or None)  # we accept the post or nothing
    if form.is_valid():
        form.save()

    return render(request, 'add_plant.html', {'form': form})


def add_pot(request):
    """view of form for adding pots to database"""
    form = PotForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_pot.html', {'form': form})


def add_soil(request):
    """view of form for adding soil to database"""
    form = SoilForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_soil.html', {'form': form})


def add_location(request):
    """view of form for adding locations to database"""
    form = LocationForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_location.html', {'form': form})


def add_supplier(request):
    """view of form for adding suppliers to database"""
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_supplier.html', {'form': form})


def add_plan(request):
    """view of form for adding plans to database"""
    form = PlanForm(request.POST or None)
    if form.is_valid():
        form.save()

    return render(request, 'add_plan.html', {'form': form})
