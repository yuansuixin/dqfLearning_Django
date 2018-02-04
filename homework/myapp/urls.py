from django.conf.urls import url

from myapp import views

urlpatterns = [
    # 添加
    url(r'^addgrades/$',views.addgrades),
    url(r'^addstudents/$',views.addstudent),
    url(r'^addstusuccess/$',views.addstusuccess),
    url(r'^addgradessuccess/$',views.addgradessuccess),
    # 显示信息
    url(r'^students/$',views.students,name='students'),
    url(r'^grades/$',views.grades,name='grades'),
    url(r'^pagestu/(\d+)/$',views.pagestu),
    # 用来html中的a标签的跳转使用
    url(r'^grades/(\w+)/$',views.gradestudents),
    url(r'^students/(\w+)/$', views.studentsgrades),
#     删除学生
    url(r'^deletestudent/$',views.deletestu,name='del'),
    url(r'^deletestudentsuccess/$', views.deletestusuccess,name='deletesuccess')
]