import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
    version='2018-05-01', 
    authenticator=authenticator
)
translator.set_service_url(url)

def englishToFrench(englishText):
    frenchText = translator.translate(
        text=englishText, 
        source='en',
        target='fr'
    ).get_result()['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    englishText = translator.translate(
        text=frenchText, 
        source='fr',
        target='en'
    ).get_result()['translations'][0]['translation']
    return englishText