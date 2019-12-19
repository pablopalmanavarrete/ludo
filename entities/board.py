from entities.cell import Cell
from entities.player import Player


class Board:
    def __init__(self):
        # Config
        self.last_cell = 51

        #Action Pawn
        self.pawn_in_movement = False
        self.dice_value = 0
        self.action_pawn = 0
        self.end_action = False

        # Active player
        self.players = []
        self.players.append(Player("green"))
        self.players.append(Player("red"))
        #self.players.append(Player("yellow"))
        #self.players.append(Player("blue"))

        self.get_player_of_turn()

        # Board cells
        self.cells = []
        self.red_cells = []
        self.blue_cells = []
        self.yellow_cells = []
        self.green_cells = []

        self.red_cells.append(Cell(450, 100, False))
        self.red_cells.append(Cell(400, 100, False))
        self.red_cells.append(Cell(400, 150, False))
        self.red_cells.append(Cell(400, 200, False))
        self.red_cells.append(Cell(400, 250, False))
        self.red_cells.append(Cell(400, 300, False))
        self.red_cells.append(Cell(400, 350, True))

        self.blue_cells.append(Cell(700, 450, False))
        self.blue_cells.append(Cell(700, 400, False))
        self.blue_cells.append(Cell(650, 400, False))
        self.blue_cells.append(Cell(600, 400, False))
        self.blue_cells.append(Cell(550, 400, False))
        self.blue_cells.append(Cell(500, 400, False))
        self.blue_cells.append(Cell(450, 400, True))

        self.yellow_cells.append(Cell(350, 700, False))
        self.yellow_cells.append(Cell(400, 700, False))
        self.yellow_cells.append(Cell(400, 650, False))
        self.yellow_cells.append(Cell(400, 600, False))
        self.yellow_cells.append(Cell(400, 550, False))
        self.yellow_cells.append(Cell(400, 500, False))
        self.yellow_cells.append(Cell(400, 450, True))

        self.green_cells.append(Cell(100, 350, False))
        self.green_cells.append(Cell(100, 400, False))
        self.green_cells.append(Cell(150, 400, False))
        self.green_cells.append(Cell(200, 400, False))
        self.green_cells.append(Cell(250, 400, False))
        self.green_cells.append(Cell(300, 400, False))
        self.green_cells.append(Cell(350, 400, True))

        # Red Side
        self.cells.append(Cell(350, 50, False))  # 0
        self.cells.append(Cell(400, 50, False))  # 1
        self.cells.append(Cell(450, 50, False))  # 2
        self.cells.append(Cell(450, 100, True))  # 3 Red Player
        self.cells.append(Cell(450, 150, False))  # 4
        self.cells.append(Cell(450, 200, False))  # 5
        self.cells.append(Cell(450, 250, False))  # 6
        self.cells.append(Cell(450, 300, False))  # 7

        # Blue Side
        self.cells.append(Cell(500, 350, False))  # 8
        self.cells.append(Cell(550, 350, False))  # 9
        self.cells.append(Cell(600, 350, False))  # 10
        self.cells.append(Cell(650, 350, False))  # 11
        self.cells.append(Cell(700, 350, False))  # 12
        self.cells.append(Cell(750, 350, False))  # 13
        self.cells.append(Cell(750, 400, False))  # 14
        self.cells.append(Cell(750, 450, False))  # 15
        self.cells.append(Cell(700, 450, True))  # 16 #Blue Player
        self.cells.append(Cell(650, 450, False))  # 17
        self.cells.append(Cell(600, 450, False))  # 18
        self.cells.append(Cell(550, 450, False))  # 19
        self.cells.append(Cell(500, 450, False))  # 20

        # Yellow Side
        self.cells.append(Cell(450, 500, False))  # 21
        self.cells.append(Cell(450, 550, False))  # 22
        self.cells.append(Cell(450, 600, False))  # 23
        self.cells.append(Cell(450, 650, False))  # 24
        self.cells.append(Cell(450, 700, False))  # 25
        self.cells.append(Cell(450, 750, False))  # 26
        self.cells.append(Cell(400, 750, False))  # 27
        self.cells.append(Cell(350, 750, False))  # 28
        self.cells.append(Cell(350, 700, True))  # 29 #Yellow Player
        self.cells.append(Cell(350, 650, False))  # 30
        self.cells.append(Cell(350, 600, False))  # 31
        self.cells.append(Cell(350, 550, False))  # 32
        self.cells.append(Cell(350, 500, False))  # 33

        # Green Side
        self.cells.append(Cell(300, 450, False))  # 34
        self.cells.append(Cell(250, 450, False))  # 35
        self.cells.append(Cell(200, 450, False))  # 36
        self.cells.append(Cell(150, 450, False))  # 37
        self.cells.append(Cell(100, 450, False))  # 38
        self.cells.append(Cell(50, 450, False))  # 39
        self.cells.append(Cell(50, 400, False))  # 40
        self.cells.append(Cell(50, 350, False))  # 41
        self.cells.append(Cell(100, 350, True))  # 42 #Green Player
        self.cells.append(Cell(150, 350, False))  # 43
        self.cells.append(Cell(200, 350, False))  # 44
        self.cells.append(Cell(250, 350, False))  # 45
        self.cells.append(Cell(300, 350, False))  # 46

        # Red Side End
        self.cells.append(Cell(350, 300, False))  # 47
        self.cells.append(Cell(350, 250, False))  # 48
        self.cells.append(Cell(350, 200, False))  # 49
        self.cells.append(Cell(350, 150, False))  # 50
        self.cells.append(Cell(350, 100, False))  # 51

    def get_cells(self):
        return self.cells

    def get_last_cell(self):
        return self.last_cell

    def get_players(self):
        return self.players

    def get_player_of_turn(self):
        for player in self.players:
            if player.turn:
                return player

    def is_pawn_in_movement(self):
        return self.pawn_in_movement

    def get_value_dice_to_move(self):
        return self.dice_value

    def is_end_action(self):
        return self.end_action

    def set_end_action(self, end_action):
        self.end_action = end_action

    def reduce_dice_value(self):
        self.dice_value = self.dice_value - 1

    def change_turn(self, last_turn):
        self.players.__getitem__(last_turn).turn = False

        if last_turn + 1 >= len(self.players):
            self.players.__getitem__(0).turn = True
        else:
            new_turn = last_turn + 1
            self.players.__getitem__(new_turn).turn = True

    def starting_movement_action(self, dice_value, pawn):
        self.pawn_in_movement = True
        self.dice_value = dice_value
        self.action_pawn = pawn

    def stoping_movement_action(self):
        self.pawn_in_movement = False
        self.dice_value = 0
        self.action_pawn = 0
        self.end_action = True
