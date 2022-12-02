## Approach 

### Task 1 

- create three lists, containing the three possibilites for each scenario (win, draw, lose) as they are written in the input file
- Check if the game is in the list of winning games, add 6 points; if it is in draw, add 3 points, if it is in lose, add 0 points
- Now check the list again for your shape. Compare it to the possibities and add the points according to the shape 
- Return the sum of both points 

** Yes, it could I know going through the list twice is not good for performance

### Task 2 

- Create a list of shapes exactly like this: ['A', 'B', 'C']
- Now the points for your shape can be calculated through the index. The points are index + 1
- Go through the list of games and check if you win, lose or have a draw. Add the points accordingly. 
- calculate the index of the needed shape and add those points as well. 
- The Index of your shape can be easily found by shifting the index a bit. So find the index and add index+1 to your points


Here is the explanation for finding your shape: 
- To win you need the shape one index further of the shape of your opponent (index + 1): If they have A, you need B. If they have C, you need A -> Cycle through the list
- To lose you need the shape one index before the shape of your opponent (index - 1): If they have A, you need C. If they have C, you need B -> Cycle through the list
- In case of draw, you just need the same shape so the index stays the same  (index)
- Since you cycle through the list the index you need may be higher than your list is. So you need to calculate modolo len(list) in our case 3
- For the points just add one. Since points for shapes are the index of your shape +1
