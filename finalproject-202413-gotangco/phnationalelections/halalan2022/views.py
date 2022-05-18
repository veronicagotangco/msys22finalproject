from django.shortcuts import render, redirect, get_object_or_404
from .models import Candidate, Users, Vote

# Create your views here.
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usr = get_object_or_404(Users, username = username, password = password)
        return redirect('home', uid = usr.pk)
    else:
        return render(request, 'halalan2022/login.html')

def create_account(request):
    if (request.method=="POST"):
        username = request.POST.get('uname')
        password = request.POST.get('pword')
        firstname = request.POST.get('fname')
        lastname= request.POST.get('lname')
        bday = request.POST.get('bday')
        sex = request.POST.get('sex')
        Users.objects.create(username=username, password=password, first_name=firstname, last_name=lastname, birthday=bday, sex=sex)
        return redirect('login')
    else:
        return render(request, 'halalan2022/create_account.html')

def candidates(request, uid):
    candidate_objects = Candidate.objects.all() 
    return render(request, 'halalan2022/candidates.html', {'candidate':candidate_objects, 'usrid': uid})

def home(request, uid):
    candidate_objects = Candidate.objects.all()
    usr = get_object_or_404(Users, pk=uid)
    return render(request, 'halalan2022/home.html', {'candidate':candidate_objects, 'message':usr.username, 'usrid': uid})
    
def about(request, uid):
    return render(request, 'halalan2022/about.html', {'usrid':uid})

def view_user(request, uid):
    usr = get_object_or_404(Users, pk=uid)
    return render(request, 'halalan2022/view_user.html', {'usrid':uid, 'username':usr.username, 'password':usr.password, 'firstname':usr.first_name, 'lastname': usr.last_name, 'birthday':usr.birthday, 'sex':usr.sex})

def update_user(request, uid):
    if (request.method == 'POST'):
        uname = request.POST.get('uname')
        pword = request.POST.get('pword')
        firstname = request.POST.get('fname')
        lastname = request.POST.get('lname')
        bday = request.POST.get('bday')
        sex = request.POST.get('sex') 
        Users.objects.filter(pk=uid).update(username = uname, password = pword, first_name = firstname, last_name = lastname, birthday = bday, sex = sex)
        return redirect('view_user', uid = uid)
    else:
        usr = get_object_or_404(Users, pk=uid)
        return render(request, 'halalan2022/update_user.html', {'usrid':uid, 'uname':usr.username, 'pword':usr.password, 'fname':usr.first_name, 'lname':usr.last_name, 'bday':usr.birthday, 'sex':usr.sex})

def vote(request, uid):
    c = get_object_or_404(Candidate, pk = 1)
    d = get_object_or_404(Candidate, pk = 2)
    e = get_object_or_404(Candidate, pk = 3)
    f = get_object_or_404(Candidate, pk = 4)
    g = get_object_or_404(Candidate, pk = 5)
    h = get_object_or_404(Candidate, pk = 6)


    if (request.method == 'POST'):
        votes = request.POST.get('votes')
        comment = request.POST.get('comments')
        Vote.objects.create(first_name = votes, comment = comment)
        return redirect('home', uid = uid)
    else:    
        return render(request, 'halalan2022/vote.html', {'usrid':uid, 'c':c, 'd':d, 'e':e, 'f':f, 'g':g, 'h':h})