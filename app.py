from flask import Flask, render_template, request, jsonify, send_file
from googletrans import Translator
from gtts import gTTS
import os

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    try:
        text = request.json.get('text', '')
        target_lang = request.json.get('target_lang', 'en')
        
        detected = translator.detect(text)
        source_lang = detected.lang
        
        translation = translator.translate(text, dest=target_lang)
        
        return jsonify({
            'original_text': text,
            'translated_text': translation.text,
            'source_language': source_lang,
            'target_language': target_lang
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/synthesize', methods=['POST'])
def synthesize():
    try:
        text = request.json.get('text', '')
        lang = request.json.get('lang', 'en')  
        
        tts = gTTS(text=text, lang=lang)
        audio_file = "output.mp3"
        tts.save(audio_file)
        
        return send_file(audio_file, mimetype="audio/mpeg", as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)