import time

from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from django.http import HttpResponseRedirect
from urllib.request import urlopen
from io import BytesIO 
from urllib.request import urlopen
from django.core.files import File

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import FlsForm
from .models import Fls





def home(request):
    count = User.objects.count()
    return render(request, 'home.html', {
        'count': count
    })



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form
    })



@login_required
def fetch_url(request):
    img_url = "https://www.cs.cmu.edu/afs/cs.cmu.edu/user/gchen/www/download/java/LearnJava.pdf"
    ret = urlopen(img_url)
    if ret.code == 200:
        fls = Fls()
        response = urlopen(img_url)
        io = BytesIO(response.read())
        fls.user = request.user
        fls.file.save("LearnJava.pdf" , File(io))
    else:
        print("url doesn't exist!!")
    return redirect('U_Base')




@login_required
def secret_page(request):
    username = request.user.username
    print(username)
    return render(request, 'secret_page.html')




class U_Base(LoginRequiredMixin, TemplateView):
    def get(self, request):
        current_user = request.user
        fls_list = Fls.objects.filter(user_id = current_user.id)
        return render(self.request, 'files/base.html', {'fls': fls_list})



class ProgressBarUploadView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        current_user = request.user
        fls_list = Fls.objects.filter(user_id = current_user.id)
        return render(self.request, 'files/progress_bar_upload/index.html', {'fls': fls_list})

    def post(self, request):
          # You don't need this line. This is just to delay the process so you can see the progress bar testing locally.
        form = FlsForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            fls = form.save(commit=False)
            fls.user = request.user
            fls.save()
            data = {'is_valid': True, 'name': fls.file.name, 'url': fls.file.url}
            return redirect('ProgressBarUploadView')
            
        else:
            data = {'is_valid': False}
        return redirect('ProgressBarUploadView')


class DragAndDropUploadView(LoginRequiredMixin, TemplateView):
    def get(self, request):
        current_user = request.user
        fls_list = Fls.objects.filter(user_id = current_user.id)
        return render(self.request, 'files/drag_and_drop_upload/index.html', {'fls': fls_list})

    def post(self, request):
        form = FlsForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            fls = form.save(commit=False)
            fls.user = request.user
            fls.save()
            data = {'is_valid': True, 'name': fls.file.name, 'url': fls.file.url}
            return redirect('DragAndDropUploadView')
        else:
            data = {'is_valid': False}
        return redirect('DragAndDropUploadView')

@login_required
def clear_database(request):
    current_user = request.user
    fls_list = Fls.objects.filter(user_id = current_user.id)
    for fls in fls_list:
        fls.file.delete()
        fls.delete()
    return redirect(request.POST.get('next'))


@login_required
def delete_file(request , pk):
    if request.method == 'POST':
        fls = Fls.objects.get(pk=pk)
        print(fls)
        fls.delete()
    return redirect('U_Base')
