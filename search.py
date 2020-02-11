# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
#
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).

#####################################################
#####################################################
# Please enter the number of hours you spent on this
# assignment here
"""
num_hours_i_spent_on_this_assignment = 0
"""
#
#####################################################
#####################################################

#####################################################
#####################################################
# Give one short piece of feedback about the course so far. What
# have you found most interesting? Is there a topic that you had trouble
# understanding? Are there any changes that could improve the value of the
# course to you? (We will anonymize these before reading them.)
"""
<Your feedback goes here>

"""
#####################################################
#####################################################

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util
import time as t
class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Q1.1
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print ( problem.getStartState() )
    You will get (5,5)

    print (problem.isGoalState(problem.getStartState()) )
    You will get True

    print ( problem.getSuccessors(problem.getStartState()) )
    You will get [((x1,y1),'South',1),((x2,y2),'West',1)]
    """
    "*** YOUR CODE HERE ***"
    states = util.Stack()  # states ( coordinations(x,y), [path])

    visitedStates = [] # states that are visited
    path = [] # Every states keeps it's path fro the beginning state

    # if initial state == goal state
    if (problem.isGoalState(problem.getStartState())):
        return []

    # add the starting coordination of the pacman position, and we start with a empty path
    states.push((problem.getStartState(), []))

    while (True):
        # if we cannot find the solution
        if states.isEmpty():
            return []

        # get info of current state
        coordinations, path = states.pop() # take position and path
        visitedStates.append(coordinations) # add the visited coordination into the visitedStates

        # if we reach our goal
        if problem.isGoalState(coordinations):
            return path
        
        # get successors of the current state
        successor = problem.getSuccessors(coordinations)

        # Add new states in stack and fix their path
        if successor:
            for element in successor:
                if element[0] not in visitedStates:
                    newPath = path +[element[1]]
                    states.push((element[0], newPath))


def breadthFirstSearch(problem):
    """
    Q1.2
    Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    states = util.Queue()

    visitedStates = []
    path = []

    # if init state == goal state
    if (problem.isGoalState(problem.getStartState())):
        return []

    # 
    states.push((problem.getStartState(), []))

    while (True):
        # if we cannot find the solution
        if states.isEmpty():
            return []

        # get info of current state
        coordinations, path = states.pop() # take position and path
        visitedStates.append(coordinations) # add the visited coordination into the visitedStates

        # if we reach our goal
        if problem.isGoalState(coordinations):
            return path
        
        # get successors of the current state
        successor = problem.getSuccessors(coordinations)

        # Add new states in stack and fix their path
        if successor:
            for element in successor:
                if element[0] not in visitedStates and element[0] not in (state[0] for state in states.list):
                    newPath = path +[element[1]]
                    states.push((element[0], newPath))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Q1.3
    Search the node that has the lowest combined cost and heuristic first."""
    """Call heuristic(s,problem) to get h(s) value."""
    "*** YOUR CODE HERE ***"

    begin = problem.getStartState()
    visitedStates = []
    states = util.PriorityQueue()
    states.push( (begin, []), nullHeuristic(begin, problem) )
    numCost = 0

    while not states.isEmpty():
        state, actions = states.pop()
        #
        if problem.isGoalState(state):
            return actions
        #
        if state not in visitedStates:
            successors = problem.getSuccessors(state)
            for successor in successors:
                coordinates = successor[0]

                if coordinates not in visitedStates:
                    paths = successor[1]
                    numActions = actions + [paths]
                    numCost = problem.getCostOfActions(numActions) + heuristic(coordinates, problem)
                    states.push( (coordinates, actions + [paths]), numCost)
        visitedStates.append(state)
    return actions
    util.raiseNotDefined()

def priorityQueueDepthFirstSearch(problem):
    """
    Q1.4a.
    Reimplement DFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"

    states = util.PriorityQueue()  # states ( coordinations(x,y), [path])

    visitedStates = [] # states that are visited
    path = [] # Every states keeps it's path fro the beginning state
    numCost = 0

    # if initial state == goal state
    if (problem.isGoalState(problem.getStartState())):
        return []

    # add the starting coordination of the pacman position, and we start with a empty path
    states.push((problem.getStartState(), []), numCost)

    while (True):
        # if we cannot find the solution
        if states.isEmpty():
            return []

        # get info of current state
        coordinations, path = states.pop() # take position and path
        visitedStates.append(coordinations) # add the visited coordination into the visitedStates

        # if we reach our goal
        if problem.isGoalState(coordinations):
            return path
        
        # get successors of the current state
        successor = problem.getSuccessors(coordinations)

        # Add new states in stack and fix their path
        if successor:
            for element in successor:
                if element[0] not in visitedStates:
                    newPath = path +[element[1]]
                    numCost += problem.getCostOfActions(newPath)
                    states.push((element[0], newPath), numCost)


def priorityQueueBreadthFirstSearch(problem):
    """
    Q1.4b.
    Reimplement BFS using a priority queue.
    """
    "*** YOUR CODE HERE ***"

    states = util.PriorityQueue()

    visitedStates = []
    path = []
    numCost = 0

    # if init state == goal state
    if (problem.isGoalState(problem.getStartState())):
        return []

    # 
    states.push((problem.getStartState(), []), numCost)

    while (True):
        # if we cannot find the solution
        if states.isEmpty():
            return []

        # get info of current state
        coordinations, path = states.pop() # take position and path
        visitedStates.append(coordinations) # add the visited coordination into the visitedStates

        # if we reach our goal
        if problem.isGoalState(coordinations):
            return path
        
        # get successors of the current state
        successor = problem.getSuccessors(coordinations)

        # Add new states in stack and fix their path
        if successor:
            for element in successor:
                if element[0] not in visitedStates and element[0] not in (state[0] for state in states.heap):
                    newPath = path +[element[1]]
                    numCost += problem.getCostOfActions(newPath)
                    states.push((element[0], newPath), numCost)

#####################################################
#####################################################
# Discuss the results of comparing the priority-queue
# based implementations of BFS and DFS with your original
# implementations.

"""

Stacks and Queue is faster than priority queue because priority queue runs in heap, which takes longer time to 

First the depth first search(dfs), the normal implementation in stack takes 0.0106658935546875 second, while the priority queue implementation takes 0.03452110290527344 second. 
Stack implementation of dfs is faster than priority queue because the runtime of pushing and popping data from the stack cost O(1) while insert and remove data from priority queue cost O(log n).

Second the breath first search(bfs), the normal implementation in stack takes 0.02259993553161621 second, while the priority queue implementation takes 0.048577070236206055 second. 
Stack implementation of dfs is faster than priority queue because the runtime of enqueuing and dequeuing data from the stack cost O(1) while insert and remove data from priority queue cost O(log n)

Therefore, Stacks and Queue is faster than priority queue because priority queue runs in heap and it requires to be sorted.
"""



#####################################################
#####################################################



# Abbreviations (please DO NOT change these.)
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
bfs2 = priorityQueueBreadthFirstSearch
dfs2 = priorityQueueDepthFirstSearch