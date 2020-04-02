from django.shortcuts import render

# Create your views here.
def game_views(request):
    """网页小游戏"""
    return render(request,'game/index.html')