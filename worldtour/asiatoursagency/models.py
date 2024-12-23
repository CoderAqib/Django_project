from django.db import models


class Tour(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField(help_text="Duration in days")

    def __str__(self):
        return self.name


class Schedule(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.tour.name} ({self.start_date} - {self.end_date})"
