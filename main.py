gravity = 5
jumpHeight = 10
speed = 4

print("Type a command to change variables!")

while True:
    exec(input("Type a command: "))

    print(f"Gravity: {gravity}")
    print(f"Jump height: {jumpHeight}")
    print(f"Speed: {speed}")
