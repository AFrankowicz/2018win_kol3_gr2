###Flight simulator. 
#Write a code in python that simulates the tilt correction of the plane (angle between plane wings and earth). 
##The program should:
# - print out current orientation
# - applied tilt correction
# - run in infinite loop
# - until user breaks the loop
#Assume that plane orientation in every new simulation step is random angle with gaussian distribution (the planes is experiencing "turbulations"). 
#With every simulation step the orentation should be corrected, applied and printed out.
#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#The whole repository MUST be a fork from https://github.com/mwmajew/kol1_gr2
#Good Luck

from random import gauss
from plane import *
import time
import multiprocessing as mp

def simulator(plane):
	print("{:*^80}".format(" FLIGHT SIMULATOR ", 'centered'))
	angle_text = "\rangle between winds and ground: "
	correction_text = "; value used to correct tilt: "
	
	while True:
		angle = str(plane.get_orientation())
		correction = str(plane.get_correction())
		data_to_print = "{0}{1:.5}{2}{3:.5}"
		data_to_print = data_to_print.format(angle_text, angle, correction_text, correction)
		print(data_to_print, end="")
		
		tilt = gauss(0, 1)
		plane.tilt(tilt)
		plane.correct()
		time.sleep(1)

if __name__ == "__main__":
	plane = Plane(0)

	p = mp.Process(target=simulator, args=(plane,))
	p.start()
	p.join()
	
