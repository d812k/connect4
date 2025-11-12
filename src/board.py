from src.player import Player


class Board:
    def __init__(self, rows: int, cols: int) -> None:
        if not (6 <= rows <= 15):
            raise ValueError("Rows must be between 6 and 15")
        if not (6 <= cols <= 15):
            raise ValueError("Columns must be between 6 and 15")

        self.rows = rows
        self.cols = cols
        self.grid: list[list[Player | None]] = [[None for _ in range(cols)] for _ in range(rows)]

    def is_column_valid(self, column: int) -> bool:
        return 1 <= column <= self.cols

    def is_column_full(self, column: int) -> bool:
        col_idx = column - 1
        return self.grid[0][col_idx] is not None

    def drop_disc(self, column: int, player: Player) -> tuple[int, int] | None:
        if not self.is_column_valid(column):
            return None
        if self.is_column_full(column):
            return None

        col_idx = column - 1
        for row_idx in range(self.rows - 1, -1, -1):
            if self.grid[row_idx][col_idx] is None:
                self.grid[row_idx][col_idx] = player
                return (row_idx, col_idx)

        return None

    def is_board_full(self) -> bool:
        return all(self.grid[0][col] is not None for col in range(self.cols))

    def display(self, current_player: Player, html_file: str = "board.html") -> None:
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="1">
    <title>Connect4</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        table {
            border-collapse: collapse;
            background-color: #0066cc;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        td {
            width: 60px;
            height: 60px;
            text-align: center;
            vertical-align: middle;
            font-size: 32px;
            border: 3px solid #004080;
        }
        .empty {
            background-color: white;
        }
        th {
            color: white;
            font-size: 20px;
            padding: 5px;
        }
        .current-turn {
            font-size: 24px;
            margin: 20px;
            padding: 15px;
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
    </style>
</head>
<body>
"""
        html += "    <h1>Connect4</h1>\n"
        html += (
            f'    <div class="current-turn">Current Turn: <strong>{current_player.name}</strong> '
            f'<span style="color: {current_player.color}; font-size: 32px;">'
            f"{current_player.symbol}</span></div>\n"
        )
        html += "    <table>\n"

        html += "        <tr>\n"
        for col in range(1, self.cols + 1):
            html += f"            <th>{col}</th>\n"
        html += "        </tr>\n"

        for row in range(self.rows):
            html += "        <tr>\n"
            for col in range(self.cols):
                player = self.grid[row][col]
                if player is None:
                    html += '            <td class="empty"></td>\n'
                else:
                    html += (
                        f'            <td style="background-color: {player.color};">'
                        f"{player.symbol}</td>\n"
                    )
            html += "        </tr>\n"

        html += "    </table>\n"
        html += "</body>\n"
        html += "</html>\n"

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)

    def display_winner(self, winner: Player, html_file: str = "board.html") -> None:
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Connect4 - Winner!</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        .winner-message {
            font-size: 36px;
            margin: 20px;
            padding: 20px;
            background-color: #4CAF50;
            color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        table {
            border-collapse: collapse;
            background-color: #0066cc;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        td {
            width: 60px;
            height: 60px;
            text-align: center;
            vertical-align: middle;
            font-size: 32px;
            border: 3px solid #004080;
        }
        .empty {
            background-color: white;
        }
        th {
            color: white;
            font-size: 20px;
            padding: 5px;
        }
    </style>
</head>
<body>
"""
        html += "    <h1>Connect4</h1>\n"
        html += f'    <div class="winner-message">🎉 {winner.name} wins! 🎉</div>\n'
        html += "    <table>\n"

        html += "        <tr>\n"
        for col in range(1, self.cols + 1):
            html += f"            <th>{col}</th>\n"
        html += "        </tr>\n"

        for row in range(self.rows):
            html += "        <tr>\n"
            for col in range(self.cols):
                player = self.grid[row][col]
                if player is None:
                    html += '            <td class="empty"></td>\n'
                else:
                    html += (
                        f'            <td style="background-color: {player.color};">'
                        f"{player.symbol}</td>\n"
                    )
            html += "        </tr>\n"

        html += "    </table>\n"
        html += "</body>\n"
        html += "</html>\n"

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)

    def display_draw(self, html_file: str = "board.html") -> None:
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Connect4 - Draw</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            margin: 20px;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        .draw-message {
            font-size: 36px;
            margin: 20px;
            padding: 20px;
            background-color: #FF9800;
            color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        table {
            border-collapse: collapse;
            background-color: #0066cc;
            padding: 10px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        }
        td {
            width: 60px;
            height: 60px;
            text-align: center;
            vertical-align: middle;
            font-size: 32px;
            border: 3px solid #004080;
        }
        .empty {
            background-color: white;
        }
        th {
            color: white;
            font-size: 20px;
            padding: 5px;
        }
    </style>
</head>
<body>
"""
        html += "    <h1>Connect4</h1>\n"
        html += '    <div class="draw-message">It\'s a draw! The board is full.</div>\n'
        html += "    <table>\n"

        html += "        <tr>\n"
        for col in range(1, self.cols + 1):
            html += f"            <th>{col}</th>\n"
        html += "        </tr>\n"

        for row in range(self.rows):
            html += "        <tr>\n"
            for col in range(self.cols):
                player = self.grid[row][col]
                if player is None:
                    html += '            <td class="empty"></td>\n'
                else:
                    html += (
                        f'            <td style="background-color: {player.color};">'
                        f"{player.symbol}</td>\n"
                    )
            html += "        </tr>\n"

        html += "    </table>\n"
        html += "</body>\n"
        html += "</html>\n"

        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)

    def display_goodbye(self, html_file: str = "board.html") -> None:
        html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Connect4 - Game Over</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 0;
            height: 100vh;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
            font-size: 48px;
            margin: 20px;
        }
        .message {
            font-size: 24px;
            color: #666;
            margin: 20px;
        }
    </style>
</head>
<body>
    <h1>Good-bye!</h1>
    <div class="message">Заходите к нам опять =)</div>
</body>
</html>
"""
        with open(html_file, "w", encoding="utf-8") as f:
            f.write(html)
