import chess
import numpy as np
import torch

def parseResult(result):
    """
    Converts the string representation of a chess game's result into an integer.

    The mapping is -1 for a black win, 0 for a draw, and 1 for a white win. This function
    is useful for converting standard chess game outcomes into a numerical format that can
    be easily processed in various algorithms.

    :param result: The string representation of the game's result.
    :type result: str
    :return: An integer representing the game's outcome (-1, 0, 1).
    :rtype: int
    :raises ValueError: If the result string does not match any expected outcomes.

    :Example:

    >>> parseResult("1-0")
    1
    >>> parseResult("1/2-1/2")
    0
    >>> parseResult("0-1")
    -1
    >>> parseResult("unknown")  # Raises ValueError
    """

    # Mapping of result strings to their integer representations.
    result_mapping = {"1-0": 1, "1/2-1/2": 0, "0-1": -1}  # White wins  # Draw  # Black wins

    # Check if the result is in the mapping and return the corresponding integer.
    if result in result_mapping:
        return result_mapping[result]

    # Raise an exception for unexpected result strings.
    raise ValueError(f"Unexpected result string {result}. Expected '1-0', '0-1', or '1/2-1/2'.")


def encodePosition(board):
    """
    Encodes a chess board position into a 16-plane array.

    The first 12 planes represent the six types of chess pieces (Pawn, Knight, Bishop, Rook, Queen, King)
    for both white and black. The last 4 planes represent the castling rights (Kingside and Queenside)
    for both sides. This encoding is useful for representing chess positions in a format suitable for
    neural network input.

    :param board: The chess board position to be encoded.
    :type board: chess.Board
    :return: A 3-dimensional array (16, 8, 8) of type float32 representing the encoded chess position.
    :rtype: numpy.array

    :Example:

    >>> import chess
    >>> board = chess.Board()
    >>> encoded_position = encodePosition(board)
    >>> print(encoded_position.shape)
    (16, 8, 8)
    """

    planes = np.zeros((16, 8, 8), dtype=np.float32)

    # Piece type mapping to their respective plane indices.
    piece_planes = {
        chess.PAWN: (0, 1),
        chess.ROOK: (2, 3),
        chess.BISHOP: (4, 5),
        chess.KNIGHT: (6, 7),
        chess.QUEEN: (8, 9),
        chess.KING: (10, 11),
    }

    # Iterate through each piece type and encode their positions.
    for piece_type, (white_plane, black_plane) in piece_planes.items():
        for square in board.pieces(piece_type, chess.WHITE):
            rank, file = chess.square_rank(square), chess.square_file(square)
            planes[white_plane, rank, file] = 1.0

        for square in board.pieces(piece_type, chess.BLACK):
            rank, file = chess.square_rank(square), chess.square_file(square)
            planes[black_plane, rank, file] = 1.0

    # Encoding castling rights.
    castling_rights = [
        (board.has_kingside_castling_rights(chess.WHITE), 12),
        (board.has_kingside_castling_rights(chess.BLACK), 13),
        (board.has_queenside_castling_rights(chess.WHITE), 14),
        (board.has_queenside_castling_rights(chess.BLACK), 15),
    ]

    # Set entire planes for castling rights to 1.0 if available.
    for has_right, plane in castling_rights:
        if has_right:
            planes[plane, :, :] = 1.0

    return planes


