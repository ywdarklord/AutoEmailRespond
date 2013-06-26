import threading
import time

class Timer(threading.Thread):
	#very simple timer 

	def __init__(self,seconds):
		self.runTime=seconds
		threading.Thread.__init__(self)
	def run(self):
                
		time.sleep(self.runTime)
		print "Buzzzzz!! Time's up!"

class CountDownTimer(Timer):
	# a timer that can count down the seconds
	def run(self):
		counter=self.runTime
		for sec in range(self.runTime):
			print counter
			time.sleep(5.0)
			counter-=1
		print "Done"

class CountDownExec(CountDownTimer):
	# a timer that excute an action at end of the timer
	def _init_(self,seconds,action,args=[]):
		self.args=args
		self.action=action
		CountDownTimer.__init__(self,seconds)

	def run(self):
		CountDownTimer.run(self)
		self.action(self,args)

def myAction(args=[]):
	print "Performing my action with args:"
	print args

if __name__=="_main_":
	t=CountDownExec(3,myAction,["Hello","World"])
	t.start()

	
