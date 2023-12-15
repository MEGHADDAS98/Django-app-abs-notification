# Employee Attendance Management System

This is a Django project that allows you to manage employee attendance data. The project includes features for importing employee attendance data from an Excel file, checking employee attendance, and sending email notifications to employees with 2 or more absences.

## Getting Started

To get started with this project, we will need to have Python and Django installed on our local machine. we'll also need to install the `pandas` and `openpyxl` libraries, which are used for reading data from Excel files.

### Prerequisites

- Python 3
- Django
- pandas
- openpyxl

### Installation

1. Navigate to the root directory of the project in a terminal or command prompt.
3. Run the command `python manage.py migrate` to create the database tables.
4. Start the Django development server by running the command `python manage.py runserver`.

## Usage

Once you have the project up and running, you can use it to manage employee attendance data. Here are some common tasks that I can perform:

- Import employee attendance data from an Excel file: To import employee attendance data from an Excel file, make sure that the data is correctly formatted and that the column names match the field names of the `EmployeeAttendance` model. Then, visit the URL `/import/` to run the `ImportEmployeeAttendanceView`, which will read the data from the Excel file and import it into the database.

- Check employee attendance: To check employee attendance and send email notifications to employees with 2 or more absences, visit the URL `/check/` to run the `CheckAttendanceView`. This view will query the database to get a list of employees with 2 or more absences and send email notifications to each employee using Gmail.

- Display email content: To display email content on a web page instead of sending emails, visit the URL `/display-email/` to run the `DisplayEmailView`. This view will query the database to get a list of employees with 2 or more absences and create email messages for each employee using a template. The email content will be displayed on a web page instead of being sent as emails.

