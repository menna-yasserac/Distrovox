# Sound Operating System

**Sound Operating System** is a voice-controlled operating system interaction project developed using **Python** on **Ubuntu Linux**.

The system allows users to interact with the computer using **Arabic or English voice commands**, including opening applications, typing text, controlling the mouse and keyboard, searching the web, scrolling, closing windows, and interacting with visible screen elements using OCR.

## Features

- 🎤 Arabic & English Speech Recognition
- 🧠 NLP-based Command Processing
- 🖥️ Dynamic Linux Application Detection & Launching
- 🖱️ Mouse & Keyboard Automation
- ⌨️ Arabic & English Voice Typing
- 🌐 Web Search & Browser Control
- 📜 Screen Scrolling
- ❌ Window Closing
- 👀 OCR-based Screen Text Detection & Clicking
- 🔄 Fuzzy Matching for flexible voice commands
- ⚡ Parallel Processing for selected tasks

## 🔄 System Workflow

```text
Voice Input
     ↓
Speech Recognition
     ↓
NLP / Command Processing
     ↓
Target Detection
     ↓
Command Execution
     ↓
System Interaction
```

## Technologies & Libraries

| Library / Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **SpeechRecognition** | Speech-to-text recognition |
| **PyAudio** | Microphone/audio input |
| **PyAutoGUI** | Mouse and keyboard automation |
| **Pyperclip** | Clipboard-based text input |
| **Pytesseract** | OCR and screen text recognition |
| **Pillow (PIL)** | Image processing |
| **Pydbus** | D-Bus communication and screenshot portal |
| **GLib** | Event loop for D-Bus operations |
| **re** | Command parsing and pattern matching |
| **difflib** | Fuzzy string matching |
| **subprocess** | Linux command execution |
| **os** | Operating-system and file operations |
| **shlex** | Safe command parsing |
| **webbrowser** | Browser control |
| **urllib.parse** | URL and search-query encoding |
| **ThreadPoolExecutor** | Parallel task execution |
| **Linux `.desktop` files** | Dynamic application discovery |
| **gtk-launch** | Linux application launching |

## 💻 Requirements

- Ubuntu Linux
- Python 3
- Working microphone
- Internet connection for speech recognition
- Tesseract OCR
- Required Python libraries

## Installation

Clone the repository:

```bash
git clone <REPOSITORY-URL>
cd <PROJECT-FOLDER>
```

Install the required Python packages:

```bash
pip3 install SpeechRecognition PyAutoGUI pyperclip Pillow pytesseract PyAudio pydbus --break-system-packages
```

Install the required Linux packages:

```bash
sudo apt update
sudo apt install portaudio19-dev python3-dev tesseract-ocr tesseract-ocr-eng tesseract-ocr-ara python3-tk -y
```

## ▶️ Run

Start the project with:

```bash
python3 project.py
```

Then speak an Arabic or English command through the microphone.

## 🧩 Project Structure

```text
Sound-Operating-System/
│
├── project.py
├── test_mic.py
├── test_input.py
├── test_ocr.py
├── portal_screenshot.py
├── portal_test.py
├── screenshot_test.py
└── README.md
```

## Team

The project is divided into multiple sprints covering:

- Voice Recognition & Audio Input
- NLP / Command Processing
- Linux Application Control
- Mouse & Keyboard Automation
- Screenshot & OCR
- Web & Search Control
- System Integration, Testing & Final Demo

## 🎯 Project Goal

The goal of **Sound Operating System** is to provide a flexible voice-based interface for interacting with a Linux desktop, reducing the need for traditional mouse and keyboard interaction and supporting both **Arabic and English users**.
