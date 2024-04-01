"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || function (mod) {
    if (mod && mod.__esModule) return mod;
    var result = {};
    if (mod != null) for (var k in mod) if (k !== "default" && Object.prototype.hasOwnProperty.call(mod, k)) __createBinding(result, mod, k);
    __setModuleDefault(result, mod);
    return result;
};
Object.defineProperty(exports, "__esModule", { value: true });
const readline = __importStar(require("readline"));
// Readline is tricky because you have to do things its way.
// This class helps silo those intricacies and clean up the Sequence class.
class rlHandler {
    /**
     * Sets all necessary event listeners for rl
     * @param question The question that the user will be shown
     * @param callback The function to be envoked on every iteration
     */
    constructor(question, callback) {
        // Keeps track of the user's response until a valid response is given
        this.response = 0;
        // Init the readline object
        this.rl = readline.createInterface({
            input: process.stdin,
            output: process.stdout
        });
        // Sets the prompt that the user will see
        this.rl.setPrompt(question);
        // Runs on user input
        this.rl.on('line', (userAnswer) => {
            // Verify the input
            if (!parseInt(userAnswer)) {
                // Input was not a number
                console.log("Please enter a number!");
            }
            else if (parseInt(userAnswer) > 0 && parseInt(userAnswer) < 101) {
                // Valid input was provided, set response to the answer and close rl
                this.response = parseInt(userAnswer);
                this.rl.close();
            }
            else {
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
exports.default = rlHandler;
