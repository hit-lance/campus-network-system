# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import CnsUser
#
#
# # Create your views here.
# def user(request):
#     return render(request, 'user.html')
#
#
# def add(request):
#     name = request.POST.get('username')
#     password = request.POST.get('passwd')
#     user = CnsUser()
#     user.username = name
#     user.passwd = password
#     user.save()
#     return HttpResponse('添加成功！')
#
# def getAllUser(request):
#     userList = CnsUser.objects.all()
#     return render(request, 'userList.html',{'users':userList})