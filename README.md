# Content
* Introduction
* Languages
* Functionality
* Demonstration




# Introduction

This file is a part of the first semester Programming Fundamentals Lab Project 'Hangman'.

The basic theme of this project is to create a hangman game that enables you to guess a word with seven lives in hand. Once you lose all your lives, the game ends. And if you can correctly guess the word within the aount of lives you're given, you win.

Whatever we learned throughout the semester was implemented in this hangman game, it tremendously helped us to build our logic.

# Languages

This program was made in ***python***.

# Functionality

 –
### RANDOM MODULE –
•	We used the random module to be able to import a random word from a list of more than 2500 words.

### DICTIONARIES – 

•	We used dictionaries to store the list of words and visual depiction of the hangman in separate files which we imported into the main hangman file.

### FUNCTIONS –
•	We defined a function to get a valid word from the list in which we use a while loop that iterates until we find a word that does not have a dash or a space in it. This is because guessing a word that has either of those would be inconvenient. 
•	We also defined another function called hangman in which we set the earlier function equal to a variable and use this to keep track of the letters that the user has guessed and the letters that are in the word.
•	We also call the hangman function at the end of the code to run the program.

###  SETS – 

•	We created three sets to store letters that the user has guessed, the letters that are in the word and a set in which we store all the letters of the English alphabet.

###  WHILE LOOPS – 

•	We used two different while loops in our project. We used one inside a function to return a valid word.
•	We used another while loop that runs until the length of the letters in the word is not equal to zero and the number of lives are also not equal to zero. In this loop, we have stored various print and conditional statements.

### CONDITIONAL STATEMENTS –

•	We use if/else statements to add and remove letters in the defined sets based on what the user has guessed and to deduct lives if the user guesses incorrectly.
•	We also use an if else statement to display the final output. If the user has ran out of lives, then the user will lose. Otherwise, the user wins the game and a print statement saying so will be displayed.

# Demonstration
* This is what is shown when the user has entered an incorrect letter:


![](https://github.com/PyromaniacSiphon/Hangman-PF1/blob/master/screenshot%201.jpg)

* This is what is shown when the user has lost the game: 



![](https://github.com/PyromaniacSiphon/Hangman-PF1/blob/master/screenshot2.jpg)

* This is what is shown when the user has successfully guessed all the letters and has won the game :


![](https://github.com/PyromaniacSiphon/Hangman-PF1/blob/master/screenshot%203.jpg)

# GROUP MEMBERS

* Muhammad Taufeeq
* Muhammad Faisal
* Humna Ali
* Ahrar Ali
* Zuha Fatima





