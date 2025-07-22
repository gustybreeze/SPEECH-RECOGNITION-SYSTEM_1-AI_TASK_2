# SPEECH-RECOGNITION-SYSTEM-1-AI-TASK-2

COMPANY: CODTECH IT SOLUTIONS PVT.LTD

NAME: SAMEER KUMAR MISHRA

INTERN ID: CT04DZ379

DOMAIN: PYTHON PROGRAMMING

DURATION: 4 WEEKS

MENTOR: NEELA SANTHOSH KUMAR


**Overview**
The Speech Recognition System is a key application of Artificial Intelligence that enables machines to interpret and process human speech. In this task, I developed a basic speech recognition tool using Python that takes spoken audio input through the microphone and converts it into text format. This system mimics human hearing and comprehension, bridging the gap between human interaction and computer systems.

Speech recognition has wide applications in real-life scenarios, including voice assistants like Google Assistant and Siri, transcription tools, smart home control, and accessibility tools for differently-abled individuals. This project focuses on developing a simple, functional model that recognizes English speech and converts it into readable and editable text using open-source libraries.


**Objectives**
- To understand how AI models interpret and process human speech signals.

- To implement a speech-to-text converter using Python and widely-used libraries.

- To explore real-time audio input through microphones and offline audio files.

- To enhance hands-on experience with speech processing libraries and APIs.

- To understand limitations like noise sensitivity, accent variation, and language models.


**Tools & Technologies Used**
- Python 3.10+: Programming language used for implementation.

- SpeechRecognition: Python library for performing speech recognition.

- PyAudio: For accessing the microphone and handling real-time audio input.

- Google Web Speech API: For cloud-based speech recognition (used via SpeechRecognition wrapper).

- Tkinter (Optional): For GUI interface to record and display converted text.

- Jupyter Notebook / .py Script: For demonstration and experimentation.


**Methodology**
1. Setup and Library Installation
Before starting, necessary Python libraries were installed using pip, such as:

bash
Copy
Edit
pip install SpeechRecognition
pip install pyaudio
Note: PyAudio installation can vary based on OS.

2. Capturing Speech Input
We used the Microphone() class from the speech_recognition module to record audio input in real-time. The system uses the default system microphone, and listens until silence or a timeout is detected.

python
Copy
Edit
with sr.Microphone() as source:
    print("Speak now...")
    audio = recognizer.listen(source)

3. Recognizing Speech
The captured audio is passed to a recognizer object which uses Google’s Web Speech API (or any other API) to transcribe the spoken words into text.

python
Copy
Edit
text = recognizer.recognize_google(audio)
print("You said: ", text)

4. Error Handling
The system was configured to handle common exceptions like:

UnknownValueError: If speech is unclear.

RequestError: If API connection fails.

5. Optional GUI Implementation
For a user-friendly experience, a basic Tkinter interface was designed where users could click a "Record" button and see the converted text displayed in a text box.


**Results & Outcomes**
- Successfully recorded and transcribed speech from real-time microphone input.

- The transcription accuracy was satisfactory for clear and short speech.

- Implemented simple noise-handling by adjusting ambient noise threshold.

- Optional GUI helped users interact with the tool without coding knowledge.


**Learnings & Insights**
- Gained hands-on experience with real-time audio processing and API-based AI models.

- Understood the workflow of converting sound waves into machine-readable formats.

- Learned how machine learning models use acoustic models and language models together to understand speech.

- Realized the impact of background noise, pronunciation, and microphone quality on the accuracy of speech recognition.

- Built the foundation to explore more advanced features like multilingual speech recognition, command control systems, and continuous speech-to-text streaming.


**Conclusion**

This task helped me explore one of the most interactive domains of AI: speech interfaces. I developed a deeper appreciation for the complexities behind seemingly simple voice assistants and built a working model that demonstrates how machines can understand human speech. The tool can be further extended with features like saving transcripts, language switching, and using offline recognizers for improved privacy and control.


**Output**
<img width="1918" height="985" alt="Image" src="https://github.com/user-attachments/assets/9b1735dd-e4dd-4fdb-bb41-d06cee529c1a" />
