#Ingresar las edades de dos personas. Si una de ellas es mayor de edad
#y la otra menor de edad, calcular y mostrar su promedio. En caso
#contrario mostrar las edades.

MAYOR_DE_EDAD = 18

persona_1 = int(input("Ingrese edad de la persona: "))
persona_2 = int(input('Ingrese edad de la segunda persona: '))

if persona_1 > MAYOR_DE_EDAD and persona_2 < MAYOR_DE_EDAD:
    print(persona_1)
    print(persona_2)
    promedio_edad = (persona_1 + persona_2) / 2
    print(f'El promedio de edad ingresado es de {promedio_edad}')
    
elif persona_1 < MAYOR_DE_EDAD and persona_2 > MAYOR_DE_EDAD:
    print(persona_1)
    print(persona_2)
    promedio_edad = (persona_1 + persona_2) / 2
    print(f'El promedio de edad ingresado es de {promedio_edad}')
    
else:
    print(f'La edad de la primera persona es: {persona_1} y la edad de la segunda persona es: {persona_2}')