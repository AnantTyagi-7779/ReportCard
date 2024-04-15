from django.contrib import admin

# Register your models here.
from .models import *
from django.db.models import Sum

admin.site.register(Department)
admin.site.register(StudentID)
admin.site.register(Subject)
admin.site.register(Student)
# admin.site.register(ReportCard)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']

admin.site.register(SubjectMarks, SubjectMarksAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_genetation']

    ordering=['student_rank']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        print(subject_marks.aaggregate(marks=Sum('marks'))['marks'])
        return 0

admin.site.register(ReportCard, ReportCardAdmin)