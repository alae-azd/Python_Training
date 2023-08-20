import time

print("Egg Cooking")
print("1 - Soft-boiled Eggs: 3 minutes")
print("2 - Medium-boiled Eggs: 6 minutes")
print("3 - Hard-boiled Eggs: 9 minutes")

while True:
    choice = input("Your choice: ")
    if choice == "1" or choice == "2" or choice == "3":
        break
    print("ERROR: You must choose an option 1, 2, or 3\n")

duration = 0
if choice == "1":
    duration = 3 * 60
elif choice == "2":
    duration = 6 * 60
else:
    duration = 9 * 60

while True:
    for i in range(0, 10):
        time.sleep(1)
        print(".", end="", flush=True)
        duration -= 1
        if duration < 0:
            break
    
    if duration < 0:
        break
    minutes = duration // 60
    seconds = duration - minutes * 60
    print()
    print(f"Time remaining: {minutes:02d}:{seconds:02d}", end="", flush=True)

print()
print("Cooking finished")
