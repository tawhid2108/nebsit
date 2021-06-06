from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404
#from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
#from .forms import ClientForm
from .models import Client



#from .models import ShowDataModel, CategoryName
#from django.views.generic import ListView, CreateView, DetailView
#from .forms import PostForm


def HomeViews(request):
    '''submitted = False
    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            #return HttpResponseRedirect('?submitted = True')
            return redirect(reverse('home'))
    else:
                    
        form = ClientForm()

        context = {
            #'form' : form,
           # 'submitted' : submitted,
            }'''
    return render (request, 'index.html')   




	
'''class HomeViews(ListView):
    #model = ShowDataModel
    template_name = 'index.html' '''

def AboutViews(request):
    return render (request, 'about.html')     


def ServiceViews(request):
    return render (request, 'services.html')  






'''class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'index.html'
   # success_url = reverse_lazy('login')'''