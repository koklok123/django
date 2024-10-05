from django.shortcuts import render
from settings.models import Setting, Galery

def nok(request):
    setting = Setting.objects.latest("id")
    gallery = Galery.objects.latest("id")
    return render(request, "index.html", locals())
