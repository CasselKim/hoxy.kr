from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

app_name = 'hoxy'
urlpatterns = [
    path('', views.main, name='main'),
    path('result/',views.search_button, name='search_button'),
    path('report/',views.report, name='report'),
    path('report/upload/profile/',views.upload_profile,name='upload_profile'),
    path('submit/',views.submit,name='submit'),
    path('test/',views.test,name='test'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)