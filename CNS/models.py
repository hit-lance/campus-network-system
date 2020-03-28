# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Classroom(models.Model):
    room_number = models.CharField(primary_key="room_number", max_length=4)
    capacity = models.SmallIntegerField()

    class Meta:
        db_table = 'classroom'


class Course(models.Model):
    cno = models.CharField(primary_key="cno", max_length=7)
    title = models.CharField(max_length=20, blank=True, null=True)
    credit = models.IntegerField()
    dept = models.ForeignKey('Department', models.DO_NOTHING, db_column='dept')
    room_number = models.ForeignKey(Classroom, models.DO_NOTHING, db_column='room_number', related_name="courses_room_number")

    class Meta:
        db_table = 'course'


class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=2)
    building = models.CharField(max_length=20)
    telephone = models.CharField(max_length=8)

    class Meta:
        db_table = 'department'


class User(models.Model):
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=16)


class Friendship(models.Model):
    user = models.ForeignKey('Student', models.DO_NOTHING, related_name="user")
    friend = models.ForeignKey('Student', models.DO_NOTHING, related_name="friend")
    class_field = models.CharField(db_column='class', max_length=20)  # Field renamed because it was a Python reserved word.

    class Meta:
        db_table = 'friendship'
        unique_together = (('user', 'friend'),)


class Instructor(models.Model):
    inst_id = models.CharField(primary_key=True, max_length=6)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=320)
    title = models.CharField(max_length=20)
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept')

    class Meta:
        db_table = 'instructor'


class InstructorArrangement(models.Model):
    inst = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='inst_id')
    cno = models.ForeignKey(Course, models.DO_NOTHING, db_column='cno')

    class Meta:
        db_table = 'instructor_arrangement'
        unique_together = (('inst', 'cno'),)


class Log(models.Model):
    log_id = models.CharField(primary_key=True, max_length=10)
    author = models.ForeignKey('Student', models.DO_NOTHING)
    title = models.CharField(max_length=20)
    text = models.TextField()
    post_time = models.DateField()
    replyable = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'log'


class Project(models.Model):
    number = models.CharField(primary_key=True, max_length=6)
    title = models.CharField(max_length=200)
    start_time = models.DateField()
    end_time = models.DateField()

    class Meta:
        db_table = 'project'


class Reply(models.Model):
    user = models.OneToOneField('Student', models.DO_NOTHING)
    log = models.ForeignKey(Log, models.DO_NOTHING)
    content = models.TextField()
    time = models.DateField()

    class Meta:
        db_table = 'reply'
        unique_together = (('user', 'log'),)


class Research(models.Model):
    inst = models.ForeignKey(Instructor, models.DO_NOTHING, db_column='inst_id')
    proj_number = models.ForeignKey(Project, models.DO_NOTHING, db_column='proj_number',related_name="proj_number")
    role = models.CharField(max_length=10)

    class Meta:
        db_table = 'research'
        unique_together = (('inst', 'proj_number'),)


class Student(models.Model):
    stud_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=1)
    email = models.CharField(max_length=320)
    password = models.CharField(max_length=16)
    grade = models.CharField(max_length=10)
    dept = models.ForeignKey(Department, models.DO_NOTHING, db_column='dept')

    class Meta:
        db_table = 'student'


class StudentFamily(models.Model):
    stud = models.OneToOneField(Student, models.DO_NOTHING, primary_key=True)
    father_name = models.CharField(max_length=20, blank=True, null=True)
    father_job = models.CharField(max_length=20, blank=True, null=True)
    mother_name = models.CharField(max_length=20, blank=True, null=True)
    mother_job = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'student_family'


class StudentGrade(models.Model):
    stud = models.ForeignKey(Student, models.DO_NOTHING, db_column='stud_id')
    cno = models.ForeignKey(Course, models.DO_NOTHING, db_column='cno', related_name="inst_cno")
    grade = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'student_grade'
        unique_together = (('stud', 'cno'),)
