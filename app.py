import speech_recognition as sr
import openai

recording = sr.Recognizer()

with sr.Microphone() as source: 
    recording.adjust_for_ambient_noise(source)
    print("Please Say something:")
    audio = recording.listen(source)
    answer = recording.recognize_google(audio)
    try:
        print("You said: " + answer)
    except Exception as e:
        print(e)

openai.api_key = ""

completion = openai.Completion.create(engine="text-davinci-003",
                         prompt=answer,
                         max_tokens="2048")

print(completion.choices[0].text)
