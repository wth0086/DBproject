from django.db import models

# Create your models here.
class Employee(models.Model):
    
    """Employee Model Definition"""

    TYPE_HOUSEMAN = "houseman"
    TYPE_LONDRY = "londry"
    TYPE_OPERATOR = "operator"
    TYPE_RECEPTION = "reception"
    TYPE_RESERVATION = "reservation"
    TYPE_ROOMMAID = "roommaid"


    TYPE_CHOICES = [
        (TYPE_HOUSEMAN, "Houseman"),
        (TYPE_LONDRY, "Londry"),
        (TYPE_OPERATOR, "Operator"),
        (TYPE_RECEPTION, "Reception"),
        (TYPE_RESERVATION, "Reservation"),
        (TYPE_ROOMMAID, "Roommaid"),
    ]
    
    e_ID = models.CharField(max_length=100)
    e_name = models.CharField(max_length=80)
    e_type = models.CharField(choices=TYPE_CHOICES, max_length=80, blank=True)
    e_birthdate = models.DateField(blank=True, null=True)
    e_address = models.CharField(max_length=140)
    e_salary = models.IntegerField()
    e_phone_number = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.e_ID