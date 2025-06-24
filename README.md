# Wordle Py

A simple graphical version of the popular Wordle game in Python using Pygame.

## Features

- Play Wordle with a graphical interface.
- Random 5-letter word chosen each game.
- Type your guesses directly into the game window.
- Feedback for each letter: green (correct spot), yellow (in word, wrong spot), grey (not in word).
- Restart the game with the space bar.

## Installation

1. Make sure you have Python 3 installed.
2. Install Pygame:
   ```bash
   pip install pygame
   ```
3. Clone this repo:
   ```bash
   git clone https://github.com/BrahimHmitti/wordle_py.git
   cd wordle_py
   ```
4. Make sure you have the word lists `en.txt` (for guesses) and `wo.txt` (for answers) in the same folder.

## How to Play

- Run the game:
  ```bash
  python main.py
  ```
- A window appears with empty squares.
- Type your 5-letter guess using your keyboard.
- Press `Enter` to submit your guess.
- Colors will show feedback for each letter:
  - **Green**: Correct letter in the correct place.
  - **Yellow**: Letter is in the word, but in a different place.
  - **Grey**: Letter is not in the word.
- You have 6 tries to guess the correct word.
- Press `Space` to start a new game.
- Press `ESC` or close the window to quit.

## Example

When you run the game, you'll see a grid. Type a word like `APPLE` and press Enter. Each letter's color will tell you if it's correct or partially correct.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

MIT (see LICENSE file)
