from django.contrib import admin
from . models import *
# Register your models here.


# admin.site.register(Student)

class stu (admin .ModelAdmin):
    list_display = ['FNAME','LNAME','BIRTHDAY','GENDER','EMAIL','PHONE','ADDRESS','CITY',
                    'COLLEGENAME','QUALIFICATION','BRANCH','PASSING_YEAR','TECHNOLOGY',]
admin.site.register(Student,stu)


admin.site.register(QualificationOption)
admin.site.register(BranchOption)
admin.site.register(PassingYearOption)
admin.site.register(TechnologyOption)
admin.site.register(Course)