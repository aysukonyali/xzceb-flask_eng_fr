''' creates an IBM Watson instance and translates en to fr and fr to en'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2022-07-17',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def e2f_translator(english_text):
    ''' translates English text to French text'''
    if(english_text==""):
        return ""
    translation = language_translator.translate(
    english_text,
    model_id='en-fr').get_result()
    french_text=translation.get('translations')[0].get('translation')
    return french_text

def f2e_translator(french_text):
    ''' translates French text to English text'''
    if(french_text==""):
        return ""
    translation = language_translator.translate(
    french_text,
    model_id='fr-en').get_result()
    english_text=translation.get('translations')[0].get('translation')
    return english_text 