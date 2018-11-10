class spaceship():
    def __init__(self):
        self.moves_executed = 0
        self.shots_fired = 0
        self.x = 0
        self.y = 0
    def increment_moves(self):
        #increment the move counter
        self.moves_executed = self.moves_executed + 1
        return self.moves_executed
    def increment_shots(self):
        self.shots_fired = self.shots_fired + 1
        return self.shots_fired
    def north(self):
        self.y = self.y+1
    def south(self):
        self.y = self.y-1
    def east(self):
        self.x = self.x+1
    def west(self):
        self.x = self.x-1
