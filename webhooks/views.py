from django.shortcuts import render,redirect
from django.http import HttpResponse
from database.models import impression_store
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    if request.method=='POST':
        time = request.POST['time']
        impression = request.POST['impression']
        print (time,impression)
        imp = impression_store.objects.create(impression=impression, time=time)
        imp.save()
        Data = impression_store.objects.all()
        return render(request, 'display.html', {'Data':Data})

def display(request):
    if request.method=='GET':
        Data = impression_store.objects.all()
        return render(request, 'display.html', {'Data':Data})
    
def clear(request):
    if request.method=='GET':
        impression_store.objects.all().delete()
        return redirect('/display/')