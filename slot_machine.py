"""
Advanced Slot Machine Game
==========================
A comprehensive slot machine simulation with proper error handling,
user experience improvements, and extensible architecture.

Features:
- Multiple betting lines (1-5)
- Various symbols with different rarities and values
- Comprehensive input validation
- Game statistics tracking
- Bonus features and jackpots
- Save/load functionality for balance
- Colorful terminal output (optional)

Author: AI Assistant
Version: 2.0
"""

import random
import json
import os
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
from enum import Enum

# =============================================================================
# GAME CONFIGURATION AND CONSTANTS
# =============================================================================

class GameConfig:
    """Central configuration class for all game parameters"""
    
    # Slot machine dimensions
    MAX_LINES = 5
    ROWS = 3
    COLS = 5
    
    # Betting limits
    MAX_BET = 1000
    MIN_BET = 1
    DEFAULT_BALANCE = 100
    
    # Game files
    SAVE_FILE = "slot_machine_save.json"
    
    # Symbol configuration: {symbol: (count_in_reel, payout_multiplier)}
    SYMBOL_CONFIG = {
        "💎": (1, 50),   # Diamond - Rare, high value
        "👑": (2, 25),   # Crown - Rare, high value  
        "🍒": (3, 15),   # Cherry - Uncommon, good value
        "🍋": (4, 10),   # Lemon - Common, medium value
        "🔔": (5, 8),    # Bell - Common, medium value
        "⭐": (6, 5),    # Star - Common, low value
        "🍇": (8, 3),    # Grapes - Very common, low value
        "🍊": (10, 2),   # Orange - Most common, lowest value
    }
    
    # Jackpot configuration
    JACKPOT_SYMBOL = "💎"
    JACKPOT_MULTIPLIER = 100
    PROGRESSIVE_JACKPOT_CONTRIBUTION = 0.01  # 1% of each bet goes to jackpot


class GameState(Enum):
    """Enum for different game states"""
    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    QUIT = "quit"


@dataclass
class GameStats:
    """Data class to track player statistics"""
    total_spins: int = 0
    total_bet: int = 0
    total_winnings: int = 0
    biggest_win: int = 0
    jackpots_won: int = 0
    sessions_played: int = 0
    
    @property
    def net_profit(self) -> int:
        """Calculate net profit/loss"""
        return self.total_winnings - self.total_bet
    
    @property
    def win_rate(self) -> float:
        """Calculate win percentage"""
        return (self.total_winnings / self.total_bet * 100) if self.total_bet > 0 else 0.0


# =============================================================================
# CORE SLOT MACHINE CLASS
# =============================================================================

