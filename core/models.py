from django.db import models

# Create your models here.
class blog(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField()
    slug = models.SlugField(max_length=100)
    content=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    author=models.CharField(max_length=100)
    def __str__(self):
        return self.title
    
    


