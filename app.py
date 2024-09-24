from flask import Flask, render_template, request
from langdetect import detect
from googletrans import Translator, LANGUAGES

app = Flask(__name__)

def detect_and_translate(text, target_lang):
    try:
        # Detect language
        detected_lang = detect(text)

        # Translate language
        translator = Translator()
        translated_text = translator.translate(text, dest=target_lang).text

        return detected_lang, translated_text
    except Exception as e:
        return None, f"Error: {str(e)}"

@app.route('/')
def index():
    # Render the form with available languages
    return render_template('index.html', languages=LANGUAGES)

@app.route('/trans', methods=['POST'])
def trans():
    # Extract form data
    text = request.form['text']
    target_lang = request.form['target_lang']
    
    # Detect language and translate
    detected_lang, translation = detect_and_translate(text, target_lang)

    # Render the results
    return render_template('index.html', translation=translation, detected_lang=detected_lang, languages=LANGUAGES)

if __name__ == '__main__':
    app.run(debug=True)
