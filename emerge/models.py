from django.db import models
from django.core.validators import FileExtensionValidator
#DataFlair Models
class Project(models.Model):
    student_name = models.CharField(max_length=60)
    year = models.PositiveIntegerField()
    semester = models.CharField(max_length=10, choices=[('Semester 1', 'Semester 1'), ('Semester 2', 'Semester 2')])
    student_photo = models.ImageField(upload_to='student_photos/')
    project_photo = models.ImageField(upload_to='project_photos/')
    short_paper = models.FileField(upload_to='papers/', validators=[FileExtensionValidator(allowed_extensions=['doc', 'docx'])])
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name