from transformers import pipeline

# Load FLAN-T5 model only once
generator = pipeline(
    "text2text-generation",
    model="google/flan-t5-base"
)


def generate_quiz(content, difficulty, num_questions=5):
    """
    Generates MCQs from uploaded notes or a topic.
    """

    prompt = f"""
You are an AI teacher.

Create exactly {num_questions} {difficulty} multiple-choice questions from the following content.

Rules:

- Each question should have exactly 4 options.
- Mention the correct answer.
- Give a short explanation.
- Do not repeat questions.
- Keep questions clear and student-friendly.

Use this format exactly:

Question 1:
A.
B.
C.
D.

Correct Answer:
Explanation:

Question 2:
A.
B.
C.
D.

Correct Answer:
Explanation:

Content:

{content[:1800]}
"""

    try:

        result = generator(
            prompt,
            max_length=1024,
            do_sample=False
        )

        return result[0]["generated_text"]

    except Exception as e:

        return f"Error generating quiz:\n\n{e}"