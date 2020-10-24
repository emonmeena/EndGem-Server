from django.db import models

# # Create your models here.
class Courses(models.Model):
    course_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.course_name
    

class Files(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=250)

    def __str__(self):
        return self.file_name
        
# class Webpage(models.Model):
    # topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
#     name = models.CharField(max_length=264, unique=True)
    
#     url = models.URLField(unique=True)

#     def __str__(self):
#         return self.name

# class Accessrecord(models.Model):
#     name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
#     date = models.DateField()

#     def __str__(self):
#         return str(self.date)