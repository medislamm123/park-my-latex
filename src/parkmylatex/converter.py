from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Optional
from pathlib import Path

package_root = Path(__file__).parent.parent.parent
env_path = package_root / '.env'
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def rephrase(text: str, modification_degree: Optional[str] = None) -> str:
    match modification_degree:
        case "correct-only":
            prompt = "Take this text and translate it to chinese:"  # "This is part of a latex document. You should correct only grave language errors, and return the corrected text. Ensure the latex code is correct. Here is the text:"
        case "correct-with-minor-changes":
            prompt = ""
        case _:
            prompt = ""

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + "\n" + text}],
    )

    return completion.choices[0].message.content