class AdvancedSlotMachine:
    """
    Advanced slot machine with comprehensive features and error handling
    """
    
    def __init__(self):
        """Initialize the slot machine with default values"""
        self.balance = GameConfig.DEFAULT_BALANCE
        self.progressive_jackpot = 1000  # Starting jackpot
        self.stats = GameStats()
        self.game_state = GameState.MENU
        
        # Generate symbol lists based on configuration
        self._generate_symbol_pool()
        
        # Load saved game if exists
        self._load_game()
    
    def _generate_symbol_pool(self) -> None:
        """Generate the pool of symbols based on their frequency configuration"""
        self.symbol_pool = []
        self.symbol_values = {}
        
        for symbol, (count, value) in GameConfig.SYMBOL_CONFIG.items():
            # Add symbols to pool based on their count (frequency)
            self.symbol_pool.extend([symbol] * count)
            # Store payout values
            self.symbol_values[symbol] = value
    
    # =========================================================================
    # GAME PERSISTENCE METHODS
    # =========================================================================
    
    def _save_game(self) -> None:
        """Save current game state to file"""
        try:
            save_data = {
                'balance': self.balance,
                'progressive_jackpot': self.progressive_jackpot,
                'stats': {
                    'total_spins': self.stats.total_spins,
                    'total_bet': self.stats.total_bet,
                    'total_winnings': self.stats.total_winnings,
                    'biggest_win': self.stats.biggest_win,
                    'jackpots_won': self.stats.jackpots_won,
                    'sessions_played': self.stats.sessions_played
                }
            }
            
            with open(GameConfig.SAVE_FILE, 'w') as f:
                json.dump(save_data, f, indent=2)
            
            print("✅ Game saved successfully!")
            
        except Exception as e:
            print(f"⚠️  Warning: Could not save game: {e}")
    
    def _load_game(self) -> None:
        """Load saved game state from file"""
        try:
            if os.path.exists(GameConfig.SAVE_FILE):
                with open(GameConfig.SAVE_FILE, 'r') as f:
                    save_data = json.load(f)
                
                self.balance = save_data.get('balance', GameConfig.DEFAULT_BALANCE)
                self.progressive_jackpot = save_data.get('progressive_jackpot', 1000)
                
                # Load statistics
                stats_data = save_data.get('stats', {})
                self.stats = GameStats(
                    total_spins=stats_data.get('total_spins', 0),
                    total_bet=stats_data.get('total_bet', 0),
                    total_winnings=stats_data.get('total_winnings', 0),
                    biggest_win=stats_data.get('biggest_win', 0),
                    jackpots_won=stats_data.get('jackpots_won', 0),
                    sessions_played=stats_data.get('sessions_played', 0)
                )
                
                print("✅ Previous game loaded!")
                
        except Exception as e:
            print(f"⚠️  Warning: Could not load saved game: {e}")
            print("Starting with default values...")
    
    # =========================================================================
    # INPUT VALIDATION METHODS
    # =========================================================================
    
    def _get_valid_integer_input(self, prompt: str, min_val: int, max_val: int, 
                                allow_quit: bool = True) -> Optional[int]:
        """
        Get valid integer input from user with comprehensive validation
        
        Args:
            prompt: The input prompt message
            min_val: Minimum allowed value
            max_val: Maximum allowed value
            allow_quit: Whether to allow 'q' to quit
            
        Returns:
            Valid integer or None if user quits
        """
        while True:
            try:
                user_input = input(prompt).strip().lower()
                
                # Handle quit option
                if allow_quit and user_input in ['q', 'quit', 'exit']:
                    return None
                
                # Convert to integer
                value = int(user_input)
                
                # Validate range
                if min_val <= value <= max_val:
                    return value
                else:
                    print(f"❌ Please enter a number between {min_val} and {max_val}")
                    
            except ValueError:
                print("❌ Please enter a valid number (or 'q' to quit)")
            except KeyboardInterrupt:
                print("\n👋 Thanks for playing!")
                return None
    
    def _get_yes_no_input(self, prompt: str) -> bool:
        """Get yes/no confirmation from user"""
        while True:
            try:
                response = input(prompt + " (y/n): ").strip().lower()
                if response in ['y', 'yes']:
                    return True
                elif response in ['n', 'no']:
                    return False
                else:
                    print("❌ Please enter 'y' for yes or 'n' for no")
            except KeyboardInterrupt:
                return False
    
    # =========================================================================
    # GAME LOGIC METHODS
    # =========================================================================
    
    def _generate_spin(self) -> List[List[str]]:
        """
        Generate a random slot machine spin
        
        Returns:
            2D list representing the slot machine grid [column][row]
        """
        columns = []
        
        for _ in range(GameConfig.COLS):
            column = []
            # Create a copy of symbol pool for this column to avoid replacement issues
            available_symbols = self.symbol_pool.copy()
            
            for _ in range(GameConfig.ROWS):
                # Pick random symbol and remove from available symbols
                symbol = random.choice(available_symbols)
                available_symbols.remove(symbol)
                column.append(symbol)
            
            columns.append(column)
        
        return columns
    
    def _check_winning_lines(self, columns: List[List[str]], lines_bet: int, 
                           bet_per_line: int) -> Tuple[int, List[int], bool]:
        """
        Check for winning combinations across bet lines
        
        Args:
            columns: The slot machine result grid
            lines_bet: Number of lines the player bet on
            bet_per_line: Amount bet per line
            
        Returns:
            Tuple of (total_winnings, winning_line_numbers, is_jackpot)
        """
        total_winnings = 0
        winning_lines = []
        is_jackpot = False
        
        for line in range(lines_bet):
            # Get the symbol in the first column for this line
            first_symbol = columns[0][line]
            line_symbols = [columns[col][line] for col in range(GameConfig.COLS)]
            
            # Check if all symbols in the line match
            if all(symbol == first_symbol for symbol in line_symbols):
                # Calculate winnings for this line
                line_winnings = self.symbol_values[first_symbol] * bet_per_line
                
                # Check for jackpot (all jackpot symbols)
                if first_symbol == GameConfig.JACKPOT_SYMBOL:
                    line_winnings = self.progressive_jackpot
                    is_jackpot = True
                
                total_winnings += line_winnings
                winning_lines.append(line + 1)
        
        return total_winnings, winning_lines, is_jackpot
    
    def _display_slot_machine(self, columns: List[List[str]]) -> None:
        """Display the slot machine result in a formatted way"""
        print("\n" + "="*50)
        print("🎰 SLOT MACHINE RESULT 🎰")
        print("="*50)
        
        # Display line numbers
        print("Lines: ", end="")
        for line in range(GameConfig.ROWS):
            print(f"{line + 1:2d}", end="  ")
        print()
        
        # Display the slot machine grid
        for row in range(GameConfig.ROWS):
            print(f"   {row + 1}: ", end="")
            for col, column in enumerate(columns):
                print(f"{column[row]:2s}", end=" ")
                if col < len(columns) - 1:
                    print("|", end=" ")
            print()
        
        print("="*50)
    
    # =========================================================================
    # USER INTERACTION METHODS
    # =========================================================================
    
    def _get_deposit_amount(self) -> Optional[int]:
        """Get deposit amount from user"""
        print("\n💰 DEPOSIT FUNDS 💰")
        print(f"Current balance: ${self.balance}")
        
        amount = self._get_valid_integer_input(
            "Enter deposit amount (or 'q' to cancel): $",
            1, 10000
        )
        
        return amount
    
    def _get_number_of_lines(self) -> Optional[int]:
        """Get number of lines to bet on"""
        print(f"\n📏 SELECT BETTING LINES (1-{GameConfig.MAX_LINES}) 📏")
        print("More lines = more chances to win, but higher total bet!")
        
        return self._get_valid_integer_input(
            f"Number of lines to bet on (1-{GameConfig.MAX_LINES}): ",
            1, GameConfig.MAX_LINES
        )
    
    def _get_bet_per_line(self) -> Optional[int]:
        """Get bet amount per line"""
        print(f"\n💵 SET BET PER LINE (${GameConfig.MIN_BET}-${GameConfig.MAX_BET}) 💵")
        
        return self._get_valid_integer_input(
            f"Bet per line (${GameConfig.MIN_BET}-${GameConfig.MAX_BET}): $",
            GameConfig.MIN_BET, GameConfig.MAX_BET
        )
    
    def _display_game_info(self) -> None:
        """Display current game information"""
        print("\n" + "="*60)
        print("🎰 ADVANCED SLOT MACHINE 🎰")
        print("="*60)
        print(f"💰 Balance: ${self.balance}")
        print(f"🎁 Progressive Jackpot: ${self.progressive_jackpot}")
        print(f"🎯 Total Spins: {self.stats.total_spins}")
        print(f"📊 Win Rate: {self.stats.win_rate:.1f}%")
        print("="*60)
    
    def _display_paytable(self) -> None:
        """Display the symbol paytable"""
        print("\n" + "="*40)
        print("💎 SYMBOL PAYTABLE 💎")
        print("="*40)
        
        # Sort symbols by value (descending)
        sorted_symbols = sorted(
            GameConfig.SYMBOL_CONFIG.items(),
            key=lambda x: x[1][1],
            reverse=True
        )
        
        for symbol, (frequency, payout) in sorted_symbols:
            rarity = "Rare" if frequency <= 2 else "Common" if frequency <= 5 else "Very Common"
            print(f"{symbol} = {payout}x bet ({rarity})")
        
        print(f"\n🎁 JACKPOT: All {GameConfig.JACKPOT_SYMBOL} = ${self.progressive_jackpot}")
        print("="*40)
    
    def _display_statistics(self) -> None:
        """Display detailed player statistics"""
        print("\n" + "="*50)
        print("📊 PLAYER STATISTICS 📊")
        print("="*50)
        print(f"Total Spins: {self.stats.total_spins}")
        print(f"Total Amount Bet: ${self.stats.total_bet}")
        print(f"Total Winnings: ${self.stats.total_winnings}")
        print(f"Net Profit/Loss: ${self.stats.net_profit}")
        print(f"Biggest Single Win: ${self.stats.biggest_win}")
        print(f"Jackpots Won: {self.stats.jackpots_won}")
        print(f"Win Rate: {self.stats.win_rate:.1f}%")
        print(f"Sessions Played: {self.stats.sessions_played}")
        print("="*50)
    
    # =========================================================================
    # MAIN GAME METHODS
    # =========================================================================
    
    def _play_single_spin(self) -> bool:
        """
        Execute a single spin of the slot machine
        
        Returns:
            True to continue playing, False to quit
        """
        # Check if player has any money
        if self.balance <= 0:
            print("💸 You're out of money! Please deposit more funds.")
            return True
        
        # Get betting parameters
        lines = self._get_number_of_lines()
        if lines is None:
            return False
        
        bet_per_line = self._get_bet_per_line()
        if bet_per_line is None:
            return False
        
        total_bet = lines * bet_per_line
        
        # Check if player has enough balance
        if total_bet > self.balance:
            print(f"❌ Insufficient funds! You need ${total_bet} but only have ${self.balance}")
            print("💡 Try betting on fewer lines or reducing your bet per line.")
            return True
        
        # Confirm the bet
        print(f"\n🎲 SPIN SUMMARY:")
        print(f"Lines: {lines}")
        print(f"Bet per line: ${bet_per_line}")
        print(f"Total bet: ${total_bet}")
        print(f"Remaining balance after bet: ${self.balance - total_bet}")
        
        if not self._get_yes_no_input("Confirm this spin?"):
            print("Spin cancelled.")
            return True
        
        # Process the bet
        self.balance -= total_bet
        self.progressive_jackpot += int(total_bet * GameConfig.PROGRESSIVE_JACKPOT_CONTRIBUTION)
        
        # Update statistics
        self.stats.total_spins += 1
        self.stats.total_bet += total_bet
        
        # Generate and display spin result
        print("\n🎰 Spinning...")
        columns = self._generate_spin()
        self._display_slot_machine(columns)
        
        # Check for winnings
        winnings, winning_lines, is_jackpot = self._check_winning_lines(
            columns, lines, bet_per_line
        )
        
        # Process winnings
        if winnings > 0:
            self.balance += winnings
            self.stats.total_winnings += winnings
            
            if winnings > self.stats.biggest_win:
                self.stats.biggest_win = winnings
            
            if is_jackpot:
                self.stats.jackpots_won += 1
                self.progressive_jackpot = 1000  # Reset jackpot
                print(f"\n🎉🎉🎉 JACKPOT! YOU WON ${winnings}! 🎉🎉🎉")
            else:
                print(f"\n🎉 You won ${winnings}!")
                
            if winning_lines:
                print(f"🏆 Winning lines: {', '.join(map(str, winning_lines))}")
        else:
            print("\n😞 No winning combinations. Better luck next time!")
        
        # Display updated balance
        print(f"\n💰 New balance: ${self.balance}")
        net_result = winnings - total_bet
        if net_result > 0:
            print(f"📈 Net gain this spin: +${net_result}")
        elif net_result < 0:
            print(f"📉 Net loss this spin: ${abs(net_result)}")
        else:
            print("➡️  Broke even this spin!")
        
        return True
    
    def _main_menu(self) -> GameState:
        """
        Display main menu and handle user choice
        
        Returns:
            Next game state
        """
        self._display_game_info()
        
        print("\n🎮 MAIN MENU:")
        print("1. 🎰 Play Slot Machine")
        print("2. 💰 Deposit Funds")  
        print("3. 💎 View Paytable")
        print("4. 📊 View Statistics")
        print("5. 💾 Save Game")
        print("6. 👋 Quit")
        
        choice = self._get_valid_integer_input(
            "\nSelect option (1-6): ", 1, 6, allow_quit=False
        )
        
        if choice == 1:
            return GameState.PLAYING
        elif choice == 2:
            amount = self._get_deposit_amount()
            if amount:
                self.balance += amount
                print(f"✅ Deposited ${amount}! New balance: ${self.balance}")
            return GameState.MENU
        elif choice == 3:
            self._display_paytable()
            input("\nPress Enter to continue...")
            return GameState.MENU
        elif choice == 4:
            self._display_statistics()
            input("\nPress Enter to continue...")
            return GameState.MENU
        elif choice == 5:
            self._save_game()
            return GameState.MENU
        elif choice == 6:
            return GameState.QUIT
        else:
            return GameState.MENU
    
    def run(self) -> None:
        """Main game loop"""
        print("🎰 Welcome to the Advanced Slot Machine! 🎰")
        print("Type 'q' at any prompt to quit")
        
        # Increment session counter
        self.stats.sessions_played += 1
        
        try:
            while self.game_state != GameState.QUIT:
                if self.game_state == GameState.MENU:
                    self.game_state = self._main_menu()
                
                elif self.game_state == GameState.PLAYING:
                    if self._play_single_spin():
                        # Ask if player wants to continue or return to menu
                        if self.balance > 0:
                            continue_playing = self._get_yes_no_input(
                                "\nPlay another spin?"
                            )
                            if not continue_playing:
                                self.game_state = GameState.MENU
                        else:
                            print("💸 You're out of money!")
                            self.game_state = GameState.MENU
                    else:
                        self.game_state = GameState.QUIT
        
        except KeyboardInterrupt:
            print("\n\n⚡ Game interrupted!")
        
        finally:
            # Save game and display final statistics
            self._save_game()
            print(f"\n👋 Thanks for playing!")
            print(f"💰 Final balance: ${self.balance}")
            
            if self.stats.total_spins > 0:
                print(f"📊 You played {self.stats.total_spins} spins")
                print(f"🎯 Net result: ${self.stats.net_profit}")


# =============================================================================
# MAIN EXECUTION
# =============================================================================

def main():
    """Main function to start the game"""
    try:
        game = AdvancedSlotMachine()
        game.run()
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")
        print("Please restart the game.")


if __name__ == "__main__":
    main()