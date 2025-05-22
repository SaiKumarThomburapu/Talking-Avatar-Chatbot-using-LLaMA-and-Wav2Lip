import os
import subprocess
import time
import pyttsx3
import streamlit as st
from langchain_community.llms import Ollama

# Configuration
AVATAR_VIDEO = "avatar.mp4"
CHECKPOINT_PATH = "checkpoints/wav2lip.pth"
PYTHON_3_10_PATH = r"C:\Users\Mastan\anaconda3\envs\wav\python.exe"
OUTPUT_AUDIO = "bot.wav"
OUTPUT_VIDEO = "bot_lipsynced.mp4"

# Initialize LLM
llm = Ollama(model="llama3.2")

# Text-to-Speech
def synthesize_speech(text, output_audio_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_audio_path)
    engine.runAndWait()
    for _ in range(10):
        if os.path.exists(output_audio_path) and os.path.getsize(output_audio_path) > 1000:
            break
        time.sleep(0.5)

# Run Wav2Lip subprocess
def generate_lipsynced_video(audio_path, output_path):
    command = [
        PYTHON_3_10_PATH, "inference.py",
        "--checkpoint_path", CHECKPOINT_PATH,
        "--face", AVATAR_VIDEO,
        "--audio", audio_path,
        "--outfile", output_path
    ]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode != 0:
        raise RuntimeError(f"Wav2Lip error:\n{result.stderr.decode()}")
    for _ in range(10):
        if os.path.exists(output_path) and os.path.getsize(output_path) > 1000:
            break
        time.sleep(0.5)

# Main app
st.set_page_config(page_title="Lipsync Avatar Chatbot", layout="centered")
st.title("🧠 Talking Avatar Chatbot")
st.write("Ask your question and get a lipsynced video response from an AI avatar.")

user_input = st.text_input("Your question", placeholder="Type your question here...")

if st.button("Generate Response"):
    if user_input.strip():
        with st.spinner("Thinking..."):
            answer = llm.invoke(user_input)
            st.session_state["answer"] = answer
            synthesize_speech(answer, OUTPUT_AUDIO)
            generate_lipsynced_video(OUTPUT_AUDIO, OUTPUT_VIDEO)

        st.success("Here is your response!")
        st.video(OUTPUT_VIDEO)
        st.caption("💬 " + answer)
    else:
        st.warning("Please enter a question.")
