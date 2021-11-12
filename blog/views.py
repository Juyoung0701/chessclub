from django.shortcuts import render
from .models import Chessuser
from .models import User
from django.http import HttpResponse


ptsPerwin = 100
ptsPerLose = -50
defaultPts = 2000
for i in range(1, 1+len(Chessuser.objects.all())):
        user = Chessuser.objects.get(id=i)
        pts = defaultPts + user.win*ptsPerwin + user.lose*ptsPerLose
        if pts < 0:
            pts = 0
        user.points = pts
        user.save()



def home(request):
    return render(request,'blog/home.html')

def board(request):
    leaderboard = {
        'rankings' : Chessuser.objects.all()
    }
    

    for i in range(1,1+len(Chessuser.objects.all())):
        user = Chessuser.objects.get(id=i)
        pts = user.points
        user.rank = rankConvert(pts)
        user.save()
    return render(request, 'blog/board.html',leaderboard)




def rankConvert(pts):
    if(pts >= 4000):
        return 'GRANDMASTER'
    elif(pts >= 3500):
        return 'MASTER'
    elif(pts >= 3000):
        return 'DIAMOND'
    elif(pts >= 2500):
        return 'PLATINUM'
    elif(pts >= 2000):
        return 'GOLD'
    elif(pts >= 1500):
        return 'SILVER'
    elif(pts >= 0):
        return 'BRONZE'
    

# Create your views here.
