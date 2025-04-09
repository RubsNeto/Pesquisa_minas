from django.contrib import admin
from django.urls import path
from feedback_antigo import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.feedback_form, name='feedback_form'),
    path('obrigado/', views.thank_you, name='thank_you'),
]