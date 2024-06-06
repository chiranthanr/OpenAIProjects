from openai import OpenAI
import os, openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI()

completion = client.chat.completions.create(
    model = "gpt-4",
    messages = [
    {"role": "system", "content":"You are an expert python programmer good at explaining details of how various python libraries work and how they can be utilized for various use cases"},
    {"role": "user", "content":"Teach me how to write a program for an application that can take input from images and provide key data elements from the image and store them as key-value pairs and save the result as a json file"}
    ]
)   

print(completion.choices[0].message)