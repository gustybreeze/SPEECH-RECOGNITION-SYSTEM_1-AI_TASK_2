import speech_recognition as sr

#created a recognizer object
recognizer = sr.Recognizer()

#loaded a .wav file 
audio_file = "c:\codtech_internship\my codes\samp_aud.wav"

#process the audio
with sr.AudioFile(audio_file) as source:
    audio_data = recognizer.record(source)
    print("Recognizing...")

    try:
        #transcribe using Google's recognizer
        text = recognizer.recognize_google(audio_data)
        print("Transcribed Text:")
        print(text)
    except sr.UnknownValueError:
        print("Speech could not be understood.")
    except sr.RequestError:
        print("API unavailable or network error.") 