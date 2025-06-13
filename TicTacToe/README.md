# Parking Lot low-level-design

Discuss basic workflow:

1. 2 Players assign 'X' and 'O'
2. Take turns to fill a board of 9 spots (3 \* 3)
3. Make sure once the spot is filled, do not overlap
4. To Win:
   a. Same sign horizontal
   b. Same sign vertical
   c. Same sign diagonal
   End the game
5. When all the spots are filled
   End the game

Clarify requirements:

1. How many pieces? I will make an enum if in case we need to an in the future
2. Assumed 2 players

Identify Entities:

1. Player - name, piece
2. PieceType - mark, Piece(Enum)
3. Board - n, board, spots_filled, mark(), get_board(), is_full(), has_winner()
4. Game - board, player1 and 2, current_player, play(), switch_player
