# chess
chess game with python
Class and Method Renaming:

The classes and methods have been renamed to provide clarity and uniqueness (ChessPiece, legal_move, etc.).
Symbol Handling:

Each chess piece now has a symbol attribute that handles how it is displayed on the board. This helps make the code modular.
Board Representation:

The ChessBoard class includes a translate_position method that converts chess notation (e.g., e2) into indices for the board grid.
Error Handling:

The move method includes robust error handling, providing feedback when an illegal move is attempted.
Modular Piece Implementation:

Each piece type is a subclass of ChessPiece, with its own legal_move method, keeping the code organized and easy to extend.
