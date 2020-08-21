from django.db import models

class Books(models.Model):

    title = models.CharField(max_length = 200)
    #slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url1(self):
        return f"record_details_id/{self.id}/"

    def get_absolute_url2(self):
        return f"/record_details_slug/{self.slug}/"

