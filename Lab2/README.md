# Lab 2

&#x20;# Lab 2: 

Search Algorithms (BFS, DFS, Hill Climbing, Best First Search, A\*)



Aim / Problem Statement



To implement five search algorithms and compare them on a road map of 7 cities (A to G). The task is to find a route from city A to city G, and to compare the algorithms  and execution time.



\## Algorithm



1. BFS (Breadth First Search):

&#x20;explores cities level by level using a queue, so it finds the path with the fewest roads.



2\. DFS (Depth First Search): 

goes as deep as possible along one route using a stack, and backtracks when it reaches a dead end.



3\. Hill Climbing: 

always moves to the neighbouring city with the lowest heuristic value. It never goes back, so it can get stuck.



4\. Best First Search: keeps all unexplored cities in a priority queue ordered by heuristic value, and always expands the lowest one. ( "have some doubts didn't get it properly i need some more learning in it").



5\. A\*: orders cities by f = g + h, where g is the distance travelled so far and h is the heuristic estimate to the goal.



\## Results / Output



| Algorithm         |  path             |   Cost (km) |



| BFS               | A -> B -> D -> G |   15        |

| DFS               | A -> C -> F -> G |   19        |

| Hill Climbing     | A -> B -> E -> G |   20        |

| Best First Search | A -> B -> E -> G |   20        |

| A\*                |   A -> B -> D -> G | 15        |



\## Performance Analysis



\- Solution quality:

&#x20;BFS and A\* found the shortest route (15 km). DFS found 19 km. Hill Climbing and Best First Search found 20 km because they follow only the heuristic and ignore the distance already travelled.



\- Execution time: 

each algorithm was run 1000 times and the average time is printed in the comparison table in SearchAlgorithms.ipynb. On this small map all the times are tiny.



\- Accuracy, precision and recall are not applicable because these are search algorithms, not learning models.









\## Learning Outcomes



\- Implementing uninformed search (BFS, DFS) and heuristic search (Hill Climbing, Best First Search, A\*).



\- Understanding how a heuristic changes the route that is found.

\- Comparing algorithms by solution quality and execution time.

\- Understanding that A\* gives the best route here by combining distance travelled and the estimate to the goal.



\## Files



\- SearchAlgorithms.ipynb: all five algorithms and the comparison

\- search\_comparison.png: bar charts of path cost and execution time

