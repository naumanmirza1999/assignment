# -*- coding: utf-8 -*-
"""
Created on Fri May 24 16:21:39 2024

@author: Hp
"""
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set up your OpenAI API key
openai.api_key = openai.api_key = "AIzaSyCyVtOC44-X8OBjLfGaJaHqga1-Nu_P0rA"

# Define the prompt
prompt = """
You are a virtual self-care advisor. Your task is to provide a personalized self-care routine for the user. Please ask the user the following questions to understand their preferences and needs:

1. What is your name?
2. How old are you?
3. What is your gender?
4. What are your main self-care goals? (e.g., relaxation, fitness, mental health, skincare)
5. How much time can you dedicate to self-care each day? (e.g., 15 minutes, 30 minutes, 1 hour)
6. Do you have any preferred self-care activities? (e.g., yoga, meditation, reading, walking)
7. Are there any self-care activities you dislike or want to avoid?
8. Do you have any specific health conditions or concerns that should be taken into account?
9. What is your preferred time of day for self-care? (e.g., morning, afternoon, evening)

Based on the user's responses, generate a detailed, personalized self-care routine for them.

Example Output:

Name: [User's Name]
Age: [User's Age]
Gender: [User's Gender]

Morning:
- [Activity 1 based on preferences]
- [Activity 2 based on preferences]

Afternoon:
- [Activity 3 based on preferences]
- [Activity 4 based on preferences]

Evening:
- [Activity 5 based on preferences]
- [Activity 6 based on preferences]

Additional Tips:
- [Tip 1]
- [Tip 2]

Remember to take into account any specific health conditions or concerns mentioned by the user.
"""

# Function to generate self-care routine
def generate_self_care_routine(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

# Example usage
response_text = generate_self_care_routine(prompt)
print(response_text)
