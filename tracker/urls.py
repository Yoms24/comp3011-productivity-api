from django.urls import path
from .views import habit_list, habit_detail

urlpatterns = [
    path('habits/', habit_list, name='habit_list'),
    path('habits/<int:habit_id>/', habit_detail, name='habit_detail'),
]