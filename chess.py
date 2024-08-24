class ChessPiece:
    def __init__(self, team):
        self.team = team

    def legal_move(self, origin, destination, board):
        raise NotImplementedError("This method should be implemented by subclasses")

    def __str__(self):
        return self.symbol.upper() if self.team == 'white' else self.symbol.lower()

class King(ChessPiece):
    symbol = 'K'
    
    def legal_move(self, origin, destination, board):
        return max(abs(destination[0] - origin[0]), abs(destination[1] - origin[1])) == 1

class Queen(ChessPiece):
    symbol = 'Q'
    
    def legal_move(self, origin, destination, board):
        row_difference = abs(destination[0] - origin[0])
        col_difference = abs(destination[1] - origin[1])
        return row_difference == col_difference or origin[0] == destination[0] or origin[1] == destination[1]

class Rook(ChessPiece):
    symbol = 'R'
    
    def legal_move(self, origin, destination, board):
        return origin[0] == destination[0] or origin[1] == destination[1]

class Bishop(ChessPiece):
    symbol = 'B'
    
    def legal_move(self, origin, destination, board):
        return abs(destination[0] - origin[0]) == abs(destination[1] - origin[1])

class Knight(ChessPiece):
    symbol = 'N'
    
    def legal_move(self, origin, destination, board):
        row_difference = abs(destination[0] - origin[0])
        col_difference = abs(destination[1] - origin[1])
        return (row_difference == 2 and col_difference == 1) or (row_difference == 1 and col_difference == 2)

class Pawn(ChessPiece):
    symbol = 'P'
    
    def legal_move(self, origin, destination, board):
        forward = -1 if self.team == 'white' else 1
        return destination[1] == origin[1] and destination[0] == origin[0] + forward

class ChessBoard:
    def __init__(self):
        self.grid = [
            [Rook('black'), Knight('black'), Bishop('black'), Queen('black'), King('black'), Bishop('black'), Knight('black'), Rook('black')],
            [Pawn('black') for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [None for _ in range(8)],
            [Pawn('white') for _ in range(8)],
            [Rook('white'), Knight('white'), Bishop('white'), Queen('white'), King('white'), Bishop('white'), Knight('white'), Rook('white')]
        ]

    def show(self):
        print("  a b c d e f g h")
        for row_idx, row in enumerate(self.grid):
            print(8 - row_idx, end=" ")
            for square in row:
                print(str(square) if square else '.', end=" ")
            print(8 - row_idx)
        print("  a b c d e f g h")

    def translate_position(self, pos):
        return 8 - int(pos[1]), ord(pos[0]) - ord('a')

    def move(self, start, end):
        origin = self.translate_position(start)
        destination = self.translate_position(end)
        piece = self.grid[origin[0]][origin[1]]

        if not piece:
            raise ValueError("No piece at the starting position.")
        
        if piece.legal_move(origin, destination, self.grid):
            self.grid[destination[0]][destination[1]] = piece
            self.grid[origin[0]][origin[1]] = None
        else:
            raise ValueError("Illegal move attempted.")

def play_chess():
    board = ChessBoard()
    current_player = 'white'
    
    while True:
        board.show()
        print(f"{current_player.capitalize()}'s turn.")
        
        move_input = input("Enter your move (e.g., e2 e4): ").strip().lower()
        try:
            start, end = move_input.split()
            board.move(start, end)
            current_player = 'black' if current_player == 'white' else 'white'
        except (ValueError, IndexError) as e:
            print(f"Invalid move: {e}")

play_chess()
