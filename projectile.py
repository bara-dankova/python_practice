heightOfBarrel = 1
horizontalDistanceTravelled = 0.5
deg = 80
initialVelocity = 44
accelerationGravity = 9.81


from math import pi, tan, cos
theta = deg * (pi/180)

a = heightOfBarrel + horizontalDistanceTravelled*tan(theta)
b = accelerationGravity*(horizontalDistanceTravelled**2)
c = (initialVelocity*cos(theta))**2
d = 2*c

heightOfProjectile = a - (b/d)


print("Height of projectile is", round(heightOfProjectile,2), "m")