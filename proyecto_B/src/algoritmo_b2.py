import pandas as pd

datos = {
    "Nombre": ["Ana", "Luis", "María"],
    "Edad": [17, 19, 18]
}

df = pd.DataFrame(datos)

print("Tabla de estudiantes:")
print(df)