def moveToIdx(move):
    """
    Converts a chess move to a unique index based on direction and distance in a 72-plane representation.

    This function categorizes chess moves into different types based on their direction (rook, bishop,
    or knight moves) and distance. This categorization allows for a compact and distinct representation
    of moves, which is particularly useful for neural network inputs in chess-related machine learning tasks.

    :param move: The chess move to be encoded.
    :type move: chess.Move
    :return: A tuple containing the plane index corresponding to the move's direction and distance,
             the starting rank (row), and the starting file (column) of the move.
    :rtype: Tuple[int, int, int]

    :Example:

    >>> import chess
    >>> move = chess.Move.from_uci('e2e4')
    >>> directionAndDistancePlane, from_rank, from_file = moveToIdx(move)
    >>> print(directionAndDistancePlane, from_rank, from_file)
    """
    # Extract the starting and ending squares of the move.
    from_rank = chess.square_rank(move.from_square)
    from_file = chess.square_file(move.from_square)
    to_rank = chess.square_rank(move.to_square)
    to_file = chess.square_file(move.to_square)

    # Calculate rank and file differences to determine direction and distance.
    rank_diff = to_rank - from_rank
    file_diff = to_file - from_file

    # Determine the direction and distance plane based on the type of move.
    if rank_diff == 0:  # Rook moves along the rank
        directionPlane = 0 if file_diff > 0 else 8
        distance = abs(file_diff)
    elif file_diff == 0:  # Rook moves along the file
        directionPlane = 16 if rank_diff > 0 else 24
        distance = abs(rank_diff)
    elif abs(rank_diff) == abs(file_diff):  # Bishop moves
        if rank_diff > 0:
            directionPlane = 32 if file_diff > 0 else 40
        else:
            directionPlane = 48 if file_diff > 0 else 56
        distance = abs(rank_diff)
    else:  # Knight moves
        # Map the knight's L-shape moves to the last 8 planes
        knight_moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        directionPlane = 64 + knight_moves.index((file_diff, rank_diff))
        distance = 0  # Distance is not relevant for knight moves

    directionAndDistancePlane = directionPlane + distance

    return directionAndDistancePlane, from_rank, from_file

def getLegalMoveMask(board):
    """
    Generates a mask encoding legal moves for a given chess position.

    This function creates a 3-dimensional array where each slice corresponds to one of the 72 move
    categories used in moveToIdx. Each slice contains a binary mask indicating whether a move belonging
    to that category is legal from each square of the board. This mask is useful for neural network
    models that need to filter out illegal moves in their predictions.

    :param board: The current chess board position.
    :type board: chess.Board
    :return: A 3-dimensional array representing the legal move mask. The array has dimensions (72, 8, 8)
             and is of type int32, where each slice corresponds to a different move category.
    :rtype: numpy.array

    :Example:

    >>> import chess
    >>> board = chess.Board()
    >>> legal_move_mask = getLegalMoveMask(board)
    >>> print(legal_move_mask.shape)
    (72, 8, 8)
    """
    # Initialize an empty mask with dimensions 72x8x8. 72 represents different types of moves.
    mask = np.zeros((72, 8, 8), dtype=np.int32)

    # Iterate through all legal moves in the current board position.
    for move in board.legal_moves:
        # Convert each move to its index representation.
        planeIdx, rankIdx, fileIdx = moveToIdx(move)
        # Set the corresponding position in the mask to 1, indicating a legal move.
        mask[planeIdx, rankIdx, fileIdx] = 1

    return mask

def mirrorMove(move):
    """
    Mirrors a given chess move vertically on the board.

    This function is used to maintain consistency in move representation irrespective of the player's color.
    Mirroring a move involves flipping the move's start and end squares along the central rank of the board.
    This is particularly useful in scenarios where a uniform representation of moves is required regardless
    of whether the player is playing with white or black pieces.

    :param move: The chess move to be mirrored.
    :type move: chess.Move
    :return: The mirrored chess move.
    :rtype: chess.Move

    :Example:

    >>> import chess
    >>> move = chess.Move.from_uci('e2e4')
    >>> mirrored_move = mirrorMove(move)
    >>> print(mirrored_move.uci())
    """

    # Get the source and destination squares of the move.
    from_square = move.from_square
    to_square = move.to_square

    # Mirror the source and destination squares vertically.
    new_from_square = chess.square_mirror(from_square)
    new_to_square = chess.square_mirror(to_square)

    # Return the new mirrored move.
    return chess.Move(new_from_square, new_to_square)


