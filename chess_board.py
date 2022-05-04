

class ChessBoard:

    def __init__(self, board_matrix):
        self.board_matrix = board_matrix
        self.piece_info = ()

    def piece_information(self, tile, ):
        print len(self.board_matrix[0][0])
        for i in range(len(self.board_matrix[0][0])):  # todo if used more than once assign this to a variable
            print self.board_matrix[tile[0]][tile[1]][i]

    def select_first_tile(self):
        self.piece_info = (piece_object, piece_name, first_tile)

    def rule_inspection(self):
        pass



    #TEXT TO SPEECH