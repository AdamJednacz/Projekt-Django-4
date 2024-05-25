from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    photo = models.ImageField(upload_to='images')
    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=100)
    date = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Done(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0) 
    def __str__(self):
        return f'Like on {self.task }'
