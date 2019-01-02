from django.conf import settings
from django.conf.urls import url, include
from django.urls import path
from django.conf.urls.static import static
from django.views.generic import TemplateView
from mysite.files import views

urlpatterns = [
    url(r'^clear/$', views.clear_database, name='clear_database'),
    url(r'^DragAndDropUploadView/$', views.DragAndDropUploadView.as_view(), name='DragAndDropUploadView'),
    path('', views.home, name='home'),
    path('U_Base/', views.U_Base.as_view(), name='U_Base'),
    url(r'^ProgressBarUploadView/$', views.ProgressBarUploadView.as_view(),name='ProgressBarUploadView'),
    path('signup/', views.signup, name='signup'),
    path('secret/', views.secret_page, name='secret'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('delete_file/<int:pk>/' , views.delete_file , name="delete_file"),
    path('fetch_url/' , views.fetch_url , name="fetch_url"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
