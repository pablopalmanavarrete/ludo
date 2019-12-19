from entities.pawn import Pawn


class Player:
    def __init__(self, color):
        self.pawns = []
        self.color = color
        self.entry_board_cell = 0
        self.turn = False
        self.turn_position = 0

        if color == "green":
            self.init_green_pawn()
        elif color == "red":
            self.init_red_pawn()
        elif color == "yellow":
            self.init_yellow_pawn()
        else:
            self.init_blue_pawn()

    def init_green_pawn(self):
        self.entry_board_cell = 42
        self.turn_position = 0
        self.turn = True
        self.pawns.append(Pawn(1, self.color, 175, 125))
        self.pawns.append(Pawn(2, self.color, 125, 175))
        self.pawns.append(Pawn(3, self.color, 225, 175))
        self.pawns.append(Pawn(4, self.color, 175, 225))

    def init_red_pawn(self):
        self.entry_board_cell = 3
        self.turn_position = 1
        self.pawns.append(Pawn(1, self.color, 625, 125))
        self.pawns.append(Pawn(2, self.color, 575, 175))
        self.pawns.append(Pawn(3, self.color, 675, 175))
        self.pawns.append(Pawn(4, self.color, 625, 225))

    def init_yellow_pawn(self):
        self.entry_board_cell = 29
        self.turn_position = 2
        self.pawns.append(Pawn(1, self.color, 175, 575))
        self.pawns.append(Pawn(2, self.color, 125, 625))
        self.pawns.append(Pawn(3, self.color, 225, 625))
        self.pawns.append(Pawn(4, self.color, 175, 675))

    def init_blue_pawn(self):
        self.entry_board_cell = 16
        self.turn_position = 3
        self.pawns.append(Pawn(1, self.color, 625, 575))
        self.pawns.append(Pawn(2, self.color, 575, 625))
        self.pawns.append(Pawn(3, self.color, 675, 625))
        self.pawns.append(Pawn(4, self.color, 625, 675))

    def set_turn_position(self, turn_position):
        self.turn_position = turn_position

    def get_turn_position(self):
        return self.turn_position

    def set_turn(self, turn):
        self.turn = turn
