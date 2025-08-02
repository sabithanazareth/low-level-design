from enum import Enum

class Piece(Enum):
  X = "X"
  O = "O"
  I = "I"
  V = "V"

class PieceType:
  def __init__(self, mark):
    self.mark = mark

class PieceTypeX(PieceType):
  def __init__(self):
    super().__init__(Piece.X)

class PieceTypeO(PieceType):
  def __init__(self):
    super().__init__(Piece.O)

class Player:
  def __init__(self, name, piece):
    self.name = name
    self.piece = piece

class Board:
  def __init__(self, n):
    self.n = n
    self.board = [["."] * n for i in range(n)]
    self.spots_filled = 0
  
  def mark(self, position, current_player):
    x = int(position[0])
    y = int(position[1])

    spot = self.board[x][y]
    if spot == ".":
      self.board[x][y] = current_player.piece.mark.name
      self.spots_filled += 1
    else:
      raise Exception(f"Spot is already marked by {self.board[x][y]}")
  
  def get_board(self):
    for row in self.board:
      print("|".join(row))

  def is_full(self):
    return self.spots_filled == self.n * self.n
  
  def has_winner(self) -> bool:
    # 1) Check each row
    for i in range(self.n):
        mark = self.board[i][0]
        if mark != "." and all(self.board[i][j] == mark for j in range(self.n)):
            return True

    # 2) Check each column
    for j in range(self.n):
        mark = self.board[0][j]
        if mark != "." and all(self.board[i][j] == mark for i in range(self.n)):
            return True

    # 3) Check main diagonal
    mark = self.board[0][0]
    if mark != "." and all(self.board[i][i] == mark for i in range(self.n)):
        return True

    # 4) Check anti-diagonal
    mark = self.board[0][self.n - 1]
    if mark != "." and all(self.board[i][self.n - 1 - i] == mark for i in range(self.n)):
        return True

    return False
     

class Game:
  def __init__(self, board, player1, player2):
    self.board = board
    self.player1 = player1
    self.player2 = player2
    self.current_player = self.player1

  def play(self):
    self.board.get_board()
    while not self.board.is_full() and not self.board.has_winner():
      print(f"Current Player: {self.current_player.name}")
      position = input('Enter the position: ')
      try:
        self.validate_input(position)
        self.board.mark(position, self.current_player)
        self.board.get_board()
        self.switch_player()
      except Exception as e:
        print("Error", e)
        continue
      
    if self.board.has_winner():
        self.switch_player()
        print(f"{self.current_player.name} wins!")
    else:
      print("Its a tie, No more positions left")
      
  
  def switch_player(self):
    self.current_player = self.player2 if self.current_player == self.player1 else self.player1

  def validate_input(self, input):
    if len(input) > 2 or len(input) < 2:
      raise Exception("Please enter 2 digits")
    x = int(input[0])
    y = int(input[1])
    if x > self.board.n - 1 or x < 0 or y > self.board.n - 1 or y < 0:
      raise Exception("Incorrect position, try again")

def get_board_size(min_size: int = 3) -> int:
  while True:
    user_input = input(f"Enter board size (integer ≥ {min_size}): ")
    try:
        n = int(user_input)
    except ValueError:
        print("  ✗ That’s not a number. Please enter an integer.")
        continue
    if n < min_size:
        print(f"  ✗ Board size must be at least {min_size}.")
        continue
    return n
    
class TicTacToe:
  @staticmethod
  def run():
    piece_x = PieceTypeX()
    player1 = Player("Player1", piece_x)

    piece_o = PieceTypeO()
    player2 = Player("Player2", piece_o)

    board_number = get_board_size()
    board = Board(board_number)
    game = Game(board, player1, player2)
    print("Results: ")
    game.play()

if __name__ == "__main__":
  TicTacToe.run()