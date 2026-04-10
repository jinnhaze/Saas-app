from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TextGeneratorSerializer,ArticleWriterSerializer,ResumeReviewSerializer,ImageEditorSerializer,ImageGeneratorSerializer
from rest_framework.parsers import MultiPartParser,FormParser
from services.grok_services import GrokService


grok = GrokService()



class TextGeneratorView(APIView):
    def post(self,request):
        serializer = TextGeneratorSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            result = grok.generate_text(prompt)
            return Response({'result ': result})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class ArticleWriterView(APIView):
    def post(self,request):
        serializer = ArticleWriterSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            system_prompt = "You are a professional article writer. Write engaging, well-structured, SEO-friendly articles."
            result = grok.generate_text(f"Write a detailed article about: {prompt}", system_prompt)    
            return Response({"article" : result})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ResumeReviewView(APIView):
    def post(self,request):
        serializer = ResumeReviewSerializer(data = request.data)

        if serializer.is_valid():
            pdf_file = serializer.validated_data['resume']
            result = grok.resume_review(pdf_file.read())  
            return Response({"resume":result})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ImageGeneratorView(APIView):
    def post(self,request):
        serializer = ImageGeneratorSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            image_url= grok.generate_image(prompt)
            return Response({"image_url":image_url})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ImageEditorView(APIView):
    parser_classes = (MultiPartParser,FormParser)


    def post(self,request):
        serializer = ImageEditorSerializer(data = request.data)

        if serializer.is_valid():
            image_file = serializer.validated_data['image']
            edit_prompt = serializer.validated_data['prompt']

            edited_url = grok.edit_image(image_file.read(),edit_prompt)
            return Response({"edited_image_url":edited_url})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


