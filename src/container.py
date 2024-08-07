class Container:
    def __init__(self) -> None:
        self.contained_squares = []
    
    def add_square(self, square):
        self.contained_squares.append(square)

    def remove_possible_number(self, number):
        for square in self.contained_squares:
            if number in square.possible_numbers:
                square.possible_numbers.remove(number)

class Row(Container):
    def __init__(self) -> None:
        super().__init__()

class Block(Container):
    def __init__(self) -> None:
        super().__init__()

class Column(Container):
    def __init__(self) -> None:
        super().__init__()