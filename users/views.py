from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}, your account has been created.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {'form':form})


@login_required
def profile(request):
    return render(request, 'accounts/profile.html')