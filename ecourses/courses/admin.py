from django.contrib import admin
from django.utils.html import mark_safe
from .models import Category, Course, Lesson, Tag
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class LessonForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget)
    class Meta:
        model = Lesson
        fields = '__all__'
class LessonInline(admin.StackedInline):
    model = Lesson.tags.through

class CourseAdmin(admin.ModelAdmin):
    inlines = (LessonInline, )

class LessonAdmin(admin.ModelAdmin):
    class Media:
        css = {
            'all':('/static/css/main.css',)
        }

    form = LessonForm
    list_display = ["id", "subject", "created_date", "active", 'course']
    search_fields = ["subject", "created_date", "course__subject"] #co the tim tren subject of khoa ngoai
    list_filter = ["subject", "course__subject"]
    readonly_fields = ["avatar"]
    inlines = [LessonInline, ]
    def avatar(self, lesson):
        return mark_safe("<img src='/static/{img_url}'/ alt='{alt}' width='120px'>".format(img_url=lesson.image.name, alt=lesson.subject))


# class LessonTagInline(admin.TabularInline):
class LessonTagInline(admin.StackedInline):
    model = Lesson
    pk_name = 'course'



admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)