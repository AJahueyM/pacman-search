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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util


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
        util.raise_method_not_defined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raise_method_not_defined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raise_method_not_defined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raise_method_not_defined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raise_method_not_defined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    searchQueue = util.Queue() # Queue for bfs, we analyze the current level before the children
    visited = []
    startState = (problem.getStartState(), [])  # Store current state and the path to it
    searchQueue.push(startState)

    while not searchQueue.isEmpty():  # While there is some state to analyze
        state = searchQueue.pop()  # Get state to analyze
        location = state[0]  # Get its location
        path = state[1]  # Get the action taken to get to this location
        if location not in visited:  # If we have not visited this location
            visited.append(location)
            if problem.isGoalState(location):  # If this location is the target, return taken path
                return path
            successors = list(problem.getSuccessors(location))  # Get available nodes from this location
            for successor in successors:
                if successor[0] not in visited:  # If we have not visited any of the available nodes
                    searchQueue.push((successor[0], path + [successor[1]]))  # Add successor to the search queue
    return []


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raise_method_not_defined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    openQueue = util.PriorityQueue()
    startLoc = problem.getStartState()
    visited = []
    current = {"loc": startLoc, "parent": None, "h": heuristic(startLoc, problem), "g": 0, "act": None}
    current["f"] = current["g"] + current["h"]

    openQueue.push(current, current["f"])
    while not openQueue.isEmpty():
        current = openQueue.pop()
        if visited.__contains__(current["loc"]):
            continue
        visited.append(current["loc"])

        if problem.isGoalState(current["loc"]):
            break
        for successor in problem.getSuccessors(current["loc"]):
            if not visited.__contains__(successor[0]):
                successor_state = {"loc": successor[0], "act": successor[1], "parent": current, "h": heuristic(successor[0], problem),
                                   "g": successor[2] + current["g"]}
                successor_state["f"] = successor_state["g"] + successor_state["h"]
                openQueue.push(successor_state, successor_state["f"])

    actions = []

    while current is not None and current["act"] is not None:
        actions.insert(0, current["act"])
        current = current["parent"]
    return actions

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
