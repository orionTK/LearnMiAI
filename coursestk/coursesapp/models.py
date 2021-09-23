from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    avatar = models.ImageField(upload_to='lessons/%Y/%m', default=None)

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

class ItemBase(models.Model):
    class Meta:
        abstract = True
    subject = models.CharField(max_length=100, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.subject

class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'cateogry')
    description = models.TextField(null=True, blank=True)
    cateogry = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)



class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
        # db_table = 'Lesson'
        ordering = ['id']
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, related_name="lessons") #course del => lesson del
    tags = models.ManyToManyField('Tag', blank=True, null=True)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name