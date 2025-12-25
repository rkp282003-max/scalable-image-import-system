from django.db import models

class ImportedImage(models.Model):
    name = models.CharField(max_length=255)
    google_drive_id = models.CharField(max_length=255)
    size = models.BigIntegerField()
    mime_type = models.CharField(max_length=100)
    storage_path = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
