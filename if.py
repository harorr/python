
age = int(input())

if age < 18:
    print("Minor")
elif age in range(18, 65):
    print("Adult")
else: print("Senior")