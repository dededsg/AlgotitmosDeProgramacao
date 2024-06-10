import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "sk-proj-WPQY5NaCIX5ediKvXaZPT3BlbkFJ00zmPNMM3NEkKHuXq3Gw"

client = OpenAI()

response = client.chat.completions.create(
  model="gpt-3.5-turbo-instruct",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]
)

print(response)