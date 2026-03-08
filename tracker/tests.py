from django.test import TestCase, Client
from .models import Habit, HabitLog
import json
from datetime import date


class HabitApiTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.habit = Habit.objects.create(
            name="Drink Water",
            description="Drink 2 litres daily",
            frequency="Daily"
        )

    def test_get_all_habits(self):
        response = self.client.get("/api/habits/")
        self.assertEqual(response.status_code, 200)

    def test_get_one_habit(self):
        response = self.client.get(f"/api/habits/{self.habit.id}/")
        self.assertEqual(response.status_code, 200)

    def test_create_habit_success(self):
        data = {
            "name": "Walk Daily",
            "description": "Walk for 20 minutes",
            "frequency": "Daily"
        }
        response = self.client.post(
            "/api/habits/create/",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_create_habit_invalid_frequency(self):
        data = {
            "name": "Bad Habit Test",
            "description": "Invalid frequency example",
            "frequency": "Monthly"
        }
        response = self.client.post(
            "/api/habits/create/",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 400)

    def test_update_habit_success(self):
        data = {
            "name": "Drink More Water",
            "description": "Drink 3 litres daily",
            "frequency": "Daily"
        }
        response = self.client.put(
            f"/api/habits/{self.habit.id}/update/",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 200)

    def test_delete_habit_success(self):
        response = self.client.delete(f"/api/habits/{self.habit.id}/delete/")
        self.assertEqual(response.status_code, 200)

    def test_habit_summary(self):
        response = self.client.get("/api/habits/summary/")
        self.assertEqual(response.status_code, 200)

    def test_create_habit_log_success(self):
        data = {
            "completed_on": str(date.today()),
            "notes": "Completed test log"
        }
        response = self.client.post(
            f"/api/habits/{self.habit.id}/logs/create/",
            data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, 201)

    def test_get_habit_logs(self):
        HabitLog.objects.create(
            habit=self.habit,
            completed_on=date.today(),
            notes="Log entry"
        )
        response = self.client.get(f"/api/habits/{self.habit.id}/logs/")
        self.assertEqual(response.status_code, 200)

    def test_habit_streak(self):
        HabitLog.objects.create(
            habit=self.habit,
            completed_on=date.today(),
            notes="Today log"
        )
        response = self.client.get(f"/api/habits/{self.habit.id}/streak/")
        self.assertEqual(response.status_code, 200)