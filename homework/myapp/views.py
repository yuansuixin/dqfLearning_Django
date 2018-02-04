import random

from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from myapp.models import Grades, Students


# 添加班级
# def addgrades(request):
#     grade = Grades()
#     num = random.randrange(1, 20)
#     grade.g_name = 'python{}'.format(num)
#     grade.g_num = num
#     grade.save()
#     return HttpResponse('添加班级成功%d' % num)
def addgrades(request):
    return render(request, 'addgrades.html')


def addgradessuccess(request):
    grade = Grades()
    grade.g_name = request.POST['g_name']
    grade.g_num = request.POST['g_num']
    grade.g_date = request.POST['g_date']
    grade.save()
    return HttpResponse('添加班级成功{}'.format(request.POST['g_name']))


# 添加学生
# def addstudent(request):
#     stu = Students()
#     num = random.randrange(1,40)
#     stu.s_name = 'tom{}'.format(num)
#     stu.s_age = num
#     # 获取到最后一个班级赋值给新生成的学生
#     stu.s_grade = Grades.objects.first()
#     stu.s_gender = False
#     # 数据的修改必须要save才能够提交上
#     stu.save()
#     return HttpResponse('添加学生成功%d'%num)

def addstudent(request):
    return render(request, 'addstudents.html')


def addstusuccess(request):
    stu = Students()
    stu.s_name = request.POST['s_name']
    stu.s_age = request.POST['s_age']
    s_gender = request.POST['s_gender']
    if s_gender == '男':
        s_gender = True
    else:
        s_gender = False
    stu.s_gender = s_gender
    name = request.POST['s_grade']
    # print(g_name)
    # 过滤出来名字相同的班级
    grades = Grades.objects.all().filter(g_name=name)
    if grades:
        # 获取到这个名字相同的班级
        grade = Grades.objects.get(g_name=name)
        # 必须要将班级的id与学生的外键相关联，
        stu.s_grade_id = grade.id
        grade.g_num += 1
        grade.save()
    else:
        # 不存在这个班级就新建一个班级
        grade = Grades()
        g = Grades.objects.last()
        grade.g_name = name
        stu.s_grade_id = 1 + g.id
        grade.g_num = 1
        grade.save()
    stu.save()
    return HttpResponse('添加学生成功%s' % request.POST['s_name'])


# 展示学生信息
def students(request):
    # 获取所有的数据
    students = Students.objects.all()
    # pageinator = Paginator(students,5)
    # page = pageinator.page(pageid)
    data = {'students': students}
    return render(request, 'students.html', data)


# 展示班级信息
def grades(request):
    grades = Grades.objects.all()
    data = {'grades': grades}
    return render(request, 'grades.html', data)


# 班级信息里点击班级可以显示班级的学生信息
def gradestudents(request, name):
    grade = Grades.objects.get(g_name=name)
    # 获取关联对象的集合
    stulist = grade.students_set.all()
    return render(request, 'students.html', {'students': stulist})


# 在学生信息页面中单击班级显示该班级的信息
def studentsgrades(request, name):
    grade = Grades.objects.get(g_name=name)
    # print(num)
    # 获取关联对象的集合
    stulist = grade.students_set.all()
    return render(request, 'students.html', {'students': stulist})


# def gs(request,num1,num2):
#     grade = Grades.objects.get(pk=num2)
#     stulist = grade.students_set.all()
#     return render(request, 'students.html', {'students': stulist})


def deletestu(request):
    return render(request, 'deletestu.html')


def deletestusuccess(request):
    name = request.POST['name']
    print(name)
    stu = Students.objects.get(s_name=name)
    stu.isdelete = True
    stu.save()
    print(123123)
    return render(request, 'deletestusuccess.html', {'stu': stu})


def pagestu(request,pageid):
    # 获取所有的数据
    # print(pageid)
    allList = Students.objects.all()
    pageinator = Paginator(allList,5)
    page = pageinator.page(pageid)
    data = {'students': page}
    return render(request, 'pagestu.html', data)