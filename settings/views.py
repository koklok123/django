from django.shortcuts import render
from .models import Setting

def emply_list(request):
    pon = Setting.objects.all()
    return render(request, 'index.html', {'pon': pon})
