from rest_framework import serializers
from .models import Generationtype,AIGeneration


class TextGeneratorSerializer(serializers.Serializer):
    prompt = serializers.CharField(

         required = True,
         min_length = 10,
         max_length = 5000,
         help_text = 'what do you want to generate using text'
    )

class ArticleWriterSerializer(serializers.Serializer):
    prompt = serializers.CharField(
        required = True,
        min_length = 10,
        max_length = 5000,
        help_text = 'what article wanna create'

    )


class ResumeReviewSerializer(serializers.Serializer):
    resume = serializers.FileField(
        required = True,
        help_text = 'upload your resume(PDF only)'
    )

    def validate_resume(self,file):
        if not file.name.lower().endswith('.pdf'):
            raise serializers.ValidationError('Only pdf files are allowed')
        if file.size>5 * 1024 *1024 :
            raise serializers.ValidationError('the file is greater than 5MB')
        return file
    



class ImageGeneratorSerializer(serializers.Serializer):
    prompt = serializers.CharField(
        required = True,
        min_length = 10,
        max_length = 5000,
        help_text = 'the image that you want to generate'
    )    


class ImageEditorSerializer(serializers.Serializer):
    image = serializers.ImageField(required = True)
    prompt = serializers.CharField(
        required = True,
        min_length = 10,
        max_length = 5000,
        help_text = 'edit the images that you want like remove background or remove the objects '
    )


    def validate_image(self,image):
        if image.size>10 * 1024 *1024 :
            raise serializers.ValidationError('the image size should be inside 10MB')
        return image