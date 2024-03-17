from openai import OpenAI
from dotenv import load_dotenv
import os
from typing import Optional
from pathlib import Path
from typing import List

package_root = Path(__file__).parent.parent.parent
env_path = package_root / ".env"
load_dotenv(dotenv_path=env_path)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)


def get_rephrased(text: str, modification_degree: Optional[str] = None) -> str:
    """
    Rephrases the input text based on the specified modification degree.

    Parameters:
    - text (str): The input text to be rephrased.
    - modification_degree (Optional[str]): Specifies the degree of modification to be applied.
        Can be one of:
            - "correct-only": Corrects only grave language errors in the text.
            - "correct-with-minor-changes": Corrects errors and makes minor changes for better readability.
            - If not specified or None, performs general rephrasing without specific constraints.

    Returns:
    - str: The rephrased text based on the specified modification degree.

    Example:
    >>> get_rephrased("This is a sample text to be rephrased.", modification_degree="correct-only")
    """
    match modification_degree:
        case "correct-only":
            prompt = """
            This is part of a Latex document. Please correct the grammatical and spelling mistakes in this text.
            Please do not change any formatting or wording. As this is just a fragment, this does not have to compile as is,
            if there is syntax like \\begin or \\end statements missing, assume they are defined in other parts of the text.
            """
        case "correct-with-minor-changes":
            prompt = "what's the meaning of life"
        case _:
            prompt = "translate to russian"

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt + "\n" + text}],
    )

    return completion.choices[0].message.content


def get_splits(text: str) -> List[str]:
    return text.split("\n\n")


def get_rephrased_doc(text: str, modification_degree: str) -> str:
    """
    Take all the given text, split it into smaller chunks, rephrase them, merge the rephrased splits.
    """

    splits = get_splits(text)
    rephrased_splits = [get_rephrased(split,modification_degree) for split in splits]
    return "\n\n".join(rephrased_splits)
