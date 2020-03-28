from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.db import connection
from collections import namedtuple

def namedtuplefetchall(cursor):
    "Return all rows from a cursor as a namedtuple"
    desc = cursor.description
    nt_result = namedtuple('Result', [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]

# Create your views here.
def index(request):
    return render(request, 'index.html')

def department(request):
    cursor = connection.cursor()
    cursor.execute('''select * from department;''')
    department=namedtuplefetchall(cursor)
    return render(request, 'department.html', {'departments': department})

def addDepartment(request):
    return render(request, 'addDepartment.html')

def addSuccess(request):
    name = request.POST.get('name')
    building = request.POST.get('building')
    telephone = request.POST.get('telephone')
    cursor = connection.cursor()
    cursor.execute('''insert into department (name,building,telephone) 
                     values (%s,%s,%s);''',[name,building,telephone])
    return HttpResponse('添加成功！')

def deleteDepartment(request):
    return render(request, 'deleteDepartment.html')

def deleteSuccess(request):
    name = request.POST.get('name')
    cursor = connection.cursor()
    cursor.execute('''delete from department where name=%s;''',[name])
    return HttpResponse('删除成功！')

def courseEnrollment(request):
    cursor = connection.cursor()
    cursor.execute('''select cno, group_concat(name) as instructor,enroll,capacity 
                    from instructor_arrangement natural join instructor natural join enrollment 
                    group by cno;''')
    courseEnrollment=namedtuplefetchall(cursor)
    return render(request, 'courseEnrollment.html', {'course_enrollment': courseEnrollment})