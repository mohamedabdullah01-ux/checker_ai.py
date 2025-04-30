def getNextBoard(game : Game, move : full_move) -> Game:
  next_board = copy.deepcopy(game)
  move.make_move(game=next_board)
  return next_board

# Function to get all possible sequences of partial moves from the current board


def getAllFullMoveSequences(game : Game): 
  fullMoveSequences = []
  player_turn = game.whose_turn()

  # Create a deque that is used to hold on to game states at partial moves
  sequenceQueue = deque()
  
  # Add an initial element corresponding to the current game
  current_game = game
  startingEntry = (current_game, [])
  sequenceQueue.append(startingEntry)

  # While the deque is not empty, continue processing move sequences
  while sequenceQueue:
    current_game, sequence = sequenceQueue.pop()

    # If the current element corresponds to a position where the current player can still move, get all possible partial moves from that position
    if current_game.whose_turn() == player_turn:
      moves = current_game.get_possible_moves()

      # For each partial move, create a new sequenceQueue element using the current sequence of moves
      for partial_move in moves:
        next_board = copy.deepcopy(current_game)
        next_board.move(partial_move)
        next_sequence = copy.deepcopy(sequence)
        next_sequence.append(partial_move)
        entry = next_board, next_sequence
        sequenceQueue.append(entry)

    # Otherwise, add the finished move sequence to the overall list
    else:
      fullMoveSequences.append(sequence)
      
  return fullMoveSequences

# Function to get all possible full_moves from the current board


def getAllFullMoves(game : Game)-> List[full_move]:
  full_moves = list()

  # Get every move sequence from the current board
  move_sequences = getAllFullMoveSequences(game)

  # Convert each move sequence to a full_move
  for move_sequence in move_sequences:
    full_moves.append(full_move(move_sequence))

  return full_moves

# Function to get all possible boards that result from moves from the current board


def getAllChildBoards(node : Node) -> List[Game]:
  child_boards = list()

  # Get all possible full_moves from the current board
  all_moves = getAllFullMoves(node.game)

  # For each full_move, get the resulting board
  for move in all_moves:
    child_boards.append((getNextBoard(node.game, move), move))

  return child_boards

# Function to write a text representation of the map to the output
