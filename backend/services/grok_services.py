import os
import base64
from io import BytesIO
from dotenv import load_dotenv
from xai_sdk import Client
from xai_sdk.chat import user, system   
from pypdf import PdfReader


load_dotenv()

class GrokService :
    def __init__(self):
        api_key = os.getenv("XAI_API_KEY")
        if not api_key :
            raise ValueError('api key not found in .env file')
        self.client = Client(api_key=api_key)



    def generate_text(self,prompt:str,system_prompt:str=None)->str :
        chat = self.client.chat.create(model = "grok-4.20-reasoning")    


        if system_prompt :
            chat.append(system(system_prompt))

            chat.append(user(prompt))
            response = chat.sample()
            return response.content
        


    def resume_review(self,pdf_bytes:bytes)->str :
        reader = PdfReader(BytesIO(pdf_bytes))
        text = ""

        for page in reader.pages :
            page_text = page.extract_text()
            if page_text :
                text += page_text + '\n'

            if not text.strip():
                return "sorry i could not read any texts from this pdf"

            system_prompt = "You are an expert career coach and resume reviewer. Give honest, detailed, and actionable feedback."
            full_prompt = f"Review this resume and give detailed feedback:\n\n{text}"

            return self.generate_text(system_prompt,full_prompt)


    def generate_image(self,prompt:str)->str :
        response = self.client.image.sample(
            prompt = prompt,
            model = "grok-imagine-image",
        )      

        return response.url



    def image_editor(self,image_bytes : bytes,edit_prompt:str)->str :
        base64_image = base64.b64encode(image_bytes).decode("utf-8")
        image_data_uri = f"data:image/png;base64,{base64_image}"

        response = self.client.image_sample(
            prompt = edit_prompt,
            model = "grok-imagine-image",
            image = image_data_uri

        )
        return response.url


        
    