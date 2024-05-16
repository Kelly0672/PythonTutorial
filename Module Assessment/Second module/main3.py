radius= input("Enter a random number") 
pii = float(3.141592653589793)
radius = float(radius)
circumference= (2* pii * radius)
area = (pii*(radius**2))
print("The circumference of the circle with the radius ",
      radius, "is ",round(circumference,2))
print("The area of the circle with the radius ", radius, 
      "is ", round(area, 2))