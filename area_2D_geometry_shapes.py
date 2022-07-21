import math

v = int(input("Enter the number of vertices in (0-4) of your shape"))

if v == 0:
    print("It's a Circle")
    r = int(input("Enter the radius"))
    a = round(math.pi*r*r, 2)
    print("Area of circle is", a)

elif v == 3:
    print("It's a Triangle")
    b = int(input("Enter the base"))
    h = int(input("Enter the height"))
    a = 1/2*b*h
    print("Area of triangle is", a)

elif v == 4:
    a = int(input("Enter side1 length"))
    b = int(input("Enter side2 length"))
    c = int(input("Enter side3 length"))
    d = int(input("Enter side4 length"))
    if a == b == c == d:
        print("It's a Square")
        area = a*a
        print("Area of square is", area)
    elif a==b and c==d or a==c and b==d or a==d and b==c:
        print("It's a Rectangle")
        if a==b or a==c:
            area = b*c
        else:
            area = a*b
        print("Area of rectangle is", area)

    else:
        print("It's a Trapezium")
        print("Sorry formula for Trapezium is missing")

elif v == 1:
    print("It's a point \nSorry, it has not a shape, it has no area.")

elif v == 2:
    print("It's a line \nSorry, it has not a shape, it has no area.")

else:
    print("Formula is missing for vertices above 4")

