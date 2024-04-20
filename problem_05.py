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

    def book_ticket(self, show_id, seat_list):
        if show_id in self.seats:
            for row, col in seat_list:
                if self.rows > row >= 0 and self.cols > col >= 0:
                    if self.seats[show_id][row][col] == 0:
                        self.seats[show_id][row][col] = 1
                        print(f"Congraulation you are succesfully book {
                              row} {col} this seat")
                    else:
                        print(f"Seat at row {row} and col {
                              col} are already booking.")
                else:
                    print(f"Invalid seat coordinates: row {row}, col {col}.")
        else:
            print(f"No show found with ID: {show_id}")

        def view_show_list(self):
            for id, movie_name, time in self.show_list:
                print(f"Show ID: {id}, Movie Name: {movie_name}, Time: {time}")


Sapla = Hall(10, 10, 1)
Sapla.entry_show(102, "jawan", "11:00 AM")
Sapla.entry_show(202, "Boss", "02:00 PM")
jawan = [(1, 5), (1, 7), (1, 9)]
Sapla.book_ticket(102, jawan)
print(Sapla.show_list)
for id, matrix in Sapla.seats.items():

    for row in matrix:
        print(row)
    print()
