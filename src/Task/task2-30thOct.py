# Q - Create a function which will take the 3 values from the user, which are length of the triangle.  side1, side2, side2
# i/p - int side1 == side2 =side3 → isoceles
# o/p = result in string - iso, eq, scalene

side1 = int(input(f"Enter side1 of triangle:"))
side2 = int(input(f"Enter side2 of triangle:"))
side3 = int(input(f"Enter side3 of triangle:"))

def triangle(side1, side2, side3):
    if side1 == side2 == side3:
        print("eq")
    elif side1 == side2 or side2 == side3:
        print("iso")
    else:
        print("esc")

print(triangle(10, 10, 20))