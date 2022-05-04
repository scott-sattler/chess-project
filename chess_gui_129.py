from Tkinter import Tk, Canvas, Label, StringVar, Text, Menu
import tkFont
from PIL import Image, ImageTk
from copy import deepcopy, copy
from time import sleep
import os
import sys
import random
import winsound
import wave
from chess_board import *
import cProfile
import chess_sound
from large_lists import Spoken_Text
from large_lists import sound_dictionary
#import sounddevice as sd
import math
import time
import datetime
from load_font import loadfont
import cPickle as pickle

# things to purchase for non-personal use:
# font
# some icons
# the pieces?
# sounds?

'''
# TODO EVERYTHING EXCEPT THE BOARD MATRIX ITSELF IS X Y

# TODO colors: #663300 #C19A6B

# TODO REFACTOR: combine piece definitions
# todo mystery  # todo why +1? the + 1 had to do with canvas.draw_rectangle
# TODO NONE v ZERO
# todo visual: WHITE v BLACK TURN (it's ugly)
# todo style: ugly title text
# todo remove many .self s for readability?

# todo consolidate current/opposite player etc?

# todo refactor consolidate current/opposite players into global variables ? and update them after each move

# todo um, refactor pawn?
# todo refactor rook/queen type movement
# todo refactor most movements into something more readable/elegant

# TODO refactor: at some point remove first_tile out of piece_info

# TODO COMPLEX IF STATEMENTS http://docs.python-guide.org/en/latest/writing/style/

# todo better names: board and piece? location_0, location_1; first_tile, second_tile

# todo CODE make the first/second_tile into a class? first_tile.x

# todo opposite => other

# todo CRITICAL disable undo button after undo, until next move (or make the game completely undoable)

# TODO TODO TODO NOTE: copying StackOverflow code for titlebar
# TODO priority
# TODO DESIGN: EACH MOVE, EG: <PAWN A1 TO A2>; <PAWN A1 CAPTURES KNIGHT B2> >>>Look up how they announce it<<<
# TODO disabled undo button (and other buttons) at correct times
# todo I never config the pieces I create... borderwidth=0, highlightthickness=0 ?
# TODO CRITICAL undo broken

# todo SOUND: pygame can solve sound problems see http://stackoverflow.com/questions/34535510/playing-a-lot-of-sounds-at-once
# todo refactor: use the large transparent pieces

# todo learning when should i use *args and what is **kwargs

# todo code design: review my use of selfs vs passing through functions.

# TODO LEARN: when to use classes and static methods etc.

# TODO LEARNING: it seems you can compare ()... not sure where I read you couldn't or shouldn't

# TODO chess notation is really useful

# todo REFACTOR update magnitude_and_direction of all pieces (created new function)

# todo SOUND: "piece capture" is clipped by "check" (should just use pygame sound)

# todo refactor v_spacer, board_container, etc

# NOTE: using canvas objects may be ideal. use the new image method to import the images, but continue to use canvas objects

# todo learn chess notation and use it

# todo visual: lighten up board

# todo should i track every pieces location ? would be easy and possibly more efficient computationally

#warning TODO remaining rules:
# todo Threefold Repetition         https://en.wikipedia.org/wiki/Threefold_repetition
# TODO omg check mate...

# Note: I'm making a design decision to remove the piece_rule() -> check_rule() -> move() chain,
#       in favor of having to manually call each, and generalizing these rule checks for use
#       in the checkmate() function (and for later experimentation with AI).
# Note: Nope. Too much work. Can just brute force through what I have. Not elegant, but quick to
#       implement.

# Note: MousePress:     board_event_handler -> event_handler_press
#       MouseRelease:   board_event_handler -> event_handler_release -> piece_rules
#                       piece_rules -> check_rules -> move_piece

# for each move, keep a copy of the previous board state.
# when undo, find difference, use old board, re-.place() objects not matching old board

# that may not work with not being able to make actual copies of these objects...
# maybe: don't delete the move list when undo(), but when exiting undo()/redo(), create new fork (discard previous path)

# TODO [Fixed?] potential king interaction with path blocking and out of index [Fixed? was related to castling?]
# TODO [Fixed?] pawn interaction with path blocking, more out of index [haven't seen in ages around time fixed the king bug]

# todo toggle the 'simulation' moves print statements

# todo substitute enemy_tile with attacking_tile/attacked_tile

# todo after a game is over go through and destroy all of the unused objects
# todo also make sure what discarded objects that are no longer tracked are destroyed
# or will python do this for me?

# TODO PERFORMANCE: USE NUMPY

# todo clean up debugging print statements

# todo does displayed captures show properly?

# todo don't destroy any objects until game ends/new game (undo)

# todo wtf does ddr stand for, and rename it?

#warning TODO temporary_move promotion

# todo rename helper functions? such as magnitude_and_direction

# TODO MAJOR REFACTOR: use piece_list and not piece_info?

# todo c_01 vs c_1

# todo At some point refactor the use of globals, better isolate functions,
# todo use more general (but possibly slightly less efficient) solutions.

# learn about @staticmethod
and http://stackoverflow.com/a/9450673/6666148


for i, chunk in enumerate(chunks):
    chunk.export("/path/to/ouput/dir/chunk{0}.wav".format(i), format="wav")

#warning TODO RULE: https://en.wikipedia.org/wiki/Fifty-move_rule
'''

#todo [DONE?] verify refactoring self.selected_tile did not break anything
# self.selected tile was representing both first_ and second_ tiles depending on the state of the game

# checkmate check seems to work fine for manual play, but not auto

# on promotion, wait for user to pick piece?
# todo sound
# todo stalemate
# todo finish/undo debugging_printer
# todo https://en.wikipedia.org/wiki/Chess_clock
#warning todo press p, and find this error in bug output.txt
#warning todo http://stackoverflow.com/a/15412863/6666148 (logging debugging)
# todo un-suppress unblocking() prints
# todo textbox castle
# todo bug [confirmed] sometimes mouse depresses and nothing happens (move coloring remains have to redo move)
#warning todo visual BUG board click to board click
#warning TODO does not handle en passant correctly (returns it as a move not a capture); does not correctl color board
# todo performance: use fast_no_valid_moves rather than no_valid_moves if really necessary... unless performance hit is very large, i'd rather use the same code/function
# todo bug press button and move mouse off board


# performance:
#   text box update [DONE: first iteration dramatic reduction 210/167 vs 54/4 (reduced calls)]
#   in checkmate
#   color piece background?  [DONE: massive reduction by reducing calls]
#   what is "(see)" ?

# todo current tasks:
    # fix/enable stalemate
    # notification window x box
    # random move seems to be broken
    # if that's not the case there's a bug somewhere else
    # promotions seem buggy (with random moves)

# todo warning just completely rewrite random move from scratch? if there is a bug in that I could have rewrote it many times over by now
#warning todo extremely likely that the bug is related to promotion (in random move)#warning todo extremely likely that the bug is related to promotion (in random move)#warning todo extremely likely that the bug is related to promotion (in random move)#warning todo extremely likely that the bug is related to promotion (in random move)#warning todo extremely likely that the bug is related to promotion (in random move)#warning todo extremely likely that the bug is related to promotion (in random move)

# could not recreate the behavior when stopping on the first promotion
#todo i think this is the bug: a pawn is getting promoted, but the king takes the promotion (eliminating the king)

# todo warning just completely rewrite random move from scratch? if there is a bug in that I could have rewrote it many times over by now

# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG
# put enemy king into check by the promoted piece immediately after promotion
# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG# TODO FOUND BUG


# -----------------------------something----------------------------------
# ----------------------------use dividers--------------------------------

# wonder if can be simplified: ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0)

# current bugs:
    # second_tile bug after castling black queen then trying to castle white king. some moves and captures prior to this

#warning TODO broke en passant far right of board

# todo functionality: copy in right click context menu (for move list)
# todo functionality: have the mute button send a command to the sound thread queue
# todo visual: consider making the text box larger (expanding upwards symmetrically)
'''
def main():
    pass
if __name__ == "__main__":
    main()
'''
# todo RULE at some point https://en.wikipedia.org/wiki/Threefold_repetition

#todo warning change castle_flag to castle_something (IT IS NOT A FLAG ANYMORE)
#todo consider making piece info a class/method or something
#todo visual new clock glitch (first moves)
# todo fuck clock vs timer
# mute doesn't mute checkmate/stalemate/draw

#todo Performance cPickle vs pickle

# todo random automated moves then reset, breaks timer


