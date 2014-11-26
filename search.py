# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for 
# educational purposes provided that (1) you do not distribute or publish 
# solutions, (2) you retain this notice, and (3) you provide clear 
# attribution to UC Berkeley, including a link to 
# http://inst.eecs.berkeley.edu/~cs188/pacman/pacman.html
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero 
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and 
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import node
import sys

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
  
   
    fridge= util.Stack()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    expanded = {}
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	expanded[n.state] = ['E', n]
	if problem.isGoalState(n.state):
		stack = []
		
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):
		if state not in expanded:
			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns)	
			expanded[n.state] = ['F',ns]
    util.raiseNotDefined()

def depthFirstSearchtree (problem):
  
    fridge= util.Queue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	if problem.isGoalState(n.state):
		stack = []
		
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):

			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns)	
    util.raiseNotDefined()

def breadthFirstSearch(problem):
   
    fridge= util.Queue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    expanded = {}
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	expanded[n.state] = ['E', n]
	if problem.isGoalState(n.state):
		stack = []
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):
		if state not in expanded:
			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns)	
			expanded[n.state] = ['F',ns]

def breadthFirstSearchTree(problem):
 
    fridge= util.Queue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	
	if problem.isGoalState(n.state):
		stack = []
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):

			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns)	
			

def uniformCostSearch(problem):
    fridge= util.PriorityQueue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0),0)
    expanded = {}
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	expanded[n.state] = ['E', n]
	if problem.isGoalState(n.state):
		stack = []
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):
		if state not in expanded:
			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns,ns.defth)	
			expanded[n.state] = ['F',ns]

def manhattanHeuristic(state, problem):
     return util.manhattanDistance(state, problem.goal)

def euclideanHeuristic(state, problem):
    return (state[0] - problem.goal[0]) ** 2 + (state[1] - problem.goal[1]) ** 2

def nullHeuristic(state, problem=None):
    return 0


def greedy(problem, heuristic=nullHeuristic):
    fridge= util.PriorityQueue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0),0)
    expanded = {}
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	expanded[n.state] = ['E', n]
	if problem.isGoalState(n.state):
		stack = []
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):
		if state not in expanded:
			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns,heuristic(ns.state, problem))
			expanded[n.state] = ['F',ns]


def aStarSearch(problem, heuristic=nullHeuristic):
    fridge= util.PriorityQueue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0),0)
    expanded = {}
    while True:
	if fridge.isEmpty(): 
		sys.exit('failure')
	n=fridge.pop()
	expanded[n.state] = ['E', n]
	if problem.isGoalState(n.state):
		stack = []
		while n.parent != None:
			stack.append(n.action)
			n=n.parent
		stack.reverse()
		return stack
	for state, action, cost in problem.getSuccessors(n.state):
		if state not in expanded:
			ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1 )
			fridge.push(ns,ns.defth+heuristic(ns.state, problem))
			expanded[n.state] = ['F',ns]


def limitedDepthFirstSearchTree(problem, k = 8):
    fridge= util.Queue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    cut=False
    while True:
	if fridge.isEmpty():		
		if cut: return cut
		else: sys.exit('failure')
	n=fridge.pop()
	
	if n.defth==k: 
		cut = True
			
	else:
		for state, action, cost in problem.getSuccessors(n.state):
				ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1)
				if problem.isGoalState(ns.state):
					stack = []
					while ns.parent != None:
						stack.append(ns.action)
						ns=ns.parent
					stack.reverse()
					return stack
				fridge.push(ns)	
					
def limitedDepthFirstSearch(problem, k=210):
    fridge= util.Queue()
    fridge.push(node.Node(problem.getStartState(),None, None, 0, 0))
    cut=False
    expanded = {}
    while True:
	if fridge.isEmpty():
		if cut: return cut
		else: sys.exit('failure') 
	n=fridge.pop()
	
	if n.defth==k: 
		cut = True
		
	else:
			
		expanded[n.state] = ['E', n]
		for state, action, cost in problem.getSuccessors(n.state):
			if state not in expanded:
				
				ns= node.Node(state, n, action, n.pathcost + cost, n.defth+1)
				
				if problem.isGoalState(ns.state):
					
					stack = []
					while ns.parent != None:
						stack.append(ns.action)
						ns=ns.parent
					stack.reverse()
					return stack
								
				fridge.push(ns)	
				expanded[n.state] = ['F',ns]		
			
    util.raiseNotDefined()

def iterativeDeepeningSearch (problem):
	defth=0
	while True:
		result=limitedDepthFirstSearch(problem,defth)
		if result!=True: return result
		defth=defth+1
		

def iterativeDeepeningSearchTree (problem):
	defth=0
	while True:
		result=limitedDepthFirstSearchTree(problem,defth)
		if result!=True: return result
		defth=defth+1

# Abbreviations
bfs = breadthFirstSearch
bfst = breadthFirstSearchTree
ids=iterativeDeepeningSearch
idst=iterativeDeepeningSearchTree
dfst =depthFirstSearchtree
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch



