import sys

grades = 0.0
credits = []

for _ in range(20):
    subject, credit, grade = sys.stdin.readline().strip().split()
    if grade != "P":
        credits.append(float(credit))
        if grade == "A+":
            grades += float(credit) * 4.5
        elif grade == "A0":
            grades += float(credit) * 4.0
        elif grade == "B+":
            grades += float(credit) * 3.5
        elif grade == "B0":
            grades += float(credit) * 3.0
        elif grade == "C+":
            grades += float(credit) * 2.5
        elif grade == "C0":
            grades += float(credit) * 2.0
        elif grade == "D+":
            grades += float(credit) * 1.5
        elif grade == "D0":
            grades += float(credit) * 1.0
        else:
            grades += float(credit) * 0.0
            
print(grades / sum(credits))