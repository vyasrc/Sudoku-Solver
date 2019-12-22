# Sudoku-Solver
Used backtracking algorithm  to find the solution of a Sudoku, both array and GUI implementations. 

### Algorithm :-

* Find row, col of an unassigned cell
* If there is none, return true
* For digits from 1 to 9
  + If there is no conflict for digit at row, col
    * assign digit to row, col and recursively try fill in rest of grid
  + If recursion successful, return true
  + Else, remove digit and try another
* If all digits have been tried and nothing worked, return false
  
### Array Implementation :-
* Python Library used :- Numpy,  

### GUI Implementation :-
* Python Libraries used :- Tkinter, Threading, Numpy

![Before](https://github.com/vyasrc/Sudoku-Solver/blob/master/Before.PNG)
![After](https://github.com/vyasrc/Sudoku-Solver/blob/master/After.png)
