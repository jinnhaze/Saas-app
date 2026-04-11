from django.urls import path
from .views import *


urlpatterns = [
    path('text-generator/',TextGeneratorView.as_view(),name = 'text generate'),
    path('article-writer/',ArticleWriterView.as_view(),name = 'article writer'),
    path('resume-reviewer/',ResumeReviewView.as_view(),name = 'resume reviewer'),
    path('image-generator/',ImageGeneratorView.as_view(),name = 'image generator'),
    path('image-editor/',ImageEditorView.as_view(),name = 'image editor'),
]