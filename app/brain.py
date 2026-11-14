import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

MODEL = "groq/openai/gpt-oss-20b"

SYSTEM_PROMPT = """
You are Sahood's Assistant ProGPT_MODv1.

You are an intelligent, friendly and powerful personal AI assistant.
Your creator is Sahood.

Answer clearly, accurately and intelligently.
"""

def ask_ai(message, history=None):

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT}
    ]

    if history:
        messages.extend(history)

    messages.append({
        "role": "user",
        "content": message
    })

    response = completion(
        model=MODEL,
        messages=messages,
        api_key=os.getenv("GROQ_API_KEY")
    )

    return response.choices[0].message.content
