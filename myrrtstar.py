import math, sys, random, pygame

class Node:
	def __init__(self, position, parent):
		self.point = position
		self.parent = parent

#global variables
count = 0
goal_set = False
goal_found = False
init_pos_set = False

#functions used
def reset():
	goal_set = False
	goal_found = False
	init_pos_set = False
	count = 0 

def distance(p1,p2):
	return sqrt((p1[0]-p2[0])*(p1[0]-p2[0])+(p1[1]-p2[1])*(p1[1]-p2[1]))

def randConfig():
	p = random.random()*XDIM,random.random()*YDIM
	return p

def nearestNode():
	for p 

def steer():

def collides():


def chooseParent():

def insertNode():

def reWire():



#code

reset()
while(count<num_nodes && (goalFound==False)):
	random_node=randConfig()
	nearest_node=nearestNode(random_node)
	new=steer(nearest_node,random_node)
	if(!collides(new)):
		optimal_parent=chooseParent(new)
		insertNode(new,optimal_parent)
		reWIre(new)
		if(new.point==goal_point): #struct should have a point
			goalFound = True

currnt_parent = optimal_parent
while(currnt_parent is not None):
	currnt_parent=currnt_parent.parent #structude should have a parent point
	pygame.draw(screen) #draw line retracing from goal to initial



