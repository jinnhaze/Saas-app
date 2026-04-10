from django.contrib import admin
from .models import AIGeneration


@admin.register(AIGeneration)

class AIGenerationAdmin(admin.ModelAdmin):
    list_display = ['user','generation_type','created_at','cost_in_credits']
    list_filter = ['generation_type']
    search_fields = ['user__email','prompt']

    
