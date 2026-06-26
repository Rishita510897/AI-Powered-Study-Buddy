# modules/summarizer.py

import re
import streamlit as st
from transformers import pipeline


# --------------------------------------------------
# Load Summarization Model (Cached)
# --------------------------------------------------

@st.cache_resource
def load_summarizer():
    """
    Load the summarization model only once.
    """
    return pipeline(
        task="summarization",
        model="facebook/bart-large-cnn"
    )


# --------------------------------------------------
# Clean Text
# --------------------------------------------------

def clean_text(text):
    """
    Remove extra spaces and unwanted characters.
    """
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# --------------------------------------------------
# Split Long Text into Chunks
# --------------------------------------------------

def split_text(text, chunk_size=700):
    """
    Split text into smaller chunks.
    """

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(
            " ".join(words[i:i + chunk_size])
        )

    return chunks


# --------------------------------------------------
# Summarize One Chunk
# --------------------------------------------------

def summarize_chunk(chunk, max_length=120, min_length=40):

    summarizer = load_summarizer()

    result = summarizer(
        chunk,
        max_length=max_length,
        min_length=min_length,
        do_sample=False
    )

    return result[0]["summary_text"]


# --------------------------------------------------
# Short Summary
# --------------------------------------------------

def generate_summary(text):

    if not text.strip():
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

        return " ".join(summaries)

    except Exception as e:

        return f"Error generating summary:\n{e}"


# --------------------------------------------------
# Detailed Summary
# --------------------------------------------------

def generate_detailed_summary(text):

    if not text.strip():
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
                    min_length=80
                )
            )

        return "\n\n".join(summaries)

    except Exception as e:

        return f"Error generating detailed summary:\n{e}"


# --------------------------------------------------
# Extract Key Points
# --------------------------------------------------

def extract_key_points(text):

    summary = generate_summary(text)

    if summary.startswith("Error"):
        return [summary]

    sentences = summary.split(".")

    key_points = []

    for sentence in sentences:

        sentence = sentence.strip()

        if len(sentence) > 15:
            key_points.append(sentence)

    return key_points