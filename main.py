import time
import streamlit as st
import json

def load_lessons(file_path):
    with open(file_path, 'r') as file:
        lessons = json.load(file)
    return lessons

st.title('📝 Python Quiz Application')

# Load lessons from JSON file
lessons = load_lessons('lessons.json')

selected_lesson = st.sidebar.selectbox("Select a lesson", list(lessons.keys()))
questions = lessons[selected_lesson]

if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0  # Initialize question index
    st.session_state.score = 0  # Initialize score

question = questions[st.session_state.current_question_index]
st.subheader(question["question"])
selected_option = st.radio("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!")
        st.session_state.score += 1  # Increment score for correct answer
    else:
        st.error("❌ Incorrect! The correct answer is: " + question["answer"])
    
    time.sleep(2)
    st.session_state.current_question_index += 1  # Move to the next question
    if st.session_state.current_question_index < len(questions):
        st.rerun()  # Use experimental_rerun for Streamlit 0.10.0+
    else:
        st.success(f"Lesson completed! Your score is: {st.session_state.score}/{len(questions)}")
        st.session_state.score = 0  # Reset score for the next lesson
        st.session_state.current_question_index = 0  # Reset question index for the next lesson
