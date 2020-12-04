from django.db import models
from django.utils import timezone
from rooms.models import Room
from employees.models import Employee

class complain_type(models.Model):
    complain_type = models.CharField(max_length=100)
    
    def __str__(self):
        return self.complain_type

class Complain(models.Model):
    
    TYPE_HOUSEMAN = "houseman"
    TYPE_LONDRY = "londry"
    TYPE_OPERATOR = "operator"
    TYPE_RECEPTION = "reception"
    TYPE_RESERVATION = "reservation"
    TYPE_ROOMMAID = "roommaid"
    TYPE_OTHER = "other"
    
    TYPE_CHOICES = [
        (TYPE_HOUSEMAN, "Houseman"),
        (TYPE_LONDRY, "Londry"),
        (TYPE_OPERATOR, "Operator"),
        (TYPE_RECEPTION, "Reception"),
        (TYPE_RESERVATION, "Reservation"),
        (TYPE_ROOMMAID, "Room maid"),
        (TYPE_OTHER, "Other"),
        ]
        
    customer_ID = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    complain_type = models.ForeignKey(complain_type, on_delete=models.CASCADE)
    room_number = models.ForeignKey(Room, on_delete=models.CASCADE)
    employee_ID = models.ForeignKey(Employee, on_delete=models.CASCADE)
    work_type = models.CharField(choices=TYPE_CHOICES, max_length=20, blank=True)
    complain_message = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_ID
