class Player:
    def __init__(self, name: str, symbol: str, color: str) -> None:
        self.name = name
        self.symbol = symbol
        self.color = color

    def __str__(self) -> str:
        return f"{self.name} ({self.symbol})"
