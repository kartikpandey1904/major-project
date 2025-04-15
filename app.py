from flask import Flask, request, jsonify, render_template, send_from_directory
import os
import time
import pyttsx3
from googletrans import Translator

app = Flask(__name__)

# Language dictionary (unchanged)
lang_dict ={
    'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
    'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
    'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
    'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
    'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
    'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht',
    'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu',
    'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja',
    'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish': 'ku',
    'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb',
    'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi',
    'marathi': 'mr', 'mongolian': 'mn', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
    'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
    'samoan': 'sm', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si',
    'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw',
    'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk',
    'urdu': 'ur', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo',
    'zulu': 'zu'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    data = request.json
    query = data.get('query')
    to_lang = data.get('to_lang').lower()

    if to_lang in lang_dict:
        to_lang_code = lang_dict[to_lang]
    else:
        return jsonify({'error': 'Language not supported'}), 400

    try:
        translator = Translator()
        translated = translator.translate(query, dest=to_lang_code)
        translated_text = translated.text

        # Generate audio file name
        audio_filename = f'captured_voice_{int(time.time())}.mp3'
        audio_file_path = os.path.join('static', audio_filename)

        # Text to Speech using pyttsx3 (offline)
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)  # Speaking speed
        engine.save_to_file(translated_text, audio_file_path)
        engine.runAndWait()

        return jsonify({
            'translated_text': translated_text,
            'audio_file': f'/static/{audio_filename}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(debug=True)
