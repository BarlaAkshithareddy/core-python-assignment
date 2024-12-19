def book(bseat, bseats, tseats):
    if bseat in bseats:
        return False
    elif bseat < 1 or bseat > tseats:
        return False
    else:
        bseats.append(bseat)
        return True

def cancel(cseat, bseats):
    if cseat in bseats:
        bseats.remove(cseat)
        return True
    else:
        return False

def available(tseats, bseats):
    available_seats = [seat for seat in range(1, tseats + 1) if seat not in bseats]
    print(f"Available seats: {available_seats}")
    return available_seats
tseats = int(input("total_seats = "))
bseats = eval(input("booked_seats = "))
bseat = int(input("book_seat = "))
cseat = int(input("cancel_seat = "))
book(bseat, bseats, tseats)
available(tseats, bseats)
cancel(cseat, bseats)