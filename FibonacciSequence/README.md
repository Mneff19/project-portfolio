# Overview
To demonstrate the TypeScript language, I have created a program that interacts with the user to calculate the Fibonacci sequence to the provided depth.

I was interested in TypeScript because I have worked for years as a website developer, spending most of my time in JavaScript. Having recently learned C++, I was highly intruiged at the idea of a slant language to JavaScript that included strong typing factors similar to C++.

[Software Demo Video](https://www.loom.com/share/a932b10530c94444ab322c020a6aa97c?sid=8ce760b9-3d20-4579-82de-6d33a2cb4948)

# Development Environment
This project was completed in VSCode, using the terminal as the user interface. It is purely wirtten in TypeScript, and it relies on the readline npm package to handle the user input.

# Useful Websites
- [How to Start a TypeScript Project (Digital Ocean)](https://www.digitalocean.com/community/tutorials/typescript-new-project) - Very useful in starting your TypeScript skeleton, compiling to JS, and running in Node!
- [How to Get User Input from Console in TypeScript](https://stackoverflow.com/questions/33858763/console-input-in-typescript) - Pointed me in the right direction to start using the Readline module
- [Readline Module Documentation](https://nodejs.org/api/readline.html#readline_readline) - Helped me understand the nuances of Readline and how to work with it better

# Future Work
- Currently the staggered output is a product of several different timeout functions, it would be ideal to consolidate all output into one function. Perhaps by creating an array of all outputs then iterating through it like that instead of having everything inline
- Integrating this into a website would be very interesting! I would like to experiment with DOM manipulation in TypeScript
- Currently the npm build command must be run manually, I'd be interested to utilize webpack or a similar package to be able to more dynamically watch and build the assets