from prac_06.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

USER_MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Taxi simulator program using Taxi and SilverServiceTaxi classes."""
    total_cost = 0
    available_taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
                       SilverServiceTaxi("Hummer", 200, 4)]
    selected_taxi = None
    print("Let's drive!")
    print(USER_MENU)
    user_choice = input(">>> ").lower()
    while user_choice != "q":
        if user_choice == "c":
            print("Available taxis: ")
            show_taxis(available_taxis)
            try:
                taxi_index = int(input("Choose taxi: "))
                selected_taxi = available_taxis[taxi_index]
            except (IndexError, ValueError):
                print("Invalid taxi choice")
        elif user_choice == "d":
            if selected_taxi:
                selected_taxi.start_fare()
                distance = float(input("Drive how far? "))
                selected_taxi.drive(distance)
                ride_cost = selected_taxi.get_fare()
                print(f"Your {selected_taxi.name} trip cost you ${ride_cost:.2f}")
                total_cost += ride_cost
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_cost:.2f}")
        print(USER_MENU)
        user_choice = input(">>> ").lower()

    print(f"Total trip cost: ${total_cost:.2f}")
    print("Taxis are now:")
    show_taxis(available_taxis)


def show_taxis(taxis):
    """Display the list of taxis with their indices."""
    for index, taxi in enumerate(taxis):
        print(f"{index} - {taxi}")


def test_classes():
    """Run tests to demonstrate Car, Taxi, and SilverServiceTaxi functionalities."""
    car_example = Car("Datsun", 180)
    car_example.drive(30)
    print("fuel =", car_example.fuel)
    print("odo =", car_example._odometer)
    car_example.drive(55)
    print("fuel =", car_example.fuel)
    print("odo =", car_example._odometer)
    print(car_example)

    # drive the car (loop ignores fuel status)
    distance = int(input("Drive how far? "))
    while distance > 0:
        distance_driven = car_example.drive(distance)
        print(f"{car_example} travelled {distance_driven}")
        distance = int(input("Drive how far? "))

    taxi_example = Taxi("Prius 1", 100)
    print(taxi_example)
    taxi_example.drive(25)
    print(taxi_example, taxi_example.get_fare())
    taxi_example.start_fare()
    taxi_example.drive(40)
    print(taxi_example, taxi_example.get_fare())

    silver_taxi_example = SilverServiceTaxi("Limo", 100, 2)
    print(silver_taxi_example, silver_taxi_example.get_fare())
    silver_taxi_example.drive(10)
    print(silver_taxi_example, silver_taxi_example.get_fare())


# test_classes()
main()
