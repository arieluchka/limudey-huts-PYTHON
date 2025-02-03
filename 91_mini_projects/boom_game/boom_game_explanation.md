# 7 Boom

Create the "7 Boom" game in python

Create the "Building blocks" functions in the "base_functions.py" file, then write 2 game variations in 2 files:
- a single player game in "single_player_game.py" (where the computer will play against the player)
- a multiplayer game in "multiplayer_game.py" (where 2 players will play against each other)

## Game rules

- The game starts with the number 1
- The players take turns counting up from the previous number
- If the number is divisible by 7 or contains the digit 7, the player must say "Boom" instead of the number
- If the player fails to say "Boom" when required, they lose the game

**example:**

1-2-3-4-5-6-Boom-8-9-10-11-12-13-Boom-15-16-Boom-...


## Work plan
- Create a function that takes a number and returns True if the number is divisible by 7
- Create a function that takes a number and returns True if the number contains the digit 7

<br>

- Create a function that takes a number and returns True if the number is a Boom number (divisible by 7 or contains the digit 7)

- Create a function to handle player input and validate it (verify it's a number/Boom)

---

Implement the multiplayer game logic + user interface 
 
- Track the numbers that are said by the players, and verify in each turn if the player said the correct next number

Implement the single player game logic + user interface

---

Implement a game log (username vs AI/username, who won, how many turns, ...)
- Save the game log in a file




## Bonuses:

- make the game adaptable to any number of players (not just 2)
- make the game adaptable to any Boom number (8 Boom, 13 Boom, ...)