def encodeTrainingPoint(board, move, winner):
    """
    Encodes a chess position, a target move, and the game outcome for training purposes.

    This function is designed to prepare data for training chess-related neural network models.
    It encodes the board position, the target move, and the game outcome into formats suitable
    for model input. The board is encoded into a 16-plane representation, the move is converted
    to an index, the winner is represented as a float, and a legal move mask is generated.

    :param board: The chess position.
    :type board: chess.Board
    :param move: The target move from this position.
    :type move: chess.Move
    :param winner: The game outcome, where -1 means black won, 0 means draw, and 1 means white won.
    :type winner: int
    :return: A tuple containing the encoded chess board position, the index of the encoded target move,
             the encoded game outcome, and the legal move mask.
    :rtype: Tuple[numpy.array, int, float, numpy.array]

    :Example:

    >>> import chess
    >>> board = chess.Board()
    >>> move = chess.Move.from_uci('e2e4')
    >>> winner = 1  # Assuming white won
    >>> positionPlanes, moveIdx, winner, mask = encodeTrainingPoint(board, move, winner)
    >>> print(positionPlanes.shape, moveIdx, winner, mask.shape)
    (16, 8, 8) [moveIdx] 1.0 (72, 8, 8)
    """

    # Mirror the board and adjust the winner and move if it's black's turn.
    if not board.turn:
        board = board.mirror()
        winner *= -1
        move = mirrorMove(move)

    # Encode the current position into a 16x8x8 array.
    positionPlanes = encodePosition(board)

    # Convert the move into an index representation.
    planeIdx, rankIdx, fileIdx = moveToIdx(move)
    moveIdx = planeIdx * 64 + rankIdx * 8 + fileIdx

    # Generate a mask of legal moves in the current position.
    mask = getLegalMoveMask(board)

    return positionPlanes, moveIdx, float(winner), mask


def encodePositionForInference(board, color):
    """
    Encodes a chess position into a format suitable for inference with a neural network, considering the player's color.

    This function prepares a chess board position for neural network inference by encoding it into a multi-dimensional
    array. The encoding takes into account the color of the player, ensuring that the position is represented from
    the perspective of the specified player. Additionally, it generates a mask array that represents all legal moves
    available in the given position, which is crucial for move generation and validation in neural network-based chess engines.

    :param board: A chess board object representing the current game state.
    :type board: chess.Board
    :param color: The color of the player for whom the position is being encoded. Should be 'white' or 'black'.
    :type color: str
    :return: A tuple containing the encoded chess board and the legal move mask.
    :rtype: Tuple[numpy.array, numpy.array]

    :Example:

    >>> import chess
    >>> board = chess.Board()
    >>> color = 'white'
    >>> positionPlanes, mask = encodePositionForInference(board, color)
    >>> print(positionPlanes.shape, mask.shape)
    (16, 8, 8) (72, 8, 8)
    """
    # Flip the board if it's black's turn and the player is black.
    if not board.turn and color == "black":
        board = board.mirror()

    # Encode the current position into a 16x8x8 array.
    positionPlanes = encodePosition(board)

    # Generate a mask of legal moves in the current position.
    mask = getLegalMoveMask(board)

    return positionPlanes, mask


def decodePolicyOutput(board, policy):
    """
    Decodes the policy output from a neural network into move probabilities.

    This function takes the raw policy output from a neural network and translates it into a set of move probabilities.
    Each probability corresponds to a legal move on the given chess board. This is an essential step in converting
    neural network outputs into actionable decisions in a chess engine.

    :param board: The chess board object representing the current game state.
    :type board: chess.Board
    :param policy: The policy output from the neural network, typically a vector of probabilities.
    :type policy: numpy.array
    :return: An array of move probabilities corresponding to each legal move on the board.
    :rtype: numpy.array

    :Example:

    >>> import chess
    >>> import numpy as np
    >>> board = chess.Board()
    >>> policy = np.random.rand(1968)  # Example policy vector
    >>> move_probabilities = decodePolicyOutput(board, policy)
    >>> print(move_probabilities.shape)
    """

    # Initialize an array to store move probabilities. The size 200 is a buffer for maximum possible moves.
    move_probabilities = np.zeros(200, dtype=np.float32)

    # Initialize a counter for the number of legal moves.
    num_moves = 0

    # Iterate over all legal moves in the current board position.
    for idx, move in enumerate(board.legal_moves):
        # If it's black's turn, mirror the move to match the training data.
        if not board.turn:
            move = mirrorMove(move)

        # Convert the move into an index representation.
        planeIdx, rankIdx, fileIdx = moveToIdx(move)
        moveIdx = planeIdx * 64 + rankIdx * 8 + fileIdx

        # Assign the probability from the policy output to the corresponding move.
        move_probabilities[idx] = policy[moveIdx]
        num_moves += 1

    # Trim the probabilities array to the number of legal moves.
    return move_probabilities[:num_moves]


