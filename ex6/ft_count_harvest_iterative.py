def ft_count_harvest_iterative():
    try:
        days = int(input("How many days are left until the harvest? "))
        for i in range(1, days + 1):
            print(f"Day {i}")
        print("Harvest time")
    except ValueError:
        print("❌ Please enter a valid number.")
