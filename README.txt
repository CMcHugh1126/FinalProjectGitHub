Introduction to the Tuple Out Dice Game
The Tuple Out Dice Game is a game in python that allows 2 users to play a game with two random 6 sided dice. 
The goal of the game is to socre the most points before you tuple out and get 0 points
You tuple out when all 3 of the dice land on the same number, there is also fixed rolls where two numbers are the same and those dice cannot be rolled again

Rules
Each player has 3 rolls and each player will get their 3 rolls before the next player starts
After each roll, the user will be asked a yes/no question on of they want to keep rolling or take their points and go to the next turn
if they elect to keep rolling and tuple out they will recieve no points and the next roll will automatically start
After player 2 is done with their 3rd roll, the terminal will announce the winner and the final score 
If there is no winner and the game ends in a tie, there will be a message prompt letting you know
There are bonus points each player can earn on each turn. You can earn these points by rolling all ecen numbers, Rolling a 6, or rolling the sequence [1, 2, 3]
Rolling a 6 gives you 5 bonus points 
Rolling all evan numbers gets you 10 bonus points
And Rolling the sequence [1,2,3] gets you 15 bonus points
However just because you have more points when the game ends, does not mean the game is over. 
This game takes time into consideration and will deduct the slower player with a 2 point penalty
The game will usually end somewhere between 50 and 100 points to these 2 points can make a difference. 


How the Code Works
The code is set up using many different functions including if statements, for loops, and while loops
The functions are built using the 5 step method and are texplained and tested below each of them
To start the code, click the play button in the top right corner and the game will play in the terminal

Frequency Chart
At the end of the game, a Seaborn window will appear and show you the roll combined frequency
This is a way to see if the distribution of numbers was 'random'
It is also a fun way to find the mean roll for each game 
