from django.urls import path
from .views import habit_list, habit_create, habit_update, habit_delete, habit_detail, habit_summary

urlpatterns = [
    path('habits/', habit_list, name='habit_list'),
    path('habits/create/', habit_create, name='habit_create'),
    path('habits/<int:habit_id>/update/', habit_update, name='habit_update'),
    path('habits/<int:habit_id>/delete/', habit_delete, name='habit_delete'),
    path('habits/<int:habit_id>/', habit_detail, name='habit_detail'),
    path('habits/summary/', habit_summary, name='habit_summary'),
]