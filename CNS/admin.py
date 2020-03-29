from django.contrib import admin
from CNS.models import *

class classroomAdmin(admin.ModelAdmin):
    list_display = ('room_number','capacity')

class courseAdmin(admin.ModelAdmin):
    list_display = ('cno','cname','credit','dept','room_number')

class departmentAdmin(admin.ModelAdmin):
    list_display = ('name','building','telephone')

class friendshipAdmin(admin.ModelAdmin):
    list_display = ('user', 'friend', 'class_field')

class instructorAdmin(admin.ModelAdmin):
    list_display = ('inst_id', 'name', 'sex', 'email', 'title', 'dept')

class instructorArrangementAdmin(admin.ModelAdmin):
    list_display = ('inst', 'cno')

class logAdmin(admin.ModelAdmin):
    list_display = ('log_id', 'author', 'title', 'text','post_time','replyable')

class projectAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'start_time','end_time')

class replyAdmin(admin.ModelAdmin):
    list_display = ('user', 'log', 'content','time')

class researchAdmin(admin.ModelAdmin):
    list_display = ('inst', 'proj_number', 'role')

class studentAdmin(admin.ModelAdmin):
    list_display = ('stud_id', 'name', 'sex','email','password','grade','dept')

class studentFamilyAdmin(admin.ModelAdmin):
    list_display = ('stud', 'father_name', 'father_job','mother_name','mother_job')

class studentGradeAdmin(admin.ModelAdmin):
    list_display = ('stud', 'cno', 'grade')

admin.site.register(Classroom, classroomAdmin)
admin.site.register(Course, courseAdmin)
admin.site.register(Department, departmentAdmin)
admin.site.register(Friendship, friendshipAdmin)
admin.site.register(Instructor, instructorAdmin)
admin.site.register(InstructorArrangement, instructorArrangementAdmin)
admin.site.register(Log, logAdmin)
admin.site.register(Project, projectAdmin)
admin.site.register(Reply, replyAdmin)
admin.site.register(Research, researchAdmin)
admin.site.register(Student, studentAdmin)
admin.site.register(StudentFamily, studentFamilyAdmin)
admin.site.register(StudentGrade, studentGradeAdmin)