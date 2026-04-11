from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import CreditBalance



User = get_user_model()

@receiver(post_save,sender=User)
def give_free_credits_onsignup(sender,instance,created,**kwargs):
    if created:
        CreditBalance.objects.create(
            user= instance,
            credits = 10,
        )