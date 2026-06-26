# modules/summarizer.py

from transformers import pipeline
import re

# Load the model only once
summarizer = pipeline(
    "summarization",
    model="facebook/bart-large-cnn"
)


# --------------------------------------------------
# Clean extracted text
# --------------------------------------------------

def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()


# --------------------------------------------------
# Split large text into chunks
# --------------------------------------------------

def split_text(text, chunk_size=900):

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):

        chunks.append(
            " ".join(words[i:i + chunk_size])
        )

    return chunks


# --------------------------------------------------
# Generate summary for one chunk
# --------------------------------------------------

def summarize_chunk(chunk,
                    max_length=120,
                    min_length=40):

    result = summarizer(
        chunk,
        max_length=max_length,
        min_length=min_length,
        do_sample=False,
    )

    return result[0]["summary_text"]


# --------------------------------------------------
# Short Summary
# --------------------------------------------------

def generate_summary(text):

    if not text:

        return "No text available."

    text = clean_text(text)

    chunks = split_text(text)

    summaries = []

    try:

        for chunk in chunks:

            summaries.append(
                summarize_chunk(
                    chunk,
                    max_length=120,
                    min_length=40
                )
            )

        final_summary = " ".join(summaries)

        return final_summary

    except Exception as e:

        return f"Error: {e}"


# --------------------------------------------------
# Detailed Summary
# --------------------------------------------------

def generate_detailed_summary(text):

    if not text:

        return "No text available."

    text = clean_text(text)

    chunks = split_text(text)

    summaries = []

    try:

        for chunk in chunks:

            summaries.append(
                summarize_chunk(
                    chunk,
                    max_length=220,
                    min_length=100
                )
            )

        return "\n\n".join(summaries)

    except Exception as e:

        return f"Error: {e}"


# --------------------------------------------------
# Key Points
# --------------------------------------------------

def extract_key_points(text):

    summary = generate_summary(text)

    sentences = summary.split(".")

    points = []

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 10:

            points.append(sentence)

    return points