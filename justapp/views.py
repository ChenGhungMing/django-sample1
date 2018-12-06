from datetime import datetime
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponse

from justapp.forms import HomeForm

def hello_world(request):
    return render(request, 'hello_world.html', {
        'current_time': str(datetime.now()),
    })

def index(request):
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })
def blank1(request):
    return render(request, 'blank.1.html', {
        'current_time': str(datetime.now()),
    })
def blank2(request):
    return render(request, 'blank.2.html', {
        'current_time': str(datetime.now()),
    })
def blank3(request):
    return render(request, 'blank.3.html', {
        'current_time': str(datetime.now()),
    })
def blank(request):
    return render(request, 'blank.html', {
        'current_time': str(datetime.now()),
    })
def buttons(request):
    return render(request, 'buttons.html', {
        'current_time': str(datetime.now()),
    })
def flot(request):
    return render(request, 'flot.html', {
        'current_time': str(datetime.now()),
    })
def forms(request):
    return render(request, 'forms.html', {
        'current_time': str(datetime.now()),
    })
def grid(request):
    return render(request, 'grid.html', {
        'current_time': str(datetime.now()),
    })
def icons(request):
    return render(request, 'icons.html', {
        'current_time': str(datetime.now()),
    })
def login(request):
    return render(request, 'login.html', {
        'current_time': str(datetime.now()),
    })
def morris(request):
    return render(request, 'morris.html', {
        'current_time': str(datetime.now()),
    })
def notifications(request):
    return render(request, 'notifications.html', {
        'current_time': str(datetime.now()),
    })
def panels_wells(request):
    return render(request, 'panels-wells.html', {
        'current_time': str(datetime.now()),
    })
def tables(request):
    return render(request, 'tables.html', {
        'current_time': str(datetime.now()),
    })
def typography(request):
    return render(request, 'typography.html', {
        'current_time': str(datetime.now()),
    })

def views(request):
    return render(request, 'typography.html', {
        'current_time': str(datetime.now()),
    })
#def post(request):
#    if request.method == "POST":        #如果是以POST的方式才處理
#       mess = request.POST['username'] #取得表單輸入資料
#    else:
#        mess = "表單資料尚未送出!"
#    return render(request,"post.html",locals())

class HomeView(TemplateView):
    template_name = 'hello_world.html'
    
    def get(self, request):
        form = HomeForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = HomeForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = HomeForm()

        args = {'form' :form, 'text' :text}
        return render(request, self.template_name, args)
