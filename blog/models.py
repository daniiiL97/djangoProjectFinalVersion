from django.db import models
class Post (models.Model):
    title = models.CharField(primary_key=True, max_length=1000)
    body = models.TextField()
    image = models.ImageField(blank=True, upload_to="images")

    def __str__(self):
        return self.title
