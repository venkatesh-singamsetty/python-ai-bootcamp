#!/usr/bin/env python3
"""
Snake Game - Terminal Version
Uses Python's built-in curses library
"""

import curses
import random
import time


def main(stdscr):
    # Setup
    curses.curs_set(0)  # Hide cursor
    stdscr.nodelay(1)   # Non-blocking input
    stdscr.timeout(100) # Refresh delay (ms)

    # Get screen dimensions
    sh, sw = stdscr.getmaxyx()

    # Create game window (leave room for border)
    win = curses.newwin(sh - 2, sw - 2, 1, 1)
    win.keypad(1)
    win.box()
    win.timeout(100)

    # Snake initial position
    snake = [
        [sh // 2, sw // 2],
        [sh // 2, sw // 2 - 1],
        [sh // 2, sw // 2 - 2]
    ]

    # Initial food position
    food = [sh // 2, sw // 2 + 5]

    # Direction (start moving right)
    key = curses.KEY_RIGHT
    direction = curses.KEY_RIGHT

    score = 0

    while True:
        # Get next key press
        next_key = win.getch()
        key = key if next_key == -1 else next_key

        # Prevent 180-degree turns
        if key == curses.KEY_DOWN and direction != curses.KEY_UP:
            direction = key
        elif key == curses.KEY_UP and direction != curses.KEY_DOWN:
            direction = key
        elif key == curses.KEY_LEFT and direction != curses.KEY_RIGHT:
            direction = key
        elif key == curses.KEY_RIGHT and direction != curses.KEY_LEFT:
            direction = key

        # Calculate new head position
        head = snake[0].copy()
        if direction == curses.KEY_DOWN:
            head[0] += 1
        elif direction == curses.KEY_UP:
            head[0] -= 1
        elif direction == curses.KEY_LEFT:
            head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            head[1] += 1

        # Check for collisions with walls
        if (head[0] <= 0 or head[0] >= sh - 3 or
            head[1] <= 0 or head[1] >= sw - 3):
            break

        # Check for collision with self
        if head in snake:
            break

        # Insert new head
        snake.insert(0, head)

        # Check if food eaten
        if head == food:
            score += 10
            # Generate new food
            while True:
                new_food = [random.randint(1, sh - 4), random.randint(1, sw - 4)]
                if new_food not in snake:
                    food = new_food
                    break
            # Speed up slightly
            timeout = max(50, 100 - score)
            win.timeout(timeout)
        else:
            # Remove tail if no food eaten
            snake.pop()

        # Draw
        win.clear()
        win.box()

        # Draw snake
        for i, segment in enumerate(snake):
            char = '@' if i == 0 else 'o'
            win.addch(segment[0], segment[1], char)

        # Draw food
        win.addch(food[0], food[1], '*')

        # Show score
        score_text = f" Score: {score} "
        win.addstr(0, 2, score_text)

        # Show controls
        controls = " Arrow keys: Move | Q: Quit "
        win.addstr(sh - 3, sw - len(controls) - 4, controls)

        win.refresh()

    # Game Over screen
    win.clear()
    win.box()
    msg = " GAME OVER "
    score_msg = f" Final Score: {score} "
    restart_msg = " Press R to restart or Q to quit "

    win.addstr(sh // 2 - 2, (sw - len(msg)) // 2, msg, curses.A_BOLD)
    win.addstr(sh // 2, (sw - len(score_msg)) // 2, score_msg)
    win.addstr(sh // 2 + 2, (sw - len(restart_msg)) // 2, restart_msg)
    win.refresh()

    while True:
        key = win.getch()
        if key == ord('r') or key == ord('R'):
            return True
        elif key == ord('q') or key == ord('Q'):
            return False


def run_game():
    """Main entry point with restart capability"""
    while True:
        restart = curses.wrapper(main)
        if not restart:
            break


if __name__ == "__main__":
    print("Starting Snake Game...")
    print("Controls: Arrow keys to move, Q to quit")
    time.sleep(1)
    run_game()
    print("Thanks for playing!")
