all:

play:
	python pacman.py

goWest:
	python pacman.py --layout testMaze --pacman GoWestAgent

goTurn:
	python pacman.py --layout tinyMaze --pacman GoWestAgent

help:
	python pacman.py -h

#### Part 1: Finding a FIxed Food dot using Search Algorithms

Part1:
	python pacman.py -l tinyMaze -p SearchAgent -a fn=tinyMazeSearch


## Question 1.1
Q11_1:
	python pacman.py -l tinyMaze -p SearchAgent

Q11_2:
	python pacman.py -l mediumMaze -p SearchAgent

Q11_3:
	python pacman.py -l bigMaze -z .5 -p SearchAgent


## Question 1.2
Q12_1:
	python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs

Q12_2:
	python pacman.py -l bigMaze -p SearchAgent -a fn=bfs -z .5

Q12_3:
	python eightpuzzle.py

## Question 1.3
Q13:
	python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic 

## Question 1.4
Q14_1:
	python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs2

Q14_2:
	python pacman.py -l bigMaze -p SearchAgent -a fn=bfs2 -z .5

Q14_3:
	python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs2

Q14_4:
	python pacman.py -l bigMaze -p SearchAgent -a fn=dfs2 -z .5

#### Part 2 Finding All the Corners

## Question 2.1

Q21_1:
	python pacman.py -l tinyCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

Q21_2:
	python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem

## Question 2.2
Q22:
	python pacman.py -l mediumCorners -p SearchAgent -a fn=aStarSearch,prob=CornersProblem,heuristic=cornersHeuristic -z 0.5