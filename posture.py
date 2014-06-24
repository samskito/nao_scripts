from naoqi import *
import math

nao = '192.168.1.10'
port = 9559

motion = ALProxy('ALMotion', nao, port)
posture = ALProxy('ALRobotPosture', nao, port)
audio = ALProxy('ALTextToSpeech', nao, port)

audio.setLanguageDefaultVoice('English', 'naoenu')

def advanceTurn():   
    motion.walkTo(0.4, 0, 0)
    motion.walkTo(0, 0, math.pi/2) 

posture.goToPosture('StandZero', 0.7)

#audio.say('Brain, I want brain')
i=0
while i < 4:
    i = i+1
    advanceTurn()

posture.goToPosture('Crouch', 0.5)
motion.setStiffnesses('Body', 0)
