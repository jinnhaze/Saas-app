from django.urls import path
from .views import *


urlpatterns = [
    path('text_generator/',TextGeneratorView.as_view(),name = 'text generate'),
    path('articlewriter/',ArticleWriterView.as_view(),name = 'article writer'),
    path('resumereviewer/',ResumeReviewView.as_view(),name = 'resume reviewer'),
    path('imagegenerator/',ImageGeneratorView.as_view(),name = 'image generator'),
    path('imageeditor/',ImageEditorView.as_view(),name = 'image editor'),
]