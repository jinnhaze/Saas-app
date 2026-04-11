from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import TextGeneratorSerializer,ArticleWriterSerializer,ResumeReviewSerializer,ImageEditorSerializer,ImageGeneratorSerializer
from rest_framework.parsers import MultiPartParser,FormParser
from services.grok_services import GrokService
from rest_framework.permissions import IsAuthenticated
from usage.services import check_and_deduct_credits


grok = GrokService()



class TextGeneratorView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = TextGeneratorSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']

            check_and_deduct_credits(
                user = request.user,
                feature="text_generator",
                prompt=prompt,
                credits_to_deduct=1
            )
            result = grok.generate_text(prompt)
            return Response({'result ': result})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    



class ArticleWriterView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ArticleWriterSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            check_and_deduct_credits(
                user = request.user,
                feature="article-writer",
                prompt=prompt,
                credits_to_deduct=2
            )
            system_prompt = "You are a professional article writer. Write engaging, well-structured, SEO-friendly articles."
            result = grok.generate_text(f"Write a detailed article about: {prompt}", system_prompt)    
            return Response({"article" : result})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ResumeReviewView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ResumeReviewSerializer(data = request.data)

        if serializer.is_valid():
            pdf_file = serializer.validated_data['resume']
            prompt_for_log = "Resume Review"
            check_and_deduct_credits(
                user = request.user,
                feature="resume-review",
                prompt=prompt_for_log,
                credits_to_deduct=3
            )
            result = grok.resume_review(pdf_file.read())  
            return Response({"resume":result})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    


class ImageGeneratorView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ImageGeneratorSerializer(data = request.data)

        if serializer.is_valid():
            prompt = serializer.validated_data['prompt']
            check_and_deduct_credits(
                user = request.user,
                feature="image-generator",
                prompt=prompt,
                credits_to_deduct=4
            )
            image_url= grok.generate_image(prompt)
            return Response({"image_url":image_url})

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class ImageEditorView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    permission_classes = [IsAuthenticated]


    def post(self,request):
        serializer = ImageEditorSerializer(data = request.data)

        if serializer.is_valid():
            image_file = serializer.validated_data['image']
            edit_prompt = serializer.validated_data['prompt']
            check_and_deduct_credits(
                user = request.user,
                feature="image-editor",
                prompt=edit_prompt,
                credits_to_deduct=5
            )

            edited_url = grok.edit_image(image_file.read(),edit_prompt)
            return Response({"edited_image_url":edited_url})
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


