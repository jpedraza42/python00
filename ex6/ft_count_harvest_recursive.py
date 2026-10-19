def ft_count_harvest_recursive():
    try:
        days = int(input("How many days are left until the harvest? "))

        def helper(current: int, total: int) -> None:
            if current > total:
                print("Harvest time!")
                return
            print(f"Day {current}")
            helper(current + 1, total)

        helper(1, days)
    except ValueError:
        print("❌ Please enter a valid number.")
