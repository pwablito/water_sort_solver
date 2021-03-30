class Move():
    def __init__(self, source, target):
        self.source = source
        self.target = target

    def __str__(self):
        # We will print 1 indexes, not zero. This is for readability
        return "{:^3} -> {:^3}".format(self.source + 1, self.target + 1)
