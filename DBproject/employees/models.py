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
    
    ID = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    work_type = models.CharField(choices=TYPE_CHOICES, max_length=20, blank=True)
    birthdate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=200)
    salary = models.IntegerField()
    phone_number = models.CharField(max_length=100)

    def __str__(self):
        return self.ID