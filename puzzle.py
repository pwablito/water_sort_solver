class Puzzle:
    def __init__(self, tubes):
        self.tubes = tubes

    def can_move(self, move):
        try:
            if not self.tubes[move.target].can_add(self.tubes[move.source].get_top_layer()):
                return False
            if self.tubes[move.target].is_empty():
                if len(self.tubes[move.source].layers) - len(self.tubes[move.source].get_top_layer()) == 0:
                    return False
            return True
        except Exception:
            return False

    def move(self, move):
        layer = self.tubes[move.source].get_top_layer()
        self.tubes[move.source].remove_top_layer()
        self.tubes[move.target].add(layer)

    def is_solved(self):
        for tube in self.tubes:
            if not tube.is_solved():
                return False
        return True
