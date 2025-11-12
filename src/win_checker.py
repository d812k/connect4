from src.board import Board
from src.player import Player


class WinChecker:
    REQUIRED_CONSECUTIVE = 4

    @staticmethod
    def check_winner(board: Board, row: int, col: int, player: Player) -> bool:
        return (
            WinChecker._check_horizontal(board, row, col, player)
            or WinChecker._check_vertical(board, row, col, player)
            or WinChecker._check_diagonal_ascending(board, row, col, player)
            or WinChecker._check_diagonal_descending(board, row, col, player)
        )

    @staticmethod
    def _count_direction(board: Board, row: int, col: int, player: Player, dr: int, dc: int) -> int:
        count = 0
        current_row = row + dr
        current_col = col + dc

        while (
            0 <= current_row < board.rows
            and 0 <= current_col < board.cols
            and board.grid[current_row][current_col] == player
        ):
            count += 1
            current_row += dr
            current_col += dc

        return count

    @staticmethod
    def _check_horizontal(board: Board, row: int, col: int, player: Player) -> bool:
        left_count = WinChecker._count_direction(board, row, col, player, 0, -1)
        right_count = WinChecker._count_direction(board, row, col, player, 0, 1)
        total = left_count + right_count + 1
        return total >= WinChecker.REQUIRED_CONSECUTIVE

    @staticmethod
    def _check_vertical(board: Board, row: int, col: int, player: Player) -> bool:
        up_count = WinChecker._count_direction(board, row, col, player, -1, 0)
        down_count = WinChecker._count_direction(board, row, col, player, 1, 0)
        total = up_count + down_count + 1
        return total >= WinChecker.REQUIRED_CONSECUTIVE

    @staticmethod
    def _check_diagonal_ascending(board: Board, row: int, col: int, player: Player) -> bool:
        bottom_left_count = WinChecker._count_direction(board, row, col, player, 1, -1)
        top_right_count = WinChecker._count_direction(board, row, col, player, -1, 1)
        total = bottom_left_count + top_right_count + 1
        return total >= WinChecker.REQUIRED_CONSECUTIVE

    @staticmethod
    def _check_diagonal_descending(board: Board, row: int, col: int, player: Player) -> bool:
        top_left_count = WinChecker._count_direction(board, row, col, player, -1, -1)
        bottom_right_count = WinChecker._count_direction(board, row, col, player, 1, 1)
        total = top_left_count + bottom_right_count + 1
        return total >= WinChecker.REQUIRED_CONSECUTIVE
