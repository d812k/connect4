from src.board import Board
from src.player import Player
from src.win_checker import WinChecker


class Game:
    PLAYER_CONFIGS = [
        ("●", "#FF0000"),
        ("■", "#0000FF"),
        ("▲", "#00FF00"),
        ("♦", "#FFFF00"),
        ("★", "#FF00FF"),
        ("◆", "#00FFFF"),
        ("▼", "#FF8000"),
        ("◉", "#8000FF"),
        ("⬢", "#FF0080"),
        ("⬣", "#00FF80"),
    ]

    def __init__(self) -> None:
        self.board: Board
        self.players: list[Player] = []
        self.current_player_idx = 0
        self.win_checker = WinChecker()

    def setup(self) -> None:
        print("Welcome to Connect4!")
        print()

        while True:
            try:
                rows = int(input("Enter number of rows (6-15, default 6): ") or "6")
                cols = int(input("Enter number of columns (6-15, default 7): ") or "7")
                self.board = Board(rows, cols)
                break
            except (ValueError, EOFError) as e:
                print(f"Invalid input: {e}. Please try again.")

        while True:
            try:
                num_players = int(input("\nEnter number of players (2-10): "))
                if not (2 <= num_players <= 10):
                    print("Number of players must be between 2 and 10.")
                    continue
                break
            except (ValueError, EOFError):
                print("Invalid input. Please enter a number between 2 and 10.")

        for i in range(num_players):
            name = input(f"Enter name for Player {i + 1} (or press Enter for default): ").strip()
            if not name:
                name = f"Player {i + 1}"

            symbol, color = self.PLAYER_CONFIGS[i]
            player = Player(name, symbol, color)
            self.players.append(player)

        print(f"\nGame setup complete! Board size: {rows}x{cols}")
        print(f"Players: {', '.join(str(p) for p in self.players)}")
        print("\nOpen board.html in your browser to view the game board.")
        print("The page will auto-refresh every second.\n")

    def play(self) -> None:
        game_over = False

        while not game_over:
            current_player = self.players[self.current_player_idx]

            self.board.display(current_player)

            while True:
                try:
                    column_input = input(
                        f"\n{current_player.name}'s turn {current_player.symbol}. "
                        f"Enter column (1-{self.board.cols}) or 'q' to quit: "
                    ).strip()

                    if column_input.lower() == "q":
                        self.board.display_goodbye()
                        print("Game quit by player.")
                        return

                    column = int(column_input)

                    if not self.board.is_column_valid(column):
                        print(
                            f"Invalid column. "
                            f"Please enter a number between 1 and {self.board.cols}."
                        )
                        continue

                    if self.board.is_column_full(column):
                        print("Column is full. Please choose another column.")
                        continue

                    position = self.board.drop_disc(column, current_player)
                    if position is None:
                        print("Failed to place disc. Please try again.")
                        continue

                    break
                except (ValueError, EOFError):
                    print("Invalid input. Please enter a valid column number.")

            row, col = position
            if self.win_checker.check_winner(self.board, row, col, current_player):
                self.board.display_winner(current_player)
                print(f"\n{'=' * 50}")
                print(f"🎉 {current_player.name} wins! 🎉")
                print(f"{'=' * 50}\n")
                game_over = True
            elif self.board.is_board_full():
                self.board.display_draw()
                print(f"\n{'=' * 50}")
                print("It's a draw! The board is full.")
                print(f"{'=' * 50}\n")
                game_over = True
            else:
                self.current_player_idx = (self.current_player_idx + 1) % len(self.players)

    def run(self) -> None:
        self.setup()
        self.play()
