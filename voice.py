from naoqi import *

text = ALProxy('ALTextToSpeech', '192.168.1.10', 9559)
list_ = text.getAvailableVoices()
text.setParameter("doubleVoice", 0) #1-4 0 to disable
text.setParameter("doubleVoiceLevel", 0) #1-4
text.setParameter("doubleVoiceTimeShift", 0) #0 - 0.5
text.setParameter("pitchShift", 1) #1 - 4
text.say('Bonjour or roar')
print(list_)
