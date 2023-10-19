# Python Speech Recognition

 This project mainly focuses on using different speech recognition libraries.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install SpeechRecognition.

```bash
pip install SpeechRecognition
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install playsound.

```bash
pip install playsound
```


## Usage

```python
import speech_recognition as sr
AUDIO_FILE=("aud.wav")
r=sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio=r.record(source)
print("audio file contains"+ r.recognize_google(audio))
```

```python
from playsound import playsound
playsound("song.wav")

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.



## License

[MIT](https://choosealicense.com/licenses/mit/)
