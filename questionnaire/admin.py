from django.contrib import admin
from questionnaire.models import Teacher
from questionnaire.models import Student
from questionnaire.models import Discipline
from questionnaire.models import Answer

admin.site.register(Teacher)
admin.site.register(Discipline)
admin.site.register(Student)
admin.site.register(Answer)