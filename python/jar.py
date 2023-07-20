total = 10
K = 5

while True:
    print(f"Available candies {total}")
    asked = int(input("Enter the number of candies want: "))
    if asked > total:
        print("Invalid Input...")
    else:
        total -= asked
        print(f"{asked} candies sold")
        if total < K:
            print(f"{10 - total} number of candies filled")
            total = 10