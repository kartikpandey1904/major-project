# Live Translator

A web-based live translator that converts speech to text and translates it to multiple languages using the Web Speech API and Google Translate service.

## Features

- Speech-to-text conversion
- Real-time translation
- Support for multiple languages
- Clean and intuitive interface
- No API key required

## Setup

1. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Usage

1. Click "Start Recording" to begin speech recognition
2. Speak clearly into your microphone
3. The text will be automatically translated to the selected language
4. You can also type directly into the input box
5. Select different target languages from the dropdown menu

## Supported Languages

- English
- Spanish
- French
- German
- Italian
- Portuguese
- Russian
- Chinese
- Japanese
- Korean

## Requirements

- Python 3.6+
- Modern web browser with microphone access
- Internet connection

## Note

This application uses the Web Speech API for speech recognition, which is supported in most modern browsers. The translation is handled by the googletrans library, which uses Google Translate's free service. 