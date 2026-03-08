from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Habit, HabitLog
import json
from datetime import date, timedelta

ALLOWED_FREQUENCIES = ["Daily", "Weekly"]


def habit_to_dict(habit):
    return {
        "id": habit.id,
        "name": habit.name,
        "description": habit.description,
        "frequency": habit.frequency,
        "created_at": habit.created_at,
    }

def log_to_dict(log):
    return {
        "id": log.id,
        "habit_id": log.habit.id,
        "habit_name": log.habit.name,
        "completed_on": str(log.completed_on),
        "notes": log.notes,
        "created_at": log.created_at,
    }


def parse_date(value):
    try:
        return date.fromisoformat(value)
    except (TypeError, ValueError):
        return None
    
def parse_request_body(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None


def validate_habit_data(body):
    if not body:
        return "Invalid JSON body"

    if not body.get("name") or not body.get("frequency"):
        return "Name and frequency are required"

    if body.get("frequency") not in ALLOWED_FREQUENCIES:
        return "Frequency must be either 'Daily' or 'Weekly'"

    return None


def method_not_allowed(method_name):
    return JsonResponse(
        {"error": f"Only {method_name} method is allowed"},
        status=405
    )


def habit_list(request):
    if request.method != "GET":
        return method_not_allowed("GET")

    habits = Habit.objects.all()
    data = [habit_to_dict(habit) for habit in habits]
    return JsonResponse(data, safe=False)


@csrf_exempt
def habit_create(request):
    if request.method != "POST":
        return method_not_allowed("POST")

    body = parse_request_body(request)
    validation_error = validate_habit_data(body)

    if validation_error:
        return JsonResponse({"error": validation_error}, status=400)

    habit = Habit.objects.create(
        name=body["name"],
        description=body.get("description", ""),
        frequency=body["frequency"]
    )

    return JsonResponse(habit_to_dict(habit), status=201)


def get_habit_or_404(habit_id):
    try:
        return Habit.objects.get(id=habit_id)
    except Habit.DoesNotExist:
        return None


def habit_detail(request, habit_id):
    if request.method != "GET":
        return method_not_allowed("GET")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    return JsonResponse(habit_to_dict(habit))


@csrf_exempt
def habit_update(request, habit_id):
    if request.method != "PUT":
        return method_not_allowed("PUT")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    body = parse_request_body(request)
    validation_error = validate_habit_data(body)

    if validation_error:
        return JsonResponse({"error": validation_error}, status=400)

    habit.name = body["name"]
    habit.description = body.get("description", "")
    habit.frequency = body["frequency"]
    habit.save()

    return JsonResponse(habit_to_dict(habit))


@csrf_exempt
def habit_delete(request, habit_id):
    if request.method != "DELETE":
        return method_not_allowed("DELETE")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    habit.delete()
    return JsonResponse({"message": "Habit deleted successfully"})


def habit_summary(request):
    if request.method != "GET":
        return method_not_allowed("GET")

    total_habits = Habit.objects.count()
    daily_habits = Habit.objects.filter(frequency="Daily").count()
    weekly_habits = Habit.objects.filter(frequency="Weekly").count()

    data = {
        "total_habits": total_habits,
        "daily_habits": daily_habits,
        "weekly_habits": weekly_habits,
    }

    return JsonResponse(data)

@csrf_exempt
def habit_log_create(request, habit_id):
    if request.method != "POST":
        return method_not_allowed("POST")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    body = parse_request_body(request)
    if not body:
        return JsonResponse({"error": "Invalid JSON body"}, status=400)

    completed_on = parse_date(body.get("completed_on"))
    if not completed_on:
        return JsonResponse(
            {"error": "completed_on must be a valid date in YYYY-MM-DD format"},
            status=400
        )

    log = HabitLog.objects.create(
        habit=habit,
        completed_on=completed_on,
        notes=body.get("notes", "")
    )

    return JsonResponse(log_to_dict(log), status=201)


def habit_log_list(request, habit_id):
    if request.method != "GET":
        return method_not_allowed("GET")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    logs = habit.logs.all()
    data = [log_to_dict(log) for log in logs]
    return JsonResponse(data, safe=False)

def habit_streak(request, habit_id):
    if request.method != "GET":
        return method_not_allowed("GET")

    habit = get_habit_or_404(habit_id)
    if not habit:
        return JsonResponse({"error": "Habit not found"}, status=404)

    log_dates = list(
        habit.logs.order_by("-completed_on").values_list("completed_on", flat=True)
    )

    unique_dates = []
    for log_date in log_dates:
        if log_date not in unique_dates:
            unique_dates.append(log_date)

    streak = 0
    current_day = date.today()

    for log_date in unique_dates:
        if log_date == current_day:
            streak += 1
            current_day = current_day - timedelta(days=1)
        elif log_date == current_day - timedelta(days=1) and streak == 0:
            streak += 1
            current_day = log_date - timedelta(days=1)
        else:
            break

    data = {
        "habit_id": habit.id,
        "habit_name": habit.name,
        "current_streak": streak,
        "total_logs": habit.logs.count(),
    }

    return JsonResponse(data)