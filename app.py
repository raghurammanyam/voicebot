import dialogflow 
import speech_recognition as sr
import pyttsx3
import os
from gtts import gTTS
export GOOGLE_APPLICATION_CREDENTIALS=/home/caratred/Downloads/voicechat-rxcihi-655967653fc9.json

# engine = pyttsx3.init() 
r = sr.Recognizer()
def detect_intent_audio(project_id,session_id, audio_file_path,
                        language_code):
    """Returns the result of detect intent with an audio file as input.

    Using the same `session_id` between requests allows continuation
    of the conversaion."""
    import dialogflow_v2 as dialogflow

    session_client = dialogflow.SessionsClient()

    # Note: hard coding audio_encoding and sample_rate_hertz for simplicity.
    audio_encoding = dialogflow.enums.AudioEncoding.AUDIO_ENCODING_LINEAR_16
    sample_rate_hertz = 16000

    session = session_client.session_path(project_id, session_id)
    print('Session path: {}\n'.format(session))

    with open(audio_file_path, 'rb') as audio_file:
        input_audio = audio_file.read()

    audio_config = dialogflow.types.InputAudioConfig(
        audio_encoding=audio_encoding, language_code=language_code,
        sample_rate_hertz=sample_rate_hertz)
    query_input = dialogflow.types.QueryInput(audio_config=audio_config)

    response = session_client.detect_intent(
        session=session, query_input=query_input,
        input_audio=input_audio)

    print('=' * 20)
    print('Query text: {}'.format(response.query_result.query_text))
    print('Detected intent: {} (confidence: {})\n'.format(
        response.query_result.intent.display_name,
        response.query_result.intent_detection_confidence))
    print('Fulfillment text: {}\n'.format(
        response.query_result.fulfillment_text))
    abc = response.query_result.fulfillment_text
    print(abc)
    # tts = gTTS(text=abc, lang='en')
    # tts.save("good.mp3")
    # os.system("good.mp3")
    engine = pyttsx3.init() 
    engine.setProperty('rate',150)
    engine.setProperty('volume', 1.0)
    engine.say(abc)
    # engine.setProperty('rate',120)
    # engine.setProperty('volume', 1.5)
    engine.runAndWait()
    # engine.stop()
    

def audiocatch():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
        print(audio)
    with open("/home/caratred/microphone-results.wav", "wb") as f:
        f.write(audio.get_wav_data())
# audiocatch()  
detect_intent_audio('voicechat-rxcihi','655967653fc9c445a3240194a9a39b1272c16c79','/home/caratred/Downloads/how.wav','en')





