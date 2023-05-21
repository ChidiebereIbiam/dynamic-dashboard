from django.shortcuts import render, redirect,get_object_or_404
from .forms import UserSignupForm
from django.urls import reverse_lazy
from django.views import generic
from .models import UserProfile
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def registerpage(request):
    form = UserSignupForm()
    if request.method == "POST":
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')

    context = {'form':form}
    return render(request, 'registration/register.html', context)
