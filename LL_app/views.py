import json
from os import environ
import requests
from django.shortcuts import render
from django.http import JsonResponse
from googletrans import Translator
# Create your views here.

def base(request):
    return render(request, 'base.html')
google_translate_api_key = environ.get('GOOGLE_TRANSLATE_API_KEY')

def translate_text(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf8'))
        text_to_translate = data.get('text_to_translate', 'Default text input')
        target_language = data.get('target_language', 'en')  # Default to English if not provided

        # text_to_translate = request.POST.get('text_to_translate', '')
        # target_language = request.POST.get('target_language', 'en')
        print("Target language:", target_language)
        print("Text to translate:", text_to_translate)
        if not text_to_translate.strip():
            return JsonResponse({'error': 'Text to translate is empty'}, status=400)

        # Use the detect method to identify the language of the input text
        translator = Translator()
        try:
            detected_language = translator.detect(text_to_translate)
            detected_language = detected_language.lang
        except AttributeError:
            detected_language = 'en'
        indian_languages = ['hi', 'bn', 'te', 'mr', 'ta', 'ur', 'gu', 'kn', 'or', 'ml', 'sd','pa','as','en']
        if detected_language in indian_languages:
            # Translate the text to the target language
            translation = translator.translate(text_to_translate, dest=target_language)
            print("Translated text: "+translation.text)
            return JsonResponse({'translated_text': translation.text,
                                 'source_language': detected_language})
        else:
            return JsonResponse({'error': 'Input text is not in an Indian language'})
        print("Text to translate:", text_to_translate)
        print("Detected language:", detected_language)
        print("Target language:", target_language)
        # url = "https://translation.googleapis.com/language/translate/v2/translate"
        # payload = {
        #     'q': text_to_translate,
        #     'target': target_language,
        #     'key': google_translate_api_key
        # }

        # response = requests.post(url, json=payload)
        # result = response.json()['data']['translations'][0]['translatedText']
        # print(result)
        # Check if the detected language is an Indian language
        
    else:
        return JsonResponse({'error': 'Invalid request method'})