# 🎰 Advanced Slot Machine Game

A feature-rich, terminal-based slot machine game built in Python with comprehensive gameplay mechanics, statistics tracking, and persistent save system.

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Platform](https://img.shields.io/badge/platform-windows%20%7C%20macOS%20%7C%20linux-lightgrey.svg)

## 🌟 Features

### 🎮 Core Gameplay
- **5×3 Slot Grid** - Professional slot machine layout
- **Multiple Betting Lines** - Bet on 1-5 lines simultaneously
- **8 Unique Symbols** - Each with different rarity and payout rates
- **Progressive Jackpot** - Grows with each bet until someone wins
- **Flexible Betting** - Bet from $1 to $1000 per line

### 💰 Advanced Features
- **Persistent Save System** - Automatic save/load using JSON
- **Comprehensive Statistics** - Track wins, losses, and performance
- **Smart Balance Management** - Deposit funds and track spending
- **Professional UI** - Clean terminal interface with emojis
- **Error Handling** - Robust input validation and edge case handling

### 📊 Statistics Tracking
- Total spins and betting history
- Win/loss ratios and profitability
- Biggest wins and jackpot tracking
- Session-based performance metrics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Terminal/Command Prompt access

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sanjaykumarpandit108/Python-Slot-Machine-Advanced.git
   cd advanced-slot-machine
   ```

2. **Run the game**
   ```bash
   python slot_machine.py
   ```

That's it! No additional dependencies required - uses only Python standard library.

## 🎯 How to Play

### Getting Started
1. **Launch the game** - Run the Python script
2. **Check your balance** - Start with $100 default balance
3. **View the paytable** - Learn symbol values and rarities
4. **Place your bet** - Choose lines and bet amount
5. **Spin and win!** - Match symbols across lines for payouts

### Game Controls
- **Number keys (1-6)** - Navigate main menu
- **Enter** - Confirm selections
- **'q' or 'quit'** - Exit at any prompt
- **Ctrl+C** - Emergency exit with auto-save

### Winning Combinations
Match identical symbols across a betting line from left to right:

| Symbol | Rarity | Payout Multiplier |
|--------|--------|-------------------|
| 💎 | Rare | 50x (Jackpot symbol) |
| 👑 | Rare | 25x |
| 🍒 | Uncommon | 15x |
| 🍋 | Common | 10x |
| 🔔 | Common | 8x |
| ⭐ | Common | 5x |
| 🍇 | Very Common | 3x |
| 🍊 | Most Common | 2x |

### 🎁 Special Features

#### Progressive Jackpot
- Triggered by getting all 💎 symbols on a betting line
- Starts at $1000 and grows with each bet (1% contribution)
- Resets to $1000 after being won

#### Statistics Dashboard
Track your performance with detailed metrics:
- **Total Spins** - Number of games played
- **Win Rate** - Percentage of profitable spins
- **Net Profit/Loss** - Overall financial performance
- **Biggest Win** - Your best single spin
- **Jackpots Won** - Number of jackpots hit

## 🛠️ Development Setup

### Project Structure
```
PYTHON-SLOT-MACHINE-ADVANCED/
├── slot_machine.py           # Main game file
├── slot_machine_save.json    # Auto-generated save file
├── README.md                 # This file
└── LICENSE                   # MIT License
```

### Code Architecture
- **Object-Oriented Design** - Clean, maintainable code structure
- **Type Hints** - Full type annotation for better development
- **Error Handling** - Comprehensive exception management
- **Configuration Class** - Easy parameter adjustments
- **Modular Functions** - Testable and reusable components

### Key Classes
- `AdvancedSlotMachine` - Main game logic and state management
- `GameConfig` - Centralized configuration and constants
- `GameStats` - Statistics tracking and calculations
- `GameState` - Enum for game state management

## 🎮 Game Configuration

Easily customize the game by modifying the `GameConfig` class:

```python
class GameConfig:
    MAX_LINES = 5              # Maximum betting lines
    ROWS = 3                   # Slot machine height
    COLS = 5                   # Slot machine width
    MAX_BET = 1000            # Maximum bet per line
    MIN_BET = 1               # Minimum bet per line
    DEFAULT_BALANCE = 100     # Starting balance
    
    # Symbol configuration: {symbol: (frequency, payout)}
    SYMBOL_CONFIG = {
        "💎": (1, 50),   # Very rare, high payout
        "👑": (2, 25),   # Rare, good payout
        # ... customize symbols and payouts
    }
```

## 📊 Save File Format

The game automatically saves progress in JSON format:

```json
{
  "balance": 150,
  "progressive_jackpot": 1250,
  "stats": {
    "total_spins": 25,
    "total_bet": 500,
    "total_winnings": 650,
    "biggest_win": 100,
    "jackpots_won": 0,
    "sessions_played": 3
  }
}
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch** (`git checkout -b feature/amazing-feature`)
3. **Commit your changes** (`git commit -m 'Add amazing feature'`)
4. **Push to the branch** (`git push origin feature/amazing-feature`)
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines
- Add type hints for all functions
- Include docstrings for public methods
- Test edge cases thoroughly
- Update README for new features

## 🐛 Bug Reports

Found a bug? Please open an issue with:
- **Description** - What happened vs. what was expected
- **Steps to Reproduce** - Detailed reproduction steps
- **Environment** - Python version, OS, terminal used
- **Save File** - Include your save file if relevant (remove sensitive data)

## 🚀 Future Enhancements

Planned features for future releases:
- [ ] **Bonus Rounds** - Special mini-games for extra rewards
- [ ] **Sound Effects** - Audio feedback for wins and spins
- [ ] **Multiplier System** - Temporary payout multipliers
- [ ] **Achievement System** - Unlock rewards for milestones
- [ ] **GUI Version** - Graphical interface using tkinter/pygame
- [ ] **Network Play** - Multiplayer tournaments and leaderboards
- [ ] **Mobile App** - React Native or Flutter version
- [ ] **Web Version** - Browser-based gameplay

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🎉 Acknowledgments

- Inspired by classic slot machine mechanics
- Built with Python's powerful standard library
- Emoji icons enhance the visual experience
- Community feedback drives continuous improvement

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/Sanjaykumarpandit108/Python-Slot-Machine-Advanced/issues)
- **Discussions**: [GitHub Discussions](https://github.com/Sanjaykumarpandit108/Python-Slot-Machine-Advanced/discussions)


---

### ⭐ Star this repository if you found it helpful!

**Made with ❤️ and Python**

---

## 🎲 Ready to Play?

```bash
git clone https://github.com/Sanjaykumarpandit108/Python-Slot-Machine-Advanced.git
cd advanced-slot-machine
python slot_machine.py
```

Good luck and have fun! 🍀🎰