from datetime import datetime, timedelta
import tkinter as tk
from tkinter import messagebox

class RestaurantReservationApp:
    def __init__(self, restaurant):
        self.restaurant = restaurant

        self.window = tk.Tk()
        self.window.title("Restaurant Reservation App")

        self.name_label = tk.Label(self.window, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.window)
        self.name_entry.pack()

        self.guests_label = tk.Label(self.window, text="Number of Guests:")
        self.guests_label.pack()
        self.guests_entry = tk.Entry(self.window)
        self.guests_entry.pack()

        self.available_times_label = tk.Label(self.window, text="Available Times:")
        self.available_times_label.pack()
        self.available_times_listbox = tk.Listbox(self.window, selectmode=tk.SINGLE)
        self.available_times_listbox.pack()

        self.reserve_button = tk.Button(self.window, text="Reserve", command=self.make_reservation)
        self.reserve_button.pack()

        self.update_available_times()

    def update_available_times(self):
        self.available_times_listbox.delete(0, tk.END)
        available_times = self.restaurant.get_available_times()
        for time in available_times:
            self.available_times_listbox.insert(tk.END, time.strftime("%Y-%m-%d %H:%M"))

    def make_reservation(self):
        name = self.name_entry.get()
        guests = int(self.guests_entry.get())
        selected_index = self.available_times_listbox.curselection()
        if selected_index:
            reservation_time = self.restaurant.get_available_times()[selected_index[0]]
            self.restaurant.make_reservation(name, guests, reservation_time)
            messagebox.showinfo("Reservation", "Reservation confirmed!")
            self.update_available_times()
        else:
            messagebox.showwarning("Reservation", "Please select a time.")

app = RestaurantReservationApp('restaurant')
app.window.mainloop()

from datetime import datetime, timedelta


class Restaurant:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.reservations = []

    def make_reservation(self, name, num_guests, reservation_time):
        if len(self.reservations) + num_guests <= self.capacity:
            reservation = Reservation(name, num_guests, reservation_time)
            self.reservations.append(reservation)
            print("Reservation confirmed!")
        else:
            print("Sorry, the restaurant is fully booked at that time.")

    def get_available_capacity(self):
        return self.capacity - sum([r.num_guests for r in self.reservations])

    def get_reservations(self):
        return self.reservations

    def get_available_times(self):
        reserved_times = [r.reservation_time for r in self.reservations]
        return [time for time in self.get_all_times() if time not in reserved_times]

    def get_all_times(self):
        opening_time = datetime.strptime("09:00", "%H:%M")
        closing_time = datetime.strptime("21:00", "%H:%M")

        time_delta = timedelta(minutes=30)
        current_time = opening_time
        all_times = []

        while current_time < closing_time:
            all_times.append(current_time)
            current_time += time_delta

        return all_times


class Reservation:
    def __init__(self, name, num_guests, reservation_time):
        self.name = name
        self.num_guests = num_guests
        self.reservation_time = reservation_time

    def __str__(self):
        return f"{self.name} - Guests: {self.num_guests} - Time: {self.reservation_time}"


# Exemplo de uso
restaurant = Restaurant("Example Restaurant", 50)

print("Welcome to Example Restaurant!")
print("Please provide the following details to make a reservation.")

name = input("Enter your name: ")
num_guests = int(input("Enter the number of guests: "))

available_times = restaurant.get_available_times()
print("Available reservation times:")
for i, time in enumerate(available_times):
    print(f"{i+1}. {time.strftime('%Y-%m-%d %H:%M')}")

time_choice = int(input("Enter the number corresponding to your desired time: "))
reservation_time = available_times[time_choice - 1]

restaurant.make_reservation(name, num_guests, reservation_time)

print("\nReservation Details:")
for reservation in restaurant.get_reservations():
    print(reservation)

