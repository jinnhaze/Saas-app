import os
import base64
from io import BytesIO
from dotenv import load_dotenv  
from pypdf import PdfReader
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage


load_dotenv()

class GrokService :
    def __init__(self):
        self.llm = ChatGroq(
            model = "llama-3.3-70b-versatile",
            temperature = 0.7,
            max_tokens = 1027,
            api_key = os.getenv("GROQ_API_KEY")
        )



    def generate_text(self,prompt:str,system_prompt:str=None)->str :
        messages = []    


        if system_prompt :
            messages.append(SystemMessage(content=system_prompt))

        messages.append(HumanMessage(content=prompt))
        response = self.llm.invoke(messages)
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


        
    