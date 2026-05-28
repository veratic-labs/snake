# Snake Game (Pygame)

A snake game written in Python using Pygame.

This project was created in December 2022, before the rise of GPT-assisted coding tools.
At the time, I had just started learning Pygame in high school and built the entire game logic step by step on my own during spare time.

Although the codebase is imperfect and lacks proper comments/documentation, I intentionally preserved the original implementation because it represents one of my earliest experiences designing a complete interactive software project from scratch.

## Features

- Real-time snake movement system
- Food collision detection
- Dynamic body growth
- Self-collision game over detection
- Score system
- Restart button
- End screen UI
- Decorative elements such as snake eyes

## Technical Implementation

The core game loop is based on an update-driven movement system.

Every fixed time interval:
- the snake head moves one grid forward,
- body segments follow the previous segment’s position,
- collisions with food are detected,
- new food is randomly generated,
- new body segments are appended to the snake.

The snake body is implemented using a Python list structure, where each segment updates according to the previous segment’s last position.

The project also includes:
- state management,
- simple UI systems,
- collision handling,
- object spawning logic,
- and game reset mechanisms.

## Why This Project Matters To Me

This was one of the first projects where I truly experienced:
- breaking down a large problem into smaller systems,
- debugging interconnected logic,
- and gradually building a working game architecture from nothing.

Most importantly, it taught me how software systems evolve through iteration and experimentation.

## Technologies

- Python
- Pygame

## Run

```bash
python snake.py
```

## License

Licensed under the Apache License, Version 2.0.

Copyright (c) 2022-2026 Ignaxus
