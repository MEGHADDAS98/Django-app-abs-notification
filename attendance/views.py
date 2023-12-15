from django.shortcuts import render


import pandas as pd
from django.views import View
from .models import EmployeeAttendance
import smtplib
from email.mime.text import MIMEText
from django.views import View
from .models import EmployeeAttendance
from django.db import models

from django.http import HttpResponse
from django.views import View

class HomeView(View):
    def get(self, request):
        
        content = '<h1>Welcome to the home page!</h1>'
        
        return HttpResponse(content)


class ImportEmployeeAttendanceView(View):
    def get(self, request):
        df = pd.read_excel('EmployeeAttendance.xlsx', engine='openpyxl')
        
        for index, row in df.iterrows():
            EmployeeAttendance.objects.create(
                e_code=row['E.Code'],
                e_name=row['E.Name'],
                date=row['Date'],
                attendance=row['Attendance']
            )
        return HttpResponse('Data imported successfully')

        

class CheckAttendanceView(View):
    def get(self, request):
        
        employees = EmployeeAttendance.objects.filter(attendance='A').values('e_code', 'e_name').annotate(absences=models.Count('e_code')).filter(absences__gte=2)
        
        for employee in employees:
            if employee['absences'] == 2:
                subject = 'Absence Notification'
                body = f'Hi {employee["e_name"]},\\n\\nThis email is to inform you that according to our attendance records, you are absent from your duties for 2 days. Please apply for leave.\\n\\nThanks\\nHR Team'
            else:
                subject = 'Absence Notification'
                body = f'Hi,\\n\\nThis email is to inform you that according to attendance records, {employee["e_name"]} did not attend to the duties for {employee["absences"]} days.\\n\\nThanks\\nHR Team'
            
            sender = 'your_email@gmail.com'
            password = 'your_password'
            recipients = ['recipient1@gmail.com', 'recipient2@gmail.com']
            
            msg = MIMEText(body)
            msg['Subject'] = subject
            msg['From'] = sender
            msg['To'] = ', '.join(recipients)
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login(sender, password)
                smtp_server.sendmail(sender, recipients, msg.as_string())
        


class DisplayEmailView(View):
    def get(self, request):
        employees = EmployeeAttendance.objects.filter(attendance='A').values('e_code', 'e_name').annotate(absences=models.Count('e_code')).filter(absences__gte=2)
        
        email_content = ''
        
        for employee in employees:
            if employee['absences'] == 2:
                subject = 'Absence Notification'
                body = f'Hi {employee["e_name"]},<br>This email is to inform you that according to our attendance records, you are absent from your duties for 2 days. Please apply for leave.<br><br>Thanks</br>HR Team. <br> Developed by Megha Das </br>'
            else:
                subject = 'Absence Notification'
                body = f'Hi,<br><br>This email is to inform you that according to attendance records, {employee["e_name"]} did not attend to the duties for {employee["absences"]} days.<br><br>Thanks<br>HR Team <br></br> <br> Developed by Megha Das </br>'
            
        email_content += f'<h3>{subject}</h3><p>{body}</p>'

        return HttpResponse(email_content)

        # for employee in employees:
        #     if employee['absences'] == 2:
        #         subject = 'Absence Notification'
        #         body = f'Hi {employee["e_name"]},\<br>\\nThis email is to inform you that according to our attendance records, you are absent from your duties for 2 days. Please apply for leave.\\n\\nThanks\</br>HR Team. '
        #     else:
        #         subject = 'Absence Notification'
        #         body = f'Hi,\\n\\nThis email is to inform you that according to attendance records, {employee["e_name"]} did not attend to the duties for {employee["absences"]} days.\\n\\nThanks\\nHR Team'
            
        #     email_content += f'<h3>{subject}</h3><p>{body}</p>'
        
        # return HttpResponse(email_content)
