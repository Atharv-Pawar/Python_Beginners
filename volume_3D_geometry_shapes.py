import math

v = int(input("Enter the number of vertices of your shape"))
e = int(input("Enter the number of edges of your shape"))
f = int(input("Enter the number of faces of your shape"))

if(v==4 and e==6 and f==4):
    print("It's Tetrahedron")
    a = int(input("Enter the side length"))
    k = math.sqrt(2)
    vol_tetra = round((a**3)/6*k, 2)
    print("Volume of tetrahedron is", vol_tetra)

elif(v==8 and e==12 and f==6):
    a = int(input("Enter the length"))
    b = int(input("Enter the width"))
    c = int(input("Enter the height"))
    if(a==b and b==c):
        print("It's Cube")
        vol_cub = a*b*c
        print("Volume of Cube is", vol_cub)

    else:
        print("It's Cuboid")
        vol_cub = a*b*c
        print("Volume of Cuboid is", vol_cub)

elif(v==5 and e==8 and f==5):
    a = int(input("Enter the length"))
    b = int(input("Enter the width"))
    c = int(input("Enter the height"))
    if a != b:
        print("It's Rectangular-based Pyramid")
        vol_pyr = a*b*c/3
        print("Volume of Rectangular-based Pyramid is", vol_pyr)

    else:
        print("It's Square-based Pyramid")
        vol_pyr = a*b*c/3
        print("Volume of Square-based Pyramid is", vol_pyr)

elif(v==6 and e==9 and f==5):
    print("It's Triangular Prism")
    a = int(input("Enter base_side-1 length"))
    b = int(input("Enter base_side-2 length"))
    c = int(input("Enter base_side-3 length"))
    h = int(input("Enter the height"))
    h = h/4
    z = ((a*b)**2+(a*c)**2+(b*c)**2)
    m = (a**4) + (b**4) + (c**4)
    k = math.sqrt(2*z - m)
    vol_prism = round(h*k, 2)
    print("Volume of Triangular Prism is", vol_prism)

elif(v==0 and e==2 and f==3):
    print("It's Cylinder")
    r = int(input("Enter the radius"))
    h = int(input("Enter the height"))
    vol_cyl = math.pi * (r ** 2) * h
    print('Volume of Cylinder is', vol_cyl)

elif(v==1 and e==1 and f==2):
    print("It's Cone")
    r = int(input("Enter the radius"))
    h = int(input("Enter the height"))
    vol_cone = 1 / 3 * math.pi * (r**2) * h
    print("Volume of Cone is", vol_cone)

elif(v==0 and e==0 and f==1):
    print("It's Sphere")
    r = int(input("Enter the radius"))
    vol_sphere = 4/3*math.pi*(r**3)
    print("Volume of Sphere is", vol_sphere)

else:
    print("Invalid")
