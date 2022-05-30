from django.db import models
import uuid 

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    bio = models.CharField(max_length = 150, null = True, blank = True)
    description = models.TextField(null = True, blank = True)
    qualification = models.CharField(max_length = 150, null = True, blank = True)
    institute = models.CharField(max_length = 150, null = True, blank = True)
    skils = models.CharField(max_length = 150, null = True, blank = True)
    contact = models.CharField(max_length = 60, null = True, blank = True)
    featured_image = models.ImageField(null = True, blank = True, default= "default.jpg")
    tag = models.ManyToManyField('Tag', blank=True)
    
    id = models.UUIDField(default= uuid.uuid4, unique = True, primary_key = True, editable = "False")

    def __str__(self):
        return self.title
    
class Review(models.Model):

    VOTE_TYPE = (
        ('up', 'Up vote'),
        ('down', 'Down vote'),
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add = True)
   

    id = models.UUIDField(default= uuid.uuid4, unique = True, primary_key = True, editable = "False")
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add = True)
    id = models.UUIDField(default= uuid.uuid4, unique = True, primary_key = True, editable = "False")
    def __str__(self):
        return self.name