class ChessGUI:

    def __init__(self, master):
        if debugging: self.debugging()
        self.debugging_ui = debugging_ui
        master.title("Chessbox Beta 1.29 [file 1.29] (todo: move text, and ?)")  # ... chess sandbox -> chessbox
        master.iconbitmap(default='icons/icon2.ico')
        master.resizable(width=False, height=False)
        application_color = '#C3B091'
        master.config(background=application_color)
        self.root_width = 780 + 160
        self.root_height = 780 + 50
        root.bind('<Escape>', self.close_windows)

        self.application_color_schemes = {'original':
                                             {'application_color': '#C3B091',
                                              'white_tile': '#C19A6B',
                                              'black_tile': '#663300',
                                              'board_border_color': '#6B4423',
                                              'board_text_color_1': '#302013',
                                              'board_text_color_2': '#302013',
                                              'button_color_1': '#7B3F00',
                                              'button_color_2': '#885219',
                                              'button_backdrop_color': '#a2784c',
                                              'button_backdrop_color_hover': '#81603c'},

                                          'original-lightened':
                                             {'application_color': '#C3B091',
                                              'white_tile': '#cdae88',
                                              'black_tile': '#845b32',
                                              'board_border_color': '#55361c',
                                              'board_text_color_1': '#302013',
                                              'board_text_color_2': '#302013',
                                              'button_color_1': '#7B3F00',
                                              'button_color_2': '#885219',
                                              'button_backdrop_color': '#a2784c',
                                              'button_backdrop_color_hover': '#81603c'},
                                           }

        local_scheme_chooser = 'original-lightened'

        self.application_color = self.application_color_schemes[local_scheme_chooser]['application_color']
        self.application_color_highlight = self.color_tone(self.application_color, .30, 'darker')
        self.white_tile = self.application_color_schemes[local_scheme_chooser]['white_tile']
        self.black_tile = self.application_color_schemes[local_scheme_chooser]['black_tile']
        self.board_border_color = self.application_color_schemes[local_scheme_chooser]['board_border_color']
        self.board_text_color_1 = self.application_color_schemes[local_scheme_chooser]['board_text_color_1']
        self.board_text_color_2 = self.application_color_schemes[local_scheme_chooser]['board_text_color_2']
        self.board_text_color_1_highlight = 'white'  # todo
        self.button_color_1 = self.application_color_schemes[local_scheme_chooser]['button_color_1']
        self.button_color_2 = self.application_color_schemes[local_scheme_chooser]['button_color_2']  # HOVER
        self.button_backdrop_color = self.application_color_schemes[local_scheme_chooser]['button_backdrop_color']
        self.button_backdrop_color_hover = self.application_color_schemes[local_scheme_chooser]['button_backdrop_color_hover']
        self.notification_backdrop_color = self.application_color  # '#C3B091' todo
        self.notification_window_button_colors = '#a2784c'
        self.move_bar_backdrop_color = self.color_tone(self.application_color, 0, 'darker')  #'#a2784c' #application_color #'#6B4423'  #
        self.move_bar_backdrop_color_highlight = self.color_tone(self.move_bar_backdrop_color, .10, 'darker')
        self.board_font = None
        self.clock_font_and_size = ('Digital-7 Mono', 28)
        self.title_text_enabled = False
        self.resize_factor = 3  # captured pieces size
        self.piece_size = 60  # NEW (ver. 0.082 <piece creation refactor>)

        self.master = master
        self.player_colors = ['white', 'black']
        self.current_player = 0

        # [tile object, white piece, black piece, piece name] todo review this design decision
        self.board_matrix = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],
                             [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]

        self.piece_object_lookup = {'white_pawn': 0,      'black_pawn': 0,
                                    'white_rook': 0,      'black_rook': 0,
                                    'white_bishop': 0,    'black_bishop': 0,
                                    'white_knight': 0,    'black_knight': 0,
                                    'white_queen': 0,     'black_queen': 0,
                                    'white_king': 0,      'black_king': 0}

        self.crop_list = {'white_pawn': [562, 100, 601, 152],   'black_pawn': [561, 4, 601, 58],
                          'white_rook': [226, 100, 271, 152],   'black_rook': [226, 4, 271, 59],
                          'white_bishop': [331, 91, 388, 154],  'black_bishop': [330, 0, 387, 60],
                          'white_knight': [443, 98, 496, 152],  'black_knight': [443, 4, 496, 58],
                          'white_queen': [106, 95, 169, 152],   'black_queen': [105, 0, 168, 58],
                          'white_king': [0, 94, 54, 152],       'black_king': [-1, -1, 53, 58]}

        self.valid_horses = [[1, 2], [2, 1], [-1, 2], [-2, 1], [1, -2], [2, -1], [-1, -2], [-2, -1]]

        self.castle_tiles_dictionary = {
            'white': {
                'O-O-O': {
                    'king': {
                        'first_tile': (4, 7), 'second_tile': (2, 7)},
                    'rook': {
                        'first_tile': (0, 7), 'second_tile': (3, 7)}},
                'O-O': {
                    'king': {
                        'first_tile': (4, 7), 'second_tile': (6, 7)},
                    'rook': {
                        'first_tile': (7, 7), 'second_tile': (5, 7)}}},
            'black': {
                'O-O-O': {
                    'king': {
                        'first_tile': (4, 0), 'second_tile': (2, 0)},
                    'rook': {
                        'first_tile': (0, 0), 'second_tile': (3, 0)}},
                'O-O': {
                    'king': {
                        'first_tile': (4, 0), 'second_tile': (6, 0)},
                    'rook': {
                        'first_tile': (7, 0), 'second_tile': (5, 0)}}}}

        # -----------------------------------------------------------------------------------------

        #todo review all of these and remove ones not used
        # http://stackoverflow.com/a/5899350/6666148  setattr(x, 'foobar', 123) is equivalent to x.foobar = 123.
        # name, p_object, value
        # "board_matrix_clean_copy":              deepcopy(self.board_matrix),
        # "board_matrix_copy":                    deepcopy(self.board_matrix_clean_copy),
        self.board_matrix_clean_copy = deepcopy(self.board_matrix)  # todo review
        self.board_matrix_copy = deepcopy(self.board_matrix_clean_copy)  # todo review
        self.initialize_variable_dictionary = {
            "piece_info":                           None,
            "first_tile":                           None,
            "captured_pieces_info":                 [],
            "number_of_captured_pieces":            {'white': 0, 'black': 0},       # used?


            "undo_flag":                            False,  # todo refactor out
            "undo_end_flag":                        False,  # todo refactor out? may be useful for controls
            "master_move_list":                     [],
            "redo_move_list":                       [],
            "player_in_check":                      (False, (None, None), None),
            "pre_move_test":                        None,
            "move_gave_check":                      False,
            "second_tile_contents":                 None,
            "piece_information_retainer":           None,
            "captured_piece_display_objects":       [],
            "control_panel_objects":                {},
            "random_move_flag":                     False,  #
            "checkmate":                            False,
            "control_panel_image_objects":          {},
            "control_panel_settings":               {
                                                        'mute': False,
                                                        'suppress_debugging': False
                                                    },
            "promoted_piece_tracker":               [],
            "mate_testing":                         False,
            "announce_flag":                        False,
            "text_to_display_object":               ["", None],
            "white_first_move":                     None,
            "black_first_move":                     None,
            "white_time":                           datetime.timedelta(microseconds=0),
            "black_time":                           datetime.timedelta(microseconds=0),
            "valid_tile_tuple":                     [],
            "clock_digits_removed":                 (0, -7),  # 0:hours; 2:minutes  ,  -5:100ms; -7:seconds
            "found_valid_move_flag":                None,  # todo review for way to avoid using this flag
            "stop":                                 False,
            "promotion_box_controls_information_store":     None

        }
        # for (name, value) in self.initialize_variable_dictionary.iteritems():
        #    setattr(self, name, value)

        # don't know how to use the dictionary and continue to get item completion
        self.piece_info = None  # todo why not [none, none] or (none, none) ?
        # todo figure out how to make this usable elsewhere
        """
                0 first_tile,                     # first tile\n
                1 second_tile,                    # second tile\n
                2 piece_object,                   # piece object\n
                3 piece_name,                     # piece name\n
                4 enemy_piece_object,             # enemy captured objectn\n
                5 enemy_tile,                     # enemy tile (defaults to second_tile)\n
                6 castle_info,                    # O-O and O-O-O: using letter O notation (algebraic uses zero "0")\n
                                                  # castle_info also contains the rook object #todo (nested?)\n
                7 time_taken,                     # time taken for move\n
                8 time_of_move                    # time the move occurred (UTC?)\n
        """
        self.first_tile = None
        self.captured_pieces_info = []
        self.number_of_captured_pieces = {'white': 0, 'black': 0}  # todo hacked using dictionary (inefficient) todo white, black (will break i think if i fix player bug)
        self.board_matrix_clean_copy = deepcopy(self.board_matrix)  # todo review
        self.board_matrix_copy = deepcopy(self.board_matrix_clean_copy)  # todo review
        self.undo_flag = False
        self.undo_end_flag = False
        self.master_move_list = []
        self.redo_move_list = []
        self.player_in_check = (False, (None, None), None)  # todo the false is not necessary; can be implicit?
        self.pre_move_test = None
        self.move_gave_check = False
        self.second_tile_contents = None
        self.piece_information_retainer = None
        self.captured_piece_display_objects = []
        self.control_panel_objects = {}
        self.random_move_flag = False
        self.checkmate = False
        self.control_panel_image_objects = {}
        self.control_panel_settings = {
            'mute': False,
            'inspection_mute': False,
            'suppress_debugging': False
        }
        self.promoted_piece_tracker = []  # todo rename?
        self.mate_testing = False
        self.announce_flag = False
        self.text_to_display_object = ["", None]  # text_box_update()
        self.white_first_move = None  # todo review: may be obsolete
        self.black_first_move = None  # todo review: may be obsolete
        self.white_time = datetime.timedelta(microseconds=0)  # todo is replaced by cumulative times below
        self.black_time = datetime.timedelta(microseconds=0)  # todo is replaced by cumulative times below
        self.valid_tile_tuple = []  # self.get_valid_moves()
        self.clock_digits_removed = (0, -7)  # 0:hours; 2:minutes  ,  -5:100ms; -7:seconds
        self.found_valid_move_flag = None  # todo only stalemate_inspection() depends on this. the function itself. if that is not used, this can be removed
        # todo separate out persistent vs reset-able
        self.stop = False
        self.promotion_box_controls_information_store = None
        # todo needs to be added to reset
        # todo needs to be added to reset
        # todo needs to be added to reset
        self.game_is_over = False
        self.open_window_list = []  # cumulative
        self.cumulative_time_white = datetime.timedelta(microseconds=0)   # this is for performance
        self.cumulative_time_black = datetime.timedelta(microseconds=0)   # this is for performance
        self.time_of_last_move = None
        self.timer_enabled = False

        # todo needs to be added to reset

        # -----------------------------------------------------------------------------------------

        # constants
        self.master_move_list_length = 7  # TODO REVIEW and find a way to not use this

        # goes with below TODO move this and other static values to top?
        self.board_tile_size = 75

        application_color = self.application_color

        # todo create the objects here and configure elsewhere?
        # debugging colors todo refacor this
        if self.debugging_ui:
            self.layout_colors = {'application_color':      application_color,
                                  'top_space':              'green',
                                  'bottom_space':           'orange',
                                  'control_panel':          'maroon',
                                  'board_container':        'blue',
                                  'text_box_container':     'grey',
                                  'text_box_spacer':        'aqua',
                                  'text_box_clock':         'black'}  # todo wtf does not work
        else:
            self.layout_colors = {'application_color':      application_color,
                                  'top_space':              application_color,
                                  'bottom_space':           application_color,
                                  'control_panel':          application_color,
                                  'board_container':        application_color,
                                  'text_box_container':     application_color,
                                  'text_box_spacer':        application_color,
                                  'text_box_clock':         'grey'}

        layout_colors = self.layout_colors

        root_width = self.root_width
        root_height = self.root_height
        dimensions = str(root_width) + "x" + str(root_height)
        root.geometry(dimensions)

        self.container_for_board_and_control_panel = Canvas(self.master, width=0, height=0)
        self.container_for_board_and_control_panel.config(bg=layout_colors['application_color'], borderwidth=0, highlightthickness=0)
        self.container_for_board_and_control_panel.pack(side='left')

        self.container_for_board_cp_text = Canvas(self.master, width=0, height=0)
        self.container_for_board_cp_text.config(bg=layout_colors['application_color'], borderwidth=0, highlightthickness=0)
        self.container_for_board_cp_text.pack(side='left')

        # board container and visual elements
        bc_w = bc_h = self.bc_w = self.bc_h = 700  # Board Container Width/Height
        bb_w = bb_h = self.bb_w = self.bb_h = 700  # Board Border Width/Height
        v_spacer = self.v_spacer = bc_w + 60
        # Chess board container
        self.board_container = Canvas(self.container_for_board_and_control_panel, width=0, height=0)
        self.board_container.config(bg=layout_colors['board_container'], borderwidth=0, highlightthickness=0)
        self.board_container.pack()
        # top visual space
        self.board_top_space = Canvas(self.board_container, width=v_spacer, height=40)
        self.board_top_space.config(bg=layout_colors['top_space'], borderwidth=0, highlightthickness=0)
        self.board_top_space.pack(side='top')
        # Board Border
        self.board_border = Canvas(self.board_container, width=bb_w, height=bb_h)  # todo remove dimensions, add actual board
        self.board_border.config(bg=self.board_border_color, borderwidth=0, highlightthickness=0)
        self.board_border.pack()
        # bottom visual space
        self.board_bottom_space = Canvas(self.board_container, width=v_spacer, height=20)
        self.board_bottom_space.config(bg=layout_colors['bottom_space'], borderwidth=0, highlightthickness=0)
        self.board_bottom_space.pack(side='bottom')

        # chess board
        self.cb_w = self.cb_h = 600  # Chess Board Width/Height
        cb_w = self.cb_w
        cb_h = self.cb_h
        self.chess_board_position_x = bc_w/2-cb_w/2  # todo forgot this was here
        self.chess_board_position_y = bc_h/2-cb_h/2
        self.chess_board = Canvas(self.board_border, width=cb_w, height=cb_h)
        self.chess_board.config(bg=application_color, borderwidth=0, highlightthickness=0)
        self.chess_board.place(x=bc_w/2-cb_w/2, y=bc_h/2-cb_h/2)

        # control panel container
        self.controls_panel_container = Canvas(self.container_for_board_and_control_panel, width=v_spacer, height=100)  # todo height
        self.controls_panel_container.config(bg=layout_colors['control_panel'], borderwidth=0, highlightthickness=0)
        self.controls_panel_container.pack()

        # todo move these
        self.text_box_spacer_width = 150
        self.text_box_spacer_height = 50 # todo wtf

        # move list title  # todo move?
        self.move_list_title = Label(self.master, text="Move List")
        self.move_list_title.config(bg=application_color, font=(self.board_font, 24))
        x = self.v_spacer + self.text_box_spacer_width/2
        y = self.text_box_spacer_height
        #self.move_list_title.place(x=x, y=y, anchor='center')

        # focus grabber
        self.focus_grabber = Canvas(root, width=1, height=1)
        self.focus_grabber.config(bg=application_color, borderwidth=0, highlightthickness=0)
        self.focus_grabber.place(x=0, y=0)

        # piece list (white side)
        self.piece_list_names = ['pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'pawn', 'rook', 'knight', 'bishop', 'queen', 'king', 'bishop', 'knight', 'rook']

        # xy zero indexed
        self.piece_list_black = [[0, 1, None], [1, 1, None], [2, 1, None], [3, 1, None], [4, 1, None], [5, 1, None], [6, 1, None], [7, 1, None], [0, 0, None], [1, 0, None], [2, 0, None], [3, 0, None], [4, 0, None], [5, 0, None], [6, 0, None], [7, 0, None]]
        self.piece_list_white = [[0, 6, None], [1, 6, None], [2, 6, None], [3, 6, None], [4, 6, None], [5, 6, None], [6, 6, None], [7, 6, None], [0, 7, None], [1, 7, None], [2, 7, None], [3, 7, None], [4, 7, None], [5, 7, None], [6, 7, None], [7, 7, None]]

        self.create_board()
        self.create_piece_images()
        self.create_pieces()
        self.piece_placement_and_binding()

        self.create_ui_images()
        self.initialize_controls_panel()
        #self.create_notification_window()
        self.initialize_promotion_box()

        self.initialize_text_box()
        self.text_box_update()

        self.initialize_clock()

        if debugging or features:
            message1 = "- undo/redo testing... ?\n" \
                       "- text box promotion/etc.\n" \
                       "- sounds for redo (check, etc.)"
            self.custom_message_box(message1, (800, 725))

    def custom_message_box(self, message, position=False):
        button_width = self.buttons_width = 90  # todo move

        self.win_control_panel_dimensions = (button_width*3, 80)  # todo rename win to game over/
        wcpd = self.win_control_panel_dimensions
        # self.board_container
        self.custom_message = Canvas(root, width=wcpd[0], height=wcpd[1])
        self.custom_message.config(bg=self.notification_backdrop_color, borderwidth=0, highlightthickness=1, highlightbackground='black')
        self.custom_message.create_text(wcpd[0]/2,wcpd[1]/2, text=message)

        if not position:
            x = self.v_spacer/2
            y = self.v_spacer/2
            self.custom_message.place(x=x, y=y, anchor='center')
        else:
            self.custom_message.place(x=position[0], y=position[1], anchor='center')

        self.close_window_button(self.custom_message)
        self.open_window_list.append(self.custom_message)

    def initialize_controls_panel(self):
        # todo refactor out some of this
        # todo many hard coded values
        bc_w = self.bc_w
        bc_h = self.bc_h
        cb_w = self.cb_w
        cb_h = self.cb_h
        if self.debugging_ui: color = 'aqua'
        else: color = self.application_color
        for i in range(20):  # highlightthickness todo
            top_spacer = Canvas(self.controls_panel_container, width=self.v_spacer / 20, height=5, bg=color, highlightthickness=0, highlightbackground='white')
            top_spacer.grid(row=0, column=i)
            bottom_spacer = Canvas(self.controls_panel_container, width=self.v_spacer / 20, height=10, bg=color, highlightthickness=0)
            bottom_spacer.grid(row=2, column=i)

        # todo redesign
        backdrop_color = '#a2784c'

        if debugging:
            #call_me_baby = Canvas(self.controls_panel_container, width=50, height=50)
            call_me_baby = Canvas(self.container_for_board_and_control_panel, width=50, height=50)
            call_me_baby.config(bg=backdrop_color, borderwidth=0, highlightthickness=0)
            call_me_baby.create_text(25, 25, text="?")
            #call_me_baby.grid(row=1, column=1, columnspan=2)
            call_me_baby.bind('<Button-1>', self.test_command)
            call_me_baby.place(x=25, y=700)

        timer = Canvas(self.controls_panel_container, width=50, height=50)
        timer.config(bg=self.application_color, borderwidth=0, highlightthickness=0)
        timer.create_image(25, 25, image=self.control_panel_image_objects['clock'])
        timer.grid(row=1, column=3, columnspan=2)
        #timer.bind('<Button-1>', self.toggle_clock)
        timer.bind('<Button-1>', lambda event: self.keyword_toggler(timer=True))
        timer.bind('<Enter>', self.enter_exit_button)
        timer.bind('<Leave>', self.enter_exit_button)

        button_reset = Canvas(self.controls_panel_container, width=50, height=50)
        button_reset.config(bg=self.application_color, borderwidth=0, highlightthickness=0)
        button_reset.create_image(25, 25, image=self.control_panel_image_objects['reset_image'])
        button_reset.grid(row=1, column=5, columnspan=2)
        button_reset.bind('<Button-1>', self.reset_board)
        button_reset.bind('<Enter>', self.enter_exit_button)
        button_reset.bind('<Leave>', self.enter_exit_button)

        self.controls_move_bar()  # todo move?

        announce_mute = Canvas(self.controls_panel_container, width=50, height=50)
        announce_mute.config(bg=self.application_color, borderwidth=0, highlightthickness=0)
        announce_mute.create_image(25, 25, image=self.control_panel_image_objects['announce'])
        announce_mute.grid(row=1, column=13, columnspan=2)
        announce_mute.bind('<Button-1>', lambda event: self.keyword_toggler(announce=True))
        announce_mute.bind('<Enter>', self.enter_exit_button)
        announce_mute.bind('<Leave>', self.enter_exit_button)

        button_mute = Canvas(self.controls_panel_container, width=50, height=50)
        button_mute.config(bg=self.application_color, borderwidth=0, highlightthickness=0)
        button_mute.create_image(25, 25, image=self.control_panel_image_objects['mute_image'])
        button_mute.grid(row=1, column=15, columnspan=2)
        button_mute.bind('<Button-1>', lambda event: self.keyword_toggler(mute=True))
        button_mute.bind('<Enter>', self.enter_exit_button)
        button_mute.bind('<Leave>', self.enter_exit_button)



        #button.bind('<Button-1>', self.player_1_AI())

    def initialize_clock(self):
        # http://stackoverflow.com/a/30631309/6666148
        # loadfont("/fonts/DS-DIGI.tff")
        if loadfont("fonts/digital7mono.ttf"):
            print "Font loaded..."
        else:
            print "Font failed to load!"

        # clock widgets
        border_size = 0
        v_spacer = self.v_spacer
        clock_box_width = 375
        clock_container_height = 50
        self.clock_container = Canvas(self.container_for_board_and_control_panel, width=clock_box_width,
                                      height=clock_container_height)
        self.clock_container.config(bg=self.layout_colors['text_box_clock'], borderwidth=0, highlightthickness=0)
        self.clock_container.place(x=v_spacer / 2, y=v_spacer / 17, anchor='center')

        self.white_clock = Canvas(self.clock_container, width=(clock_box_width / 2) - border_size * 2,
                                  height=50 - border_size * 2)
        self.white_clock.config(bg='grey66', borderwidth=0, highlightthickness=0)
        self.white_clock_text = self.white_clock.create_text(clock_box_width / 4, 25, font=(
        self.clock_font_and_size[0], self.clock_font_and_size[1]), text="0:00:00")  # self.clock_time)  # .get())
        self.white_clock.place(x=clock_box_width / 4, y=clock_container_height / 2, anchor='center')

        self.black_clock = Canvas(self.clock_container, width=(clock_box_width / 2) - border_size * 2,
                                  height=50 - border_size * 2)
        self.black_clock.config(bg='black', borderwidth=0, highlightthickness=0)
        self.black_clock_text = self.black_clock.create_text(clock_box_width / 4, 25, font=(
        self.clock_font_and_size[0], self.clock_font_and_size[1]), text="0:00:00",
                                                             fill='grey66')  # self.clock_time)  # .get())
        self.black_clock.place(x=clock_box_width * 3 / 4, y=clock_container_height / 2, anchor='center')

        self.clock_update()

    def initialize_text_box(self):
        # text box containers          # todo a lot of hard-coding
        application_height = self.root_height
        text_box_spacer_width = self.text_box_spacer_width # = 150
        text_box_spacer_height = self.text_box_spacer_height  # = 90
        self.text_box_container = Canvas(self.container_for_board_cp_text, width=text_box_spacer_width, height=application_height)  # todo height
        self.text_box_container.config(bg=self.layout_colors['text_box_container'], borderwidth=0, highlightthickness=0)
        self.text_box_container.pack(side='left', fill='both')
        # todo spacer does nothing?
        self.text_box_spacer = Canvas(self.text_box_container, width=text_box_spacer_width, height=text_box_spacer_height)
        self.text_box_spacer.config(bg=self.layout_colors['text_box_spacer'], borderwidth=0, highlightthickness=0)
        #self.text_box_spacer.pack(fill='both')  # todo rename/change color of "text_box_container"

        width_max = 18  # todo width
        list_size = len(self.master_move_list)
        self.text_to_display_object[1] = Text(self.text_box_container, height=list_size + 1, width=width_max, borderwidth=0)
        #text_widget = Text(self.text_widget_position, height=list_size, width=width_max, borderwidth=0)
        #self.text_to_display_object[1].insert("1.0", "001.")  # todo useful "end"

        text_box_text_bg = self.color_tone(self.application_color, .10, 'darker')
        self.text_to_display_object[1].config(bg=text_box_text_bg, foreground='black')
        # selectbackground='white'  todo this covers text ?
        self.text_to_display_object[1].configure(state="disabled")
        #self.text_to_display_object[1].grid(column=1, row=1)
        #self.text_to_display_object[1].pack(side='left')
        #self.text_to_display_object[1].pack(side='top')
        self.text_to_display_object[1].place(x=0, y=40)  # todo find a way to not use place; hard coded
        self.text_to_display_object[1].bind('<Enter>', self.enter_exit_button)
        self.text_to_display_object[1].bind('<Leave>', self.enter_exit_button)

        # text box border
        '''
        top = Canvas(self.master, width=text_box_spacer_width, height=3)
        top.config(bg='black', borderwidth=0, highlightthickness=0)
        x = self.v_spacer
        y = text_box_spacer_height + 35
        top.place(x=x, y=y)
        bottom = Canvas(self.master, width=text_box_spacer_width, height=3)
        bottom.config(bg='black', borderwidth=0, highlightthickness=0)
        x = self.v_spacer
        y = self.v_spacer
        bottom.place(x=x, y=y)
        '''


        #self.text_box_border = self.text_box_container.create_polygon(0,100, 0,700,
        #                                                              200,700, 200,100,
        #
        #                                                             0,100,
        #
        #                                                             1,100, 1,101,
        #                                                             199,101, 199,699,
        #                                                             1,699
        #                                                             )

    def toggle_clock(self, event):  # todo clock vs timer
        new_game = False
        if len(self.master_move_list) == 0:
            new_game = True
        if not self.timer_enabled:
            if new_game:
                self.timer_enabled = True
                self.white_clock.itemconfig(self.white_clock_text, text="0:00:00")
                self.black_clock.itemconfig(self.black_clock_text, text="0:00:00")
                self.sound_handler('timer enabled')
                print "Clock enabled..."
                self.redo_move_list = []  # reset redo moves
            else:
                self.sound_handler('timer: in progress')
                return
        else:
            if not new_game:
                self.cumulative_time_white = datetime.timedelta(microseconds=0)  # this is for performance
                self.cumulative_time_black = datetime.timedelta(microseconds=0)  # this is for performance
                self.time_of_last_move = None
                self.white_first_move = None
                self.black_first_move = None
            self.timer_enabled = False
            # notify user
            self.sound_handler('timer disabled')
            print "Clock not enabled..."

    # move; looks good!
    def clock_update(self, white_moves=False, black_moves=False):
        # undo/redo is not implemented because:
        # (1) there are no rules in chess where undo/redo are allowed (AFAIK)
        # (2) (more importantly) no way to implement without many arbitrary decisions

        c_l_d_r = self.clock_digits_removed

        if self.game_is_over:
            return

        current_time = datetime.datetime.utcnow()
        c_1 = not bool(self.time_of_last_move) and white_moves
        c_2 = not bool(self.time_of_last_move) and black_moves
        if c_1 or c_2:
            self.time_of_last_move = current_time

        if white_moves:  # and not black_moves:
            self.cumulative_time_white += current_time - self.time_of_last_move
        elif black_moves:  # and not white_moves:
            self.cumulative_time_black += current_time - self.time_of_last_move

        c_1 = bool(self.white_first_move)
        c_2 = not white_moves and not black_moves
        c_3 = self.timer_enabled
        if c_1 and c_2 and c_3:
            if self.player_colors[self.current_player] == 'white':
                display_time_white = current_time - self.time_of_last_move + self.cumulative_time_white
                text = str(display_time_white)[c_l_d_r[0]:c_l_d_r[1]]
                self.white_clock.itemconfig(self.white_clock_text, text=text)
            else:  # self.player_colors[self.current_player] == 'black'
                display_time_black = current_time - self.time_of_last_move + self.cumulative_time_black
                text = str(display_time_black)[c_l_d_r[0]:c_l_d_r[1]]
                self.black_clock.itemconfig(self.black_clock_text, text=text)

        if white_moves or black_moves:
            self.time_of_last_move = current_time

        if not white_moves and not black_moves:
            root.after(100, self.clock_update)

    # current implementation already near 100% compatible with undo
    def text_box_update(self):
        # todo color bg based on white/black player (may not be possible)
        # todo use symbolic
        # todo convert xy to letter/number
        # todo complete all cases in notation (eg castle)
        # todo buggy
        # todo performance profile #update: moved to only run during valid player moves dramatically reducing overhead

        # trim to correct length (or recalculate every move)
        # .delete
        # event.widget.delete("%s-1c" % END, ?)   the 1c is the number of characters
        #
        # .delete(index1, index2=None)
        # Deletes text starting just after index1. If the second argument is omitted, only one character is deleted.
        # If a second index is given, deletion proceeds up to, but not including, the character after index2. Recall
        # that indices sit between characters.

        print "\tNOT FULLY IMPLEMENTED: https://www.chessclub.com/user/help/notation pawn promotion, check, checkmate..."

        # create the text to be displayed
        #self.text_to_display_object[0] = ""
        list_size = len(self.master_move_list)
        text_to_display = ""
        i = 0
        # '''
        for each_move in self.master_move_list:
            #i = len(self.master_move_list) - 1
            #move = self.master_move_list[-1]

            move = each_move
            piece_name = move[3]  # piece_name = u'\u2656' not working
            if piece_name == 'knight':
                piece_name = 'N'
            piece_name_formatted = piece_name[:1].upper()
            first_tile_chess_notation = self.xy_to_notation(move[0]).lower()
            second_tile_chess_notation = self.xy_to_notation(move[1]).lower()
            move_or_capture = "-"
            if move[4] != 0:
                move_or_capture = "x"
            move_text = ""
            move_number = ""
            if (i + 2) % 2 == 0:
                number = int(math.ceil((float(i) + 1)/2.0))
                move_number = "%s." % "{:0>3d}".format(number)
            move_text += move_number
            if each_move[6] is None:
                move_text += " %s%s%s%s" % (piece_name_formatted, first_tile_chess_notation, move_or_capture, second_tile_chess_notation)
            else:  # each_move[6] is not None
                castle_text = str(each_move[6][0])
                spaces = 6 - len(castle_text)
                for space in range(spaces): # correct length
                    castle_text += " "
                move_text += " %s" % castle_text
            #if (i + 1) % 2 == 0:
            #    move_text += '\n'
            if (i + 1) % 2 == 0:
                move_text += ''  # u'\u200B'  # zero width space  #todo wtf is this for? it was ' ', but I changed it
            text_to_display += move_text
            i += 1
            #self.text_to_display_object[0] += text_to_display
            #break
        # '''

        ''' # todo include castle
        #for each_move in self.master_move_list:
        move_list_length = len(self.master_move_list)
        if move_list_length > 0:
            i = move_list_length - 1
            move = self.master_move_list[-1]

            #move = each_move
            piece_name = move[3]  # piece_name = u'\u2656' not working
            if piece_name == 'knight':
                piece_name = 'N'
            piece_name_formatted = piece_name[:1].upper()
            first_tile_chess_notation = self.xy_to_notation(move[0]).lower()
            second_tile_chess_notation = self.xy_to_notation(move[1]).lower()
            move_or_capture = "-"
            if move[4] != 0:
                move_or_capture = "x"
            move_text = self.text_to_display_object[0]
            move_number = ""
            if (i + 2) % 2 == 0:
                number = int(math.ceil((float(i) + 1)/2.0))
                move_number = "%s." % "{:0>3d}".format(number)
            move_text += move_number
            move_text += " %s%s%s%s" % (piece_name_formatted, first_tile_chess_notation, move_or_capture, second_tile_chess_notation)
            #if (i + 1) % 2 == 0:
            #    move_text += '\n'
            if (i + 1) % 2 == 0:
                move_text += ' '  # u'\u200B'  # zero width space
            self.text_to_display_object[0] = move_text
            #i += 1
            #self.text_to_display_object[0] += text_to_display
            #break
            text_to_display = self.text_to_display_object[0]
        '''

        # display the text
        #text_h_w_string = "%d.0" % (((i + 1) / 2) + 1)
        #if int(text_h_w_string[:-2]) > 38:
        #    text_h_w_string = "38.0"
        text_h_w_string = "44.0"  # 38

        self.text_to_display_object[1].configure(state="normal")
        self.text_to_display_object[1].config(height=text_h_w_string)
        self.text_to_display_object[1].delete("1.0", "end")
        self.text_to_display_object[1].insert(text_h_w_string, text_to_display)
        self.text_to_display_object[1].configure(state="disabled")

        self.text_to_display_object[1].see("end")
        # yscrollcommand
        # takefocus=0

    @staticmethod  # text_box_update helper (and others)
    def xy_to_notation(tile):
        tile_letter = chr(ord('A') + tile[0])
        tile_number = str(8 - tile[1])
        tile_chess_notation = tile_letter + tile_number
        return tile_chess_notation

    def controls_move_bar(self):
        move_bar_backdrop_color = self.move_bar_backdrop_color  # '#a2784c'  # todo
        m_b_b_c = move_bar_backdrop_color
        move_bar_backdrop = Canvas(self.controls_panel_container, width=400, height=60)
        move_bar_backdrop.config(bg=move_bar_backdrop_color, borderwidth=0, highlightthickness=0)
        move_bar_backdrop.grid(row=1, column=5, columnspan=10)

        move_bar_button_names = ['move_bar_backward_end',
                                 'move_bar_backward',
                                 'move_bar_forward',
                                 'move_bar_forward_end']
        move_bar_button_objects = {'move_bar_backward_end': 0,
                                   'move_bar_backward': 0,
                                   'move_bar_forward': 0,
                                   'move_bar_forward_end': 0}

        for i in range(4):
            move_bar_button_objects[move_bar_button_names[i]] = Canvas(move_bar_backdrop, width=50, height=50)
            move_bar_button_objects[move_bar_button_names[i]].config(bg=m_b_b_c, borderwidth=0, highlightthickness=0)
            image = self.control_panel_image_objects[move_bar_button_names[i][9:]]
            move_bar_button_objects[move_bar_button_names[i]].create_image(25, 25, image=image)
            move_bar_button_objects[move_bar_button_names[i]].pack(side='left')
            move_bar_button_objects[move_bar_button_names[i]].bind('<Enter>', self.enter_exit_button)
            move_bar_button_objects[move_bar_button_names[i]].bind('<Leave>', self.enter_exit_button)

        move_bar_button_objects['move_bar_backward_end'].bind('<Button-1>', self.undo_end)
        move_bar_button_objects['move_bar_backward'].bind('<Button-1>', self.undo)
        move_bar_button_objects['move_bar_forward'].bind('<Button-1>', self.redo)
        move_bar_button_objects['move_bar_forward_end'].bind('<Button-1>', self.redo_end)

    # move & refactor
    # todo generalize this (allow inserting text, using 0 or all buttons, etc...)
    def create_notification_window(self):
        # todo generalize this, make title bar (movable may be time consuming)
        button_width = self.buttons_width = 90  # todo move
        button_height = self.buttons_height = 45  # todo move
        n_w_b_c = self.notification_window_button_colors

        self.win_control_panel_dimensions = (button_width*3, 80)  # todo rename win to game over/
        wcpd = self.win_control_panel_dimensions
        # self.board_container
        self.quit_reset_container = Canvas(root, width=wcpd[0], height=wcpd[1])
        self.quit_reset_container.config(bg=self.notification_backdrop_color, borderwidth=0, highlightthickness=1, highlightbackground='black')

        wcpd = self.win_control_panel_dimensions
        x = self.v_spacer/2  # -wcpd[0]/2
        y = self.v_spacer-wcpd[1]*3/4
        #y += +145  # todo
        #x = self.v_spacer + 50
        #y = 50
        self.quit_reset_container.place(x=x, y=y, anchor='center')

        # button
        end_button_reset = Canvas(self.quit_reset_container, width=button_width, height=button_height)
        end_button_reset.config(bg=n_w_b_c, borderwidth=0, highlightthickness=0)
        end_button_reset.create_text(self.buttons_width/2, self.buttons_height/2, font=(self.board_font, 12), text='RESET', fill=self.board_text_color_1)
        end_button_reset.place(x=wcpd[0]/2-self.buttons_width+self.buttons_width/3.5, y=wcpd[1]/2+5, anchor='center')
        end_button_reset.bind('<Button-1>', self.reset_board)
        end_button_reset.bind('<Enter>', self.enter_exit_button)
        end_button_reset.bind('<Leave>', self.enter_exit_button)

        # button
        end_button_quit = Canvas(self.quit_reset_container, width=button_width, height=button_height)
        end_button_quit.config(bg=n_w_b_c, borderwidth=0, highlightthickness=0)
        end_button_quit.create_text(self.buttons_width/2, self.buttons_height/2, font=(self.board_font, 12), text='EXIT', fill=self.board_text_color_1)
        end_button_quit.place(x=wcpd[0]/2+self.buttons_width-self.buttons_width/3.5, y=wcpd[1]/2+5, anchor='center')
        end_button_quit.bind('<Button-1>', self.exit_application)
        end_button_quit.bind('<Enter>', self.enter_exit_button)
        end_button_quit.bind('<Leave>', self.enter_exit_button)

        self.close_window_button(self.quit_reset_container)
        self.open_window_list.append(self.quit_reset_container)  # used by close_windows()

    def close_window_button(self, window_object):
        # there is some sort of visual issue drawing these small lines
        # hacky workaround using a box and drawing to extents of the box, with 1,1 offset in the top left (no idea)
        # it seems like the first point is drawn at, but the second (i.e. last) point is drawn up to
        width_0 = 30
        height_0 = 20
        bg = window_object.cget("bg")
        root.update_idletasks()  # todo performance?
        x = window_object.winfo_width() - width_0
        y = 0  #window_object.winfo_height() - 10

        close_window = Canvas(window_object, width=width_0, height=height_0)
        close_window.config(bg=bg, borderwidth=0, highlightthickness=0)

        close_window.create_line(1+10, 1+4, 10+10, 10+4)
        close_window.create_line(0+10+1, 10+4-1, 10+10, 0+4)

        close_window.place(x=x-1, y=y+1)

        close_window.bind('<Button-1>', lambda event: window_object.place_forget())
        close_window.bind('<Enter>', self.enter_exit_button)
        close_window.bind('<Leave>', self.enter_exit_button)


    # clean this up
    def controls_event_handler(self, event, **kwargs):

        if event is not None and event.char == 'k':
            #cProfile.runctx("self.random_move_game()", globals(), locals())
            #cProfile.runctx("self.create_notification_window()", globals(), locals())
            jectO = ChessBoard(board_matrix=self.board_matrix)
            jectO.piece_information((4, 0))
        if 'reset' in kwargs:
            print "currently useless"
            raise NotImplementedError("currently useless")
            #self.debugging_printer("Resetting initialize_controls_panel...")
            print "Resetting initialize_controls_panel..."
            #root.unbind('<space>')
            #root.unbind('<p>')
            #self.random_move_flag = False      # done in reset_board()
            #self.checkmate = False             # done in reset_board()
        elif not self.random_move_flag:
            #root.bind('<space>', self.random_move, "+")
            #root.bind('<p>', self.random_move_game, "+")
            self.random_move_flag = True
            #self.checkmate = False
            self.checkmate = True
        elif self.random_move_flag:
            #root.unbind('<space>')
            #root.unbind('<p>')
            self.random_move_flag = False
            #self.checkmate = True
            self.checkmate = False

    def enter_exit_button(self, event):

        if event.widget == self.text_to_display_object[1]:
            if root.focus_get() != event.widget:
                self.text_to_display_object[1].focus_set()
            if root.focus_get() == event.widget:
                self.text_to_display_object[1].grab_release()  #warning todo why does this work?
            return

        #bc1 = self.button_color_1
        bc1 = self.button_color_1
        abc1 = self.button_backdrop_color  # arrow button color
        abc1h = self.button_backdrop_color_hover
        bc1h = self.button_color_2
        #tc1 = self.board_text_color_1
        #tc1h = self.board_text_color_1_highlight
        app = self.application_color
        apph = self.application_color_highlight

        bg = event.widget.cget('bg')

        if bg == bc1:
            event.widget.config(bg=bc1h)

        if bg == bc1h:
            event.widget.config(bg=bc1)

        if bg == abc1:
            event.widget.config(bg=abc1h)
            #event.widget.itemconfig(self.control_panel_objects['undo_arrow'], fill=tc1h)
        if bg == abc1h:
            event.widget.config(bg=abc1)
            #event.widget.itemconfig(self.control_panel_objects['undo_arrow'], fill=tc1)

        if bg == self.move_bar_backdrop_color:
            event.widget.config(bg=self.move_bar_backdrop_color_highlight)
        if bg == self.move_bar_backdrop_color_highlight:
            event.widget.config(bg=self.move_bar_backdrop_color)

        if bg == app:
            event.widget.config(bg=apph)
        if bg == apph:
            event.widget.config(bg=app)




    def board_event_handler(self, event):
        # todo promotion
        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        #if self.piece_information_retainer is not None:  #warning todo review
        #    return

        # mouse button press
        if event.type == '4':
            #################################################################################
            # find the selected board tile for every event type
            # todo refactor this out (also address how the handler does a similar search)
            #self.selected_tile = None  # todo review this
            self.first_tile = first_tile = None  # todo review this
            for i in range(8):
                for j in range(8):
                    tile = self.board_matrix[i][j][0]
                    piece_current_player = self.board_matrix[i][j][current_player + 1]
                    piece_opposite_player = self.board_matrix[i][j][opposite_player + 1]
                    widget = event.widget
                    if tile == widget or piece_current_player == widget or piece_opposite_player == widget:
                        self.first_tile = (j, i)  # XY
                        first_tile = self.first_tile

                    if debugging:
                        # tiles
                        if self.board_matrix[i][j][0] == event.widget:
                            #self.debugging_printer("Board clicked at (XY): (%d, %d)" % (j, i))
                            print "Board clicked at (XY): (%d, %d)" % (j, i)
                            #self.selected_tile = (j, i)  # XY
                        # current player pieces
                        if self.board_matrix[i][j][current_player + 1] == event.widget:
                            #self.debugging_printer("Piece clicked at (XY): (%d, %d)" % (j, i))
                            print "Piece clicked at (XY):", (j, i)
                            #self.selected_tile = (j, i)  # XY
                        # other player pieces
                        if self.board_matrix[i][j][opposite_player + 1] == event.widget:
                            self.debugging_printer("Enemy clicked at (XY): (%d, %d)" % (j, i))
                            print "Enemy clicked at (XY):", (j, i)
                            #self.selected_tile = (j, i)  # XY

            if self.first_tile is None:
                raise Exception("board tile not found")
            #################################################################################
            print "Event handling...", event.type, "Select piece event."
            self.first_tile_information_store(first_tile, user_input=True)
        # mouse button release
        elif event.type == '5':
            self.second_tile = None
            #self.debugging_printer(("Event handling...", event.type, "Place piece event."))
            print "Event handling...", event.type, "Place piece event."
            object_id_below_cursor = root.winfo_containing(event.x_root, event.y_root)
            for i in range(8):
                for j in range(8):
                    for k in range(4):  # todo should be range(3)
                        if self.board_matrix[i][j][k] == object_id_below_cursor:
                            #self.debugging_printer(("Board clicked at (XY):", (j, i)))
                            print "Board clicked at (XY):", (j, i)
                            #self.selected_tile = (j, i)  # XY
                            self.second_tile = (j, i)  # todo use?
                            second_tile = self.second_tile
            if self.second_tile is not None:
                self.rule_and_state_inspections(second_tile, user_input=True)  # object_id_below_cursor)
            if self.second_tile is None:
                print "Board tile not found!\n"
                self.color_piece_background(reset_board_tile_coloring=True)

    # modifies: self.piece_info AND self.first_tile
    def first_tile_information_store(self, first_tile, user_input=False, inspection=False):  # mouse press

        #warning todo review interaction between self.piece_info, state inspections, this inspection=False...

        current_player = self.current_player

        # if no piece has yet been selected to move, create info about first event
        if self.piece_info is None or inspection:  #WARNING TODO BLOCKS STATE CHECKS
            #self.debugging_printer("Creating piece info...")
            if user_input: print "Creating piece info..."
            # does this tile have a piece on it corresponding to the correct player
            if self.board_matrix[first_tile[1]][first_tile[0]][current_player + 1] != 0:  # checking w/b piece object TODO 0 to None
                piece_object = self.board_matrix[first_tile[1]][first_tile[0]][current_player + 1]  # todo can't use event because the event may be the board not the piece?
                piece_name = self.board_matrix[first_tile[1]][first_tile[0]][3]  # get piece name
                self.piece_info = (piece_object, piece_name, first_tile[0], first_tile[1])
                self.first_tile = first_tile  # todo not necessary (see above)
                if user_input:
                    print "Player's piece selected!...", '\n'  # todo review
                    self.sound_handler(called_sound_key='pickup piece', rename_flag=False)  # SOUND  todo disable in auto
            else:
                print "Select a %s piece to play. \n" % self.player_colors[current_player]  # todo send error to user

        # color tiles
        if user_input:
            valid_move_list, valid_capture_list = self.get_valid_moves(first_tile, combined_list=False)
            self.valid_tile_tuple = valid_move_list + valid_capture_list
            print "self.valid_tile_tuple", self.valid_tile_tuple
            # color tiles
            for each_valid_move in valid_move_list:
                self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#008000', highlightthickness=1)
            for each_valid_move in valid_capture_list:
                self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#800000', highlightthickness=1)

    def rule_and_state_inspections(self, second_tile, user_input=False, inspection=False):  # mouse release
        # todo can user_input and inspection be combined? (maybe rename to something that is more accurately descriptive than user_input)
        # todo refactor this into piece_rules, check_rules, checkmate_test (this encapsulates?)
        # if a piece has been selected to move

        move = False  # todo this is so that the return can follow some cleanup, see if this can be refactored to simplify
        enemy_tile = None
        castle_flag = False  # tile the king castles to
        # todo consider only using the global self.first_tile, then obtaining the piece info through a helper function called from this function
        if self.piece_info is not None:  # todo this isn't necessary, is it? error prevention maybe
            first_tile = self.first_tile  # todo change to piece info when piece_info is refactored
            move = False
            # todo can refactor the check_rules into a single statement

            # for pawn
            if self.piece_info[1] == 'pawn':  # 1
                rule_bool, enemy_tile = self.pawn_rules(first_tile, second_tile, inspection=inspection)  #warning todo
                if rule_bool:
                    if enemy_tile is None:  # en passant  # todo useless compare?
                        if self.check_rules(first_tile, second_tile):  # == "pass":  # todo "pass" vs bool
                            move = True
                    else:  # enemy_tile is not None  # todo useless compare?
                        if self.check_rules(first_tile, second_tile):  # == "pass":  # todo "pass" vs bool
                            move = True

            # for rook
            elif self.piece_info[1] == 'rook':  # 2  # todo castle king side
                if self.rook_rules(first_tile, second_tile):
                    if self.check_rules(first_tile, second_tile):  # == "pass":
                        move = True

            # for bishop
            elif self.piece_info[1] == 'bishop':  # 5
                if self.bishop_rules(first_tile, second_tile):
                    if self.check_rules(first_tile, second_tile):  # == "pass":
                        move = True

            # for knight
            elif self.piece_info[1] == 'knight':  # 3/4?
                if self.knight_rules(first_tile, second_tile):
                    if self.check_rules(first_tile, second_tile):  # == "pass":
                        move = True

            # for queen
            elif self.piece_info[1] == 'queen':  # 6
                if self.queen_rules(first_tile, second_tile):
                    if self.check_rules(first_tile, second_tile):  # == "pass":
                        move = True

            # for king
            elif self.piece_info[1] == 'king':  # 4/3?  # TODO CAN'T MOVE INTO CHECK FUCK
                rule_bool, castle_flag = self.king_rules(first_tile, second_tile)
                if rule_bool:
                    if castle_flag is None:
                        if self.check_rules(first_tile, second_tile):  # == "pass":
                            move = True
                    else:  # castle_flag:
                        # the piece rules inspect for check  todo verify
                        move = True

            if user_input:  # todo should it only be on user input?
                # reset board tile color
                print "self.valid_tile_tuple", self.valid_tile_tuple
                for each_board_tile in self.valid_tile_tuple:
                    self.color_piece_background(board_tile=each_board_tile)
                self.valid_tile_tuple = []

            # if valid move from user (or forced user)
            if move and user_input:
                if enemy_tile is None and not castle_flag:
                    self.move_piece(first_tile, second_tile)
                elif enemy_tile is not None:
                    self.move_piece(first_tile, second_tile, enemy_tile=enemy_tile)
                elif castle_flag:
                    self.move_piece(first_tile, second_tile, castle_flag=castle_flag)  # was a flag, now more
                else:
                    raise StandardError
                self.text_box_update()
                self.color_piece_background(piece=second_tile)
                if self.piece_information_retainer is not None and user_input and not inspection:  # promotion  #warning todo review
                    self.promotion_box_display(second_tile=second_tile)  # todo alternate_players() with promotion box may be causing problems
                    print self.promoted_piece_tracker  #debugging here
                self.alternate_players()  # todo alternate_players() with promotion box may be causing problems
            #if self.piece_information_retainer is not None:
                #print "if self.piece_information_retainer is not None AND not user_input"

            # todo try to call self.alternate_players() only after that player is no longer relevant

            #warning TODO review the change in indent from here to end (right 1 tab)

            # todo combine this with state inspection
            if move and user_input and not inspection:  # todo not inspection necessary?
                if self.fifty_move_rule():
                    # allow player to select draw (this is before their move)
                    # have the auto-bot always draw (which is what is coded here)
                    self.game_over('draw')
                    return
                if self.draw_rules():
                    # performance: these state checks based on pieces (and not position) can be only updated when piece numbers change
                    self.game_over('draw')
                    return

            # test for checkmate todo move?why check even when no move occurred
            # these are checking for the next (current) player that has just been switched to, but has not moved
            # todo completely refactor state_inspection, stalemate_inspection, and how these states are checked
            if move and user_input and not inspection:  # if the state changed  #warning todo inspections/simulations are checking this
                if not inspection:  #warning todo review
                    self.state_inspection()  # todo move?  #warning todo review

                    if self.checkmate:
                        print "Checkmate after state_inspection()"
                        return
                if not inspection:
                    pass

            # reset piece selection  # todo refactor this out and replace with inspection=True or similar explicit
            self.piece_info = None  # TODO review
            self.first_tile = None
            #if not inspection:
            self.second_tile = None  # todo
            self.move_gave_check = False  # todo review

            if move:  # and not inspection:
                # todo undo/redo
                # time management
                if user_input and self.timer_enabled:  # todo review
                    if len(self.master_move_list) == 1:
                        self.white_first_move = datetime.datetime.utcnow()
                    if len(self.master_move_list) == 2:
                        self.black_first_move = datetime.datetime.utcnow()

                    # player's already alternated
                    if self.player_colors[self.current_player] == 'black':  # white moves
                        self.clock_update(white_moves=True, black_moves=False)
                    else:  # self.player_colors(self.current_player) == 'white'  # black moves
                        self.clock_update(white_moves=False, black_moves=True)
                return True
            if not move:
                return False

    def state_inspection(self):
        print "State inspection... (players have alternated)"
        # players have alternated
        # todo possibly combine with stalemate_inspection

        # checkmate test self.move_gave_check = False taken from move_piece
        # todo can use captured pieces list to call captures outside of move_piece()
        # replace with inspection?
        # if not inspection:

        if not self.mate_testing:
            # checkmate inspection
            self.mate_testing = True  # todo review & rename & refactor out?
            print "self.move_gave_check:", self.move_gave_check
            if self.move_gave_check:  # the other player gave this player check (from check_rules())
                print "self.move_gave_check:", self.move_gave_check
                if self.no_valid_moves():
                    self.mate_testing = False
                    self.game_over('checkmate')
                    return False # fail
                else:  # (self.move_gave_check)
                    self.mate_testing = False
                    self.sound_handler('check')  # todo doesn't seem to be working

            # stalemate inspection
            else:  # not self.move_gave_check
                pass
                ####if self.found_valid_move_flag is None:
                    #print "\t\t\t\tpossible stalemate... todo implement"
                    #self.found_valid_move_flag = True
                    ####self.found_valid_move_flag = not self.fast_no_valid_moves()

                stalemate = False
                #if self.captured_pieces_info is not []:

                # no available moves
                #if self.found_valid_move_flag is False:  # can also be None (so if not self... can be buggy)
                    #stalemate = True
                if self.no_valid_moves():  # todo can run once above and use below
                    stalemate = True
                    #self.found_valid_move_flag = None
                self.mate_testing = False
                if stalemate:
                    self.game_over('stalemate')
                    return

            # draw inspection
            draw = self.draw_rules()
            if draw:
                self.game_over('draw')
                return

            self.mate_testing = False
            self.move_gave_check = False  # todo review



    # todo review/remove
    def fast_no_valid_moves(self):
        print "Fast valid move check..."
        verbose = True

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        #board_matrix = self.a_copy_rename(self.board_matrix)  # todo this is not necessary with the recent refactor (and is expensive)

        # find all of the player pieces on the board
        piece_list_with_XY = []  # (board_matrix, tile)
        for i in range(8):
            for j in range(8):
                if self.board_matrix[i][j][3] != 0:  # piece names
                    if self.board_matrix[i][j][self.current_player + 1] != 0:  # correct player
                        #piece_list_with_XY.append(((self.board_matrix[i][j]), (j, i)))

                        # test every piece
                        #for each_piece in piece_list_with_XY:
                        #each_piece = piece_list_with_XY[-1]
                        first_tile = (j, i)  #(each_piece[1][0], each_piece[1][1])
                        #if verbose: print "\tFirst tile:", first_tile#, each_piece[0][3]
                        for ii in range(8):
                            for jj in range(8):
                                # either an empty tile or enemy piece
                                if self.board_matrix[ii][jj][3] == 0 or self.board_matrix[ii][jj][opposite_player + 1] != 0:
                                    second_tile = (jj, ii)
                                    #if verbose: print "\tSecond_tile:", second_tile
                                    self.first_tile_information_store(first_tile, inspection=True)  # inspection required
                                    if self.rule_and_state_inspections(second_tile):
                                        if verbose: print "\tValid move at (XY):", second_tile, "from", first_tile
                                        if verbose: print "\tPlayer >%s< has valid moves!" % self.player_colors[self.current_player]
                                        return False
        return True

    def stalemate_inspection(self):
        print "stalemate_inspection() called"
        if not self.mate_testing:
            self.mate_testing = True
            if self.found_valid_move_flag is None:
                print "\t\t\t\tpossible stalemate... todo implement"
                self.found_valid_move_flag = True
                #self.found_valid_move_flag = not self.fast_no_valid_moves()
                #self.found_valid_move_flag = not self.no_valid_moves()


            stalemate = False
            # two kings
            #if self.captured_pieces_info is not []:
            if len(self.captured_pieces_info) == 30:
                stalemate = True
            # no available moves
            if self.found_valid_move_flag is False:  # can also be None (so if not self... can be buggy)
                stalemate = True

            self.mate_testing = False
            self.found_valid_move_flag = None
            if stalemate:
                self.game_over('stalemate')

    # possibly rename to, execute/update matrix for intended move or something
    def move_piece(self, first_tile, second_tile, **keyword_parameters):
        # todo refactor: use piece_list and not piece_info?
        print "keyword_parameters:", keyword_parameters
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        piece_object = self.board_matrix[first_tile[1]][first_tile[0]][self.current_player + 1]
        piece_name = self.board_matrix[first_tile[1]][first_tile[0]][3]
        #move_time = datetime.datetime.utcnow()
        time_taken = None  # clock_update()
        time_of_move = None  # clock_update()


        if 'enemy_tile' not in keyword_parameters:
            enemy_tile = second_tile
        elif 'enemy_tile' in keyword_parameters:
            enemy_tile = keyword_parameters['enemy_tile']

        # castle move
        # refactor out?
        if 'castle_flag' in keyword_parameters:
            # recurse move rook
            if self.player_colors[current_player] == 'white':
                castle_moves = [((2, 7), (0, 7), (3, 7), "O-O-O"), ((6, 7), (7, 7), (5, 7), "O-O")]  # todo can refactor this information
            else:  # self.player_colors[current_player] == 'white'
                castle_moves = [((2, 0), (0, 0), (3, 0), "O-O-O"), ((6, 0), (7, 0), (5, 0), "O-O")]
            #
            for each_valid_castle in castle_moves:  # todo refactor based on castle information passed (O-O...)
                    if second_tile == each_valid_castle[0]:
                        valid_castle = each_valid_castle
            first_tile_rook = valid_castle[1]
            second_tile_rook = valid_castle[2]

            # recurse move king
            print "\tCastle move_piece() recursion: king..."
            castle_tuple = (keyword_parameters['castle_flag'],  # O- notation
                            self.board_matrix[first_tile_rook[1]][first_tile_rook[0]][self.current_player + 1], # rook object
                            first_tile_rook,  # first_tile_rook (not necessary; simplifies undo())
                            second_tile_rook)  # second_tile_rook (not necessary; simplifies undo())
            if 'redo_flag' not in keyword_parameters:
                self.move_piece(first_tile, second_tile, castle_info=castle_tuple)  # keyword_parameters['castle_flag'])
            else:  # if 'redo_flag' in keyword_parameters:
                self.move_piece(first_tile, second_tile, castle_info=castle_tuple, redo_flag=True)

            print "\tCastle move_piece() recursion: rook..."
            # castle_info='skip move_list' skips adding to move list
            self.move_piece(first_tile_rook, second_tile_rook, castle_info='skip move_list')

            # sound
            if valid_castle[0][0] == 2:  # test king x destination
                self.sound_handler('O-O-O')  # use neat-O O-O-O notation
            else:  # valid_rook_tile[0][0][0] == 6
                self.sound_handler('O-O')   # use neat-O O-O notation
            return

        enemy_piece_object = self.board_matrix[enemy_tile[1]][enemy_tile[0]][opposite_player+1]
        if 'castle_info' not in keyword_parameters:
            castle_info = None
        else:
            castle_info = keyword_parameters['castle_info']

        # update move list and branch redo list
        if not self.undo_flag and castle_info != 'skip move_list':  # todo pass undo/redo flags as keyword arguments
            # todo turn into dict?
            master_move_list_entry = [
                first_tile,                     # first tile
                second_tile,                    # second tile
                piece_object,                   # piece object
                piece_name,                     # piece name
                enemy_piece_object,             # enemy captured object
                enemy_tile,                     # enemy tile (defaults to second_tile)
                castle_info                    # O-O and O-O-O: using letter O notation (algebraic uses zero "0")
                                                # castle_info also contains the rook object #todo (nested?)
                #time_taken,                     # time taken for move
                #time_of_move                    # time the move occurred (UTC?)
                ]
            self.master_move_list.append(master_move_list_entry)
            if 'redo_flag' not in keyword_parameters:
                self.redo_move_list = []


        ################ todo move this grouping to end?########################################
        # if not self.undo_flag: self.sound_handler(sound_selector='drop piece')  # SOUND
        if castle_info != 'skip move_list':
            self.sound_handler(called_sound_key='drop piece', rename_flag=True)  # SOUND  #todo review this rename_flag
        # place piece
        self.place_piece(piece_object, second_tile)
        ########################################################################################

        # destroy/FORGET and clear opponent object/name if present todo should I use the name list here?
        capture_bool = False
        capture_sound = False
        if self.board_matrix[enemy_tile[1]][enemy_tile[0]][opposite_player+1] != 0:  # todo readability
            capture_bool = True
            capture_sound = True
            self.sound_handler('captures')  # todo can move elsewhere (captured_pieces_info list)
            print "matrix_copy", self.board_matrix[second_tile[1]][second_tile[0]],  # todo why second tile?

            # copy information to captured pieces list
            copy_captured_piece_info = []  # todo find a better name for "info"?
            for i in range(4):
                copy_captured_piece_info.append(self.board_matrix[enemy_tile[1]][enemy_tile[0]][i])
            print "copy_captured_piece_info", copy_captured_piece_info
            self.captured_pieces_info.append(copy_captured_piece_info)  # todo refactor to captured_pieces_tile?
            print "captured_pieces_info", self.captured_pieces_info[-1]

            # clear opponent's information from tile
            self.board_matrix[enemy_tile[1]][enemy_tile[0]][opposite_player + 1].place_forget()
            self.board_matrix[enemy_tile[1]][enemy_tile[0]][opposite_player + 1] = 0
            self.board_matrix[enemy_tile[1]][enemy_tile[0]][3] = 0

            self.captured_piece_display()  # self.captured_pieces_info[-1][3])
            # todo captured_piece_display: better to pass the important information, or get it in the function?

        # update board matrix
        # update object and name
        self.board_matrix[second_tile[1]][second_tile[0]][current_player+1] = piece_object
        self.board_matrix[second_tile[1]][second_tile[0]][3] = piece_name
        # (NEW-ish) update background color todo refactor out using function call
        self.color_piece_background(piece=second_tile)

        if capture_bool: print "captured_pieces_info", self.captured_pieces_info[-1]

        # clear previous entry
        for i in range(1, 4):
            self.board_matrix[first_tile[1]][first_tile[0]][i] = 0

        # sound hacks todo refactor #warning todo remove (mostly)

        # redo promotion (todo much of this is redundant and can be combined with above)
        # todo not sure how I feel about redo promotion in move_piece()... need to read about how to do these things
        if 'redo_flag' in keyword_parameters:
            # if the move was a promotion
            if len(self.redo_move_list[-1]) == self.master_move_list_length + 1:
                self.board_matrix[second_tile[1]][second_tile[0]][self.current_player + 1].place_forget()  # todo figure out why this is necessary
                for i in range(1, 4):
                    self.board_matrix[second_tile[1]][second_tile[0]][i] = 0
                piece_object = self.redo_move_list[-1][-1][0]
                piece_name = self.redo_move_list[-1][-1][1]
                # place piece todo combine with above
                self.place_piece(piece_object, second_tile)
                self.board_matrix[second_tile[1]][second_tile[0]][current_player + 1] = piece_object
                self.board_matrix[second_tile[1]][second_tile[0]][3] = piece_name



    def create_board(self):

        # create tiles and color them
        bt_s = self.board_tile_size - 2  # Board Tile Size (-2 => border)
        for i in range(8):
            for j in range(8):
                self.board_matrix[i][j][0] = Canvas(self.chess_board, width=bt_s, height=bt_s)
                self.board_matrix[i][j][0].config(bg=self.white_tile, borderwidth=0, highlightthickness=1)
                self.board_matrix[i][j][0].config(highlightbackground=self.white_tile)
                if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                    self.board_matrix[i][j][0].config(bg=self.black_tile)
                    self.board_matrix[i][j][0].config(highlightbackground=self.black_tile)
                self.board_matrix[i][j][0].place(x=j*(bt_s+2), y=(i*(bt_s+2)))
                self.board_matrix[i][j][0].bind('<Button-1>', self.board_event_handler)
                self.board_matrix[i][j][0].bind('<ButtonRelease-1>', self.board_event_handler)

        # todo move this and create a todo script that saves (not delete) and removes all todos

        # numbering and lettering
        bc_w = self.bc_w  # Board Container Width/Height
        bc_h = self.bc_h
        cb_w = self.cb_w  # Chess Board Width/Height
        cb_h = self.cb_h
        # numbering
        x = bc_w/2-cb_w/2-bt_s/3
        for j in range(8):
            #x = bc_w/2-cb_w/2-bt_s/3
            y = bc_h/2-cb_h/2+(j*bt_s)+bt_s/2
            self.board_border.create_text(x, y, font=(self.board_font, 24), text=8-j, fill=self.board_text_color_1)
            #x += self.board_tile_size*8+bt_s*2/3
            #self.board_border.create_text(x, y, font=(self.board_font, 24), text=8-j, fill=self.board_text_color_1)
        # lettering
        y = bc_h/2+cb_h/2+bt_s/3
        for i in range(8):
            x = bc_w/2-cb_w/2+(i*bt_s)+bt_s/2
            #y = bc_h/2+cb_h/2+bt_s/3
            self.board_border.create_text(x, y, font=(self.board_font, 24), text=chr(65+i), fill=self.board_text_color_2)
            #y -= self.board_tile_size*8+bt_s*2/3
            #self.board_border.create_text(x, y, font=(self.board_font, 24), text=chr(65+i), fill=self.board_text_color_2)

        # title text (disabled)
        if self.title_text_enabled:  # todo this is ugly
            x = bc_w/2
            y = bc_h/2-cb_h/2-bt_s*3/5
            self.title_text = StringVar()  # todo move
            #self.board_border.create_text(x, y, font=(None, 24), text=self.title_text.get())
            self.title_label = Label(self.board_border, textvariable=self.title_text)
            self.title_label.config(font=(self.board_font, 24), bg=self.board_border_color, fg=self.board_text_color_1)  # todo fixed width font
            self.title_label.place(x=x, y=y, anchor='n')
            self.title_text.set("Move: White")  # TODO hardcoded because my player_color etc are backwards

        # outlines for captured_piece_display
        #self.captured_piece_display_position_rename1 = (bc_w-40, bc_h/2-20, bc_w-10, 100)  # todo
        #self.captured_piece_display_position_rename2 = (bc_w-40, bc_h/2+20, bc_w-10, bc_h-100)  # todo
        self.board_border.create_rectangle(bc_w-40, bc_h/2-10, bc_w-10, 32, outline=self.board_text_color_1)
        self.board_border.create_rectangle(bc_w-40, bc_h/2+10, bc_w-10, bc_h-32, outline=self.board_text_color_1)

        # todo refactor (can remove use of canvas objects)

    def create_piece_images(self):  # no idea why I can't get this working in the create_pawn/x functions
        """ crops, resizes, and stores piece images from single raw image

        self.crop_list = {'white_pawn': [562, 100, 601, 152],   'black_pawn': [561, 4, 601, 58],
                          'white_rook': [226, 100, 271, 152],   'black_rook': [226, 4, 271, 59],
                          'white_bishop': [331, 91, 388, 154],  'black_bishop': [330, 0, 387, 60],
                          'white_knight': [443, 98, 496, 152],  'black_knight': [443, 4, 496, 58],
                          'white_queen': [106, 95, 169, 152],   'black_queen': [105, 0, 168, 58],
                          'white_king': [0, 94, 54, 152],       'black_king': [-1, -1, 53, 58]}

        self.piece_object_lookup = {'white_pawn': 0,      'black_pawn': 0,
                                    'white_rook': 0,      'black_rook': 0,
                                    'white_bishop': 0,    'black_bishop': 0,
                                    'white_knight': 0,    'black_knight': 0,
                                    'white_queen': 0,     'black_queen': 0,
                                    'white_king': 0,      'black_king': 0}
        """

        piece_size = self.piece_size
        self.resized_piece_object_lookup = deepcopy(self.piece_object_lookup)

        # crop, resize, and store images to be drawn onto canvas objects
        r_f = self.resize_factor
        i = 0  # todo how to combine this?

        raw_image = Image.open('images/pieces.png')
        for each_piece in self.crop_list:
            crop_coordinates = self.crop_list[each_piece]
            crop_dimensions = (crop_coordinates[2]-crop_coordinates[0], crop_coordinates[3]-crop_coordinates[1])

            '''
            canvas_crop = Canvas(self.master, width=crop_dimensions[0], height=crop_dimensions[1])
            canvas_crop.config(borderwidth=0, highlightthickness=0)
            canvas_resize = Canvas(self.master, width=crop_dimensions[0]/r_f, height=crop_dimensions[1]/r_f)
            canvas_resize.config(borderwidth=0, highlightthickness=0)
            '''

            image_cropped = raw_image.crop(crop_coordinates)
            image_resized = image_cropped.resize((crop_dimensions[0]/r_f, crop_dimensions[1]/r_f), Image.ANTIALIAS)

            cropped_image_object = ImageTk.PhotoImage(image_cropped)
            resized_image_object = ImageTk.PhotoImage(image_resized)

            self.piece_object_lookup[each_piece] = cropped_image_object
            self.resized_piece_object_lookup[each_piece] = resized_image_object

            # for testing (do not delete)
            # canvas_crop.create_image(crop_dimensions[0]/2, crop_dimensions[1]/2, image=self.piece_objects[i])
            # canvas_crop.place(x=10+i*65, y=10+i*65)
            # canvas_resize.create_image(crop_dimensions[0]/r_f/2, crop_dimensions[1]/r_f/2, image=self.piece_objects_resized[i])
            # canvas_resize.place(x=10+i*65, y=600-i*65)
            i += 1

    # group by related function (pieces functions, UI functions, etc.)?
    def create_ui_images(self):
        load_image = ['images/forward.png', 'images/forward_end_c.png', 'images/mute.png', 'images/reset.png']
        image_names = ['forward', 'forward_end', 'mute_image', 'reset_image']
        for i in range(len(load_image)):
            raw_image = Image.open(load_image[i])
            image_resized = raw_image.resize((40, 40), Image.ANTIALIAS)
            resized_image_object = ImageTk.PhotoImage(image_resized)
            self.control_panel_image_objects.update({image_names[i]: resized_image_object})

        # todo refactor these with new knowledge
        raw_image = Image.open('images/forward_end_c.png')
        rotated_image = raw_image.rotate(180)
        image_resized = rotated_image.resize((40, 40), Image.ANTIALIAS)
        resized_image_object = ImageTk.PhotoImage(image_resized)
        self.control_panel_image_objects.update({'backward_end': resized_image_object})

        raw_image = Image.open('images/forward.png')
        rotated_image = raw_image.rotate(180)
        image_resized = rotated_image.resize((40, 40), Image.ANTIALIAS)
        resized_image_object = ImageTk.PhotoImage(image_resized)
        self.control_panel_image_objects.update({'backward': resized_image_object})

        # todo refactor this into above
        raw_image = Image.open('images/announce.png')
        image_resized = raw_image.resize((40, 40), Image.ANTIALIAS)
        resized_image_object = ImageTk.PhotoImage(image_resized)
        self.control_panel_image_objects.update({'announce': resized_image_object})

        # todo refactor this into above
        raw_image = Image.open('images/clock.png')
        image_resized = raw_image.resize((40, 40), Image.ANTIALIAS)
        resized_image_object = ImageTk.PhotoImage(image_resized)
        self.control_panel_image_objects.update({'clock': resized_image_object})

    def create_pieces(self):
        """ creates canvas objects, draws image, and correctly colors background """

        piece_size = self.piece_size
        black = self.player_colors.index('black') + 1
        white = self.player_colors.index('white') + 1

        for i in range(8):
            # assign names to the respective board_matrix elements (can refactor)
            self.board_matrix[0][i][3] = self.piece_list_names[i+8]
            self.board_matrix[1][i][3] = self.piece_list_names[i]
            self.board_matrix[6][i][3] = self.piece_list_names[i]
            self.board_matrix[7][i][3] = self.piece_list_names[i+8]

            # create canvas objects that function as the pieces (and will have piece images drawn on them)
            self.piece_list_black[i][2] = Canvas(self.board_border, width=piece_size, height=piece_size)
            self.board_matrix[1][i][black] = self.piece_list_black[i][2]
            self.piece_list_black[8 + i][2] = Canvas(self.board_border, width=piece_size, height=piece_size)
            self.board_matrix[0][i][black] = self.piece_list_black[8 + i][2]

            self.piece_list_white[i][2] = Canvas(self.board_border, width=piece_size, height=piece_size)
            self.board_matrix[6][i][white] = self.piece_list_white[i][2]
            self.piece_list_white[8 + i][2] = Canvas(self.board_border, width=piece_size, height=piece_size)
            self.board_matrix[7][i][white] = self.piece_list_white[8 + i][2]

        # draw images on the canvas piece objects
        for i in range(8):
            black_piece_name = 'black_' + self.piece_list_names[8 + i]
            white_piece_name = 'white_' + self.piece_list_names[8 + i]
            self.board_matrix[0][i][black].create_image(piece_size/2, piece_size/2, image=self.piece_object_lookup[black_piece_name])
            self.board_matrix[1][i][black].create_image(piece_size/2, piece_size/2, image=self.piece_object_lookup['black_pawn'])
            self.board_matrix[6][i][white].create_image(piece_size/2, piece_size/2, image=self.piece_object_lookup['white_pawn'])
            self.board_matrix[7][i][white].create_image(piece_size/2, piece_size/2, image=self.piece_object_lookup[white_piece_name])

        # colors background correctly (no canvas transparency hack)
        for i in range(8):
            if i < 2 or i > 5:
                if i < 2:
                    k = black
                else:
                    k = white
                for j in range(8):
                    if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                        self.board_matrix[i][j][k].config(bg=self.black_tile, borderwidth=0, highlightthickness=0)
                    else:
                        self.board_matrix[i][j][k].config(bg=self.white_tile, borderwidth=0, highlightthickness=0)

    def piece_placement_and_binding(self, default=True):
        bt_s = self.board_tile_size
        piece_size = self.piece_size

        # create piece lists with objects
        combined_piece_list = self.piece_list_white + self.piece_list_black
        '''
        if default:

        else:
            #warning todo this does not work (remove)
            for i in range(12):
                del self.piece_list_white[0]
            for i in range(3):
                del self.piece_list_white[1]

            for i in range(8):
                del self.piece_list_black[0]
            for i in range(3):
                del self.piece_list_black[1]
            for i in range(2):
                del self.piece_list_black[2]

            combined_piece_list = self.piece_list_white + self.piece_list_black
        '''

        for each_piece in combined_piece_list:
            x_position = each_piece[0]
            y_position = each_piece[1]
            x = self.chess_board_position_x - piece_size/2 + bt_s/2 + bt_s*x_position
            y = self.chess_board_position_y - piece_size/2 + bt_s/2 + bt_s*y_position
            each_piece[2].place(x=x, y=y)

            each_piece[2].bind('<Button-1>', self.board_event_handler)
            each_piece[2].bind('<ButtonRelease-1>', self.board_event_handler)


    def captured_piece_display(self):  #, piece_to_display):
        # todo captured_piece_display: better to pass the important information, or get it in the function?

        piece_name = self.captured_pieces_info[-1][3]
        i = self.number_of_captured_pieces['black']
        j = self.number_of_captured_pieces['white']

        if self.player_colors[self.current_player] == 'white':
            creating_key = "black_%s" % piece_name
            image_y = (self.bc_h/2+25)+20*i  # black pieces (the +20 is a function of the size of the mini pieces)
            self.number_of_captured_pieces['black'] += 1
        else:
            creating_key = "white_%s" % piece_name
            image_y = (self.bc_h/2-25)-20*j  # could un-hardcode with: image.height()
            self.number_of_captured_pieces['white'] += 1

        image = self.resized_piece_object_lookup[creating_key]
        image_x = self.bc_w-25
        display_object = self.board_border.create_image(image_x, image_y, image=image)
        self.captured_piece_display_objects.append(display_object)

    # todo bug check after refactor
    #warning todo make passthrough for inspections after a promotion has triggered
    def pawn_rules(self, first_tile, second_tile, inspection=False):
        if debugging_manual: print "Pawn rules..."

        #board_matrix = self.board_matrix
        board_matrix = self.a_copy_rename(self.board_matrix)  # todo review: necessary? (after recent refactor)
        #print board_matrix
        piece_info = self.piece_info
        #first_tile = self.first_tile

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        player_color = self.player_colors[current_player]

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']
        movement_direction = magnitude_and_direction['direction']

        path_unblocked = self.path_unblocked  # todo hum

        # if you're black, you add, if you're white, you subtract
        if player_color == 'black':
            forward_direction = 1
        else:
            forward_direction = -1

        # two-square advance
        c_1 = movement_magnitude[0] == 0                    # the movement is vertical todo review (necessary)?
        c_2 = (first_tile[1] == 1 or first_tile[1] == 6)    # in the initial position  todo problems including both white/black?
        c_3 = abs(movement_magnitude[1]) == 2               # movement is 2 tiles
        c_4 = movement_direction[1] == forward_direction    # movement_magnitude[1]/abs(movement_magnitude[1]) == forward_direction  # in the correct direction
        c_5 = path_unblocked(first_tile, second_tile)       # includes destination square (for pawns)
        if c_1 and c_2 and c_3 and c_4 and c_5:
            print "Two-square advance!"
            return True, None

        # promotion AND/OR one tile forward movement
        c_1 = movement_direction[1] == forward_direction    # forward movement (includes diagonal)
        c_2 = movement_direction[0] == 0                    # directly forward movement  # first_tile[0] = second_tile[0]
        c_3 = abs(movement_magnitude[1]) == 1               # movement is one tile
        c_4 = path_unblocked(first_tile, second_tile)       # path unblocked

        if c_1 and c_2 and c_3 and c_4:
            # pawn promotion  todo review/refactor
            white_promotion = (second_tile[1] == 0 and self.player_colors[current_player] == 'white')
            black_promotion = (second_tile[1] == 7 and self.player_colors[current_player] == 'black')
            if white_promotion or black_promotion:
                print "Promotion!"
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                #raise Exception("if this is accessed while doing a state check, it over-rights the piece_info_retainer ... ?")
                #if not self.mate_testing:  #warning todo remove after debugged
                #if self.piece_information_retainer is None: vs
                if not inspection:
                    self.piece_information_retainer = piece_info  # todo review after refactor
                else:
                    print "WARNING-UPPER: avoided overwriting piece information retainer"
                    #self.stop = True
                    #raise Exception("WARNING")
                return True, None
            # non-promotion move
            else:
                return True, None

        # promotion AND/OR capture  todo review/refactor with above
        c_1 = board_matrix[second_tile[1]][second_tile[0]][1+opposite_player] != 0   # enemy piece present
        c_2 = movement_direction[1] == forward_direction                             # forward movement (includes diagonal)
        c_3 = second_tile[0] != first_tile[0]                                        # movement not directly forward
        c_4 = abs(movement_magnitude[0]) == 1                                        # movement is one tile x  todo review
        c_5 = abs(movement_magnitude[1]) == 1                                        # movement is one tile y  todo review
        if c_1 and c_2 and c_3 and c_4 and c_5:
            # pawn promotion  todo review/refactor
            white_promotion = (second_tile[1] == 0 and self.player_colors[current_player] == 'white')
            black_promotion = (second_tile[1] == 7 and self.player_colors[current_player] == 'black')
            if white_promotion or black_promotion:
                print "Promotion!"
                #warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # warning TODO REVIEW REMOVE DEBUGGINS STUFF
                # if self.piece_information_retainer is None: vs
                if not inspection:
                    self.piece_information_retainer = piece_info  # todo review after refactor
                else:
                    print "WARNING-LOWER: avoided overwriting piece information retainer"
                    #self.stop = True
                    # raise Exception("WARNING")

                return True, None
            # capture (either forward diagonal)
            else:
                print "Capture!"
                return True, None

        # todo consider refactor into capture movement
        # en passant capture (special cased because it is unique)
        if self.en_passant_rules(first_tile, second_tile, forward_direction):
            print "En passant!"
            enemy_tile = (second_tile[0], second_tile[1]-(1*forward_direction))
            return True, enemy_tile

        if debugging_valid_move: print "Not a valid move!(1)"
        return False, None

    def en_passant_rules(self, first_tile, second_tile, forward_direction):
        """ en passant capture (special cased because it is unique)
        Args:
            first_tile:
            second_tile:
            forward_direction:
        Returns: Boolean, move allowed.
        The en passant capture must be made at the very next turn or the right to do so is lost.
        """
        board_matrix = self.board_matrix
        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']

        c_01 = first_tile[1] == (3 + current_player)  # the attacking pawn is on the correct row
        c_02 = 7 >= second_tile[1]-(1*forward_direction) >= 0  # removed same check on second_tile[0] (bug)
        if c_01 and c_02:  # a check to: protect accessing master_move_list AND c_04/06/09 out of range todo review
            # move to space is empty (capture would have already occurred)
            c_03 = board_matrix[second_tile[1]][second_tile[0]][3] == 0
            # only pawns
            c_04 = board_matrix[second_tile[1]-(1*forward_direction)][second_tile[0]][3] == 'pawn'
            # forward diagonal (NOT directly forward)
            c_05 = second_tile[0] != first_tile[0]
            # enemy piece to the same side as diagonal (is behind)
            c_06 = board_matrix[second_tile[1]-(1*forward_direction)][second_tile[0]][opposite_player+1] != 0
            # the last move was a 2 space move
            c_07 = abs(self.master_move_list[-1][1][1] - self.master_move_list[-1][0][1]) == 2
            # by a pawn
            c_08 = self.master_move_list[-1][3] == 'pawn'
            # the pawn is in the correct position (checks for correct tile)
            c_09 = self.master_move_list[-1][5] == (second_tile[0], second_tile[1]-(1*forward_direction))
            # pretty much does what the preceding condition was supposed to do
            c_10 = abs(movement_magnitude[0]) == 1 == abs(movement_magnitude[1])

            if c_02 and c_03 and c_04 and c_05 and c_06 and c_07 and c_08 and c_09 and c_10:
                return True
        return False

    # move this
    def a_copy_rename(self, copied_board_matrix):
        local_board_matrix_copy = deepcopy(self.board_matrix_clean_copy)
        length_rename = len(self.board_matrix[0][0])
        for i in range(8):
            for j in range(8):
                for k in range(1, length_rename):
                    if k == 1 or k == 2:  # refactor if board_matrix is ever changed
                        if copied_board_matrix[i][j][k] != 0:
                            local_board_matrix_copy[i][j][k] = 1
                        # else: value is already zero
                    elif k == 3:
                        local_board_matrix_copy[i][j][k] = copied_board_matrix[i][j][k]
        return local_board_matrix_copy

    # todo needs refactor (eg refactor to use first_tile rather than outer scope vars)
    def rook_rules(self, first_tile, second_tile):
        # todo refactor (refactored in queen movement)
        # todo everything ix xy except the matrix itself. change accordingly
        # todo castle is apparently a king move. also allow the rook to do it?
        if debugging_manual: print "Rook rules..."

        piece_info = self.piece_info
        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        # valid move, straight line v/h, with no pieces in the path to the final position.
        # check names of in the line from the final position to the origin

        #first_tile = self.first_tile
        '''
        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']
        ddr = magnitude_and_direction['direction']
        '''

        # get absolute difference in positions
        difference_xy_rename = [0, 0]
        difference_xy_rename[0] = abs(second_tile[0] - self.piece_info[2])  # todo refactor abs
        difference_xy_rename[1] = abs(second_tile[1] - self.piece_info[3])

        # movement direction
        difference_direction_rename = [0, 0]
        if difference_xy_rename[0] != 0:
            difference_direction_rename[0] = difference_xy_rename[0]/abs(difference_xy_rename[0])
        if difference_xy_rename[1] != 0:
            difference_direction_rename[1] = difference_xy_rename[1]/abs(difference_xy_rename[1])
        ddr = difference_direction_rename

        # get direction ?  todo refactor
        direction = None
        if difference_xy_rename != [0, 0]:
            if difference_xy_rename[1] != 0 and second_tile[1] > self.piece_info[3]:
                var_print = "DOWN"
                direction = 1
            elif difference_xy_rename[1] != 0:
                var_print = "UP"
                direction = -1
            if difference_xy_rename[0] != 0 and second_tile[0] > self.piece_info[2]:
                var_print = "RIGHT"
                direction = 1
            elif difference_xy_rename[0] != 0:
                var_print = "LEFT"
                direction = -1
            # todo re-enable? print "Rook moving %s XY" % var_print, (self.piece_info[2], self.piece_info[3])

        # test for only horizontal or vertical movement AND movement  # todo words
        #movement = (self.piece_info[0+2] - second_tile[0], self.piece_info[1+2] - second_tile[1])
        if (difference_xy_rename[1] == 0 or difference_xy_rename[0] == 0) and difference_xy_rename != [0, 0]:  # todo this is redundant, but readable
            # horizontal line (y delta is zero)
            if difference_xy_rename[1] == 0:
                # check spaces between piece and tile
                for i in range(difference_xy_rename[0]-1):
                    i = self.piece_info[0+2] + i*direction + direction
                    if self.board_matrix[second_tile[1]][i][3] != 0:
                        if debugging_valid_move: print "Not a valid move!(1)"  # todo send error to user
                        return  # todo necessary?
                # test second_tile for piece name (to move)
                if self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                    print "Valid move!"
                    #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                    return True
                # test for enemy (to capture)
                elif self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0:  # todo  combine w above
                    print "Capture!"
                    #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                    return True
                else:
                    print "Not valid move!(2)"  # todo send error to user
                    return False

            # vertical line (x delta is zero)
            elif difference_xy_rename[0] == 0:  # todo elif?
                # check spaces between piece and tile
                for i in range(difference_xy_rename[1]-1):
                    i = self.piece_info[1+2] + i*direction + direction
                    #print self.board_matrix[i][second_tile[0]][3]
                    if self.board_matrix[i][second_tile[0]][3] != 0:
                        if debugging_valid_move: print "Not a valid move!(3)"  # todo send error to user
                        return False
                # test second_tile for piece name (to move)
                if self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:  # TODO I CAN MERGE THIS WITH BELOW
                    print "Valid move!"
                    #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                    return True
                # test for enemy (to capture)
                elif self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0:
                    print "Capture!"
                    #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                    return True
                else:
                    if debugging_valid_move: print "Not valid move!(4)"  # todo send error to user
                    return False
                #print "Valid move!"  # todo this?
        else:
            if debugging_valid_move: print "Not a valid move!(5)"  # todo send error to user
        return False

    def knight_rules(self, first_tile, second_tile):
        if debugging_manual: print "Knight rules..."

        piece_info = self.piece_info
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        #first_tile = self.first_tile

        # get difference, compare to valid_horses
        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']

        # valid moves: Ls
        valid_horses = self.valid_horses

        # verify second_tile is L shape
        if movement_magnitude in valid_horses:
            # if own piece is in second_tile, invalid move
            if self.board_matrix[second_tile[1]][second_tile[0]][current_player+1] != 0:
                if debugging_valid_move: print "Not a valid move!(1)"  # todo send error to user
                return False
            # if enemy piece is in second_tile, take
            if self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0:
                print "Capture!"
                #self.check_rules(piece_info[0], second_tile)
                return True
            # if space is empty
            if self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:  # todo can combine this (bur readability?)
                print "Valid move!"
                #self.check_rules(piece_info[0], second_tile)
                return True
        else:
            if debugging_valid_move: print "Not a valid move!(2)"  # todo send error to user
        return False

    def bishop_rules(self, first_tile, second_tile):
        # TODO move movement to the first if statement?
        if debugging_manual: print "Bishop rules..."

        piece_info = self.piece_info
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        #first_tile = self.first_tile

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']

        # the x and y absolute differences must always be equal AND greater than 0 (movement)
        if abs(movement_magnitude[0]) == abs(movement_magnitude[1]) and abs(movement_magnitude[0]) > 0:
            print "Moving diagonal..."
            #first_tile = (piece_info[2], piece_info[3])
            if self.path_unblocked(first_tile, second_tile):
                # check second_tile for enemy OR empty
                if self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0 or self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                    #self.check_rules(piece_info[0], second_tile)
                    return True
        if debugging_valid_move: print "Not a valid move!()"  # todo send error to user
        return False

    def king_rules(self, first_tile, second_tile):  # TODO CAN'T MOVE INTO CHECK FUCK
        # todo factor out the second part of the return?
        """
        [DONE]Your king has been moved earlier in the game.
        [DONE]The rook that castles has been moved earlier in the game.
        [DONE]There are pieces standing between your king and rook.
        [DONE]The king is in check.
        [DONE]The king moves through a square that is attacked by a piece of the opponent.
        [DONE]The king would be in check after castling.
        """
        if debugging_manual: print "King rules..."

        piece_info = self.piece_info
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        #first_tile = self.first_tile

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']

        # if difference is is 1 tile
        c_01 = abs(movement_magnitude[0]) == 1 and abs(movement_magnitude[1]) == 0  # x movement
        c_02 = abs(movement_magnitude[0]) == 0 and abs(movement_magnitude[1]) == 1  # y movement
        c_03 = abs(movement_magnitude[0]) == 1 and abs(movement_magnitude[1]) == 1  # diagonal movement
        if c_01 or c_02 or c_03:  # changed from < 2 (explicit vs implicit)
            # if move is not blocked by own piece
            if self.board_matrix[second_tile[1]][second_tile[0]][current_player+1] == 0:
                # if move is a capture OR empty space  todo consistency with these shits
                if self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0 or self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                    #self.check_rules(piece_info[0], second_tile)
                    return True, None

        # castle test  todo refactor into castle_rules_rename
        # todo refactor? this does the check_rules. okay special casing this?
        # if movement is exactly 2 tiles
        elif abs(movement_magnitude[0]) == 2:  # todo performance (low priority) avoid check this every time a player tries to move a king 2 spaces?
            # [((king_final_position), (rook_initial_position), (rook_final_position))]
            valid_castle_moves_black = [((2, 0), (0, 0), (3, 0), "O-O-O"), ((6, 0), (7, 0), (5, 0), "O-O")]  # fuck it hard-coding
            valid_castle_moves_white = [((2, 7), (0, 7), (3, 7), "O-O-O"), ((6, 7), (7, 7), (5, 7), "O-O")]
            #combined_list = valid_castle_moves_black + valid_castle_moves_white  # todo consistency: white or black always appear first

            if self.player_colors[current_player] == 'white':
                castle_moves = valid_castle_moves_white
            else:  # self.player_colors[current_player] == 'white'
                castle_moves = valid_castle_moves_black

            # check if king has not moved (check if the king being moved is (NOT) in master_move_list)
            if self.piece_info[0] not in (each_move[2] for each_move in self.master_move_list):  # todo "abusive"?
                # find the corresponding rook tile
                for each_valid_castle in castle_moves:
                    if second_tile == each_valid_castle[0]:
                        valid_rook_tile = each_valid_castle[1]
                        # check for a rook on the corresponding tile
                        rook_name = self.board_matrix[valid_rook_tile[1]][valid_rook_tile[0]][3]
                        if rook_name == 'rook':
                            # check if that rook has not moved
                            rook_piece = self.board_matrix[valid_rook_tile[1]][valid_rook_tile[0]][current_player+1]
                            if rook_piece not in (each_move[2] for each_move in self.master_move_list):
                                # check for pieces between king and rook
                                if self.path_unblocked(first_tile, valid_rook_tile):
                                    # check if currently in check
                                    if not self.in_check(first_tile, self.player_colors[current_player]):
                                        # check those tiles for check
                                        # todo will the initial position of the king already be verified to not be in check?
                                        # todo review and consider refactor
                                        direction_x = magnitude_and_direction['direction'][0]
                                        for i in range(1, 3):  # todo checking second_tile is redundant from the first check check (above)
                                            receiving_tile = (first_tile[0]+direction_x*i, first_tile[1])
                                            if self.in_check(receiving_tile, self.player_colors[current_player]):  # todo gah event
                                                if debugging_valid_move: print "Not a valid move!(2) failed check check"
                                                return False, None
                                        # move king
                                        return True, each_valid_castle[3]
                                    else:
                                        self.sound_handler('castle while checked')

        if debugging_valid_move: print "Not a valid move!(3)"  # todo send error to user
        return False, None

    def castle_rules_rename(self):
        pass

    def queen_rules(self, first_tile, second_tile):
        # todo refactor the rook movement
        # todo refactor
        if debugging_manual: print "Queen rules..."

        piece_info = self.piece_info
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        #first_tile = self.first_tile

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']
        ddr = magnitude_and_direction['direction']

        # movement
        if movement_magnitude != [0, 0]:
            # h/v movement
            if movement_magnitude[1] == 0 or movement_magnitude[0] == 0:  # todo this is redundant, but readable
                # horizontal line (y delta is zero)
                if movement_magnitude[1] == 0:
                    # check spaces between piece and tile
                    for i in range(abs(movement_magnitude[0])-1):
                        i = self.piece_info[0+2] + i*ddr[0] + ddr[0]    #+ i*direction + direction
                        if self.board_matrix[second_tile[1]][i][3] != 0:
                            if debugging_valid_move: print "Not a valid move!(1)"  # todo send error to user
                            return False
                    # test second_tile for piece name (to move)
                    if self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                        print "Valid move!"
                        #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                        return True
                    # test for enemy (to capture)
                    elif self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0:  # todo  combine w above
                        print "Capture!"
                        #self.check_rules(piece_info[0], second_tile)  # todo too much copy/paste?
                        return True
                    else:
                        print "Not valid move!(2)"  # todo send error to user
                        return False

                # vertical line (x delta is zero)
                elif movement_magnitude[0] == 0:  # todo elif?
                    # check spaces between piece and tile
                    if self.path_unblocked(first_tile, second_tile):
                        # test second_tile for piece name (to move)
                        if self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                            print "Valid move!"
                            #self.check_rules(piece_info[0], second_tile)
                            return True
                        # test for enemy (to capture)
                        elif self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0:
                            print "Capture!"
                            #self.check_rules(piece_info[0], second_tile)
                            return True
                        else:
                            print "Not valid move!(3)"  # todo send error to user
                            return False

            # diagonal lines (using bishop code)
            # the x and y absolute differences must always be equal AND greater than 1 (movement)
            elif abs(movement_magnitude[0]) == abs(movement_magnitude[1]) and abs(movement_magnitude[0]) > 0:
                print "Moving diagonal..."
                first_tile = (piece_info[2], piece_info[3])
                if self.path_unblocked(first_tile, second_tile):
                    # check second_tile for enemy OR empty
                    if self.board_matrix[second_tile[1]][second_tile[0]][opposite_player+1] != 0 or self.board_matrix[second_tile[1]][second_tile[0]][3] == 0:
                        #self.check_rules(piece_info[0], second_tile)
                        return True
                # todo add invalid move prints/etc after every IF statement
            else:
                if debugging_valid_move: print "Not a valid move!"  # todo send error to user
        return False

    def check_rules(self, first_tile, second_tile, board_matrix=None, **keyword_parameters):
        # todo the board_matrix copy is not necessary after making move_piece depend on a necessary condition
        """ handles check rules
        verifies the move does not result in check

        # makes the changes of a move (sans visually updating),
        does check checks, reverts changes,
        then does them again if the tests were passed (with visual update)

        Args:
            first_tile:
            second_tile:
            board_matrix:
            **keyword_parameters:

        Returns:

        """

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        if 'enemy_tile' not in keyword_parameters:
            enemy_tile = second_tile
        elif 'enemy_tile' in keyword_parameters:
            enemy_tile = keyword_parameters['enemy_tile']

        if board_matrix is None:
            board_matrix = self.a_copy_rename(self.board_matrix)

        # inspecting board to determine if current player is in check before the move
        # (for sound logic)
        # todo make these into a function? self.king_check(self, current_player) return: players in check
        check_before_move = False
        for i in range(8):  # todo can remove these by constantly updating the piece lists
            for j in range(8):
                if board_matrix[i][j][3] == 'king' and board_matrix[i][j][current_player+1] != 0:
                    if self.in_check((j, i), self.player_colors[current_player]):  # checks current self.board_matrix
                        check_before_move = True

        # update the board to the move being rule checked (revert below)
        board_matrix = self.temporary_move(self.first_tile, second_tile, board_matrix, revert=False)

        # self_check: inspecting board to determine if that move "gave check" (to the CURRENT player)
        # todo better description: if check exists after the move (if it does not, the move removed check)
        # inspecting board to determine if current player is in check (moves can never end with the current player still in check)
        self_check = False
        for i in range(8):  # todo can remove these by constantly updating the piece lists
            for j in range(8):
                if board_matrix[i][j][3] == 'king' and board_matrix[i][j][current_player+1] != 0:
                    if self.in_check((j, i), self.player_colors[current_player], board_matrix):  # todo best practices/readability: switched to using self. because non-self. version was not updated when self was updated
                        self_check = True  # todo rename?: if check exists after move

        # inspecting board to determine if that move "gave check" (to the other player)
        # inspecting board to determine if the other player is in check
        # todo review this (is it necessary (here), can it be moved, should it be moved, etc)
        gave_check = False
        for i in range(8):  # todo can remove these by constantly updating the piece lists
            for j in range(8):
                if board_matrix[i][j][3] == 'king' and board_matrix[i][j][opposite_player+1] != 0:
                    if self.in_check((j, i), self.player_colors[opposite_player], board_matrix):  # todo best practices/readability: switched to using self. because non-self. version was not updated when self was updated
                        gave_check = True

        # revert the board to the initial state
        # todo not necessary when using a disposable copy
        #self.temporary_move(self.first_tile, second_tile, board_matrix, revert=True)

        if gave_check and not self_check:
            print "king takes control... todo change text"  # todo change text
            self.move_gave_check = True  # todo review after refactor finishes

        # todo review (found one major bug already)
        if self_check:
            if not check_before_move:
                print "That move would put your king in check!"
                self.sound_handler('self check')
                self.piece_information_retainer = None
                return False  # "fail"
            else: # check_before_move
                print "That move does not remove check!"
                self.sound_handler('check not removed')
                self.piece_information_retainer = None
                return False  # "fail"
        else:  # not self_check:
            if not check_before_move:
                # do stuff ?
                return True  # "pass"
            else:  # check_before_move
                print "That move removes check!"
                return True  # "pass"

        current_player = self.current_player
        print ">>> Control now with:", self.player_colors[current_player], '\n'  #warning TODO WHY IS THIS BROKEN

        # todo replace this (if it is used) with a 1 line call to a function
        if self.title_text_enabled:
            if self.player_colors[current_player] == 'white':
                self.title_text.set("Move: White")
            else:  # self.player_colors[current_player] == 'black'
                self.title_text.set("Move: Black")

    # todo verify working
    # todo move into draw_rules?
    def fifty_move_rule(self):
        # if 50 moves have occurred
        if len(self.master_move_list) >= 50:
            print "fifty_move_rule:\n\t", self.master_move_list[-50:]
            for i in range(50):
                c_1 = self.master_move_list[-50 + i][4] != 0
                c_2 = self.master_move_list[-50 + i][3] == 'pawn'
                if c_1 or c_2:
                    return False
            print "Fifty move rule satisfied!"
            return True
        return False



        # and within those 50 moves there were neighter pawn moves nor any captures


    # warning todo # 2 kings 2*n (same color) bishops
    # todo performance: these state checks based on pieces (and not position) can be only updated when piece numbers change
    def draw_rules(self):
        '''
        [DONE]king versus king
        [DONE]king and bishop versus king
        [DONE]king and knight versus king
        king and bishop versus king and bishop with the bishops on the same colour. (Any number of additional
        bishops of either color on the same color of square due to underpromotion do not affect the situation.)
        '''
        ''' #warning TODO
        Impossibility of checkmate - if a position arises in which neither player could possibly give checkmate by
        a series of legal moves, the game is a draw. This is usually because there is insufficient material left,
        but it is possible in other positions too. Combinations with insufficient material to checkmate are:

        king versus king
        king and bishop versus king
        king and knight versus king
        king and bishop versus king and bishop with the bishops on the same colour. (Any number of additional
        bishops of either color on the same color of square due to underpromotion do not affect the situation.)

        '''


        print "Draw rules..."
        # todo add other rules that are already elsewhere
        # todo refactor for readability
        draw = False
        number_of_captured_pieces = len(self.captured_pieces_info)
        if number_of_captured_pieces > (32 - 5):
            #warning todo # 2 kings 2*n (same color) bishops
            white_piece_list = self.get_player_piece_list('white')
            black_piece_list = self.get_player_piece_list('black')
            if number_of_captured_pieces == (32 - 4):  # 2 kings & 2 (same color) bishops
                combined_piece_list = white_piece_list + black_piece_list
                bishop_list = []
                for each_list_entry in combined_piece_list:
                    if each_list_entry[1][3] == 'bishop':
                        bishop_list.append(each_list_entry)
                if len(bishop_list) == 2:  # two bishops
                    if bishop_list[0][1][1] != bishop_list[1][1][1]:  # of different players
                        # get background color  todo sort of hacky (bg color vs tile location)
                        bg_1 = bishop_list[0][1][0].cget("bg")
                        bg_2 = bishop_list[1][1][0].cget("bg")
                        if bg_1 == bg_2:
                            draw = True  # todo test this lol
                            print "\t2 kings 2 (same color) bishops"
                        '''
                        i = bishop_list[0][0][1]
                        j = bishop_list[0][0][0]
                        ii = bishop_list[1][0][1]
                        jj = bishop_list[1][0][0]
                        # ((i + 1) % 2 == 0 and (j + 1) % 2 != 0) or (i % 2 == 0 and (j + 1) % 2 == 0)
                        if [
                                ((i + 1) % 2 == 0 and (j + 1) % 2 != 0)
                                or (i % 2 == 0 and (j + 1) % 2 == 0)
                                ==
                                ((ii + 1) % 2 == 0 and (jj + 1) % 2 != 0)
                                or (ii % 2 == 0 and (jj + 1) % 2 == 0)
                        ]:
                            draw = True  # todo test this lol
                            print "\t2 kings 2 (same color) bishops"
                            #raise NotImplementedError("this doesn't seem to be working (check)")
                        '''
            elif number_of_captured_pieces == (32 - 3):  # 2 kings 1 bishop/knight
                combined_piece_list = white_piece_list + black_piece_list
                for each_list_entry in combined_piece_list:
                    if each_list_entry[1][3] == 'bishop' or each_list_entry[1][3] == 'knight':
                        draw = True
                        print "\tdraw: 2 kings 1 bishop/knight"
            elif number_of_captured_pieces == (32 - 2):  # kings
                draw = True
                print "\tkings"
        if draw:
            print "Draw rules satisfied!"
            return True
        print "Draw rules not satisfied!"
        return False


    def temporary_move(self, first_tile, second_tile, board_matrix, revert, **keyword_parameters):  # todo change to move_test?
        """
        easily updates and reverts board without visual updates
        # ALL moves passed here are piece rule valid

        Args:
            first_tile:
            second_tile:
            board_matrix:
            revert:
            **keyword_parameters:

        Returns:

        """
        #warning TODO way to handle special cases: en passant addressed with 'enemy_tile',
                #TODO remaining: promotion
                #TODO CASTLE DOES NOT COME THROUGH HERE
        # TODO review enemy_tile replacing second_tile did not cause unintended behavior

        if 'enemy_tile' not in keyword_parameters:
            enemy_tile = second_tile
        elif 'enemy_tile' in keyword_parameters:
            enemy_tile = keyword_parameters['enemy_tile']

        if not revert:
            # keep track of second tile contents
            self.second_tile_contents = copy(self.board_matrix[enemy_tile[1]][enemy_tile[0]])  # todo is this copy necessary?
            # update tiles
            for i in range(1, 4):
                board_matrix[enemy_tile[1]][enemy_tile[0]][i] = board_matrix[first_tile[1]][first_tile[0]][i]
                board_matrix[first_tile[1]][first_tile[0]][i] = 0
        elif revert:
            # revert tiles
            for i in range(1, 4):
                board_matrix[first_tile[1]][first_tile[0]][i] = board_matrix[enemy_tile[1]][enemy_tile[0]][i]
                board_matrix[enemy_tile[1]][enemy_tile[0]][i] = self.board_matrix[enemy_tile[1]][enemy_tile[0]]  # self.second_tile_contents[i]
                self.second_tile_contents[i] = 0
        return board_matrix

    def path_unblocked(self, first_tile, second_tile):
        # returns true if the path is unblocked
        # todo consider combining both tests
        # todo do I want to check everything but the last spot?
        #warning TODO not sure this was implemented correctly; currently gives index errors

        #warning todo http://stackoverflow.com/a/15412863/6666148
        verbose = False  # todo
        if self.control_panel_settings['suppress_debugging']:
            verbose = False

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        player_colors = self.player_colors
        piece_info = self.piece_info
        board_matrix = self.board_matrix

        magnitude_and_direction = self.magnitude_and_direction(first_tile, second_tile)
        movement_magnitude = magnitude_and_direction['magnitude']
        ddr = magnitude_and_direction['direction']

        # pawn path blocking
        if piece_info[1] == 'pawn':
            if player_colors[current_player] == 'black':
                pawn_direction = 1
            else:
                pawn_direction = -1

            # todo generalize the pawn test
            #if abs(first_tile[1]-second_tile[1]) == 2:
            if verbose: print "PATH BLOCKING:", '\n', "\tMovement magnitude:", abs(movement_magnitude[1])
            # this specific range is going to test the destination square because pawns can't capture from movement
            # other implementations should handle this differently: probably by modifying the range
            # todo verify this works correctly
            for k in range(1, abs(movement_magnitude[1])+1):  # todo describe offset
                i = first_tile[1]+(pawn_direction*k)  # todo review: think of alternative i that does not result in index problems
                if -1 < i < 8:
                    if board_matrix[i][first_tile[0]][3] != 0:  # and board_matrix[first_tile[1]+2*pawn_direction][first_tile[0]][3] == 0:
                        if verbose: print "\tPawn CANNOT move!"
                        return False
                else:
                    if verbose: print "\tPawn CANNOT move!"
                    return False
            if verbose: print "\tPawn CAN move!"
            return True

        # non-pawn path blocking? (could make pawns a range(1) case)
        # if piece_info[1]
        else:
            # ddr = difference_direction_rename
            # range_0 is offset to avoid checking the piece tile
            # range_f is not offset to avoid checking the destination tile
            # todo shouldn't this be the lower range for diagonals
            upper_range = max(abs(movement_magnitude[0]), abs(movement_magnitude[1]))  # todo not sure if this works in every case
            for k in range(1, upper_range):  # todo describe offset TODO k vs n
                i = first_tile[1]+(ddr[1]*k)
                j = first_tile[0]+(ddr[0]*k)
                if -1 < i < 8 and -1 < j < 8:
                    if board_matrix[i][j][3] != 0:
                        if verbose: print "PATH BLOCKING: Piece CANNOT move!"
                        return False
            if verbose: print "PATH BLOCKING: Piece CAN move!"
            return True

    def in_check(self, receiving_tile, receiving_player_color, board_matrix=None, **keyword_parameters):  #warning TODO remove event
        """
        if 'detailed' is present, returns a list of piece names paired with location tuples
        receiving check is the opposite of "giving check"
        Args:
            receiving_tile:
            receiving_player_color:
            **keyword_parameters:

        Returns:

        """
        # note: better check yo-self, before you wreck yo-self
        # in_check = False todo for testing I can use this and run every test every time (worse performance)
        # todo refactor this into a separate debugging function that passes event information to this function
        d_c = debugging_check
        if debugging_check and 'event' in keyword_parameters:  # or event != None
            event = keyword_parameters['event']
            print event
            #receiving_tile = [None, None]
            receiving_player_color = None
            # get object ID
            object_id_below_cursor = root.winfo_containing(event.x_root, event.y_root)
            # find i, j,
            for i in range(8):
                for j in range(8):
                    if self.board_matrix[i][j][0] == object_id_below_cursor:
                        receiving_tile[0] = j
                        receiving_tile[1] = i
            receiving_player_color = 'white'
        if d_c: print "CHECKING FOR %s IN CHECK at %s:" % (receiving_player_color, receiving_tile)

        # todo refactor once self.current_player is fixed
        current_player = None
        if receiving_player_color == 'white':
            if self.player_colors[0] == 'white':  # todo remove after self.current_player is fixed
                current_player = 0
            else:  # self.player_colors[0] == 'black'
                current_player = 1
        elif receiving_player_color == 'black':
            if self.player_colors[1] == 'black':
                current_player = 1
            else:
                current_player = 0
        opposite_player = abs(current_player - 1)

        if board_matrix is None:
            board_matrix = self.board_matrix

        # check each valid_horse tile FROM the receiving tile
        check_list = []
        valid_horses = self.valid_horses
        for each_valid_horse in valid_horses:
            i = receiving_tile[1] + each_valid_horse[1]
            j = receiving_tile[0] + each_valid_horse[0]
            if -1 < i < 8 and -1 < j < 8:
                # is there a knight on that tile AND it is the opponent
                if board_matrix[i][j][3] == 'knight' and board_matrix[i][j][opposite_player+1] != 0:
                    if d_c: print '\t', "IN CHECK BY:", '\t\t', "   KNIGHT from (relative)", each_valid_horse
                    check_list.append((board_matrix[i][j][3], each_valid_horse))

        # todo can generalize this by passing receiving_tile and receiving_player_color
        # todo move
        def cardinal_and_intercardinal(direction):  # up = -1; down = 1
            """ # check horizontal, vertical, and diagonal lines
            Tests cardinal and intercardinal directions (horizontal, vertical, and diagonal) for pieces that give check.
            Search these lines for first the piece, check if piece is a corresponding enemy queen/rook/bishop
            """
            # todo refactor is this too complex?
            # todo consolidate/refactor [SEE HOW I DID THIS IN THE RULES FUNCTIONS] ==> looks like this may be better
            # description here
            if direction in ('N', 'E', 'S', 'W'):
                rook_or_bishop = "rook"
            elif direction in ('NE', 'SE', 'SW', 'NW'):
                rook_or_bishop = "bishop"
            # rook/queen (cardinal)
            if direction == 'N':
                direction_modifier = -1
                upper_range = receiving_tile[1]
                j_1 = receiving_tile[0]  # todo consider something like j, j1, j2 to avoid this problem?
            elif direction == 'E':
                direction_modifier = 1
                upper_range = 7 - receiving_tile[0]
                i_1 = receiving_tile[1]
            elif direction == 'S':
                direction_modifier = 1
                upper_range = 7 - receiving_tile[1]
                j_1 = receiving_tile[0]
            elif direction == 'W':
                direction_modifier = -1
                upper_range = receiving_tile[0]
                i_1 = receiving_tile[1]
            # bishop/queen (intercardinal)
            if direction == 'NE':
                direction_modifier = 1
                upper_range = min(7 - receiving_tile[0], receiving_tile[1])
            elif direction == 'SE':
                direction_modifier = 1
                upper_range = min(7 - receiving_tile[0], 7 - receiving_tile[1])
            elif direction == 'SW':
                direction_modifier = -1
                upper_range = min(receiving_tile[0], 7 - receiving_tile[1])
            elif direction == 'NW':
                direction_modifier = -1
                upper_range = min(receiving_tile[0], receiving_tile[1])

            # find the first piece
            found_piece_flag = False  # todo refactor? the flag hack
            for each_tile in range(1, upper_range + 1):  #warning TODO check this range
                if direction in ('N', 'S', 'SE', 'NW'):
                    i_1 = receiving_tile[1] + each_tile*direction_modifier
                if direction in ('W', 'E', 'SE', 'NW'):  # removed elif for intercardinal
                    j_1 = receiving_tile[0] + each_tile*direction_modifier
                elif direction == 'NE' or direction == 'SW':  # todo review: can this be further simplified? does not appear so
                    i_1 = receiving_tile[1] - each_tile*direction_modifier
                    j_1 = receiving_tile[0] + each_tile*direction_modifier
                if board_matrix[i_1][j_1][3] != 0 and not found_piece_flag:
                    found_piece_flag = True
                    # check for enemy player
                    if board_matrix[i_1][j_1][opposite_player+1] != 0:
                        # check if enemy piece is queen OR rook or bishop
                        if board_matrix[i_1][j_1][3] == 'queen' or board_matrix[i_1][j_1][3] == rook_or_bishop:
                            if d_c: print '\t', "IN CHECK BY:", '\t\t',  direction.rjust(2, " "), board_matrix[i_1][j_1][3].upper(), "at", (i_1, j_1)
                            check_list.append((board_matrix[i_1][j_1][3], (i_1, j_1)))
                            return True
            #if d_c: print '\t', "NOT IN CHECK BY:", '\t', direction.rjust(2, " "), "QUEEN/%s" % rook_or_bishop.upper()
            return False

        # todo performance: immediately return True if found (like with knight)
        c_1 = cardinal_and_intercardinal('N')
        c_2 = cardinal_and_intercardinal('E')
        c_3 = cardinal_and_intercardinal('S')
        c_4 = cardinal_and_intercardinal('W')
        c_5 = cardinal_and_intercardinal('NE')
        c_6 = cardinal_and_intercardinal('SE')
        c_7 = cardinal_and_intercardinal('SW')
        c_8 = cardinal_and_intercardinal('NW')

        # todo review after player number is fixed
        if receiving_player_color == 'white':
            direction_of_pawn = -1
        else:  # self.player_colors[receiving_player_color] == 'black'
            direction_of_pawn = 1
        # pawn check
        diagonals = [None, None]
        diagonals[0] = (receiving_tile[0]-1, receiving_tile[1]+direction_of_pawn)
        diagonals[1] = (receiving_tile[0]+1, receiving_tile[1]+direction_of_pawn)
        for each_diagonal in diagonals:
            # if the tile is on the board
            if -1 < each_diagonal[0] < 8 and -1 < each_diagonal[1] < 8:
                # if an enemy pawn is present
                condition_one = board_matrix[each_diagonal[1]][each_diagonal[0]][3] == 'pawn'
                condition_two = board_matrix[each_diagonal[1]][each_diagonal[0]][opposite_player+1] != 0
                if condition_one and condition_two:
                    if d_c: print '\t', "IN CHECK BY:  ", '\t\t  ', board_matrix[each_diagonal[1]][each_diagonal[0]][3].upper(), "at", each_diagonal
                    #return True
                    check_list.append((board_matrix[each_diagonal[1]][each_diagonal[0]][3], each_diagonal))

        # king check
        enemy_king_tile = None
        for i in range(8):  # todo can remove these by constantly updating the piece lists
            for j in range(8):
                if board_matrix[i][j][3] == 'king' and board_matrix[i][j][opposite_player+1] != 0:
                    enemy_king_tile = (j, i)
        if enemy_king_tile is None:  #warning todo remove after debugged
            print "\n\n******************"
            print "board_matrix[i][j]:", board_matrix[i][j]
            print "current_player:", current_player
            print "receiving_tile, receiving_player_color:", receiving_tile, receiving_player_color
            raise Exception("debugging: it appears the king was captured")
        magnitude_and_direction = self.magnitude_and_direction(receiving_tile, enemy_king_tile)
        magnitude = magnitude_and_direction['magnitude']
        c_1 = abs(magnitude[0]) == 0 and abs(magnitude[1]) < 2
        c_2 = abs(magnitude[0]) < 2 and abs(magnitude[1]) == 0
        c_3 = abs(magnitude[0]) == abs(magnitude[1]) and abs(magnitude[0]) < 2  # todo: ? x == y < 2 ?
        if c_1 or c_2 or c_3:
            check_list.append((board_matrix[i][j][3], enemy_king_tile))

        if len(check_list) == 0:
            if d_c: print "\tAll tests passed. Kn/Q/R/B/P"
            return False
        else:
            if 'detailed' not in keyword_parameters:
                return True
            elif 'detailed' in keyword_parameters:
                if d_c: print "\tcheck_list", check_list
                return check_list

    # todo rename to: no_valid_moves or similar
    # todo rename: also include ... or stalemate
    def no_valid_moves(self):
        # tests for current player in checkmate
        print "Checkmate test (no_valid_moves())..."  # todo rename
        #warning todo don't forget about stalemate
        verbose = True

        # can simulate (for single moves, long term would need more information for duplicate pieces)
        # by creating a copy of the names, and a 1 or some value where the piece object was (can just remove the board object)

        # get game state
        # play every possible move with depth of 1
        # if no legal move results in removing check
        # return checkmate

        # can check be removed:
        # capture piece giving check
        # block piece giving check (all pieces except horse)

        # check every valid move for check
        # if every valid move itself results in check
        # checkmate
        # BUT that's every valid move for the player, not just the king


        # can check be removed:
        # capture piece giving check
            # run in_check on the piece?
                # the piece may be pinned, run in_check to verify it's an allowed move?
        # block piece giving check (all pieces except horse)
        # when double check, king must move

        # brute forcing (copy-pasting from random moves)
        # will be in check (castling not allowed)
        # promotion move can be treated as a normal move w/o promotion
        # en passant rules are included in

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        #board_matrix = self.a_copy_rename(self.board_matrix)  # todo this is not necessary with the recent refactor (and is expensive)

        self.found_valid_move_flag = False  # todo review should remove
        #warning this will not work if this function is called prior to this flag being used

        # find all of the player pieces on the board
        piece_list = self.get_player_piece_list(self.player_colors[current_player])

        # test every piece
        for each_piece in piece_list:
            first_tile = (each_piece[0][0], each_piece[0][1])
            if verbose: print "\tFirst tile:", first_tile, each_piece[1][3]
            valid_move_list = self.get_valid_moves(first_tile, combined_list=True)
            if bool(valid_move_list):  # a list can function as a bool. empty=false  # issues with bool() and is not
                ''' indent 1 back <---
                for i in range(8):
                    for j in range(8):
                        # either an empty tile or enemy piece
                        if board_matrix[i][j][3] == 0 or board_matrix[i][j][opposite_player + 1] != 0:
                            second_tile = (j, i)
                            if verbose: print "\tSecond_tile:", second_tile
                            self.first_tile_information_store(first_tile, inspection=True)  # todo review
                            if self.rule_and_state_inspections(second_tile, inspection=True):
                '''
                #if verbose: print "\tValid move at (XY):", (j, i)
                #print "\tPlayer >%s< has valid moves!" % self.player_colors[self.current_player]
                if verbose: print "\tValid move(s) at (XY):", valid_move_list
                self.found_valid_move_flag = True  # use for stalemate_inspection  # todo review for remove
                return False

        # commented out to encapsulate (I think that's the correct word)
        '''
        if self.move_gave_check:
            self.checkmate = True  #warning TODO REVIEW... is this necessary? don't think so
        else:
            print "TODO STALEMATE HERE........................................................."
        '''
        return True



    # rename helper functions?
    def magnitude_and_direction(self, first_tile, second_tile):
        """
        finds the magnitude and direction from the first to second tile
        :param first_tile:
        :param second_tile:
        :return: ((magnitude_x, magnitude_y), (direction_x, direction_y))
        """

        # movement magnitude
        movement_magnitude = [0, 0]
        movement_magnitude[0] = second_tile[0] - first_tile[0]
        movement_magnitude[1] = second_tile[1] - first_tile[1]

        # movement direction
        movement_direction = [0, 0]
        if movement_magnitude[0] != 0:
            movement_direction[0] = movement_magnitude[0]/abs(movement_magnitude[0])
        if movement_magnitude[1] != 0:
            movement_direction[1] = movement_magnitude[1]/abs(movement_magnitude[1])

        # ((movement_magnitude[0], movement_magnitude[1]), (movement_direction[0], movement_direction[1]))
        return {'magnitude': movement_magnitude, 'direction': movement_direction}

    def alternate_players(self):
        # if not self.undo_flag:  #warning TODO self.castle_flag?
        # alternate current player
        self.current_player -= 1
        self.current_player *= -1
        print "Current player alternated to %s." % self.player_colors[self.current_player]
        # todo here is where I would update opposite_player

    # todo generalize this operation to moving backward on master_move_list, able to also move forward
    def undo(self, *event):
        #warning TODO special cases: promotion... and?
        # todo suppress undo end

        if self.timer_enabled:
            self.sound_handler('must disable timer')
            return

        self.undo_flag = True  # todo use? make undo/redo flag? rename?

        if len(self.master_move_list) > 0:
            self.sound_handler('undo')
            print "Player <%s> must have blundered!" % self.player_colors[abs(self.current_player-1)]
            bt_s = self.board_tile_size  # Board Tile Size
            bc_w = self.bc_w  # Board Container Width/Height
            bc_h = self.bc_h
            cb_w = self.cb_w  # Chess Board Width/Height
            cb_h = self.cb_h

            # undo last move (run the first/second tiles through the mover backward?)

            print "self.master_move_list[-1]:\n\t", self.master_move_list[-1]

            # alternate current player (BACK 0to player that just played/moved)
            self.alternate_players()

            # promotion
            promotion_info = None
            #warning todo promotion capture (works with below? wow lol)
            # if the previous move's second_tile has a piece name that's not the same as the current piece name
            i = self.master_move_list[-1][1][1]
            j = self.master_move_list[-1][1][0]
            # todo and there was no capture; or todo and the piece is from the same player?
            if self.board_matrix[i][j][3] != self.master_move_list[-1][3]:
                print "Capture undo!"
                promotion_object = self.board_matrix[i][j][self.current_player + 1]
                promotion_object.place_forget()
                promotion_info = (promotion_object, self.board_matrix[i][j][3])

            # rook piece of castle (king is handled below)
            castle = False
            # if more than one move has been made
            if len(self.master_move_list) > 1:  # todo warning: castle on the first move is bugged (not possible move)
                # check for castle
                if self.master_move_list[-1][6] is not None:
                    castle = True
                    print "self.master_move_list[-1][6][0]:", self.master_move_list[-1][6][0]
                    castle_notation = self.master_move_list[-1][6][0]
                    if castle_notation == "O-O" or castle_notation == "O-O-O":
                        print "Castle undo!"

                        castle_object = self.master_move_list[-1][6][1]
                        first_tile_rook = self.master_move_list[-1][6][2]
                        second_tile_rook = self.master_move_list[-1][6][3]

                        # revert move
                        # update board matrix
                        self.board_matrix[first_tile_rook[1]][first_tile_rook[0]][self.current_player + 1] = castle_object
                        self.board_matrix[first_tile_rook[1]][first_tile_rook[0]][3] = 'rook'
                        for i in range(1, 4):
                            self.board_matrix[second_tile_rook[1]][second_tile_rook[0]][i] = 0

                        self.color_piece_background(piece=first_tile_rook)

                        self.place_piece(castle_object, first_tile_rook)

            first_tile = self.master_move_list[-1][0]  # todo rename to indicate any differences, such as first_tile_-1 or something, then replace below

            # revert move
            # update board matrix
            self.board_matrix[self.master_move_list[-1][0][1]][self.master_move_list[-1][0][0]][self.current_player + 1] = self.master_move_list[-1][2]
            self.board_matrix[self.master_move_list[-1][0][1]][self.master_move_list[-1][0][0]][3] = self.master_move_list[-1][3]
            # clear second tile
            for i in range(1, 4):
                self.board_matrix[self.master_move_list[-1][1][1]][self.master_move_list[-1][1][0]][i] = 0

            # place object  todo use function
            i = self.master_move_list[-1][0][1]
            j = self.master_move_list[-1][0][0]
            piece_s = self.piece_size
            x = bc_w/2-cb_w/2+(j*bt_s)+bt_s/2-piece_s/2
            y = bc_h/2-cb_h/2+(i*bt_s)+bt_s/2-piece_s/2
            print "Moving to (placing) (XY):", (i, j)  # x, y
            self.board_matrix[self.master_move_list[-1][0][1]][self.master_move_list[-1][0][0]][self.current_player + 1].place(x=x, y=y)

            # update background color # todo use function
            i = self.master_move_list[-1][0][1]
            j = self.master_move_list[-1][0][0]
            if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                self.board_matrix[self.master_move_list[-1][0][1]][self.master_move_list[-1][0][0]][self.current_player+1].config(bg=self.black_tile)
            else:
                self.board_matrix[self.master_move_list[-1][0][1]][self.master_move_list[-1][0][0]][self.current_player+1].config(bg=self.white_tile)

            # place the captured piece
            # if the previous move was a capture move
            if self.master_move_list[-1][4] != 0 and not castle:  # todo verify usefulness of castle bool
                opposite_player = abs(self.current_player - 1)
                # location (XY)
                piece_size = self.piece_size
                x = self.chess_board_position_x - piece_size/2 + bt_s/2 + bt_s*self.master_move_list[-1][5][0]
                y = self.chess_board_position_y - piece_size/2 + bt_s/2 + bt_s*self.master_move_list[-1][5][1]
                print "self.captured_pieces_info[-1]", self.captured_pieces_info[-1]
                self.captured_pieces_info[-1][opposite_player + 1].place(x=x, y=y)
                # update board
                for i in range(1, 4):
                    self.board_matrix[self.master_move_list[-1][5][1]][self.master_move_list[-1][5][0]][i] = self.captured_pieces_info[-1][i]
                # update captured pieces list
                print "Captured Pieces:"
                del self.captured_pieces_info[-1]
                print '\t', self.captured_pieces_info
                # update captured display and information
                self.board_border.delete(self.captured_piece_display_objects[-1])
                print "self.captured_piece_display_objects", self.captured_piece_display_objects
                del self.captured_piece_display_objects[-1]
                print "self.captured_piece_display_objects", self.captured_piece_display_objects
                self.number_of_captured_pieces[self.player_colors[opposite_player]] -= 1
                print "self.number_of_captured_pieces[self.player_colors[self.current_player]] -= 1:", self.number_of_captured_pieces

            self.redo_move_list.append(self.master_move_list[-1])
            if promotion_info is not None:
                self.redo_move_list[-1].append(promotion_info)
            del self.master_move_list[-1]
            # reset piece selection
            self.piece_info = None  # TODO review
            self.first_tile = None
            # second_tile?
            # todo consider .destroy()... what am I saving? <1mb of memory?
            print
        else:
            print "Nothing to undo!"
            self.sound_handler('undo error')

        self.undo_flag = False
        self.text_box_update()

    def undo_end(self, *event, **kwargs):
        """

        Args:
            *event:
            **kwargs:

        Returns:

        """
        if self.timer_enabled:
            self.sound_handler('must disable timer')
            return

        if len(self.master_move_list) > 0:
            self.focus_grabber.grab_set()

            # todo re-work this
            '''
            if len(self.master_move_list) < 3:
                sleep_duration = .5/len(self.master_move_list) + .1
            else:
                sleep_duration = 3/len(self.master_move_list) + .1
            '''
            sleep_duration = .15  # todo useful?

            while len(self.master_move_list) > 0:
                sleep(sleep_duration/2)
                self.undo()

                if len(self.master_move_list) > 0:
                    root.update()
                    sleep(sleep_duration/2)
                #todo grab focus on something
            print "Undo complete!"  # todo

            self.focus_grabber.grab_release()
        else:
            print "Nothing to undo!"
            self.sound_handler('undo error')

    def place_piece(self, piece, place_tile):  # , is_current_player):
        """
        # board_border center 800x800 bc_w/2
        # from board container center to (0, 0) of board
        # once at (0, 0) of board x=(j*bt_s), y=(i*bt_s)
        # offset to center of tile based on piece size
        Args:
            piece:
            place_tile:

        Returns:
        """
        bt_s = self.board_tile_size  # Board Tile Size
        bc_w = self.bc_w  # Board Container Width/Height
        bc_h = self.bc_h
        cb_w = self.cb_w  # Chess Board Width/Height
        cb_h = self.cb_h

        i = place_tile[1]
        j = place_tile[0]
        piece_s = self.piece_size
        x = bc_w/2-cb_w/2+(j*bt_s)+bt_s/2-piece_s/2
        y = bc_h/2-cb_h/2+(i*bt_s)+bt_s/2-piece_s/2
        if debugging: "Moving to (XY):", (i, j)  # x, y
        piece.place(x=x, y=y)

    #warning todo enemy tile (en passant)
    #warning todo castle
    #warning todo promotion
    def redo(self, *args):

        if self.timer_enabled:
            self.sound_handler('must disable timer')
            return

        #raise NotImplementedError("bug: undo, then redo, after promotion (promotion piece information lost)")
        if debugging: "Redo... todo grab_set()/release delay?"

        #warning todo grab_set()/release delay?

        if len(self.redo_move_list) > 0:

            # move information
            piece_object = self.redo_move_list[-1][2]
            piece_name = self.redo_move_list[-1][3]
            first_tile = self.redo_move_list[-1][0]
            second_tile = self.redo_move_list[-1][1]
            enemy_tile = self.redo_move_list[-1][5]
            castle_info = self.redo_move_list[-1][6]
            #time_taken = self.redo_move_list[-1][7]
            #time_of_move = self.redo_move_list[-1][8]
            en_passant = False
            castle = False
            if second_tile != enemy_tile:
                en_passant = True
            elif castle_info is not None:
                castle = True

            # test to see if the redo was a promotion
            # len(self.master_move_list[0]) equals 7 (currently)  # todo warning hardcoded
            if len(self.redo_move_list[-1]) == self.master_move_list_length + 1:  # the first entry of the master_move_list can never be a promotion
                print "self.redo_move_list[-1][-1][0]:\t", self.redo_move_list[-1][-1][0]
                print self.redo_move_list[-1]
                print "WARNING: hardcoded"
                ####self.place_piece(self.redo_move_list[-1][-1][0], second_tile)  #warning todo should not use last element
                #warning todo update board!?
                #self.board_matrix[second_tile[1]][second_tile[0]][3] = piece_name
                #self.board_matrix[second_tile[1]][second_tile[0]]
                #raise NotImplementedError("uh, promotion undo redo undo will cause error")
                ####self.board_matrix[first_tile[1]][first_tile[0]][self.current_player + 1].place_forget()
                #for i in range(1, 4):
                #    self.board_matrix[first_tile[1]][first_tile[0]][i] = 0
                # todo this was done in move_piece(); should keep redo promotion out of there???


            # test to see if the redo was en passant



            # test to see if the redo was castle

            # create piece info  # todo could also pass the first_tile info to press() (if it accepted **kwargs)
            self.piece_info = (piece_object, piece_name, first_tile[0], first_tile[1])  # todo why tuple? style? best practice?
            self.first_tile = first_tile

            if not en_passant and not castle:
                self.move_piece(first_tile, second_tile, redo_flag=True) #self.move_piece(piece_object, second_tile, redo_flag=True)
            elif en_passant:
                self.move_piece(first_tile, second_tile, redo_flag=True, enemy_tile=enemy_tile)
            elif castle:
                print "REDO MOVE CASTLE #######################################\nREDO MOVE CASTLE #######################################\n\REDO MOVE CASTLE #######################################\nREDO MOVE CASTLE #######################################\nREDO MOVE CASTLE #######################################\nREDO MOVE CASTLE #######################################"
                print castle_info
                self.move_piece(first_tile, second_tile, redo_flag=True, castle_flag=castle_info[0])

            # update time (NOT WORKING)
            #self.master_move_list[-1][7] = time_taken
            #self.master_move_list[-1][8] = time_of_move

            self.alternate_players()

            del self.redo_move_list[-1]
            # reset piece selection
            self.piece_info = None  # TODO create an implementation that does not require things like this
            self.first_tile = None

        else:
            print "Noting to redo!"
            self.sound_handler('redo error')

        #self.redo_flag = False
        self.text_box_update()

    def redo_end(self, *event):

        if self.timer_enabled:
            self.sound_handler('must disable timer')
            return

        if len(self.redo_move_list) > 0:
            self.focus_grabber.grab_set()

            sleep_duration = .15  # todo useful?

            while len(self.redo_move_list) > 0:
                sleep(sleep_duration/2)
                self.redo()

                if len(self.redo_move_list) > 0:
                    root.update()
                    sleep(sleep_duration/2)
            print "Redo complete!"  # todo

            self.focus_grabber.grab_release()
        else:
            print "Nothing to redo!"
            self.sound_handler('redo error')

    def game_over(self, outcome):
        self.game_is_over = True
        #self.control_panel_settings['mute'] = False
        print "Game over. [game_over]"
        if outcome == 'checkmate':
            # remove this later
            self.checkmate = True  # todo where else is this used? game_is_over may render this obsolete
            self.sound_handler('checkmate')
            self.game_is_over = True
            if self.player_colors[self.current_player] == 'white':
                self.sound_handler('black wins')
            else:
                self.sound_handler('white wins')
        elif outcome == 'stalemate':
            print "TODO STALEMATE THINGS"
            self.sound_handler('stalemate')
            self.game_is_over = True
            # remove this later
            #self.checkmate = True
        elif outcome == 'draw':
            print "TODO DRAW THINGS"
            self.sound_handler('draw')
            self.game_is_over = True
            # remove this later
            #self.checkmate = True
        self.stop = True



        # todo rather than initialize the window objects, they're created when needed. acceptable?
        # probably except on mobile devices
        # cProfile.runctx("self.create_notification_window()", globals(), locals())
        #wcpd = self.win_control_panel_dimensions
        #x = self.v_spacer/2-wcpd[0]/2
        #y = self.v_spacer/2-wcpd[1]/2
        #y += -345  # todo
        #self.quit_reset_container.place(x=x, y=y)
        self.create_notification_window()  # this method requires modification to focus grabbing

    # todo rename reset_ X  (more than just the board) maybe reset game.
    def reset_board(self, *args):
        #warning TODO refactor out things beyond resetting the board into their own functions
        # todo reset initialize_controls_panel, debugging, etc.
        if debugging: print "\nResetting board... reset_board()"

        # do nothing if no moves have been made (or undone)
        c_1 = len(self.master_move_list) == 0
        c_2 = len(self.redo_move_list) == 0
        if c_1 and c_2:
            self.sound_handler('nothing to reset')
            return

        # clear board matrix
        for i in range(8):
            for j in range(8):
                for k in range(1, 4):
                    self.board_matrix[i][j][k] = 0

        # restore board matrix to initial state
        black = self.player_colors.index('black') + 1
        white = self.player_colors.index('white') + 1
        for each_piece in self.piece_list_black:
            i = each_piece[1]
            j = each_piece[0]
            self.board_matrix[i][j][black] = each_piece[2]
            self.board_matrix[i][j][3] = self.piece_list_names[self.piece_list_black.index(each_piece)]
        for each_piece in self.piece_list_white:
            i = each_piece[1]
            j = each_piece[0]
            self.board_matrix[i][j][white] = each_piece[2]
            self.board_matrix[i][j][3] = self.piece_list_names[self.piece_list_white.index(each_piece)]

        # re place all the pieces
        combined_piece_list = self.piece_list_white + self.piece_list_black
        for each_piece in combined_piece_list:
            place_tile = (each_piece[0], each_piece[1])
            self.place_piece(each_piece[2], place_tile)
        # recolor
        self.color_piece_background(reset_piece_coloring=True)  #warning todo verify

        # destroy any promoted pieces
        if debugging: print "promoted_piece_tracker:\n\t", self.promoted_piece_tracker
        for each_piece in self.promoted_piece_tracker:
            each_piece.destroy()
        if debugging: print '\t', self.promoted_piece_tracker

        # reset captured piece display
        if debugging: print "captured_piece_display_objects:\n\t", self.captured_piece_display_objects
        for i in self.captured_piece_display_objects:
            #i.place_forget()
            #i.destroy()  # todo how to destroy
            self.board_border.delete(i)
        if debugging: print '\t', self.captured_piece_display_objects
        # todo raise NotImplementedError("self.place_piece(self.captured_piece_display_objects[-1], (4, 4))")
        #self.captured_piece_display_objects = [] todo del?

        # reset variables
        #self.board_matrix_clean_copy = deepcopy(self.board_matrix)  # todo review
        self.board_matrix_copy = deepcopy(self.board_matrix_clean_copy)  # todo review
        self.initialize_variable_dictionary = {
            "piece_info": None,
            "first_tile": None,
            "captured_pieces_info": [],
            "number_of_captured_pieces": {'white': 0, 'black': 0},  # used?


            "undo_flag": False,  # todo refactor out
            "undo_end_flag": False,  # todo refactor out? may be useful for controls
            "master_move_list": [],
            "redo_move_list": [],
            "player_in_check": (False, (None, None), None),
            "pre_move_test": None,
            "move_gave_check": False,
            "second_tile_contents": None,
            "piece_information_retainer": None,
            "captured_piece_display_objects": [],
            "control_panel_objects": {},
            "random_move_flag": False,  #
            "checkmate": False,
            #"control_panel_image_objects": {},
            #"control_panel_settings": {
            #    'mute': False,
            #    'suppress_debugging': False
            #},
            "promoted_piece_tracker": [],
            "mate_testing": False,
            "announce_flag": False,
            #"text_to_display_object": ["", None],
            "white_first_move": None,
            "black_first_move": None,
            "white_time": datetime.timedelta(microseconds=0),
            "black_time": datetime.timedelta(microseconds=0),
            "valid_tile_tuple": [],
            "clock_digits_removed": (0, -7),  # 0:hours; 2:minutes  ,  -5:100ms; -7:seconds
            "found_valid_move_flag": None,  # todo review for way to avoid using this flag
            "stop": False,
            "promotion_box_controls_information_store": None

        }
        for (name, value) in self.initialize_variable_dictionary.iteritems():
            setattr(self, name, value)

        self.text_box_update()
        self.white_clock.itemconfig(self.white_clock_text, text=self.white_time)
        self.black_clock.itemconfig(self.black_clock_text, text=self.black_time)

        self.cumulative_time_white = datetime.timedelta(microseconds=0)   # this is for performance
        self.cumulative_time_black = datetime.timedelta(microseconds=0)   # this is for performance
        self.time_of_last_move = None
        #self.clock_enabled = False


        '''
        self.piece_info = None
        self.first_tile = None
        self.captured_pieces_info = []
        self.number_of_captured_pieces = {'white': 0, 'black': 0}
        self.undo_flag = False
        ###############################################################
        self.master_move_list = []
        self.player_in_check = (False, (None, None), None)
        self.pre_move_test = None
        self.move_gave_check = False
        self.second_tile_contents = None
        self.piece_information_retainer = None
        #self.captured_piece_display_objects = []
        #self.control_panel_objects = {}  todo DO NOT RESET
        self.random_move_flag = False
        self.checkmate = False
        self.debug_x = 0
        self.debug_y = 0
        ##############################################################
        self.piece_info = None  # todo why not [none, none] or (none, none) ?
        self.first_tile = None
        self.captured_pieces_info = []
        self.number_of_captured_pieces = {'white': 0, 'black': 0}  # todo hacked using dictionary (inefficient) todo white, black (will break i think if i fix player bug)
        self.undo_flag = False
        self.undo_end_flag = False
        self.master_move_list = []
        self.redo_move_list = []
        self.player_in_check = (False, (None, None), None)  # todo the false is not necessary; can be implicit?
        self.pre_move_test = None
        self.move_gave_check = False
        self.second_tile_contents = None
        self.piece_information_retainer = None
        #todo review all of these and remove ones not used
        self.captured_piece_display_objects = []
        self.random_move_flag = False
        self.checkmate = False
        self.control_panel_settings = {
            'mute': False
        }
        self.promoted_piece_tracker = []  # todo rename?
        self.mate_testing = False
        '''
        ##############################################################

        #self.controls_event_handler(None, reset=True)  # currently useless

        # reset to white's move
        self.current_player = 0

        # todo
        try:
            self.quit_reset_container.place_forget()  # has to be above the variable/object reset?
        except AttributeError:
            print "ERROR (TRY FAILED): self.quit_reset_container.place_forget()"

        self.sound_handler('board reset')

        if debugging: print

    def exit_application(self, *args):
        root.destroy()
        #raise SystemExit

    # move up after sufficiently iterating sound
    # move this to chess_sound.py?
    def sound_handler(self, called_sound_key, rename_flag=False):
        """

        Args:
            called_sound_key:
            rename_flag:

        Returns:

        """
        # todo when multiple same sounds are queued, ignore them

        # todo redo isn't used, not sure about undo; redo uses move_piece

        # from large_lists import sound_dictionary
        # seems winsounds is better because my program is a little laggy and winsound bypasses it making calls directly from winsound to my os???

        # todo interrupts

        # todo acceptable?
        if self.mate_testing:
            return

        # find sound path of file
        if called_sound_key in sound_dictionary:
            selected_sound = sound_dictionary[called_sound_key]
        else:
            print "\nERROR: Sound not found!\n"
            selected_sound = 'null'

        # mute functionality  # refactor this test D:
        c_1 = disabled_sounds_debugging
        c_2 = self.control_panel_settings['mute']
        c_3 = self.control_panel_settings['inspection_mute']
        if c_1 or c_2 or c_3:
            c_4 = called_sound_key == 'draw'
            c_5 = called_sound_key == 'checkmate'
            c_6 = called_sound_key == 'stalemate'
            c_7 = called_sound_key == 'muted' or called_sound_key == 'unmuted'
            if c_4 or c_5 or c_6 or c_7:
                pass
            else:
                return

        # todo change undo_flag to the mute
        # todo consider pickle test consolidation?
        if not self.undo_flag:  #warning todo refactor this logic into the undo function
            c_1 = rename_flag
            c_2 = self.announce_flag
            c_3 = not self.control_panel_settings['inspection_mute']  # todo review: and not working
            if c_1 and c_2 and c_3:  # second_tile
                # todo castle, promotion?,
                # piece name
                piece_name = 'sounds/google_mp3_converted/' + self.piece_info[1] + '.wav'
                if self.pickled_audio_processor(piece_name):
                    chess_sound.thread_queue.put(piece_name)

                # convert and play board tile
                #second_tile = self.selected_tile
                second_tile = self.master_move_list[-1][1]  # self.second_tile
                letter = chr(ord('A') + second_tile[0])
                number = str(8 - second_tile[1])
                tile_l_n = 'sounds/google_mp3_converted/' + letter + number + '.wav'

                if self.pickled_audio_processor(tile_l_n):
                    chess_sound.thread_queue.put(tile_l_n)

            else:
                if self.pickled_audio_processor(selected_sound):
                    chess_sound.thread_queue.put(selected_sound)

                # player color
                #player_color = 'sounds/google_mp3_converted/' + self.player_colors[self.current_player] + '.wav'
                #chess_sound.thread_queue.put(player_color)
                # piece name
                #piece_name = 'sounds/google_mp3_converted/' + self.piece_info[1] + '.wav'
                #chess_sound.thread_queue.put(piece_name)

        elif self.undo_flag:
            if self.pickled_audio_processor(selected_sound):
                chess_sound.thread_queue.put(selected_sound)

        return

    def pickled_audio_processor(self, queued_sound):
        """

        Args:
            queued_sound:

        Returns: true if the sound is not already in the queue.

        """

        print "PICKLE ALERT:"
        queue_list = pickle.load(open("save.p", "rb"))
        print "\t\t\t\tpickle_1", queue_list
        if queued_sound not in queue_list:
            # Save a dictionary into a pickle file.
            # import pickle
            # favorite_color = {"lion": "yellow", "kitty": "red"}
            # pickle.dump(favorite_color, open("save.p", "wb"))
            queue_list.insert(0, queued_sound)
            pickle.dump(queue_list, open("save.p", "wb"))
            print "\t\t\t\tsaving pickle"
            print "\t\t\t\tpickle_2", queue_list
            return True
        return False

    def keyword_toggler(self, **keyword_parameters):  # todo rename to toggler

        if 'mute' in keyword_parameters:
            # todo find fix to avoid useless keyword_parameters
            # not all sound; for debugging sanity
            if self.control_panel_settings['mute']:
                self.control_panel_settings['mute'] = False
                self.sound_handler('unmuted')
                print "Sound un-muted!"
            elif not self.control_panel_settings['mute']:
                self.control_panel_settings['mute'] = True
                self.sound_handler('muted')
                print "Sound (mostly) muted!"
            return

        if 'announce' in keyword_parameters:
            if not self.announce_flag:
                self.announce_flag = True
                self.sound_handler('move announcement')
                self.sound_handler('enabled')
                print "Announcer muted!"
            elif self.announce_flag:
                self.announce_flag = False
                self.sound_handler('move announcement')
                self.sound_handler('disabled')
                print "Announcer un-muted!"
            return

        if 'timer' in keyword_parameters:  #warning todo consistency between timer vs clock (switching to timer)
            new_game = False
            if len(self.master_move_list) == 0:
                new_game = True
            if not self.timer_enabled:
                if new_game:
                    self.timer_enabled = True
                    self.white_clock.itemconfig(self.white_clock_text, text="0:00:00")
                    self.black_clock.itemconfig(self.black_clock_text, text="0:00:00")
                    self.sound_handler('timer enabled')
                    print "Clock enabled..."
                    self.redo_move_list = []  # reset redo moves
                else:
                    self.sound_handler('timer: in progress')
                    return
            else:
                if not new_game:
                    self.cumulative_time_white = datetime.timedelta(microseconds=0)  # this is for performance
                    self.cumulative_time_black = datetime.timedelta(microseconds=0)  # this is for performance
                    self.time_of_last_move = None
                    self.white_first_move = None
                    self.black_first_move = None
                self.timer_enabled = False
                # notify user
                self.sound_handler('timer disabled')
                print "Clock not enabled..."
            return

    def initialize_promotion_box(self):
        # todo consider re-using the backdrop for other notifications (the fixed size is problematic)
        bc_w = self.bc_w
        bc_h = self.bc_h
        cb_w = self.cb_w
        cb_h = self.cb_h
        v_spacer = self.v_spacer
        nb_w = 350
        nb_h = 100
        change_me_rename = '#cfbfa7'

        self.notification_backdrop = Canvas(self.master, width=nb_w, height=nb_h)
        self.notification_backdrop.config(bg=change_me_rename, borderwidth=0, highlightthickness=0)
        #self.notification_backdrop.place(x=self.v_spacer/2, y=self.v_spacer/2, anchor='center')

        self.notification_container = Canvas(self.master, width=nb_w, height=nb_h)
        self.notification_container.config(bg=change_me_rename, borderwidth=0, highlightthickness=0)
        #self.notification_container.place(x=self.v_spacer/2, y=self.v_spacer/2, anchor='center')

        # dictionaries order uses hashes
        # queen, knight, rook, bishop (order of most picked: https://en.wikipedia.org/wiki/Promotion_(chess))
        self.promotion_object_lookup = [0, 0, 0, 0, 0, 0, 0, 0]

        self.promotion_object_lookup_names = ('white_queen', 'white_knight', 'white_rook', 'white_bishop', 'black_queen', 'black_knight', 'black_rook', 'black_bishop')

        self.notification_box_buttons = {'button_one': 0, 'button_two': 0, 'button_three': 0, 'button_four': 0}

        for each_key in self.promotion_object_lookup_names:
            i = self.promotion_object_lookup_names.index(each_key)
            self.promotion_object_lookup[i] = Canvas(self.notification_container, width=self.piece_size, height=self.piece_size)
            self.promotion_object_lookup[i].config(bg=change_me_rename, borderwidth=0, highlightthickness=0)
            self.promotion_object_lookup[i].create_image(self.piece_size/2, self.piece_size/2, image=self.piece_object_lookup[each_key])
            self.promotion_object_lookup[i].bind('<Button-1>', self.promotion_box_controls)

    def promotion_box_display(self, second_tile):
        current_player = self.current_player

        self.notification_backdrop.place(x=self.v_spacer/2, y=self.v_spacer/2, anchor='center')
        self.notification_container.place(x=self.v_spacer/2, y=self.v_spacer/2, anchor='center')

        self.notification_container.grab_set()

        if self.player_colors[current_player] == 'white':
            for i in range(0, 4):
                self.promotion_object_lookup[i].pack(side='left', padx=10)
        else:  # if self.player_colors[current_player] == 'black'
            for i in range(4, 8):
                self.promotion_object_lookup[i].pack(side='left', padx=10)

        if self.promotion_box_controls_information_store == None:
            self.promotion_box_controls_information_store = deepcopy(second_tile)
        else:
            raise ValueError("this should be None... fix")

    def promotion_box_controls(self, event, **keyword_parameters):

        self.alternate_players()  #warning todo

        current_player = self.current_player  #warning todo this will not change when alternate players is called
        opposite_player = abs(current_player - 1)

        bt_s = self.board_tile_size

        #warnint TODO refactor later
        #self.selected_tile = self.second_tile

        second_tile = self.promotion_box_controls_information_store

        # forget piece being promoted

        print "self.board_matrix[second_tile[1]][second_tile[0]]:", self.board_matrix[second_tile[1]][second_tile[0]]
        print "second_tile:", second_tile
        self.board_matrix[second_tile[1]][second_tile[0]][current_player + 1].place_forget()
        # preserve background
        background = self.board_matrix[second_tile[1]][second_tile[0]][current_player + 1].cget("bg")

        # creating and storing piece
        if event is not None:
            index = self.promotion_object_lookup.index(event.widget)
        elif 'index' in keyword_parameters:
            index = keyword_parameters['index']
        promoted_piece = self.create_piece(self.promotion_object_lookup_names[index])  #warning todo name piece/pieces
        self.promoted_piece_tracker.append(promoted_piece)

        # updating board matrix
        self.board_matrix[second_tile[1]][second_tile[0]][self.current_player + 1] = promoted_piece
        x_position = second_tile[0]
        y_position = second_tile[1]
        x = self.chess_board_position_x - self.piece_size/2 + bt_s/2 + bt_s*x_position
        y = self.chess_board_position_y - self.piece_size/2 + bt_s/2 + bt_s*y_position
        self.board_matrix[second_tile[1]][second_tile[0]][3] = self.promotion_object_lookup_names[index][6:]
        self.board_matrix[second_tile[1]][second_tile[0]][self.current_player + 1].config(bg=background)
        self.board_matrix[second_tile[1]][second_tile[0]][self.current_player + 1].place(x=x, y=y)

        self.alternate_players()  # warning todo
        current_player = self.current_player

        # inspecting board to determine if that move "gave check" (to the other player)
        #warning todo seems hacky
        # could call in_check for the appropriate player rather than this manual check
        gave_check = False
        for i in range(8):
            for j in range(8):
                if self.board_matrix[i][j][3] == 'king' and self.board_matrix[i][j][current_player+1] != 0:
                    if self.in_check((j, i), self.player_colors[current_player]):
                        gave_check = True
        if gave_check:
            print "Gave check on promotion... inspecting for checkmate..."
            self.move_gave_check = True
            self.state_inspection()

        # return to game
        for i in range(len(self.promotion_object_lookup)):
            self.promotion_object_lookup[i].pack_forget()
        self.notification_backdrop.place_forget()
        self.notification_container.place_forget()
        self.piece_information_retainer = None

        self.notification_container.grab_release()
        self.promotion_box_controls_information_store = None

    def create_piece(self, piece_name):
        # todo REFACTOR: combine with piece_placement_and_binding
        piece = Canvas(self.board_border, width=self.piece_size, height=self.piece_size)
        piece.config(bg='blue', borderwidth=0, highlightthickness=0)  #warning TODO change bg
        piece.create_image(self.piece_size/2, self.piece_size/2, image=self.piece_object_lookup[piece_name])
        piece.bind('<Button-1>', self.board_event_handler)
        piece.bind('<ButtonRelease-1>', self.board_event_handler)
        return piece

    def color_piece_background(self, reset_board_tile_coloring=False, reset_piece_coloring=False, **kwargs):
        """

        Args:
            reset_board_tile_coloring:
            reset_piece_coloring:
            **kwargs:
                piece: (x, y) of piece to color\n
                board_tile: (x, y) of board tile to color

        Returns:

        """

        # todo refactor maybe. this implementation, although completely functional, does not feel clean

        # colors background of board tiles
        if reset_board_tile_coloring:
            for i in range(8):
                for j in range(8):
                    k = 0
                    if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                        self.board_matrix[i][j][k].config(bg=self.black_tile)
                    else:
                        self.board_matrix[i][j][k].config(bg=self.white_tile)

        # colors background of every piece (no canvas transparency hack)
        if reset_piece_coloring:
            black = self.player_colors.index('black') + 1
            white = self.player_colors.index('white') + 1
            for i in range(8):
                if i < 2 or i > 5:
                    if i < 2:
                        k = black
                    else:  # if i > 5
                        k = white
                    for j in range(8):
                        if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                            self.board_matrix[i][j][k].config(bg=self.black_tile)
                        else:
                            self.board_matrix[i][j][k].config(bg=self.white_tile)

        # colors background of one piece or one board tile (no canvas transparency hack)
        elif 'piece' in kwargs or 'board_tile' in kwargs:  # todo review
            if 'piece' in kwargs:
                i = kwargs['piece'][1]
                j = kwargs['piece'][0]
                k = self.current_player + 1
            elif 'board_tile' in kwargs:
                i = kwargs['board_tile'][1]
                j = kwargs['board_tile'][0]
                k = 0
            if ((i+1) % 2 == 0 and (j+1) % 2 != 0) or (i % 2 == 0 and (j+1) % 2 == 0):
                self.board_matrix[i][j][k].config(bg=self.black_tile)
            else:
                self.board_matrix[i][j][k].config(bg=self.white_tile)

    def helper_king_inspection(self):
        # raise error on king capture
        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        found_one_king = False
        found_two_king = False
        for i in range(8):
            for j in range(8):
                if self.board_matrix[i][j][current_player + 1] != 0 and self.board_matrix[i][j][3] == 'king':
                    found_one_king = True
                if self.board_matrix[i][j][opposite_player + 1] != 0 and self.board_matrix[i][j][3] == 'king':
                    found_two_king = True
        if not found_one_king or not found_two_king:
            if not found_one_king:
                print "Current player's king not found..."
            else:
                print "Other player's king not found..."
            raise Exception("KING DOWN")

    def old_random_move(self, *args):

        self.helper_king_inspection()

        # use random to pick piece, then randomly pick from the possible moves #
        # observe as a way of debugging
        # monitor moves by looking at current_player

        print "RANDOMS:"
        self.control_panel_settings['mute'] = True
        self.control_panel_settings['suppress_debugging'] = True

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        piece_list_with_XY = []  # (board_matrix, tile)
        for i in range(8):
            for j in range(8):
                if self.board_matrix[i][j][3] != 0:  # piece names
                    if self.board_matrix[i][j][self.current_player + 1] != 0:  # correct player
                        piece_list_with_XY.append(((self.board_matrix[i][j]), (j, i)))

        found_valid_move = False
        while not found_valid_move and len(piece_list_with_XY) > 0:

            randomly_selected_piece = random.choice(piece_list_with_XY)
            del piece_list_with_XY[piece_list_with_XY.index(randomly_selected_piece)]
            self.first_tile = first_tile = (randomly_selected_piece[1][0], randomly_selected_piece[1][1])  # todo review
            print "\tFirst tile:", self.first_tile, randomly_selected_piece[0][3]

            valid_moves = []
            for i in range(8):
                for j in range(8):
                    # either an empty tile or enemy piece
                    if self.board_matrix[i][j][3] == 0 or self.board_matrix[i][j][opposite_player + 1] != 0:
                        second_tile = (j, i)
                        #print "\tSecond_tile:", second_tile
                        first_tile = (randomly_selected_piece[1][0], randomly_selected_piece[1][1])
                        self.first_tile_information_store(first_tile, inspection=True)  # todo does not require inspection because the inspection is not occurring within a move
                        if self.rule_and_state_inspections(second_tile):
                            print "\tSecond_tile:", second_tile
                            valid_moves.append((j, i))

            self.helper_king_inspection()

            print "\tValid moves:", valid_moves
            if valid_moves != []:
                found_valid_move = True
                randomly_selected_move = random.choice(valid_moves)
                second_tile = randomly_selected_move
                first_tile = (randomly_selected_piece[1][0], randomly_selected_piece[1][1])

                self.first_tile_information_store(first_tile, inspection=True)

                # color tiles --------------------------------------------------------------------------------------
                valid_move_list, valid_capture_list = self.get_valid_moves(first_tile)
                self.valid_tile_tuple = valid_move_list + valid_capture_list
                print "self.valid_tile_tuple", self.valid_tile_tuple
                for each_valid_move in valid_move_list:
                    self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#008000',
                                                                                        highlightthickness=1)
                for each_valid_move in valid_capture_list:
                    self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#800000',
                                                                                        highlightthickness=1)
                root.update()
                sleep(1*debug_sleep_ratio)
                # color tiles --------------------------------------------------------------------------------------

                self.rule_and_state_inspections(second_tile, user_input=True)

                self.helper_king_inspection()


                if self.piece_information_retainer is not None:  # todo find better check?
                    #raise Exception
                    sleep(1*debug_sleep_ratio)  #warning todo not verified to not cause problems
                    if self.player_colors[current_player] == 'white':
                        promotion_select = [0, 1, 2, 3]
                    else:  # if self.player_colors[current_player] == 'black'
                        promotion_select = [4, 5, 6, 7]
                    promotion_piece_index = random.choice(promotion_select)
                    self.promotion_box_controls(event=None, index=promotion_piece_index)
                    root.update()  # todo review (necessary?)
                    sleep(1*debug_sleep_ratio)  #warning todo not verified to not cause problems

                self.helper_king_inspection()

        self.control_panel_settings['mute'] = False
        self.control_panel_settings['suppress_debugging'] = False

        #warning todo handle stalemate
        if not found_valid_move:
            if self.checkmate:
                raise Exception
                #self.checkmate = True
                #self.sound_handler('checkmate')
                self.game_over('checkmate')
            if not self.checkmate:
                raise Exception
                #self.sound_handler('stalemate')
                self.game_over('stalemate')

    def random_move(self, *args):

        self.helper_king_inspection()

        # use random to pick piece, then randomly pick from the possible moves #
        # observe as a way of debugging
        # monitor moves by looking at current_player

        print "RANDOMS:"
        self.control_panel_settings['inspection_mute'] = True
        self.control_panel_settings['suppress_debugging'] = True

        current_player = self.current_player
        opposite_player = abs(current_player - 1)

        piece_list = self.get_player_piece_list(self.player_colors[current_player])  # (tile, board_matrix) # todo switch below

        found_valid_move = False  # todo review
        while not found_valid_move and len(piece_list) > 0:

            randomly_selected_piece = random.choice(piece_list)
            del piece_list[piece_list.index(randomly_selected_piece)]
            self.first_tile = first_tile = (randomly_selected_piece[0][0], randomly_selected_piece[0][1])  # todo review
            #warning todo avoid using globals
            print "\tFirst tile:", self.first_tile, randomly_selected_piece[1][3]

            valid_moves = self.get_valid_moves(first_tile, combined_list=True)

            #self.helper_king_inspection()  #todo remove

            print "\tValid moves:", valid_moves
            if valid_moves:  # empty lists are False, all others are True (stack overflow)
                found_valid_move = True
                randomly_selected_move = random.choice(valid_moves)
                second_tile = randomly_selected_move
                first_tile = (randomly_selected_piece[0][0], randomly_selected_piece[0][1])

                self.first_tile_information_store(first_tile, inspection=True)

                # color tiles --------------------------------------------------------------------------------------
                valid_move_list, valid_capture_list = self.get_valid_moves(first_tile, combined_list=False)
                self.valid_tile_tuple = valid_move_list + valid_capture_list
                print "self.valid_tile_tuple", self.valid_tile_tuple
                for each_valid_move in valid_move_list:
                    self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#008000',
                                                                                        highlightthickness=1)
                for each_valid_move in valid_capture_list:
                    self.board_matrix[each_valid_move[1]][each_valid_move[0]][0].config(bg='#800000',
                                                                                        highlightthickness=1)
                root.update()
                sleep(1 * debug_sleep_ratio)
                # color tiles --------------------------------------------------------------------------------------

                self.rule_and_state_inspections(second_tile, user_input=True)

                #self.helper_king_inspection()  #todo remove

                #if self.piece_information_retainer is not None:  # todo find better check?
                if self.promotion_box_controls_information_store is not None:  # todo test
                    # raise Exception
                    sleep(1 * debug_sleep_ratio)  # warning todo not verified to not cause problems
                    if self.player_colors[current_player] == 'white':
                        promotion_select = [0, 1, 2, 3]
                    else:  # if self.player_colors[current_player] == 'black'
                        promotion_select = [4, 5, 6, 7]
                    promotion_piece_index = random.choice(promotion_select)
                    self.promotion_box_controls(event=None, index=promotion_piece_index)
                    root.update()  # todo review (necessary?)
                    sleep(1 * debug_sleep_ratio)  # warning todo not verified to not cause problems

                #self.helper_king_inspection()  #todo remove

        self.control_panel_settings['inspection_mute'] = False
        self.control_panel_settings['suppress_debugging'] = False

        #warning todo how is this necessary? wouldn't this be caught before this move (at the end of the last move?)
        if not found_valid_move:
            # find king
            for i in range(8):
                for j in range(8):
                    if self.board_matrix[i][j][current_player + 1] != 0 and self.board_matrix[i][j][3] == 'king':
                        king_tile = (j, i)
            if self.in_check(king_tile, self.player_colors[self.current_player]):
                # raise Exception
                print "\nCHECKMATE FROM RANDOM MOVE\n"
                self.game_over('checkmate')
            else:  # not in check
                # raise Exception
                print "\nSTALEMATE FROM RANDOM MOVE\n"
                self.game_over('stalemate')

    # move up
    # helper function
    def get_player_piece_list(self, player_color):
        """

        Args:
            player_color:

        Returns: list of objects: (tile location, board_matrix object)

        """
        if player_color == 'white':
            player_offset = 0
        elif player_color == 'black':
            player_offset = 1
        elif player_color == 'both':
            raise NotImplementedError
        else:
            raise Exception("player_color not provided")

        piece_list = []  # (board_matrix, tile)
        for i in range(8):
            for j in range(8):
                if self.board_matrix[i][j][3] != 0:  # piece names
                    if self.board_matrix[i][j][player_offset + 1] != 0:  # correct player
                        piece_list.append(((j, i), self.board_matrix[i][j]))
        return piece_list



    #warning todo check inspection? isn't this covered in rule_and_state_inspections?
    # todo use this in other functions and generalize it? YES
    # move up
    # helper function
    def get_valid_moves(self, first_tile, combined_list=False):
        """

        Args:
            first_tile:
            combined_list: toggles a combined list

        Returns: either a combined list or a tuple separated into moves and captures

        """

        verbose = False
        #warning TODO sigh... does not handle en passant
            # mostly visual: it correctly identifies the move, but will not correctly identify the move as a capture
            # if valid_capture_list is ever used, it will cause more than visual bugs
        # todo performance: (every move) -> getPieceInfo -> drop piece info to do other things -> getPieceInfo

        # mute sound without changing mute settings
        inspection_mute_flag = False
        if not self.control_panel_settings['inspection_mute']:
            self.control_panel_settings['inspection_mute'] = True
            inspection_mute_flag = True
        # todo suppress text here and remove verbose?

        # retain current first_tile_information_store
        retain_first_tile = deepcopy(first_tile)  # todo review if necessary (warning for high performance penalty); can use the function's first_tile

        current_player = self.current_player
        opposite_player = abs(current_player - 1)
        valid_move_list = []
        valid_capture_list = []

        # piece rule and state inspection
        for i in range(8):
            for j in range(8):
                # either an empty tile or enemy piece
                #warning TODO does not handle en passant correctly (returns it as a move not a capture)
                if self.board_matrix[i][j][3] == 0:
                    second_tile = (j, i)
                    self.first_tile_information_store(first_tile, inspection=True)
                    if self.rule_and_state_inspections(second_tile, inspection=True):
                        if verbose: print "\tValid move at (XY):", (j, i)
                        valid_move_list.append(second_tile)
                #warning TODO does not handle en passant correctly (returns it as a move not a capture)
                elif self.board_matrix[i][j][opposite_player + 1] != 0:
                    second_tile = (j, i)
                    self.first_tile_information_store(first_tile, inspection=True)
                    if self.rule_and_state_inspections(second_tile, inspection=True):
                        if verbose: print "\tValid capture at (XY):", (j, i)
                        valid_capture_list.append(second_tile)

        converted_notation_list = []
        for each_valid_move in valid_move_list:
            converted_notation_list.append(self.xy_to_notation(each_valid_move))
        print converted_notation_list
        converted_notation_list = []
        for each_valid_move in valid_capture_list:
            converted_notation_list.append(self.xy_to_notation(each_valid_move))
        print converted_notation_list

        #warning todo check inspection?
        # todo checkmate?

        # restore piece information todo fix for performance

        self.first_tile_information_store(retain_first_tile)

        if inspection_mute_flag:
            # warning todo this is resetting other settings elsewhere (this may be adequately controllable from elsewhere)
            self.control_panel_settings['inspection_mute'] = False

        if combined_list:
            combined_move_list = valid_move_list + valid_capture_list
            return combined_move_list
        else:
            return valid_move_list, valid_capture_list


    def random_move_game(self, *args):
        # todo review correct usage of self.stop
        #warning TODO set focus on only stop button

        #canvas_object = self.control_panel_objects['random_move_button']
        #canvas_text_object = self.control_panel_objects['random_move_button_text']
        #canvas_object.itemconfig(canvas_text_object, text='STOP')

        self.focus_grabber.grab_set()
        self.control_panel_settings['inspection_mute'] = True  # todo consolidate the different mute methods
        while not self.checkmate and not self.stop:
            self.random_move()
            root.update()
            sleep(.5*debug_sleep_ratio)
        #canvas_object.itemconfig(canvas_text_object, text='Rand(Move)')
        if self.game_is_over:
            #self.game_over()
            self.checkmate = False
            self.stop = False
            if debugging_endless_loop:
                self.reset_board()
        self.control_panel_settings['inspection_mute'] = False  # todo review/move
        self.focus_grabber.grab_release()
        #self.stop = False
        # no way to break out of loop (other than closing application/stopping execution) todo infinite loop
        if debugging_endless_loop and not self.stop:
            root.after(1000, self.random_move_game())

    def color_tone(self, color, tone_percent, lighter_or_darker):
        """

        Args:
            color:
            tone_percent:
            lighter_or_darker:

        Returns:

        """
        # todo error handling
        if helper_debugging == True:
            h_d = True
        else:
            h_d = False

        if lighter_or_darker == 'lighter':
            lightness = 1
        if lighter_or_darker == 'darker':
            lightness = -1

        if h_d: print color
        if color[0] == '#':
            color = color[1:]

        # deconstruct hex
        red = color[:2]
        green = color[2:4]
        blue = color[4:6]
        hex_colors = [red, green, blue]
        if h_d: print hex_colors

        # convert to numerical
        numerical_colors = []
        for each_color in hex_colors:
            numerical_colors.append(int(each_color, base=16))
        if h_d: print numerical_colors

        # modify
        darkened_colors = []
        for each_color in numerical_colors:
            each_color += int((255 - each_color)*tone_percent*lightness)
            darkened_colors.append(each_color)
        if h_d: print darkened_colors

        # convert to hex
        hex_colors = []
        for each_color in darkened_colors:
            hex_colors.append(hex(each_color)[2:])
        if h_d: print hex_colors

        # reconstruct
        darkened_hex_value = "#" + hex_colors[0] + hex_colors[1] + hex_colors[2]
        if h_d: print darkened_hex_value, '\n'

        return darkened_hex_value

    def close_windows(self, event):
        # todo create all windows on application startup and then hide/place them? or keep using this way and create
        # windows on command (the performance seems to be negligible)?

        # todo if using this method, be sure to destroy everything associated with the window
        # currently any time a window needs to be used, it is created. then forgotten (rather than destroyed)
        # and new windows are then created
        if len(self.open_window_list) != 0:
            print "Escaping window..."
            self.open_window_list[0].place_forget()
            del self.open_window_list[0]
        else:
            print "No windows to escape..."



    def player_1_AI(self):
        #self.is_player_1_AI = True
        #print "AI"
        pass

        # disable player input

        # run ai

    @staticmethod
    def debugging_printer(to_print, *args, **kwargs):
        print to_print

    #@staticmethod
    def test_command(self, *args):
        """
        Testing the docstring in the test command!
        Args:
            *args: Args info here.

        Returns: Tested shit.

        Note: this is google's format.

        """
        print "test_command(*args):",
        for each in args:
            print each,
        print
        self.game_over('checkmate')

    def rename_debugging(self, event):

        #receiving_tile = [None, None]
        receiving_player_color = None
        # get object ID
        object_id_below_cursor = root.winfo_containing(event.x_root, event.y_root)
        # find i, j,
        for i in range(8):
            for j in range(8):
                for k in range(3):
                    if self.board_matrix[i][j][k] == object_id_below_cursor:
                        tile_below = (j, i)

        self.get_valid_moves(tile_below)

    def debugging_event_handler(self, event):
        # todo refactor

        if event.char == "t":
            #self.toggle_clock(event)
            self.keyword_toggler(timer=True)
            return
        if event.char == "o":
            self.stop = True
            return
        if event.char == "b":  # todo not working (have to refactor too much)
            if self.debugging_ui:
                self.debugging_ui = False
            else:
                self.debugging_ui = True
            root.update()
            return

        bt_s = self.board_tile_size
        piece_size = self.piece_size

        # get object ID
        object_id_below_cursor = root.winfo_containing(event.x_root, event.y_root)
        print '\t', "object_id_below_cursor:", object_id_below_cursor

        # find i, j,
        for i in range(8):
            for j in range(8):
                #for k in range(1,3):
                k = 0
                if self.board_matrix[i][j][k] == object_id_below_cursor:
                    tile = (j, i)

        piece_dictionary = {
            "1":    'pawn',
            "2":    'rook',
            "3":    'knight',
            "4":    'bishop',
            "5":    'queen',
            "6":    'king'
        }

        if event.char == "0":
            self.alternate_players()
        # clear board (including kings)
        elif event.char == "9":
            for i in range(8):
                for j in range(8):
                    for k in range(1, 3):
                        try:
                            self.board_matrix[i][j][k].place_forget()
                            self.board_matrix[i][j][k] = 0
                        except AttributeError:
                            self.board_matrix[i][j][k] = 0
                    self.board_matrix[i][j][3] = 0
        elif event.char == "m":
            self.control_panel_settings['mute'] = True
        elif event.char == "z":
            print "\n\n******* DEBUG OUTPUT *******"
            try:
                print "self.first_tile:\t", self.first_tile
                print "self.second_tile:\t", self.second_tile
                print "self.piece_info:\t", self.piece_info
                print "self.move_gave_check\t", self.move_gave_check
                print "self.cumulative_time_white\t", self.cumulative_time_white
                print "self.cumulative_time_black\t", self.cumulative_time_black
                print "self.board_matrix:"
                for each_row in self.board_matrix:
                    print each_row
                print "self.master_move_list:"
                for each_move in self.master_move_list:
                    print each_move
                print "self.redo_move_list:"
                for each_redo in self.redo_move_list:
                    print each_redo
            except AttributeError:
                print "AttributeError"

        elif event.char == "1" or event.char == "2" or event.char == "3" or event.char == "4" or event.char == "5" or event.char == "6":  # todo is using else for 1-6 acceptable? only bound numbers will be passed here...
            color = self.player_colors[self.current_player]
            piece_name = piece_dictionary[event.char]
            name_with_color = color + "_" + piece_name
            print piece_name
            piece_object = self.create_piece(name_with_color)
            x = self.chess_board_position_x - piece_size / 2 + bt_s / 2 + bt_s * tile[0]
            y = self.chess_board_position_y - piece_size / 2 + bt_s / 2 + bt_s * tile[1]
            piece_object.place(x=x, y=y)
            #update board
            self.board_matrix[tile[1]][tile[0]][self.current_player + 1] = piece_object
            self.board_matrix[tile[1]][tile[0]][3] = piece_name
            print


    def debugging(self):
        self.stop_random_move_game = False
        root.bind('<d>', self.delete_piece, "+")
        #root.bind('<m>', self.keyword_toggler, "+")  # todo verify
        root.bind('<m>', self.debugging_event_handler, "+")
        root.bind('<p>', self.random_move_game, "+")
        root.bind('<space>', self.random_move, "+")
        #root.bind('<o>', self.controls_event_handler, "+")
        root.bind('<o>', self.debugging_event_handler, "+")
        root.bind('<k>', self.controls_event_handler, "+")
        root.bind('<q>', self.debugging_remove_notification, "+")
        root.bind('<w>', self.rename_debugging, "+")
        for i in range(1, 7):
            root.bind(str(i), self.debugging_event_handler, "+")
        root.bind("0", self.debugging_event_handler, "+")
        root.bind("9", self.debugging_event_handler, "+")
        root.bind("z", self.debugging_event_handler, "+")
        root.bind("b", self.debugging_event_handler, "+")  # todo not working (have to refactor too much)
        root.bind("t", self.debugging_event_handler, "+")
        root.bind("/", self.debugging_event_handler, "+")


        receiving_tile = [None, None]
        receiving_player = 'white'
        root.bind('<c>', lambda event: self.in_check(receiving_tile, receiving_player, event=event, detailed=True))  # TODO LEARNING: UNDERSTAND THIS
        root.bind('<v>', lambda event: self.no_valid_moves())

        # Should not bind to root? http://stackoverflow.com/questions/7299955/tkinter-binding-a-function-with-arguments-to-a-widget/7301218#7301218
        # bind_all(sequence=None, func=None, add=None)
        # Adds an event binding to the application level. Usually, the new binding replaces any existing binding for the same event sequence. By passing in "+" as the third argument, the new function is added to the existing binding.

    def delete_piece(self, event):
        self.sound_handler('delete piece')
        print "BUGGY DEBUGGING:"

        # get object ID
        object_id_below_cursor = root.winfo_containing(event.x_root, event.y_root)
        print '\t', "object_id_below_cursor:", object_id_below_cursor

        # find i, j,
        for i in range(8):
            for j in range(8):
                for k in range(1,3):
                    if self.board_matrix[i][j][k] == object_id_below_cursor:

                        # copy information to captured pieces list
                        copy_captured_piece_info = []  # todo find a better name for "info"?
                        for ii in range(4):
                            copy_captured_piece_info.append(self.board_matrix[i][j][ii])
                        print "copy_captured_piece_info", copy_captured_piece_info
                        self.captured_pieces_info.append(copy_captured_piece_info)  # todo refactor to captured_pieces_tile?
                        print "captured_pieces_info", self.captured_pieces_info[-1]

                        # destroy piece
                        self.board_matrix[i][j][k].place_forget()  # destroy()
                        print '\t', "board_matrix[i][j][k] == object_id_below_cursor"
                        print '\t', "pre clean: board_matrix[i][j]:", self.board_matrix[i][j]
                        # clear previous entry
                        for m in range(1, 4):
                            self.board_matrix[i][j][m] = 0
                        print '\t', "post clean: board_matrix[i][j]:", self.board_matrix[i][j]
        self.captured_piece_display()

    def debugging_toggles(self, *event):
        if not self.stop_random_move_game:
            self.stop_random_move_game = True
        if self.stop_random_move_game:
            self.stop_random_move_game = False

    def debugging_remove_notification(self, *event):
        self.quit_reset_container.place_forget()


    # UNUSED
    def undo_clock_update(self, white_moves=False, black_moves=False):
        """
        master_move_list_entry = [
        0 first_tile,                     # first tile
        1 second_tile,                    # second tile
        2 piece_object,                   # piece object
        3 piece_name,                     # piece name
        4 enemy_piece_object,             # enemy captured object
        5 enemy_tile,                     # enemy tile (defaults to second_tile)
        6 castle_info,                    # O-O and O-O-O: using letter O notation (algebraic uses zero "0")
                                          # castle_info also contains the rook object #todo (nested?)
        7 time_taken,                     # time taken for move
        8 time_of_move                    # time the move occurred (UTC?)
        ]
        Args:
            white_moves:
            black_moves:

        Returns:

        """
        # todo flickering display on first move
        # todo only 1 zero for hours place
        # todo undo/redo

        c_l_d_r = self.clock_digits_removed

        if self.game_is_over:
            return

        current_time = datetime.datetime.utcnow()

        '''
        if white_moves:  # and not black_moves:
            # self.white_time = current_time - self.white_first_move - self.black_time  # updates white
            # updates white
            if len(self.master_move_list) >= 3:  # 2 + the current
                black_last_move_occurred = self.master_move_list[-2][8]  # -2 is the previous move
                white_move_time = current_time - black_last_move_occurred
            else:
                white_move_time = current_time - current_time
            self.master_move_list[-1][7] = white_move_time
            self.cumulative_time_white += white_move_time
        elif black_moves:  # and not white_moves:
            # self.black_time = current_time - self.white_first_move - self.white_time  # updates black
            # updates black
            if len(self.master_move_list) >= 2:  # 2 + the current
                white_last_move_occurred = self.master_move_list[-2][8]
                black_move_time = current_time - white_last_move_occurred
            else:
                black_move_time = current_time - current_time
            self.master_move_list[-1][7] = black_move_time
            self.cumulative_time_black += black_move_time
        if white_moves or black_moves:
            self.master_move_list[-1][8] = current_time
        '''

        # todo remove (debugging)
        '''
        if white_moves or black_moves:
            print self.master_move_list[-1][7]
            print self.master_move_list[-1][8]
            print self.cumulative_time_white
            print self.cumulative_time_black
        '''

        if white_moves:  # and not black_moves:
            # self.white_time = current_time - self.white_first_move - self.black_time  # updates white
            # updates white
            if len(self.master_move_list) >= 3:  # 2 + the current
                black_last_move_occurred = self.master_move_list[-2][8]  # -2 is the previous move
                white_move_time = current_time - black_last_move_occurred
            else:
                white_move_time = current_time - current_time
            self.master_move_list[-1][7] = white_move_time
            #self.cumulative_time_white += white_move_time
        elif black_moves:  # and not white_moves:
            # self.black_time = current_time - self.white_first_move - self.white_time  # updates black
            # updates black
            if len(self.master_move_list) >= 2:  # 2 + the current
                white_last_move_occurred = self.master_move_list[-2][8]
                black_move_time = current_time - white_last_move_occurred
            else:
                black_move_time = current_time - current_time
            self.master_move_list[-1][7] = black_move_time
            #self.cumulative_time_black += black_move_time
        if white_moves or black_moves:
            self.master_move_list[-1][8] = current_time

        # EZ PZ (poor performance)
        if white_moves or black_moves:  # todo separate for performance
            self.cumulative_time_white = datetime.timedelta(microseconds=0)
            self.cumulative_time_black = datetime.timedelta(microseconds=0)
            if len(self.master_move_list) > 0:
                i = 0
                for each_move in self.master_move_list:
                    if (i + 2) % 2 == 0:  # todo the +2
                        self.cumulative_time_white += each_move[7]
                    else:
                        self.cumulative_time_black += each_move[7]
                    i += 1

        # todo review: intentionally keeping time ticking from other players last move

        if self.white_first_move is not None:
            #total_time = current_time - self.white_first_move
            if len(self.master_move_list) > 0:
                last_move_occurred = self.master_move_list[-1][8]
            else:
                last_move_occurred = current_time
            if self.player_colors[self.current_player] == 'white':
                #display_time_white = total_time - self.black_time
                #black_last_move_occurred = last_move_occurred
                #display_time_white = current_time - black_last_move_occurred + self.cumulative_time_white
                #self.white_clock.itemconfig(self.white_clock_text, text=str(display_time_white)[c_l_d_r[0]:c_l_d_r[1]])

                #print current_time, last_move_occurred, self.cumulative_time_white

                time_white = current_time - last_move_occurred + self.cumulative_time_white
                self.white_clock.itemconfig(self.white_clock_text, text=str(time_white)[c_l_d_r[0]:c_l_d_r[1]])
                #self.black_clock.itemconfig(self.black_clock_text, text=str(self.cumulative_time_black)[c_l_d_r[0]:c_l_d_r[1]])

            else:  # if self.player_colors[self.current_player] == 'black'
                #display_time_black = total_time - self.white_time
                #white_last_move_occurred = last_move_occurred
                #display_time_black = current_time - white_last_move_occurred + self.cumulative_time_black
                #self.black_clock.itemconfig(self.black_clock_text, text=str(display_time_black)[c_l_d_r[0]:c_l_d_r[1]])

                #print current_time, last_move_occurred, self.cumulative_time_black

                time_black = current_time - last_move_occurred + self.cumulative_time_black
                self.black_clock.itemconfig(self.black_clock_text, text=str(time_black)[c_l_d_r[0]:c_l_d_r[1]])
                #if self.cumulative_time_white == 0: don't use c_l_d_r
                #self.white_clock.itemconfig(self.white_clock_text, text=str(self.cumulative_time_white)[c_l_d_r[0]:c_l_d_r[1]])


        if not white_moves and not black_moves:
            root.after(100, self.clock_update)



