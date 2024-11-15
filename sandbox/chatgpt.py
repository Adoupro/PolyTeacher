import requests
import google.generativeai as genai
import os

# Set the API key correctly
api_key = "AIzaSyA1jUeGvh0MoAzY7y_iz8XQvb6NM89xjnI"
genai.configure(api_key=api_key)

model = "gpt-4o-mini"
prompt = "Here the prompt to send to chatgpt"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
parameters = {
    "model": model,
    "prompt": prompt,
    "max_tokens": 100
}
model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Write a story about a magic backpack.")
print(response.text)

response = requests.post("https://api.openai.com/v1/completions", headers=headers, json=parameters).json()
