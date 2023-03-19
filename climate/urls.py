from django.urls import path, include
from . import views

app_name = 'climate'
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('survey', views.survey, name='survey'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/result/', views.result, name='result'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]