# http://stackoverflow.com/a/36456550/6666148
if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

root = Tk()
debugging = True
features = False

debugging_valid_move = False
debugging_ui = False

debugging_check = False
debugging_manual = False

debugging_endless_loop = False

sound_delay_hacks = False
disabled_sounds_debugging = False

helper_debugging = False
debug_sleep_ratio = .01



# initialize a cleaned pickle
queue_list = []  # todo make self.?
pickle.dump(queue_list, open("save.p", "wb"))
print "PICKLE ALERT:"
print "\t\t\t\tpickle_0", queue_list


'''
image = pyglet.image.load('cursor.png')
cursor = pyglet.window.ImageMouseCursor(image, 16, 8)
window.set_mouse_cursor(cursor)

#window = pyglet.window.Window()
#window.set_mouse_visible(False)
'''

chess = ChessGUI(root)

#cProfile.runctx("ChessGUI(root)", globals(), locals())
#chess.player_1_AI()
#root.overrideredirect(1)

root.mainloop()
#cProfile.runctx("root.mainloop()", globals(), locals())

# stack overflow
'''
# import tempfile
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64

_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)
'''


'''
sd.default.samplerate = 44100

time = 2.0
frequency = 440

# Generate time of samples between 0 and two seconds
samples = np.arange(44100 * time) / 44100.0
# Recall that a sinusoidal wave of frequency f has formula w(t) = A*sin(2*pi*f*t)
wave = 10000 * np.sin(2 * np.pi * frequency * samples)
# Convert it to wav format (16 bits)
wav_wave = np.array(wave, dtype=np.int16)

sd.play(wav_wave, blocking=True)
'''

'''
#define stream chunk
chunk = 1024

#open a wav format music
f = wave.open(sound_dictionary[sound_selector])
    #open(r"C:/users/admin/dropbox/chess/sounds/castle_while_checked.wav","rb")
#instantiate PyAudio
p = pyaudio.PyAudio()
#open stream
stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
                channels = f.getnchannels(),
                rate = f.getframerate(),
                output = True)
#read data
data = f.readframes(chunk)

#paly stream
while data != '':
    stream.write(data)
    data = f.readframes(chunk)

#stop stream
stream.stop_stream()
stream.close()

#close PyAudio
p.terminate()
return
'''

'''
# stalemate rework:
    # not in check, and any move will put in check
elif False:  # not self.move_gave_check
    if len(self.captured_pieces_info) == 30 or self.fast_no_valid_moves():
        self.checkmate_testing = False
        self.game_over('stalemate')
        return
else:
    if False: # self.stalemate_inspection():
        self.checkmate_testing = False
        self.game_over('stalemate')
        return
'''