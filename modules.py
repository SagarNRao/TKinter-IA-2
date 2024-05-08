import tkinter as tk
import google.generativeai as genai
import google.ai.generativelanguage as glm
import os
import requests
from dotenv import load_dotenv
from PIL import Image
import openai 

load_dotenv()

genai.configure(api_key=os.environ['GEMINI_KEY'])
model = genai.GenerativeModel('gemini-pro')

openai.api_key = os.getenv('OPENAI_KEY')

def get_response(entry, result):
    prompt = entry.get()
    response = model.generate_content(f'{str(prompt)}')
    result.set(response.text)

