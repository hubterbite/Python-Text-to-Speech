from gtts import gTTS # Import the required module for text to speech conversion
import os # This module is imported so that we can play the converted audio
import time
language = 'en'
def ttspage():
    print(time.time())
    date = time.time()
    print('What do you need to page?')
    mytext = input() # The text that you want to convert to audio

    # save & play the stuff
    myobj = gTTS(text=mytext, lang=language, slow=False)
    myobj.save(str(date) + ".mp3")
    os.system('start ' + str(date) + '.mp3')
    print('\n')