from unreliable_car import UnreliableCar


def main():
    unreliable_car = UnreliableCar("Old Car", 100, 50)

    # Try to drive the car 40 km multiple times
    distances = []
    for _ in range(5):
        distance_driven = unreliable_car.drive(40)
        distances.append(distance_driven)
        print(f"Attempt to drive 40km: Drove {distance_driven}km")

    # Print the car's final details
    print(unreliable_car)


if __name__ == "__main__":
    main()
