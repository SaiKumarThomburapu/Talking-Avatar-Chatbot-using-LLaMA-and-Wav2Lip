# 🧠 Talking Avatar Chatbot using LLaMA and Wav2Lip

This project is an AI-powered chatbot that responds to user queries with a **lipsynced talking avatar video**. It combines advanced natural language generation with deep learning-based video synthesis to create a more engaging user experience.

---

## 🚀 Features

- Conversational interface powered by a local LLaMA 3.2 model via Ollama
- Generates text responses and converts them to speech using `pyttsx3`
- Uses Wav2Lip (via subprocess) to create realistic lipsynced avatar videos
- Simple and intuitive UI using Streamlit
- Cross-environment execution: LLM runs in Python 3.12, Wav2Lip in Python 3.10

---

## 🧰 Technologies Used

- [Python 3.12.2](https://www.python.org/)
- [LangChain](https://python.langchain.com/)
- [Ollama](https://ollama.com/)
- [Wav2Lip](https://github.com/Rudrabha/Wav2Lip) (runs in Python 3.10)
- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [Streamlit](https://streamlit.io/)

---

## 🗂️ Project Structure

├── project.py # Main Streamlit app
├── avatar.mp4 # Static avatar face video
├── bot.wav # TTS-generated audio for the bot's answer
├── bot_lipsynced.mp4 # Final output video (lip-synced avatar)
├── inference.py # Wav2Lip inference script (Python 3.10)
├── checkpoints/
│ └── wav2lip.pth # Pretrained Wav2Lip model



---

## 🔧 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/talking-avatar-chatbot.git
cd talking-avatar-chatbot

2. Install Python 3.12 Dependencies
In your base environment (Python 3.12), install required packages:

###Install Python 3.12 Dependencies
bash
pip install streamlit pyttsx3 langchain

### Set Up Wav2Lip (Python 3.10 Environment)

Create a separate Python 3.10 environment.
Clone and install Wav2Lip and its dependencies.
Download the model file wav2lip.pth and place it under checkpoints/.

#Bash#
conda create -n wav python=3.10
conda activate wav
pip install -r requirements.txt  # Wav2Lip requirements

#Ensure Ollama is Running
Make sure Ollama is active and running LLaMA 3.2:
#Bash#
ollama run llama3

#Run the Streamlit App
streamlit run project.py







