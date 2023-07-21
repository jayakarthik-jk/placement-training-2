from dataclasses import dataclass
from threading import Thread
from time import sleep
@dataclass
class Station:
    name: str
    position: int

@dataclass
class Taxi:
    label: str
    current_station: Station
    distance_traveled: int = 0
    availability: bool = True

    def move_to(self, destination: Station):
        distance = abs(self.current_station.position - destination.position)
        def moving():
            self.availability = False
            sleep(distance * 60)
            self.current_station = destination
            self.availability = True
        thread = Thread(target=moving)
        thread.start()

    def is_busy(self):
        return self.availability

    def print_availability_msg(self, pickup: Station):
        if self.current_station.position != pickup.position:
            print(f"the nearest taxi {self.label} is currently at {self.current_station.name}")
            print(f"You need to wait for {abs(self.current_station.position - pickup.position) * 60} mins for the taxi to arrive")
        else:
            print(f"there is a taxi {self.label} at your station {pickup.name}")

    def book(self, pickup: Station, drop: Station):
        distance_in_km = abs(pickup.position - drop.position) * 15
        amount = 0
        if distance_in_km > 5:
            amount += 100
            distance_in_km -= 5
        amount += distance_in_km * 10
        print("==============================")
        print(f"Taxi Name    :        {self.label}")
        print(f"Total charges:        {amount}")
        print("==============================")
        decision = input("Do you want to confirm booking (yes / no): ")
        if decision.lower().startswith("y"):
            print("Booking Successfull")
            self.move_to(drop)
        else:
            print("Booking Cancelled")

@dataclass
class CallTaxiSystem:
    stations: list[Station]
    taxis: list[Taxi]

    def print_available_stations(self):
        print("-----Available stations-------")
        for (i, station) in enumerate(self.stations):
            print(f"{station.name}", end="" if i + 1 == len(self.stations) else " -> ")
        print()

    def get_station_by_label(self, label):
        dest = None
        for station in self.stations:
            if station.name.lower().startswith(label.lower()):
                dest = station
        return dest

    def print_menu(self):
        print("==============================")
        print("       Call Taxi System       ")
        print("==============================")
        self.print_available_stations()
        user_station_name = input("Enter your current location: ")
        pickup = self.get_station_by_label(user_station_name)
        if not pickup:
            print(f"sorry, we don't provide service in your location {user_station_name}")
            return
        nearest_taxi = self.find_nearest_available_taxi(pickup)
        if not nearest_taxi:
            print("sorry, no taxis are available right now...")
            return
        nearest_taxi.print_availability_msg(pickup)

        self.print_available_stations()
        destination_name = input("Enter the destination: ")
        destination = self.get_station_by_label(destination_name)
        if not destination:
            print(f"sorry, we don't provide service in for the entered destination {user_station_name}")
            return
        nearest_taxi.book(pickup, destination)
        # find nearest available station

    def find_nearest_available_taxi(self, pickup: Station):
        best_match: Taxi = None
        for taxi in self.taxis:
            if taxi.availability:
                if not best_match:
                    best_match = taxi
                    continue
                best_diference = abs(best_match.current_station.position - pickup.position)
                current_diference = abs(taxi.current_station.position - pickup.position)
                if current_diference < best_diference:
                    best_match = taxi
        return best_match

station_names = "ABCDEF"
stations = []
for (i, names) in enumerate(station_names):
    stations.append(Station(names, i))

cars = [
    Taxi('Taxi 1', stations[0]),
    Taxi('Taxi 2', stations[0]),
    Taxi('Taxi 3', stations[0]),
    Taxi('Taxi 4', stations[0]),
]
system = CallTaxiSystem(stations, cars)
while True:
    system.print_menu()