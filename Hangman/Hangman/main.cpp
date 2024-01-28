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
    // Displays ASCII
    cout << "____  \n";
    cout << "|  |  \n";
    if (incorrectGuesses > 0){
        cout << "|  O  \n";
    }
    else {
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
        cout << "|\n";
    }
    if (incorrectGuesses > 4){
        cout << "|  |  \n";
    }
    else {
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
                cout << word[i_char];
                letterKnown = true;
            }
        }
        
        if (!letterKnown)
        {
            cout << "_";
        }
    }
    cout << "\n";
    
    return 0;
}

int displayIncorrectLetters(char incorrectLetterList[7])
{
    // Displays all incorrect letters
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
    string word;
    cout << "\nWhat word do you think it is? (Enter your guess in uppercase)\n> ";
    cin >> word;
    return word;
}

char getLetterGuess()
{
    char letter;
    cout << "\nWhich letter would you like to guess next?\n> ";
    cin >> letter;
    return toupper(letter);
}

int countUniqueLetters(string word)
{
    unordered_set<char> uniqueLetters;
    
    for(int i_char = 0; i_char < word.length(); i_char++)
    {
        uniqueLetters.insert(word[i_char]);
    }
    
    return uniqueLetters.size() & INT_MAX;
}

string getWordFromFile()
{
    string currWord;
    string chosenWord = "";
    string words = "";
    int numWords = 0;

    ifstream file;
    file.open("/Users/matthewneff/Classes/cse-310/Hangman/Hangman/words.txt");
    
    while (getline(file, currWord))
    {
        words = words + currWord + " ";
        numWords++;
    }
    
    file.close();
    
    int i_word = 0;
    string ssword;
    srand((unsigned int)time(NULL));
    int wordIndex = rand() % numWords;
    cout << wordIndex;
    
    stringstream ssin(words);
    while (chosenWord == "" && ssin >> ssword){
        if (i_word == wordIndex)
        {
            chosenWord = ssword;
        }
        
        ++i_word;
    }
    
    return chosenWord;
}

int main() {
    int incorrectGuesses = 0;
    char incorrectLetters[7] = {' ', ' ', ' ', ' ', ' ', ' ', ' '};
    // Need to make dynamic from file
    string word = getWordFromFile();
    int uniqueCorrectLetters = countUniqueLetters(word);
    int correctGuesses = 0;
    char correctLetters[word.length()];
    
    bool gameNotDone = true;
    cout << "Welcome to Hangman!\nMake your first guess to get started.\n\n";
    
    while (gameNotDone)
    {
        displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
        int guessChoice;
        cout << "Would you like to guess another letter or the entire word?\n(1) Letter\n(2) Word\n\n> ";
        cin >> guessChoice;
        
        if (guessChoice == 1)
        {
            char letterGuess = ' ';
            while (find(begin(incorrectLetters), end(incorrectLetters), letterGuess) != end(incorrectLetters))
            {
                letterGuess = getLetterGuess();
            }
            
            if (word.find(letterGuess) != string::npos)
            {
                correctLetters[correctGuesses] = letterGuess;
                correctGuesses++;
                
                if (correctGuesses == uniqueCorrectLetters)
                {
                    displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
                    cout << "Well done, you got the word!\n";
                    gameNotDone = false;
                }
            }
            else
            {
                incorrectLetters[incorrectGuesses] = letterGuess;
                incorrectGuesses++;
                
                if (incorrectGuesses == sizeof(incorrectLetters))
                {
                    displayStatus(word, incorrectGuesses, correctLetters, incorrectLetters);
                    cout << "Game over! The word was \"" << word << "\"\n";
                    gameNotDone = false;
                }
            }
        }
        else
        {
            string wordGuess = getWordGuess();
            
            if (wordGuess == word)
            {
                cout << "\n\nCorrect!\n";
                gameNotDone = false;
            } else
            {
                cout << "\n\"" << wordGuess << "\"" << " is incorrect.\n";
            }
        }
    }
    
    return 0;
}
