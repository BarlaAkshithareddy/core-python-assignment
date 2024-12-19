def positive_feedback(ratings):
    if len(ratings) == 0:
        return False
    count = 0  
    for x in ratings:
        if x == 4 or x == 5:
            count += 1 
    percent = (count * 100) / len(ratings)
    return percent
ratings = eval(input("ratings = "))
positive_percentage = positive_feedback(ratings)
print(f"Positive Feedback: {positive_percentage:.1f}%") 