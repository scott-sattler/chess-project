sound_dictionary = {
    'drop piece':           'sounds/digi_plink.wav',
    'pickup piece':         'sounds/click_04.wav',
    'not allowed':          'sounds/invalid2.wav',
    'undo':                 'sounds/click_04.wav',      # TODO default sound being used
    'undo error':           'sounds/google_mp3_converted/no moves to undo.wav',  # 'sounds/undo_error.wav',
    'redo':                 'sounds/digi_plink.wav',    # TODO default sound being used
    'redo error':           'sounds/google_mp3_converted/no moves to redo.wav',  # 'sounds/redo_error.wav',    # todo

    'check':                'sounds/google_mp3_converted/check.wav',  #'sounds/check.wav',
    'captures':             'sounds/google_mp3_converted/captures.wav',  # 'sounds/piece_capture.wav',
    'self check':           'sounds/google_mp3_converted/that move would put your king into check.wav',  # 'sounds/self_check.wav',
    'check not removed':    'sounds/google_mp3_converted/that move does not remove check.wav',  # 'sounds/check_not_removed.wav',
    'castle while checked': 'sounds/google_mp3_converted/cannot castle while in check.wav',  # 'sounds/castle_while_checked.wav',
    'castle queen':         'sounds/google_mp3_converted/castle queen side.wav',  # 'sounds/castle_queen.wav',
    'O-O-O':                'sounds/google_mp3_converted/castle queen side.wav',
    'castle king':          'sounds/google_mp3_converted/castle king side.wav',  # 'sounds/castle_king.wav',
    'O-O':                  'sounds/google_mp3_converted/castle king side.wav',
    'draw':                 'sounds/google_mp3_converted/draw.wav',
    'checkmate':            'sounds/google_mp3_converted/checkmate.wav',  # 'sounds/checkmate.wav',
    'stalemate':            'sounds/google_mp3_converted/stalemate.wav',
    'white wins':           'sounds/white_wins.wav',  # todo warning remove
    'black wins':           'sounds/black_wins.wav',  # todo warning remove
    'wins':                 'sounds/google_mp3_converted/wins!.wav',

    'white':                'sounds/google_mp3_converted/white.wav',
    'black':                'sounds/google_mp3_converted/black.wav',
    'pawn':                 'sounds/google_mp3_converted/pawn.wav',
    'rook':                 'sounds/google_mp3_converted/rook.wav',
    'bishop':               'sounds/google_mp3_converted/bishop.wav',
    'knight':               'sounds/google_mp3_converted/knight.wav',
    'queen':                'sounds/google_mp3_converted/queen.wav',
    'king':                 'sounds/google_mp3_converted/king.wav',

    'timer enabled':        'sounds/google_mp3_converted/timer enabled.wav',
    'timer disabled':       'sounds/google_mp3_converted/timer disabled.wav',
    'timer: in progress':   'sounds/google_mp3_converted/the timer cannot be enabled for games already in progress.wav',
    'nothing to reset':     'sounds/google_mp3_converted/nothing to reset.wav',
    'move announcement':    'sounds/google_mp3_converted/move announcement.wav',
    'muted':                'sounds/google_mp3_converted/muted.wav',
    'unmuted':              'sounds/google_mp3_converted/unmuted.wav',
    'board reset':          'sounds/google_mp3_converted/board. re-set.wav',  # board reset.wav',
    # 'board already reset':  'sounds/google_mp3_converted/the board is already in its initial state.wav',
    'must disable timer':   'sounds/google_mp3_converted/the timer must be disabled to use this function.wav',


    'enabled':              'sounds/google_mp3_converted/enabled.wav',
    'disabled':             'sounds/google_mp3_converted/disabled.wav',

    # debugging
    'delete piece':         'sounds/debugging/Skorpion-Kibblesbob-1109158827.wav',
    'not implemented':      'sounds/google_mp3_converted/not implemented.wav'

}

Spoken_Text = [
    "White",
    "Black",
    "Pawn",
    "Rook",
    "Bishop",
    "Knight",
    "Queen",
    "King",
    "A1", "A2", "A3", "A4", "A5", "A6", "A7", "A8",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
    "C1", "C2", "C3", "C4", "C5", "C6", "C7", "C8",
    "D1", "D2", "D3", "D4", "D5", "D6", "D7", "D8",
    "E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8",
    "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8",
    "G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8",
    "H1", "H2", "H3", "H4", "H5", "H6", "H7", "H8",
    # 72
    "Check",
    "Checkmate",
    "Castle King Side",
    "Castle Queen Side",
    "That move would put your king into check",
    "That move does not remove check",
    "Captures",
    "Wins!",
    # edited
    "Hello. I am Google's new Text To Speech algorithm that uses long-short-term-memory-recurrent-neural-networks",
    "I was trained by listening to donated voice mails. I can be found in every up-to-date Android device",
    # reorder and rerun entire thing?
    "Cannot castle while in check",
    "No moves to undo",
    "No moves to redo",

    # todo add these
    'stalemate',
    'not implemented',
    'draw',
    'Timer enabled',
    'Timer disabled',
    'The timer cannot be enabled for games already in progress',
    'nothing to reset',
    'enabled',
    'disabled',
    'move announcement',
    'move announcement enabled',  # todo sounds better, but google's model needs to be replaced
    'muted',
    'unmuted',
    'board reset',  # 'board. re-set',
    'the board is already in its initial state',
    'the timer must be disabled to use this function'
]

