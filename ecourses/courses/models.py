from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='uploads/%Y/%m')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.name
class ItemBase(models.Model):
    class Meta:
        abstract = True
    image = models.ImageField(upload_to='courses/%Y/%m', default=None)
    subject = models.CharField(max_length=255, null=False)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

class Course(ItemBase):
    class Meta:
        unique_together = ('subject', 'category')
        ordering = ["-id"]
    description = models.TextField(null=True, blank=True)
    # Khoa ngoai
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True) # CASCADE xoa category => course xoa theo

    def __str__(self):
        return self.name

class Lesson(ItemBase):
    class Meta:
        unique_together = ('subject', 'course')
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)