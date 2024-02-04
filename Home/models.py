from django.db import models


# Create your models here.
class GlobalVariable(models.Model):
    variable_name = models.CharField(max_length=50, unique=True , default="visit")
    variable_value = models.IntegerField(default=0)


class brain(models.Model):
    order = models.CharField(max_length=20,default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()

    def __str__(self):
        return self.order + "   " + self.name
    
class recursion(models.Model):
    order = models.CharField(max_length=20,default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()

    def __str__(self):
        return self.order + "   " + self.name    

class beginner(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class brute(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class greed(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class sub(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class implement(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class sort(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class binary(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class pointer(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class hash(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class pair(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class dpstand(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class dp(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class tree(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class graph(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class dsu(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()
    def __str__(self):
        return self.order + "   " + self.name

class segtree(models.Model):
    order = models.CharField(max_length=20 , default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()        
    def __str__(self) :
        return self.order + "   " + self.name
    
class mixed(models.Model):
    order = models.CharField(max_length=20,default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()

    def __str__(self):
        return self.order + "   " + self.name  


class add(models.Model):
  
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    email = models.EmailField()
    link = models.URLField()

    def __str__(self):
        return self.name  


class bit(models.Model):
    order = models.CharField(max_length=20,default="1")
    
    name = models.CharField(max_length=90)
    description = models.TextField(max_length=250 , default="Do it yourself!")
    link = models.URLField()

    def __str__(self):
        return self.order + "   " + self.name  
    