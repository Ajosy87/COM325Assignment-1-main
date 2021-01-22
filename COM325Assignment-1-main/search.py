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
        path, stepCost), where 'successor' is a successor to the current
        state, 'path' is the path required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfpaths(self, paths):
        """
         paths: A list of paths to seen

        This method returns the total cost of a particular sequence of paths.
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
    Search the deepest nodes in the search search_maze first.

    Your search algorithm needs to return a list of paths that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    # Stack is used, so the search survey is LIFO
    from util import Stack
    from game import Directions

    # the component of search_maze is (state, the path to the state)
    search_maze = Stack()

    # pushing the seen nodes into tha stack
    search_maze.push(((problem.getStartState()), []))

    # storing nodes that are seen
    seen = []

    # surveying the seen nodes in the stack by popping
    while (not search_maze.isEmpty()):
        (state, path) = search_maze.pop()
        if (problem.isGoalState(state)):
            break

        successors = problem.getSuccessors(state)
        for i in successors:
            if (i[0] not in seen):  # any state has been seen doesn't need to be seen again
                seen.append(i[0])
                search_maze.push((i[0], path + [i[1]]))

    return path

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search search_maze first."""
    "*** YOUR CODE HERE ***"
    # Bdf uses the Queue to store its visted states which is FIFO
    from util import Queue
    from game import Directions

    # the component of search_maze is (state, the path to the state)
    search_maze = Queue()
    search_maze.push(((problem.getStartState()), []))

    # store the visited state
    seen = []

    while (not search_maze.isEmpty()):
        (state, path) = search_maze.pop()
        if (problem.isGoalState(state)):
            break

        successors = problem.getSuccessors(state)
        for i in successors:
            if (i[0] not in seen):  # the state is visited once
                seen.append(i[0])
                search_maze.push((i[0], path + [i[1]]))

    return path

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # initialising the process from a start node
    search_maze = problem.getStartState()
    if problem.isGoalState(search_maze):
        return []

    # store the visited state
    seen = []

    # pushing into open list
    que = util.PriorityQueue()
    # ((coordinate/node , path to current node , cost to current node),priority)
    que.push((search_maze, [], 0), 0)

    while not que.isEmpty():

        # popping from open list
        state, paths, prevCost = que.pop()
        if state not in seen:
            seen.append(state)

            # states with small cost processed
            if problem.isGoalState(state):
                return paths

            # comparing path with small total cost and being added to closed list until the goal is reached
            for next_state, path, cost in problem.getSuccessors(state):
                new_transition = paths + [path]
                priority = prevCost + cost
                que.push((next_state, new_transition, priority), priority)
    util.raiseNotDefined()


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Bdf uses the Queue to store its visted states which is FIFO


    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
