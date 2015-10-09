
# NOTE: this example requires PyAudio because it uses the Microphone class

from bin_sentiment import bin_classifier
import emotion_classifier
import speech_recognition as sr

# obtain audio from the microphone

def reconocer():
	r = sr.Recognizer()
	with sr.Microphone() as source:
	    print("Say something!")
	    audio = r.listen(source)

	# recognize speech using Google Speech Recognition
	try:
	    # for testing purposes, we're just using the default API key
	    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
	    # instead of `r.recognize_google(audio)`
	    txt = r.recognize_google(audio , language = 'es-PE')
	    print("Google Speech Recognition thinks you said " + txt)
	    if txt == '':
	    	return
	    clas_ = bin_classifier.classify(txt)
	    emotion = emotion_classifier.classify(txt)

	    print emotion

	    if clas_ == 0: print 'negativo'
	    else : print 'positivo'
	    # return clas_

	    f = open('file.txt' , 'w')
	    str_ = str(clas_) + "/" + str(emotion) + '\n'


	    print str_
	    f.write(str_)
	    f.close()

	except sr.UnknownValueError:
	    print("Google Speech Recognition could not understand audio")
	except sr.RequestError:
	    print("Could not request results from Google Speech Recognition service")


while 1:
	reconocer()

