from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# Create your views here.
def user(request):
    return render(request, 'user.html')


def add(request):
    name = request.POST.get('username')
    password = request.POST.get('passwd')
    user = User()
    user.username = name
    user.passwd = password
    user.save()
    return HttpResponse('添加成功！')

def getAllUser(request):
    userList = User.objects.all()
    return render(request, 'userList.html',{'users':userList})

def courseEnrollment(request):
    cursor = connection.cursor()
    cursor.execute('''select cno, group_concat(name) as instructor,enroll,capacity 
                    from instructor_arrangement natural join instructor natural join enrollment 
                    group by cno;''')
    courseEnrollment=namedtuplefetchall(cursor)
    return render(request, 'courseEnrollment.html', {'course_enrollment': courseEnrollment})