import pulp


# Crear el problema
problema = pulp.LpProblem("comida", pulp.LpMinimize)

# Variables de decisión
x1 = pulp.LpVariable("x1", lowBound=0, upBound=6, cat='Integer')  # Cantidad de manzanas
x2 = pulp.LpVariable("x2", lowBound=0, upBound=4, cat='Integer')  # Cantidad de plátanos
x3 = pulp.LpVariable("x3", lowBound=0, upBound=10, cat='Integer')  # Cantidad de yogur

# Función objetivo
problema += (0.5 * x1) + (0.4 * x2) + (1.2 * x3)

# Restricciones
problema += (50 * x1) + (89 * x2) + (150 * x3) >= 2000  # Restricción de calorías
problema += (5 * x1) + (5 * x2) + (3.4 * x3) >= 80  # Restricción de proteínas

    # Restricción de  calorias 
problema += (x1) <= 6

    # Restricción de  calorias 
problema += (x2) <= 4

    # Restricción de  calorias 
problema += (x3) <= 10 

# Restricción de no negatividad
for var in [x1, x2, x3]:
    problema += var >= 0

# Resolver el problema
problema.solve()
print("Estado:", pulp.LpStatus[problema.status])

if pulp.LpStatus[problema.status] == "Optimal":
    print("Solución encontrada:")
    for var in [x1, x2, x3]:
        print(f"{var.name} = {var.varValue}")
else:
    print("No se encontró una solución óptima.")
 
 
 







    
    