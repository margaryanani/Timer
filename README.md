# Timer

## Introduction
This is a mini-project that takes time from the user as a timer and starts to countdown in the terminal. 

## How to download files

- ### Downloading Individual Files
  - Click on the file that you want to download.
  - Click the download icon, which lets you download the raw file or right-click the "Raw" button and select "Save link as..." to download the file.
- ### Cloning the Repository
  If you want to work with the entire repository and want to make changes, cloning is the best option.
  
  - Make sure that you have Git installed on your computer.
  - Open a terminal.
  - Navigate to the directory where you want to clone the repository.
  - Run this command. ` git clone https://github.com/margaryanani/Timer.git `
 
## Usage

You only need 'timer.py' file for this project. 

## Code Structure

1. `get_positive_int(prompt)` function is used for getting the right input from the user (The right input will be a positive integer.)
2.  `h = get_positive_int("Enter hours: ")`

    `m = get_positive_int("Enter minutes: ")`
    
    `s = get_positive_int("Enter seconds: ")`
    
    `h` (hour), `m` (minute), `s` (second) give the prompts to the user by activating the `get_positive_int(prompt)` function.
3. The (1) and (2) rearrange the timer.

   For example if the user enters 120 seconds, the program converts it to 2 minutes.

   The same goes for minutes.

4. The third while loop is where the countdown starts.
   
   The timer updates the display in place without printing a new line for each second. It continuously overwrites the previous line on the console using `sys.stdout.write` and `sys.stdout.flush`.

   
   




