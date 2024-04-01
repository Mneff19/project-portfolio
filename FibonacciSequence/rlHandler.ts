import * as readline from 'readline';

// Readline is tricky because you have to do things its way.
// This class helps silo those intricacies and clean up the Sequence class.
export default class rlHandler {
    // Keeps track of the user's response until a valid response is given
    response: number = 0;

    // Init the readline object
    rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    /**
     * Sets all necessary event listeners for rl
     * @param question The question that the user will be shown
     * @param callback The function to be envoked on every iteration
     */
    constructor(question: string, callback: Function) {
        // Sets the prompt that the user will see
        this.rl.setPrompt(question);

        // Runs on user input
        this.rl.on('line', (userAnswer) => {
            // Verify the input
            if (!parseInt(userAnswer)) {
                // Input was not a number
                console.log("Please enter a number!");
            } else if (parseInt(userAnswer) > 0 && parseInt(userAnswer) < 101) {
                // Valid input was provided, set response to the answer and close rl
                this.response = parseInt(userAnswer);
                this.rl.close();
            } else {
                // Number out of range was provided
                console.log("Number must be 1-100!");
            }
            // Pause the stream
            this.rl.pause();
        });
    
        // When rl is paused, trigger callback
        this.rl.on('pause', () => {
            callback(this.response);
        });

        // When rl is closed, trigger callback
        this.rl.on('close', () => {
            callback(this.response);
        });
    }

    /**
     * Runs the prompt, resuming the stream if it had been paused
     */
    runQuestion() {
        this.rl.resume();
        this.rl.prompt();
    }
}