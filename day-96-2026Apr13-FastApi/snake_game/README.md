# Snake Game

A classic Snake game implemented in Python using the built-in `curses` library.

## Features

- Classic Snake gameplay
- Score tracking
- Increasing difficulty (speeds up as you score)
- Game over and restart functionality
- No external dependencies required

## How to Play

### Controls

| Key | Action |
|-----|--------|
| ↑ (Up Arrow) | Move up |
| ↓ (Down Arrow) | Move down |
| ← (Left Arrow) | Move left |
| → (Right Arrow) | Move right |
| Q | Quit game |
| R | Restart (after game over) |

### Objective

- Eat the food (`*`) to grow your snake and increase your score
- Each food item is worth 10 points
- Avoid hitting the walls or yourself
- The game speeds up as your score increases

## Running the Game

### On macOS/Linux

```bash
python3 snake.py
```

### On Windows

Windows requires the `windows-curses` package:

```bash
pip install windows-curses
python snake.py
```

## Tips

- Plan your moves ahead - the snake moves continuously!
- Don't trap yourself in corners
- Use the border walls strategically (but don't hit them!)
