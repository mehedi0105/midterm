
class Star_Cinema:
    hall_list = []

    def entry_hall(self, rows, cols, hall_no):
        obj = Hall(rows, cols, hall_no)
        self.hall_list.append(obj)


class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        self.__seats = {}
        self.show_list = []
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        touple = (id, movie_name, time)
        self.show_list.append(touple)
        self.__seats[id] = [['free' for _ in range(
            self.__cols)] for _ in range(self.__rows)]

    def book_ticket(self, show_id, seat_list):
        if show_id in self.__seats:
            for row, col in seat_list:
                if self.__rows > row >= 0 and self.__cols > col >= 0:
                    if self.__seats[show_id][row][col] == 'free':
                        self.__seats[show_id][row][col] = 'already booking'
                        # print("Congraulation you are succesfully book this seat")
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

    def view_available_seats(self, show_id):
        if show_id in self.__seats:
            print(f"Available seats for show ID {show_id}:")
            for row_index, row in enumerate(self.__seats[show_id]):
                for col_index, seat in enumerate(row):
                    if seat == 'free':
                        print(f"Row: {row_index}, Col: {col_index}")
        else:
            print(f"No show found with ID: {show_id}")


Sapla_Cinema = Hall(rows=30, cols=15, hall_no=1)
Sapla_Cinema.entry_show(id='111', movie_name='Jawan', time='12:00')
Sapla_Cinema.entry_show(id='222', movie_name='Pathan', time='17:00')
jawan = [(1, 5), (1, 7), (1, 9)]
Sapla_Cinema.book_ticket('111', jawan)
pathan = [(1, 4), (1, 7), (1, 3)]
Sapla_Cinema.book_ticket('222', pathan)


while True:
    print("1. View all show in today")
    print("2. View available all seats")
    print("3. Book ticket")
    print("4. Exit")
    option = input("Enter Option: ")

    if option == "1":

        Sapla_Cinema.view_show_list()

    elif option == "2":
        show_id = input("Enter Show ID: ")
        Sapla_Cinema.view_available_seats(show_id)
    elif option == "3":
        show_id = input("Enter Show ID: ")
        seats = input(
            "Enter seats no to book (demo like: row,col  '1,2 2,3'): ")
        seat_list = [tuple(map(int, seat.split(',')))
                     for seat in seats.split()]
        Sapla_Cinema.book_ticket(show_id, seat_list)
    elif option == "4":
        break
    else:
        print("Invalid option. Please try again.")