def callNeuralNetwork(board, neural_network, color, device='cpu'):
    """
    Evaluate a chess board position using a neural network.

    This function uses a neural network model to evaluate a given chess board position. It takes into account
    the player's color to determine the evaluation perspective. The neural network provides both the value
    of the position and move probabilities for legal moves.

    :param board: The current state of the chess board.
    :type board: chess.Board
    :param neural_network: The neural network model to use for evaluation.
    :type neural_network: torch.nn.Module
    :param color: The color of the player to move, where True represents white and False represents black.
    :type color: bool
    :param device: The device on which to perform the evaluation (e.g., 'cpu' or 'cuda:0').
    :type device: str, optional
    :return: A tuple containing the value of the position from the perspective of the player to move (float)
             and an array of move probabilities for each legal move (numpy.array).
    :rtype: Tuple[float, numpy.array]

    :Example:

    >>> import chess
    >>> import torch
    >>> board = chess.Board()
    >>> neural_net = torch.nn.Module()  # Example neural network model
    >>> color = True  # White to move
    >>> value, move_probabilities = callNeuralNetwork(board, neural_net, color)
    >>> print(value, move_probabilities.shape)
    """
    # Encode the board position for inference
    position, mask = encodePositionForInference(board, color)

    # Convert the position and mask to torch tensors
    position = torch.from_numpy(position)[None, ...]
    mask = torch.from_numpy(mask)[None, ...]

    # Transfer tensors to the appropriate device
    position = position.to(device)
    mask = mask.to(device)
    neural_network = neural_network.to(device)

    # Perform inference using the neural network
    value, policy = neural_network(position, policyMask=mask)

    # Move the outputs back to CPU and convert them to numpy arrays
    value = value.cpu().detach().numpy()[0, 0]
    policy = policy.cpu().detach().numpy()[0]

    # Decode the policy output to move probabilities
    move_probabilities = decodePolicyOutput(board, policy)

    return value, move_probabilities


def callNeuralNetworkBatched(boards, neural_network, device='cpu'):
    """
    Evaluate multiple chess board positions using a neural network in a batched manner.

    This function efficiently evaluates a batch of chess board positions using a neural network model.
    It takes a list of chess board states and returns an array containing the values of each position
    and a 2D array containing move probabilities for each board position.

    :param boards: A list of chess board states to evaluate.
    :type boards: list of chess.Board
    :param neural_network: The neural network model to use for evaluation.
    :type neural_network: torch.nn.Module
    :param device: The device on which to perform the evaluation (e.g., 'cpu' or 'cuda:0').
    :type device: str, optional
    :return: A tuple containing:
        - An array containing the values of each position.
        - A 2D array containing move probabilities for each board position.
    :rtype: Tuple[numpy.array, numpy.array]

    :Example:

    >>> import chess
    >>> import torch
    >>> boards = [chess.Board() for _ in range(5)]  # Example list of chess board states
    >>> neural_net = torch.nn.Module()  # Example neural network model
    >>> values, move_probabilities = callNeuralNetworkBatched(boards, neural_net)
    >>> print(values.shape, move_probabilities.shape)
    """
    num_inputs = len(boards)

    # Initialize tensors to hold input positions and masks
    inputs = torch.zeros((num_inputs, 16, 8, 8), dtype=torch.float32)
    masks = torch.zeros((num_inputs, 72, 8, 8), dtype=torch.float32)

    # Encode each board position and mask, and store them in the respective tensors
    for i, board in enumerate(boards):
        position, mask = encodePositionForInference(board)
        inputs[i] = torch.from_numpy(position)
        masks[i] = torch.from_numpy(mask)

    # Transfer tensors to GPU if available
    inputs = inputs.to(device)
    masks = masks.to(device)
    neural_network = neural_network.to(device)

    # Perform batch inference using the neural network
    value, policy = neural_network(inputs, policy_mask=masks)

    # Prepare to store move probabilities
    move_probabilities = np.zeros((num_inputs, 200), dtype=np.float32)

    # Move the outputs back to CPU and reshape them as needed
    value = value.cpu().numpy().reshape((num_inputs))
    policy = policy.cpu().numpy()

    # Decode policy outputs for each board and store the results
    for i, board in enumerate(boards):
        move_probs = decodePolicyOutput(board, policy[i])
        move_probabilities[i, : move_probs.shape[0]] = move_probs

    return value, move_probabilities
