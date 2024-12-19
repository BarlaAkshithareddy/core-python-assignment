def fare():
    base_fare=50
    distance_fare=10
    total_fare=0
    for x in trips:
        each_fare=base_fare+(x*distance_fare)
        print(f"Trip 1: ${each_fare}")
        total_fare+=each_fare
    print(f"Total Fare: ${total_fare}")
trips=eval(input("trips = "))
fare()