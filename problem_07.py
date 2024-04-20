ok = False


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
        global ok
        if show_id in self.seats:
            for row, col in seat_list:
                if self.rows > row >= 0 and self.cols > col >= 0:
                    if self.seats[show_id][row][col] == 0:
                        self.seats[show_id][row][col] = 1
                        ok = True
                    else:
                        print(f"\tSeat at row {row} and col {
                              col} are already booking.")
                else:
                    print(f"\tInvalid seat coordinates: row {row}, col {col}.")
        else:
            print(f"\tNo show found with ID: {show_id}")

    def view_show_list(self):
        for id, movie_name, time in self.show_list:
            print(f"\tShow ID: {id}, Movie Name: {movie_name}, Time: {time}")

    def view_available_seats(self, show_id):
        if show_id in self.seats:
            print(f"\tAvailable seats for show ID {show_id}:")
            for row_index, row in enumerate(self.seats[show_id]):
                for col_index, seat in enumerate(row):
                    if seat == 0:
                        print(f"\tRow: {row_index}, Col: {col_index}")
        else:
            print(f"\tNo show found with ID: {show_id}")


Sapla = Hall(10, 10, 1)
Sapla.entry_show("102", "jawan", "11:00 AM")
Sapla.entry_show("202", "Boss", "02:00 PM")
jawan = [(1, 5), (1, 7), (1, 9)]
Sapla.book_ticket("102", jawan)
Boss = [(2, 1), (2, 7), (2, 9)]
Sapla.book_ticket("202", Boss)


while True:
    print("1. View all show in today")
    print("2. View available all seats")
    print("3. Book ticket")
    print("4. Exit")
    option = input("Enter Option: ")

    if option == "1":

        Sapla.view_show_list()
        print()

    elif option == "2":
        show_id = input("Enter Show ID: ")
        Sapla.view_available_seats(show_id)
        print()
    elif option == "3":
        # global ok
        show_id = input("Enter Show ID: ")
        seats = input(
            "Enter seats no to book (demo like: row,col  '1,2 2,3'): ")
        seat_list = [tuple(map(int, seat.split(',')))
                     for seat in seats.split()]
        Sapla.book_ticket(show_id, seat_list)
    elif option == "4":
        break
    else:
        print("Invalid option. Please try again.")
