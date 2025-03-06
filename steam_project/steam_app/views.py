from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    return render(request, 'index.html')

def elden_ring(request):
    return render(request, 'elden-ring.html')

def dota_2(request):
    return render(request, 'dota-2.html') 

def assassins_creed(request):
    return render(request, 'assassins-creed.html') 

def god_of_war(request):
    return render(request, 'god-of-war.html') 

def browse_games(request):
    return render(request, 'browse-games.html') 

def red_dead_redemption(request):
    return render(request, 'red-dead-redemption.html')

def cyberpunk(request):
    return render(request, 'cyberpunk.html')

def the_witcher_3(request):
    return render(request, 'the-witcher-3.html')

def final_fantasy(request):
    return render(request, 'final-fantasy.html')

def community(request):
    return render(request, 'community.html')

def about(request):
    return render(request, 'about.html')

def profile(request):
    return render(request, 'profile.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')  # ✅ Redirect to home after login
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')  # ✅ Redirects to login after logout
