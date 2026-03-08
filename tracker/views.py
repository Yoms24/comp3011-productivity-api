from django.http import JsonResponse
from .models import Habit


def habit_list(request):
    habits = Habit.objects.all()

    data = []
    for habit in habits:
        data.append({
            "id": habit.id,
            "name": habit.name,
            "description": habit.description,
            "frequency": habit.frequency,
            "created_at": habit.created_at,
        })

    return JsonResponse(data, safe=False)


def habit_detail(request, habit_id):
    try:
        habit = Habit.objects.get(id=habit_id)

        data = {
            "id": habit.id,
            "name": habit.name,
            "description": habit.description,
            "frequency": habit.frequency,
            "created_at": habit.created_at,
        }

        return JsonResponse(data)

    except Habit.DoesNotExist:
        return JsonResponse({"error": "Habit not found"}, status=404)