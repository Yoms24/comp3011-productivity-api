from django.http import JsonResponse
import json
from .models import Habit
from django.views.decorators.csrf import csrf_exempt

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

@csrf_exempt
def habit_create(request):
    if request.method == 'POST':
        body = json.loads(request.body)

        habit = Habit.objects.create(
            name=body.get('name'),
            description=body.get('description', ''),
            frequency=body.get('frequency')
        )

        data = {
            "id": habit.id,
            "name": habit.name,
            "description": habit.description,
            "frequency": habit.frequency,
            "created_at": habit.created_at,
        }

        return JsonResponse(data, status=201)

    return JsonResponse({"error": "Only POST method is allowed"}, status=405)

@csrf_exempt
def habit_update(request, habit_id):
    if request.method == 'PUT':
        try:
            habit = Habit.objects.get(id=habit_id)
            body = json.loads(request.body)

            habit.name = body.get('name', habit.name)
            habit.description = body.get('description', habit.description)
            habit.frequency = body.get('frequency', habit.frequency)
            habit.save()

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

    return JsonResponse({"error": "Only PUT method is allowed"}, status=405)

@csrf_exempt
def habit_delete(request, habit_id):
    if request.method == 'DELETE':
        try:
            habit = Habit.objects.get(id=habit_id)
            habit.delete()
            return JsonResponse({"message": "Habit deleted successfully"})

        except Habit.DoesNotExist:
            return JsonResponse({"error": "Habit not found"}, status=404)

    return JsonResponse({"error": "Only DELETE method is allowed"}, status=405)

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