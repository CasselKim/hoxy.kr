from django.urls import path
from . import views

app_name = 'hoxy'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:account_id>/',views.result, name='result'),
    path('to/report/',views.report_button, name='report_button'),
    path('report/',views.report, name='report'),
    path('submit/',views.submit, name='submit'),
]
