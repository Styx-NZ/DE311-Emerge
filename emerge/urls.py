from django.urls import path
from . import views
from emergeapp.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('emerge/', views.index, name='emerge'),
    path('about/', views.about, name='about'),
    path('upload/', views.upload, name='upload-project'),
    path('update/<int:project_id>/', views.update_project, name='update-project'),  # Name added
    path('delete/<int:project_id>/', views.delete_project, name='delete-project'),  # Name added
]

#DataFlair
if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)
