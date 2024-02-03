from openai import OpenAI
from typing import Optional

client = OpenAI()

def rephrase(text:str, modification_degree:Optional[str] = None)-> str:

    match modification_degree:
        case "correct-only":
            prompt = ""
        case "correct-with-minor-changes":
            prompt = ""
        case _:
            prompt = ""

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt + "\n" + text}
    ]
    )

    print(completion.choices[0].message)