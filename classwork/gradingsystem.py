def gradingsytem (mark):
    if mark <= 100 and mark >= 90:
        return "A"
    
    if mark >= 80:
        return "B"
    
    if mark<= 50:
        return "F"
    
score = int(input("Enter Grade: "))
grade = gradingsytem(score)
print(grade)