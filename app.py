import streamlit as st

from modules.pdf_reader import extract_text_from_pdf
from modules.summarizer import (
    generate_summary,
    generate_detailed_summary,
    extract_key_points,
)

from modules.study_assistant import answer_question
from modules.quiz_generator import generate_quiz
from modules.flashcard_generator import generate_flashcards


# ----------------------------------------------------
# Page Configuration
# ----------------------------------------------------

st.set_page_config(
    page_title="AI Powered Study Buddy",
    page_icon="📚",
    layout="wide",
)

# ----------------------------------------------------
# Session State
# ----------------------------------------------------

if "notes" not in st.session_state:
    st.session_state.notes = ""

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False


# ----------------------------------------------------
# Sidebar
# ----------------------------------------------------

st.sidebar.title("📚 Study Buddy")

menu = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "📂 Upload Notes",
        "📄 Summarizer",
        "💬 Study Assistant",
        "❓ Quiz Generator",
        "📝 Flashcards",
    ],
)
# ----------------------------------------------------
# Home
# ----------------------------------------------------

if menu == "🏠 Home":

    st.title("📚 AI Powered Study Buddy")

    st.subheader("Your Personal AI Learning Assistant")

    st.write(
        """
This application helps students learn faster using Artificial Intelligence.

### Features

✅ Upload PDF Notes

✅ AI Summarizer

✅ Ask Questions from Notes

✅ Quiz Generator

✅ Flashcard Generator
"""
    )
# ----------------------------------------------------
# Upload PDF
# ----------------------------------------------------

elif menu == "📂 Upload Notes":

    st.title("📂 Upload Study Notes")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
    )

    if uploaded_file is not None:

        with st.spinner("Extracting text..."):

            text = extract_text_from_pdf(uploaded_file)

        if len(text) == 0:

            st.error("No text found in PDF.")

        else:

            st.session_state.notes = text

            st.session_state.pdf_uploaded = True

            st.success("PDF uploaded successfully!")

            st.write(f"Characters Extracted : {len(text)}")

            st.text_area(
                "Preview",
                text[:3000],
                height=300,
            )


# ----------------------------------------------------
# Summarizer
# ----------------------------------------------------

elif menu == "📄 Summarizer":

    st.title("📄 AI Notes Summarizer")

    if not st.session_state.pdf_uploaded:

        st.warning("Please upload a PDF first.")

    else:

        option = st.selectbox(
            "Select Summary Type",
            [
                "Short Summary",
                "Detailed Summary",
                "Key Points",
            ],
        )

        if st.button("Generate"):

            with st.spinner("Generating..."):

                if option == "Short Summary":

                    summary = generate_summary(
                        st.session_state.notes
                    )

                    st.success("Done!")

                    st.write(summary)

                elif option == "Detailed Summary":

                    summary = generate_detailed_summary(
                        st.session_state.notes
                    )

                    st.success("Done!")

                    st.write(summary)

                else:

                    points = extract_key_points(
                        st.session_state.notes
                    )

                    st.success("Done!")

                    for p in points:
                        st.markdown(f"• {p}")

# ----------------------------------------------------
# Study Assistant
# ----------------------------------------------------

elif menu == "💬 Study Assistant":

    st.title("💬 AI Study Assistant")

    if not st.session_state.pdf_uploaded:

        st.warning("⚠ Please upload your study notes first.")

    else:

        st.success("📄 Notes loaded successfully!")

        question = st.text_input(
            "Ask a question from your notes",
            placeholder="Example: What is Machine Learning?"
        )

        st.markdown("### Suggested Questions")

        col1, col2 = st.columns(2)

        with col1:

            if st.button("What is the main topic?"):
                question = "What is the main topic?"

            if st.button("Explain the important concepts"):
                question = "Explain the important concepts."

        with col2:

            if st.button("What are the advantages?"):
                question = "What are the advantages?"

            if st.button("Give a quick revision"):
                question = "Give a quick revision."

        if question:

            if st.button("Get Answer", use_container_width=True):

                with st.spinner("Thinking..."):

                    answer = answer_question(
                        st.session_state.notes,
                        question
                    )

                st.success("Answer Generated")

                st.markdown("### Answer")

                st.write(answer)
# ----------------------------------------------------
# Quiz Generator
# ----------------------------------------------------
elif menu == "❓ Quiz Generator":

    st.title("❓ AI Quiz Generator")

    if not st.session_state.pdf_uploaded:

        st.warning("⚠ Upload a PDF first.")

    else:

        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

        questions = st.slider(
            "Number of Questions",
            5,
            10,
            5
        )

        if st.button("Generate Quiz", use_container_width=True):

            with st.spinner("Generating Quiz..."):

                quiz = generate_quiz(
                    st.session_state.notes,
                    difficulty,
                    questions
                )

            st.success("Quiz Generated")

            st.markdown(quiz)

# ----------------------------------------------------
# Flashcards
# ----------------------------------------------------

elif menu == "📝 Flashcards":

    st.title("📝 AI Flashcard Generator")

    if not st.session_state.pdf_uploaded:

        st.warning("⚠ Please upload a PDF first.")

    else:

        num_cards = st.slider(
            "Number of Flashcards",
            min_value=5,
            max_value=20,
            value=10
        )

        if st.button("Generate Flashcards", use_container_width=True):

            with st.spinner("Generating Flashcards..."):

                cards = generate_flashcards(
                    st.session_state.notes,
                    num_cards
                )

            st.success("✅ Flashcards Generated Successfully!")

            st.markdown(cards)