# Audio Module – Voxy

## Overview

The Audio Module is responsible for capturing user speech and converting it into text to support voice-controlled interaction with the operating system.

This module is part of **The Sound Operating System** graduation project, which aims to enable users to interact with the operating system through voice commands instead of relying entirely on a keyboard and mouse.

## Files

- `smart_record.py`: The initial audio recording implementation, developed and tested as part of the audio module.
- `audio_service.py`: The audio service used to record speech and transcribe it into text using Faster-Whisper.
- `smart_record.wav`: A sample audio recording, included only if required for testing.

## Features

- Records audio through the microphone.
- Detects when the user stops speaking and automatically ends the recording.
- Converts recorded speech into text using Faster-Whisper.
- Returns the transcription to the application for further processing.
- Supports integration with the Voxy graphical user interface.

## Technologies

- Python
- Faster-Whisper
- SoundDevice
- NumPy

## Setup

1. Navigate to the project directory.
2. Activate the Python virtual environment.
3. Install the required dependencies listed in `requirements.txt`.
4. Ensure that a working microphone is available and accessible to the application.

Example:

```bash
cd ~/OS
source .venv/bin/activate
pip install -r requirements.txt
```

## Integration

The `audio_service.py` module provides the audio functionality used by the Voxy GUI.

The application calls the audio service to record speech and obtain its transcription. The resulting text can then be passed to the command-processing component for interpretation and execution.

## Notes

- The Faster-Whisper model must be available locally or downloaded when required by the application.
- Audio recordings used only for testing do not need to be included unless they are required to reproduce a test.
- The Python virtual environment should not be uploaded to the repository.
- Keep dependencies documented in `requirements.txt` to help team members configure their environments.

## Project

**The Sound Operating System**

Audio Module – Voice Recording and Speech-to-Text Integration
