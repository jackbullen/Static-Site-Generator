# Problem Class

| Value | A | B | C | D |
|---|---|---|---|---|
| A | -1 | 2 | 1 | 7 |
| B | 1 | -1 | 3 | 10 |
| C | 4 | 12 | -1 | 6 |
| D | 2 | 34 | 0 | -1 |

Interpret this table as collection of cities that are connected by a cost. 

*Examples:*

- *The cost of going from city A to city B is 2.*

- *The cost of going from city B to city A is 1.*

- *The cost of going from city C to city D is 6*

## Task

Write a program that will find the shortest path between two cities.

Include a class called Problem that has the following methods for storing the problem data and for finding the least cost paths between two cities:

## Example

The following code shows how the Problem class can be used to find the least cost path between two cities.

```python
board = [
    [-1, 2, 1, 7],
    [1, -1, 3, 10],
    [4, 12, -1, 6],
    [2, 34, 0, -1]
]
p = Problem(board)

print(p.least_cost_path(0, 3))
```
