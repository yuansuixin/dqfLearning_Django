from django.db import models

# Create your models here.
class myManager(models.Manager):
    def get_queryset(self):
        # 过滤出来没有删除的
        return super(myManager, self).get_queryset().filter(isdelete=False)



# 班级信息表
class Grades(models.Model):
    g_name = models.CharField(max_length=20,unique=True)
    g_date = models.DateField(default='2018-01-24')
    g_num = models.IntegerField(default=0)
    isdelete = models.BooleanField(default=False)
    def __str__(self):
        return self.g_name
    # 设置表的名称及排序
    # 元选项
    class Meta():
        db_table = 'grades'
        # ordering = ['id']
    objects = myManager()
# 学生信息表
class Students(models.Model):
    s_name = models.CharField(max_length=20)
    s_age = models.IntegerField()
    s_gender = models.BooleanField()
    isdelete = models.BooleanField(default=False)
    # 这里使用的是外键
    s_grade = models.ForeignKey(Grades)
    objects = myManager()
    def __str__(self):
        return self.s_name
    # 对于布尔类型的性别进行转变成中文
    def gender(self):
        if self.s_gender:
            return '男'
        else:
            return '女'

    class Meta():
        db_table = 'students'
        # ordering = ['s_age']



