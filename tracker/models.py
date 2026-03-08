from django.db import models


class Habit(models.Model):
    DAILY = "Daily"
    WEEKLY = "Weekly"

    FREQUENCY_CHOICES = [
        (DAILY, "Daily"),
        (WEEKLY, "Weekly"),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    frequency = models.CharField(max_length=20, choices=FREQUENCY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Habit"
        verbose_name_plural = "Habits"

    def __str__(self):
        return self.name


class HabitLog(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name="logs")
    completed_on = models.DateField()
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_on", "-created_at"]
        verbose_name = "Habit Log"
        verbose_name_plural = "Habit Logs"

    def __str__(self):
        return f"{self.habit.name} - {self.completed_on}"