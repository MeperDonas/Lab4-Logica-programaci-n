 #! Punto 3

#? Variables
a_1 = 4
a_2 = -8 
t_1 = 4
t_2 = 10

#? Formulas 
v = a_1*t_1
d_1 = (a_1*t_1**2)/2
d_2 = v * t_2
t_3 = v/-(a_2)
d_3 = (v/2)*t_3


print("La distancia recorrida en el primer tramo es: ", int(d_1), "m")
print("La distancia recorrida en el tramo es: ", d_2, "m")
print("La distancia recorrida en el tercer tramo es: ", int(d_3), "m")
print("La distancia total recorrida es: ", int(d_1 + d_2 + d_3), "m")
