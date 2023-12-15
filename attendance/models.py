from django.db import models

from django.db import models

class EmployeeAttendance(models.Model):
    e_code = models.IntegerField()
    e_name = models.CharField(max_length=100)
    date = models.DateField()
    attendance = models.CharField(max_length=1)
