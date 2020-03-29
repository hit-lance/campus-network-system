from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
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
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            cursor = connection.cursor()
            cursor.execute('''select * from department;''')
            department=namedtuplefetchall(cursor)
            cursor.execute('''select * from department_history;''')
            departmentHistory=namedtuplefetchall(cursor)
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return HttpResponse('Oops, an error has occurred!')
        transaction.savepoint_commit(save_id)
    return render(request, 'department.html', {'departments': department, 'historys': departmentHistory})

def addDepartment(request):
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            name = request.POST.get('name')
            building = request.POST.get('building')
            telephone = request.POST.get('telephone')
            cursor = connection.cursor()
            cursor.execute('''insert into department (name,building,telephone) 
                             values (%s,%s,%s);''',[name,building,telephone])
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return HttpResponse('Oops, an error has occurred!')
        transaction.savepoint_commit(save_id)
    return HttpResponse('Success！')

def deleteDepartment(request):
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            name = request.POST.get('name')
            cursor = connection.cursor()
            cursor.execute('''delete from department where name=%s;''',[name])
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return HttpResponse('Oops, an error has occurred!')
    return HttpResponse('Success！')


def studentInfo(request):
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            cursor = connection.cursor()
            cursor.execute('''select * from student;''')
            student=namedtuplefetchall(cursor)
            cursor.execute('''select * from student_info;''')
            studentInfo=namedtuplefetchall(cursor)
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return HttpResponse('Oops, an error has occurred!')
    return render(request, 'studentInfo.html', {'students': student, 'studentInfos': studentInfo})

def courseEnrollment(request):
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            cursor = connection.cursor()
            cursor.execute('''select * from instructor;''')
            instructor=namedtuplefetchall(cursor)
            cursor.execute('''select * from instructor_arrangement;''')
            instructorArrangement=namedtuplefetchall(cursor)
            cursor.execute('''select * from enrollment;''')
            enrollment=namedtuplefetchall(cursor)
            cursor.execute('''select cno, cname, group_concat(name) as instructor,enroll,capacity 
                            from instructor_arrangement natural join instructor natural join enrollment 
                            group by cno;''')
            courseEnrollment=namedtuplefetchall(cursor)
        except Exception as e:
            transaction.savepoint_rollback(save_id)
            return HttpResponse('Oops, an error has occurred!')
    return render(request, 'courseEnrollment.html',
                  {'instructors':instructor,
                   'instructorArrangements':instructorArrangement,
                   'enrollments':enrollment,
                   'course_enrollment': courseEnrollment})

def maxCreditCourse(request):
    with transaction.atomic():
        try:
            save_id = transaction.savepoint()
            cursor = connection.cursor()
            cursor.execute('''select * from course;''')
            course=namedtuplefetchall(cursor)
            cursor.execute('''select * from course where credit = (select max(credit) from course);''')
            maxCreditCourse=namedtuplefetchall(cursor)
        except Exception as e:
            transaction.savepoint_rollback(save_id)
    return render(request, 'maxCreditCourse.html', {'courses': course, 'maxCreditCourses': maxCreditCourse})