from errors import TubeEmptyError, TubeOverfilledError, TubeAddError


class Tube:

    MAXIMUM_LAYERS = 4

    def __init__(self, layers):
        if len(layers) > Tube.MAXIMUM_LAYERS:
            raise TubeOverfilledError()
        self.layers = layers

    def can_add(self, layers):
        if len(self.layers) > Tube.MAXIMUM_LAYERS:
            raise TubeOverfilledError()
        if len(self.layers) + len(layers) > Tube.MAXIMUM_LAYERS:
            return False
        if len(self.layers) == 0:
            return True
        if self.layers[len(self.layers) - 1] == layers[0]:
            return True

    def add(self, layers):
        if not self.can_add(layers):
            raise TubeAddError()
        self.layers = self.layers + layers

    def __str__(self):
        return_string = ""
        for layer in self.layers:
            return_string += layer
        return return_string

    def get_top_layer(self):
        if len(self.layers) == 0:
            raise TubeEmptyError()
        top_layers = []
        current_layer_level = len(self.layers) - 1
        while True:
            if current_layer_level < 0:
                break
            if len(top_layers) > 0:
                if self.layers[current_layer_level] != top_layers[0]:
                    break
            top_layers.append(self.layers[current_layer_level])
            current_layer_level -= 1
        return list(reversed(top_layers))

    def remove_top_layer(self):
        new_layers = []
        for i in range(len(self.layers) - len(self.get_top_layer())):
            new_layers.append(self.layers[i])
        self.layers = new_layers

    def is_solved(self):
        return ((len(set(self.layers))) == 1 and len(self.layers) == Tube.MAXIMUM_LAYERS) or self.is_empty()

    def is_empty(self):
        return len(self.layers) == 0
