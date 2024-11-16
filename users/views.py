from django.shortcuts import render,redirect
from django.contrib.auth import logout
from .forms import UserRegisterForm
# Create your views here.
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout-done')
    return render(request,'users/logout.html')

def logout_done(request):
    return render(request, "users/logout-done.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data.get('username') 
            form.save()
            return redirect ('login')
    else:
        form = UserRegisterForm()
    context = {
        'form': form
    }
    return render(request, 'users/register.html',context)