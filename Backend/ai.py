import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

token = os.environ["GITHUB_TOKEN"]
endpoint = "https://models.inference.ai.azure.com"
model_name = "gpt-4o-mini"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)

user_input =input("Enter your prompt: ")
response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.Who is an expert linkedin content creator? You will assist the user to generate linkedin content.Generate suitable hashtags for the given content.",
        },
        {
            "role": "user",
            "content": user_input,
        },
        # {
        #     "role": "assistant",
        #     "content": "The capital of France is Paris.",
        # },
        # {
        #     "role": "user",
        #     "content": "What about Spain?",
        # }
    ],
    model=model_name,
)

print(response.choices[0].message.content)