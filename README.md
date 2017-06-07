# Speake3

Speake3 library provides a wrapper around Espeak to easily
write efficient programs utilizing the text-to-speech functionalities
of espeak tts engine in Python.

## Installation

### Requirements
```
 - Linux system
 - Espeak
 - python3.x
```
### Install commands
If pip is installed simply do;
````
 pip3 install speake3
````


## Quick start
A simple script using speake module;

````
>>> import speake3
>>> 
>>> engine = speake3.Speake() # Initialize the speake engine
>>> engine.set('voice', 'en')
>>> engine.set('speed', '107')
>>> engine.set('pitch', '99')
>>> engine.say("Hello world!") #String to be spoken
>>> engine.talkback()
````

You can view the version of espeak installed;

````
 >>> engine.get("version")
````

You  can view voices installed in your system both generally and specifially;

````
 >>> voices = engine.get("voices") # General
 >>> for voice in voices:
 >>>	print voice 
 >>> voices_2 = engine.get("voices", "en") # Specific
 >>> for voice in voices_2:
 >>>	print voice
 ````

 You can set properties using set method;

````
 >>> engine.set("voice", "en") # voice attribute can be any VoiceName value or 
 >>>			   #File value gotten from the voices dictionaries
````
    
Possible attributes that can be set are:```textfile, stdin, amplitude, wordgap, 
capitals, line-length, pitch, speed, voice, wavfile, stdout, version, voices, text-encoding, 
markup, quiet, punct, split, write-pm, nopause```

Properties that have been set can also be unset;

````
 >>> engine.unset("speed")
 >>> engine.unset("pitch")
````
If you make multiple calls on say before calling the talkback method all the string parameters in
the say methods will be spoken one after the other since they are put in an internal queue.

````
 >>> engine.say("Hello World")
 >>> engine.say("Foo bar")
 >>> engine.say("Monty Python")
 >>> engine.talkback()
````
