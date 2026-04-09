from django.db import models
from django.conf import settings

class Generationtype(models.TextChoices):
    TEXT = 'text','Text Generator'
    ARTICLE = 'article','Article Writer'
    RESUME_REVIEW = 'resume','Resume Review'
    IMAGE_GENERATE = 'image_generate','Image Generator'
    IMAGE_EDIT = 'image_edit','Image Editor (remove object/background)'



class AIGeneration(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='ai_generations')
    generation_type = models.CharField(max_length=20,choices=Generationtype.choices)
    prompt = models.TextField()
    result_text = models.TextField(blank=True,null=True)
    result_image_url = models.URLField(blank=True,null=True)

    tokens_used = models.PositiveIntegerField(default=0)
    cost_in_credits = models.PositiveIntegerField(default=1)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta :
        