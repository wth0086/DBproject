from django.db import models
from django.utils import timezone
from rooms.models import Room
from employees.models import Employee

class complain_type(models.Model):
    complain_type = models.CharField(max_length=100, primary_key=True)
    
    def __str__(self):
        return self.complain_type

class Complain(models.Model):
    
    TYPE_1 = "1"
    TYPE_2 = "2"
    TYPE_3 = "3"
    TYPE_A = "A"
    TYPE_B = "B"
    TYPE_C = "C"
    TYPE_OTHER = "other"
    
    TYPE_CHOICES = [
        (TYPE_1, "room clean after checkout"),
        (TYPE_2, "room clean by client request"),
        (TYPE_3, "room clean by complain"),
        (TYPE_A, "delivery amenity"),
        (TYPE_B, "delivery client things"),
        (TYPE_C, "add extra bed"),
        (TYPE_OTHER, "Other"),
        ]

    def number():
        no = Complain.objects.count()
        if no == None:
            return 1
        else:
            return no + 1
    
    complain_number = models.CharField(max_length=6, primary_key=True, default=number)
    customer_ID = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    complain_type = models.ForeignKey(complain_type, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    problem_type = models.CharField(choices=TYPE_CHOICES, max_length=30, blank=True)
    complain_message = models.CharField(max_length=100)
    complain_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.complain_number
