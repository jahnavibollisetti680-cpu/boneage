from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('prediction/', views.prediction, name='prediction'),
    path('training/', views.training_view, name='training'),  # training view
]