from django.conf.urls import url
from django.views.generic import ListView, DetailView
from questionnaire.models import Teacher
from questionnaire.models import Student
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^auth/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^rating/$', ListView.as_view(queryset=Teacher.objects.all().order_by("m_nRating"),
    template_name="questionnaire/rating.html"), name="rating"),
    url(r'^questionnaire/$', views.quest),
]