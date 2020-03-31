from django.shortcuts import render

# Create your views here.
def game_views(request):
    return render(request,'game/index.html')