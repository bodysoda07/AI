
def water_jug():

    A = int(input("Enter Jug A capacity: "))
    B = int(input("Enter Jug B capacity: "))
    target = int(input("Enter target amount: "))

    a = 0
    b = 0
    step = 1
    visited = set()

    while (a, b) not in visited:

        visited.add((a, b))

        print("\nStep", step)

        if a == target or b == target:
            print("Goal Reached!")
            print("Jug A =", a, "Jug B =", b)
            return

        elif b == 0:
            b = B
            print("Fill Jug B")

        elif a < A:
            x = min(b, A - a)
            a += x
            b -= x
            print("Pour Jug B into Jug A")

        elif a == A:
            a = 0
            print("Empty Jug A")

        print("Jug A =", a, "Jug B =", b)

        step += 1

    print("No Solution Found")


water_jug()
