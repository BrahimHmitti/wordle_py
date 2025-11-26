# Wordle Py

A simple graphical version of the popular Wordle game in Python using Pygame.

## 🎯 Play Online

**Play directly in your browser: [https://brahimhmitti.github.io/wordle_py](https://brahimhmitti.github.io/wordle_py)**

No installation required! Works on desktop and mobile browsers.

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

## Test Web Version Locally

To test the web version with Pygbag:

```bash
# Install pygbag
pip install pygbag

# Run local web server
python -m pygbag main.py

# Open http://localhost:8000 in your browser
```

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

## Technologies

- **Pygame**: Game engine
- **Pygbag**: WebAssembly conversion for browser compatibility
- **GitHub Pages**: Free hosting
- **GitHub Actions**: Automatic deployment on every push

## Deployment

The game automatically deploys to GitHub Pages when you push to the `main` branch, thanks to the configured GitHub Actions workflow.

## Contributing

Pull requests are welcome! For major changes, please open an issue first.

## License

MIT (see LICENSE file)
