from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from dashboard.forms import AddOldageHomeForm
from landing.models import Site, OldageHome, Patient, Illness, Doctor


@login_required
def dashboard_home(request):
    site = Site.objects.get()
    context = {
        "site": site,
    }
    return render(request, 'dashboard/index.html', context)


@login_required
def oldage_home(request):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.all()
    context = {
        "site": site,
        "oldagehomes": oldagehomes,
    }
    return render(request, 'dashboard/oldagehome.html', context)


@login_required
def oldage_home_details(request, pk):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.get(pk=pk)
    member = oldagehomes.patient_set.all().count()
    doctors = oldagehomes.doctor_set.all().count()
    staff = oldagehomes.staff_set.all().count()
    illness_list = oldagehomes.patient_set.all().count()

    context = {
        "site": site,
        "oldagehome": oldagehomes,
        "member": member,
        "doctors": doctors,
        "staff": staff,
        "illness_list": illness_list,
    }
    return render(request, 'dashboard/oldagehomedetails.html', context)


@login_required
def oldage_home_members(request, pk):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.get(pk=pk)
    member = oldagehomes.patient_set.all()
    context = {
        "site": site,
        "oldagehome": oldagehomes,
        "patients": member,
    }
    return render(request, 'dashboard/Patient_list.html', context)


def oldage_home_doctors(request, pk):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.get(pk=pk)
    doctors = Illness.objects.filter(patientoldagehome=oldagehomes)
    context = {
        "site": site,
        "oldagehome": oldagehomes,
        "doctors": doctors,
    }
    return render(request, 'dashboard/doctors_list.html', context)


def oldage_home_patient(request, pk):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.get(pk=pk)
    illnesss = oldagehomes.patient_set.all()
    context = {
        "site": site,
        "oldagehome": oldagehomes,
        "illnesss": illnesss,
    }
    return render(request, 'dashboard/ilness_list.html', context)


@login_required
def view_oldage_home(request, pk):
    site = Site.objects.get()
    oldagehomes = OldageHome.objects.get(pk=pk)
    oldagehomes = OldageHome.objects.all()
    context = {
        "site": site,
        "oldagehomes": oldagehomes,
    }
    return render(request, 'dashboard/oldagehome.html', context)


@login_required
def add_oldage_home(request):
    site = Site.objects.get()

    if request.method == "POST":
        form = AddOldageHomeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('oldage_home')

    else:
        form = AddOldageHomeForm()

    context = {
        "site": site,
        "title": "add home",
        "form": form,
    }
    return render(request, 'dashboard/forms.html', context)


def update_oldage_home(request, pk):
    site = Site.objects.get()
    home = OldageHome.objects.get(pk=pk)
    if request.method == "POST":
        form = AddOldageHomeForm(request.POST, request.FILES, instance=home)
        if form.is_valid():
            form.save()
            return redirect('oldage_home')

    else:
        form = AddOldageHomeForm(instance=home)

    context = {
        "site": site,
        "title": "update home",
        "form": form,
    }
    return render(request, 'dashboard/forms.html', context)


@login_required
def patient_list(request):
    site = Site.objects.get()
    patients = Patient.objects.all()
    context = {
        "site": site,
        "patients": patients,
    }
    return render(request, 'dashboard/Patient_list.html', context)


@login_required
def illness_list(request):
    site = Site.objects.get()
    illnesss = Illness.objects.all()
    context = {
        "site": site,
        "illnesss": illnesss,
    }
    return render(request, 'dashboard/ilness_list.html', context)


@login_required
def doctors_list(request):
    site = Site.objects.get()
    doctors = Doctor.objects.all()
    context = {
        "site": site,
        "doctors": doctors,
    }
    return render(request, 'dashboard/doctors_list.html', context)
