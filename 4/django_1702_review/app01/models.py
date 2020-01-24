#coding:utf8
from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=30)
    age = models.IntegerField(default=0)
    choice = ((1,'男'),(0,'女'))
    gender = models.BooleanField(choices=choice)

    # choices = (('1','洗头'),('2','洗澡'),('3','洗脚'))
    # department = models.CharField(choices=choices,max_length=30)
    department = models.ForeignKey('Department')
    group = models.ManyToManyField('Group')
    date_add = models.DateTimeField(auto_now_add=True) # 添加时间
    date_modi = models.DateTimeField(auto_now=True) # 修改时间
    avatar = models.ImageField(upload_to='avatar/')  #  pip install Pillow

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '员工信息表'
        ordering = ['-id']

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name