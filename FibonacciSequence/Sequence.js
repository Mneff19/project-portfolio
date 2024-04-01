"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const rlHandler_1 = __importDefault(require("./rlHandler"));
// Handles setting the depth and calculating the sequence
class Sequence {
    constructor() {
        this.depth = 0; // How many numbers in the sequence to calculate
        this.question = '\nHow deep into the sequence would you like to calculate? (1-100)\n> '; // Question shown to the user
        this.rlh = new rlHandler_1.default(this.question, this.handleDepthSetting.bind(this)); // Handles getting user input for depth
        this.calculatingSequence = false; // Prevents calculations from running twice (rl caused it to run multiple times without this)
    }
    /**
     * Wrapper function to easily set depth and calcualte the sequence
     */
    run() {
        this.rlh.runQuestion();
    }
    /**
     * Either accepts the user's input and runs the sequence or runs the question again to get a valid response
     * @param response The number passed in from rl, 0 means an invalid input was given and we should run it again
     */
    handleDepthSetting(response) {
        if (response > 0) {
            // input was valid, set depth
            this.depth = response;
            if (!this.calculatingSequence) {
                // Initiate the sequence calculation and prevent multiple calculations just in case
                this.calculateSeqeunce();
                this.calculatingSequence = true;
            }
        }
        else {
            // input was invalid, ask user again
            this.rlh.runQuestion();
        }
    }
    /**
     * Begins the recursive calculation, displaying the first two numbers (0 and 1) in the process
     */
    calculateSeqeunce() {
        console.log("\nCalculating Fibonacci sequence...");
        // We set timeouts to give the user a line-by-line calculation experience
        setTimeout((() => {
            // Show the first number in the sequence
            console.log(0);
            if (this.depth > 1) {
                // Depth was given as more than 1, continue
                setTimeout((() => {
                    // Show the second number in the sequence
                    console.log(1);
                    if (this.depth > 2) {
                        // Depth was given as more than 2, continue to recursion
                        this._calculateSequenceRecursive(0, 1, 2);
                    }
                    else {
                        // Depth was 2, show complete
                        setTimeout(() => { console.log("Complete!\n"); }, 300);
                    }
                }).bind(this), 300);
            }
            else {
                // Depth was 1, show complete
                setTimeout(() => { console.log("Complete!\n"); }, 300);
            }
        }).bind(this), 300);
    }
    /**
     * Recursively computes the Fibonacci sequence
     * @param n0 Two numbers previous
     * @param n1 The previous number
     * @param runningDepth How deep the recusrion is
     */
    _calculateSequenceRecursive(n0, n1, runningDepth) {
        // Base case, depth is met
        if (runningDepth >= this.depth) {
            // Show delayed complete message to match delayed calculation output
            setTimeout(() => { console.log("Complete!\n"); }, 300);
            return;
        }
        // Delay calculation output to create a better user experience
        setTimeout((() => {
            // Show next calculated number
            console.log(n0 + n1);
            // Call the next recusrive iteration shifting n0 to the current n1,
            // setting n1 to the newly calcuated figure and incrementing the depth
            this._calculateSequenceRecursive(n1, n0 + n1, runningDepth + 1);
        }).bind(this), 300);
    }
}
exports.default = Sequence;
