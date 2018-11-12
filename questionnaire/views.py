from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib import auth
from django.views.generic.edit import FormView
from django.template.context_processors import csrf
from questionnaire.models import Teacher
from questionnaire.models import Student
from questionnaire.models import Answer
from django.contrib.auth.models import User

def index(request):
    return render(request, 'questionnaire/home.html')

def rating(request):
    return render(request, 'questionnaire/rating.html')


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return index(request)
        else:
            args['login_error'] = "User not found"
            return render_to_response('questionnaire/auth.html', args)
    else:
        return render_to_response('questionnaire/auth.html', args)

def logout(request):
    auth.logout(request)
    return index(request)


def CheckAnswer(sStudEmail, sTeachEmail):
    answers = Answer.objects.all()
    for answer in answers:
        if answer.m_sStEmail == sStudEmail and answer.m_sTeachEmail == sTeachEmail:
            return True
    return False

def quest(request):
    if request.method == "POST":
        studentname = request.POST['userem']
        teachername = request.POST['teacher']
        teachers = Teacher.objects.all()
        for teacher in teachers:
            if teacher.m_sFullName == teachername:
                if CheckAnswer(studentname, teacher.m_sEmail):
                    return render(request, 'questionnaire/home.html')
                newRating = teacher.m_nRating
                answer = Answer()
                answer.m_sStEmail = studentname
                answer.m_sTeachEmail = teacher.m_sEmail
                if 'quest1' in request.POST:
                    newRating += int(request.POST['quest1'])
                    answer.m_nScores1 = int(request.POST['quest1'])
                if 'quest2' in request.POST:
                    answer.m_nScores2 = int(request.POST['quest2'])
                    newRating += int(request.POST['quest2'])
                if 'quest3' in request.POST:
                    newRating += int(request.POST['quest3'])
                    answer.m_nScores3 = int(request.POST['quest3'])
                if 'quest4' in request.POST:    
                    newRating += int(request.POST['quest4'])
                    answer.m_nScores4 = int(request.POST['quest4'])
                if 'quest5' in request.POST:
                    newRating += int(request.POST['quest5'])
                    answer.m_nScores5 = int(request.POST['quest5'])
                teacher.m_nRating = newRating
                teacher.save()
                answer.save()
                return render(request, 'questionnaire/rating.html')
    else:
        return render(request, 'questionnaire/questionnaire.html')
        