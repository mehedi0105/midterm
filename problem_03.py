class Star_Cinema:
    hall_list = []

    def entry_hall(self, newHall):
        self.hall_list.append(newHall)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.entry_hall(self)

    def entry_show(self, id, movie_name, time):
        touple = (id, movie_name, time)
        self.show_list.append(touple)
        self.seats[id] = [[0 for i in range(
            self.cols)] for j in range(self.rows)]


Sapla = Hall(10, 10, 1)
Sapla.entry_show(98, "jawan", "11 : 00")
for id, matrix in Sapla.seats.items():

    for row in matrix:
        print(row)
    print()
