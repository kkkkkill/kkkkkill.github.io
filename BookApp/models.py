from django.db import models

class User(models.Model):
    '''
    保存用户数据
    '''
    username = models.CharField(max_length= 20)
    password = models.IntegerField()
    email = models.EmailField()


class Publisher(models.Model):
    '''
    出版社信息
    '''
    name = models.CharField(max_length= 20)
    address = models.CharField(max_length= 20)


class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory = models.IntegerField()
    #创建出版社外键
    publisher = models.ForeignKey(to='Publisher', on_delete=models.CASCADE)


class Autthor(models.Model):
    name = models.CharField(max_length=15)
    book = models.ManyToManyField(to='Book')