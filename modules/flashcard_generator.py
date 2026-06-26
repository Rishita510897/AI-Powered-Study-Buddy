# modules/flashcard_generator.py

from transformers import pipeline

# Load the model only once
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def generate_flashcards(content, num_cards=10):
    """
    Generate flashcards from a topic or uploaded notes.

    Parameters:
        content (str): Topic name or study notes.
        num_cards (int): Number of flashcards to generate.

    Returns:
        str: Generated flashcards.
    """

    if not content.strip():
        return "Please provide a topic or upload study notes."

    prompt = f"""
You are an expert study assistant.

Create exactly {num_cards} educational flashcards from the following study material.

Instructions:
- Keep each answer short (1-3 sentences).
- Cover important concepts.
- Do not repeat questions.
- Use simple language suitable for students.

Format exactly like this:

Flashcard 1
Q: ...
A: ...

Flashcard 2
Q: ...
A: ...

Study Material:

{content[:1800]}
"""

    try:

        result = generator(
            prompt,
            max_length=1024,
            do_sample=False,
            temperature=0.3
        )

        return result[0]["generated_text"]

    except Exception as e:

        return f"Error generating flashcards:\n\n{e}"