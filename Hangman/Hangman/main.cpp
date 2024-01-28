//
//  main.cpp
//  Hangman
//
//  Created by Matthew Neff on 1/16/24.
//

#include <iostream>
#include <unordered_set>
#include <fstream>
#include <sstream>

using namespace std;

int displayASCII(int incorrectGuesses)
{
    // Displays ASCII, line by line depending on number of incorrect guesses
    cout << "____  \n";
    cout << "|  |  \n";
    if (incorrectGuesses > 0){
        cout << "|  O  \n";
    }
    else {
        // Only draw the structure, not a hangman
        cout << "|\n";
    }
    if (incorrectGuesses > 1){
        cout << "| /";
        if (incorrectGuesses > 2)
        {
            cout << "|";
            
            if (incorrectGuesses > 3)
            {
                cout << "\\";
            }
        }
        cout << "\n";
    }
    else {
        // Only draw the structure, not a hangman
        cout << "|\n";
    }
    if (incorrectGuesses > 4){
        cout << "|  |  \n";
    }
    else {
        // Only draw the structure, not a hangman
        cout << "|\n";
    }
    if (incorrectGuesses > 5){
        cout << "| /";
        
        if (incorrectGuesses > 6)
        {
            cout << " \\";
        }
        
        cout << "\n";
    }
    else {
        // Only draw the structure, not a hangman
        cout << "|\n";
    }
    cout << "|\n\n";
    return 0;
}

int displayKnownWord(string word, char correctLetterGuesses[])
{
    // Displays word as currently known with underscores
    for (int i_char = 0; i_char < word.length(); i_char++)
    {
        bool letterKnown = false;
        for (int i_knownLetter = 0; i_knownLetter < strlen(correctLetterGuesses); i_knownLetter ++)
        {
            if (correctLetterGuesses[i_knownLetter] == word[i_char])
            {
                // User has guessed word, display it now
                cout << word[i_char];
                letterKnown = true;
            }
        }
        
        if (!letterKnown)
        {
            // User has not guessed letter, display underscore
            cout << "_";
        }
    }
    cout << "\n";
    
    return 0;
}

int displayIncorrectLetters(char incorrectLetterList[7])
{
    // Displays all incorrect letters separated by spaces
    for(int i_char = 0; i_char < strlen(incorrectLetterList) - 1; i_char++)
    {
        cout << incorrectLetterList[i_char] << " ";
    }
    cout << "\n\n";
    return 0;
}

int displayStatus(string word, int incorrectGuesses, char correctLetterGuesses[], char incorrectLetterList[7])
{
    // Display hangman ASCII
    displayASCII(incorrectGuesses);
    // Display word as known
    displayKnownWord(word, correctLetterGuesses);
    // Display incorrect letters
    displayIncorrectLetters(incorrectLetterList);
    return 0;
}

string getWordGuess()
{
    // Get the user's guess for the word
    string word;
    cout << "\nWhat word do you think it is? (Enter your guess in uppercase)\n> ";
    cin >> word;
    return word;
}

char getLetterGuess()
{
    // Get the user's guess for a letter
    char letter;
    cout << "\nWhich letter would you like to guess next?\n> ";
    cin >> letter;
    return toupper(letter);
}

int countUniqueLetters(string word)
{
    // Get the number of unique letters in a given string
    unordered_set<char> uniqueLetters;
    
    for(int i_char = 0; i_char < word.length(); i_char++)
    {
        uniqueLetters.insert(word[i_char]);
    }
    
    return uniqueLetters.size() & INT_MAX;
}

string getWordFromFile()
{
    // Gets a random word from the file
    string currWord;
    string chosenWord = "";
    string words = "";
    int numWords = 0;

    // Open the file and create one long string from each word separated by spaces
    // Also keep track of how many words there were
    ifstream file;
    file.open("/Users/matthewneff/Classes/cse-310/Hangman/Hangman/words.txt");
    
    while (getline(file, currWord))
    {
        words = words + currWord + " ";
        numWords++;
    }
    
    // String is created, we're done with the file
    file.close();
    
    // Get a random index to be our chosen word
    srand((unsigned int)time(NULL));
    int wordIndex = rand() % numWords;
    
    // Use a stringstream to go through each word in words
    int i_word = 0;
    string ssword;
    stringstream ssin(words);
    // Go through each word until we hit our chosen index
    while (chosenWord == "" && ssin >> ssword){
        if (i_word == wordIndex)
        {
            // This is the chosen word! Loop will stop here
            chosenWord = ssword;
        }
        
        ++i_word;
    }
    
    return chosenWord;
}

int main() {
    // Instantiate vars
    int incorrectGuesses = 0;
    char incorrectLetters[7] = {' ', ' ', ' ', ' ', ' ', ' ', ' '};
    string word = getWordFromFile();
    int uniqueCorrectLetters = countUniqueLetters(word);
    int correctGuesses = 0;
    char correctLetters[word.length()];
    
    // Start the game
    bool gameNotDone = true;
    cout << "Welcome to Hangman!\nMake your first guess to get started.\n\n";
    
    // Gmae loop
    while (gameNotDone)
    {
        // Always start with showing status
        displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
        
        // Get choice of guessing a letter or the word
        int guessChoice;
        cout << "Would you like to guess another letter or the entire word?\n(1) Letter\n(2) Word\n\n> ";
        cin >> guessChoice;
        
        if (guessChoice == 1)
        {
            // Guessing a letter
            char letterGuess = ' ';
            while (find(begin(incorrectLetters), end(incorrectLetters), letterGuess) != end(incorrectLetters))
            {
                // Go until we get a letter they haven't guessed already
                letterGuess = getLetterGuess();
            }
            
            if (word.find(letterGuess) != string::npos)
            {
                // Letter is in word, add it to correctGuesses list and increment number of correct gueses
                correctLetters[correctGuesses] = letterGuess;
                correctGuesses++;
                
                if (correctGuesses == uniqueCorrectLetters)
                {
                    // User won!
                    displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
                    cout << "Well done, you got the word!\n";
                    gameNotDone = false;
                }
            }
            else
            {
                // Letter is not in word, add to incorrect letters guessed list and increment number of incorrect guesses
                incorrectLetters[incorrectGuesses] = letterGuess;
                incorrectGuesses++;
                
                if (incorrectGuesses == sizeof(incorrectLetters))
                {
                    // User lost...
                    displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
                    cout << "Game over! The word was \"" << word << "\"\n";
                    gameNotDone = false;
                }
            }
        }
        else
        {
            // Guessisng the word
            string wordGuess = getWordGuess();
            
            if (wordGuess == word)
            {
                // User won!
                cout << "\n\nCorrect!\n";
                gameNotDone = false;
            } else
            {
                // User didn't get it right
                cout << "\n\"" << wordGuess << "\"" << " is incorrect.\n";
            }
        }
    }
    
    return 0;
}
