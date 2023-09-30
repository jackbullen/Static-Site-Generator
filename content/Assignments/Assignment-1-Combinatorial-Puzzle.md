# Assignment 1: Combinatorial Puzzle

- **Date:** September 29, 2023
- **Duration:** 2 weeks

Welcome to the first assignment. Here build sliding tile puzzle solver. 

## What is a sliding tile puzzle?

A sliding tile puzzle is a combination puzzle that challenges a player to slide tiles along routes to establish end state configurations. The pieces to be moved may are numbers or letters.

## Board and rules

- The puzzle consists of an $n \times n$ grid with $n^2 - 1$ tiles numbered from 1 to $n^2 - 1$ and a blank space.

- Any tile adjacent to the blank space can be moved onto the blank space.

- The goal of the puzzle is to place the tiles in order by making sliding moves that use the empty space.

## Example

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a4/15-puzzle-02.jpg/1200px-15-puzzle-02.jpg" alt="Alt text" width="500" height="500"/>

## Task

- Implement a sliding tile puzzle solver. 

    - Include a class for the puzzle and a class for the solver.*

- Write a report that clearly defines:

    - How the program takes in the input board state.

    - How the program tests for unsolvable/solvable puzzles.

    - How the program computes solutions. 

    - Discussion of the heuristic function used and why it is admissible.

    - Discussion of the time and space complexity of the algorithm.

- **Bonus:** Include a routine that takes in board size n and generates all possible solvable $n \times n$ sliding tile puzzles.