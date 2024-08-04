from unreliable_car import UnreliableCar

def main():
    # Create a new UnreliableCar
    my_unreliable_car = UnreliableCar("Unreliable", 100, 50)

    # Attempt to drive the car several times
    for i in range(10):
        distance_driven = my_unreliable_car.drive(10)
        print(f"Attempt {i+1}: Drove {distance_driven}km")

    # Print the final state of the car
    print(my_unreliable_car)

if __name__ == "__main__":
    main()