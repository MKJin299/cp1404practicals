from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Drive the taxi
    fancy_taxi.drive(18)

    # Calculate and print the fare
    fare = fancy_taxi.get_fare()
    print(f"Fare for 18km trip: ${fare:.2f}")

    # Test the str method
    print(fancy_taxi)

    # Assert test
    assert round(fare, 2) == 48.80, f"Expected fare $48.80, got ${fare:.2f}"
    print("Assert test passed!")

if __name__ == "__main__":
    main()