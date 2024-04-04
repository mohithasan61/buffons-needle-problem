# Buffon's Needle Problem

Welcome to the repository! This repository contains Python code to simulate and explore Buffon's Needle Problem, a classic problem in geometric probability.

## What is Buffon's Needle Problem?
Buffon's Needle Problem is a famous question in probability theory posed by the French mathematician Georges-Louis Leclerc, Comte de Buffon in the 18th century. The problem involves dropping a needle of a certain length onto a lined surface and determining the probability that the needle will intersect one of the lines.

## About this Repository
In this repository, you'll find:

1. **Python Code**: Python scripts to simulate Buffon's Needle experiment and calculate the probability of intersection.
3. **Documentation**: Detailed explanations of the problem, the simulation methodology, and the mathematical background.

## Getting Started
To get started with exploring Buffon's Needle Problem:

1. Clone this repository to your local machine.
2. Install Python 3.6.
3. Run the script to conduct your own experiments and analyze the results.

## Contributing
Contributions to this repository are welcome! If you have ideas for improvements, bug fixes, or new features, feel free to open an issue or submit a pull request. Please follow the contribution guidelines outlined in `CONTRIBUTING.md`.

## Explaination of The Program
### How the Script Works

1. **Setup and Constants**: 
   - The script imports necessary modules (`random` for generating random numbers and `sin` from `math` for trigonometric calculations).
   - Constants `L` and `G` represent the length of the needle and the spacing between the lines, respectively.
   - The constant `PI` is approximately equals the mathematical constant π. (This is only for generating random angles, not directly used for finding the value of pi with this method.)

2. **User Interaction**: 
   - The script prints a welcome message and instructions for the user.
   - It prompts the user to input a natural number to specify the number of experiments (number of times the simulation will run).
   - Entering `0` breaks the loop and exits the program.

3. **Simulation Loop**: 
   - Inside the loop, the number of experiments is determined based on the user input.
   - The script measures the time taken for the simulations to execute.
   - For each experiment, a needle is dropped randomly on a grid of parallel lines.
   - The number of times the needle intersects with the lines is counted (variable `hits`).

4. **Data Collection**: 
   - Experiment results, including the number of hits and estimated values of π, are stored in a dictionary named `list`.
   - Each experiment's data (number of hits, estimated value of π, and attempt number) is appended to the respective lists in the dictionary.

5. **Calculation of Average**: 
   - The average value of π is calculated based on the results of five consecutive experiments.

6. **Output**: 
   - The script prints the experiment data (including number of hits, estimated values of π, and execution time) for each attempt.
   - After completing all experiments, it prints the average estimated value of π and the total execution time.

7. **Loop Continuation**: 
   - The loop continues until the user inputs `0`, allowing for multiple sets of experiments to be run.

Overall, the script simulates Buffon's Needle experiment to estimate the value of π, providing users with the flexibility to specify the number of experiments and observe the results.

## Acknowledgments
Special thanks to Georges-Louis Leclerc, Comte de Buffon for posing such an intriguing problem, and to the contributors who have helped improve this repository.

Happy exploring Buffon's Needle Problem! 🧵📏
