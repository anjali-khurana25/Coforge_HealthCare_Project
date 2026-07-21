def surface_area(radius):
    pi = 3.14
    area = 4 * pi * radius * radius
    return area

r = float(input("Enter the radius of the sphere: "))

result = surface_area(r)

print("Surface Area of the Sphere =", result)