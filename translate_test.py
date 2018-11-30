import os
import sys

import google.cloud.translate as translate


os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.curdir, 'creds.json')
translate_client = translate.Client()



text = "Random test"
target = 'es'

translation = translate_client.translate(text,target_language=target)

detect = translate_client.detect_language(text)

print(translation['translatedText'])
