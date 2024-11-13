from django.shortcuts import render,redirect
from django.contrib.auth import logout

# Create your views here.
def logout_confirm(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout-done')
    return render(request,'users/logout.html')

def logout_done(request):
    return render(request, "users/logout-done.html")