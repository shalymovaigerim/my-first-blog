from django.db import models
from django.conf import settings
from django.utils import timezone

class Post(models.Model): #defines our model
    author=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title=models.CharField(max_length=200) #define text with limited number of characters
    text=models.TextField()#for long text without a limit
    created_date=models.DateTimeField(default=timezone.now) #date and time
    published_date=models.DateTimeField(blank=True, null=True)# link to another model


    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def __str__(self): #get a text with a Post title
        return self.title
