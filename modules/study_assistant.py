# modules/study_assistant.py

from transformers import pipeline

# Load FLAN-T5 model once
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def answer_question(notes, question):
    """
    Answer questions using the uploaded notes.
    """

    if not notes.strip():
        return "Please upload study notes first."

    if not question.strip():
        return "Please enter a question."

    prompt = f"""
You are an intelligent study assistant.

Answer the question ONLY using the study notes below.

If the answer is not present in the notes, reply:

"The answer is not available in the uploaded notes."

Keep the answer:
- Simple
- Accurate
- Student-friendly
- Maximum 6 sentences

Study Notes:
{notes[:1800]}

Question:
{question}

Answer:
"""

    try:

        result = generator(
            prompt,
            max_length=300,
            do_sample=False
        )

        return result[0]["generated_text"]

    except Exception as e:

        return f"Error: {e}"