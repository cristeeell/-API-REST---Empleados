import requests

url = 'https://dummy.restapiexample.com/api/v1/employees'
empleados_data = requests.get(url).json()

# Información sobre los empleados
empleados = empleados_data.get('data', [])

# Verificacion de datos
if not empleados:
    print(" Lo sentimos,No hay información sobre empleados.")
else:
    # Inicializar variables
    total_empleados = len(empleados)
    total_salario = 0
    total_edad = 0
    salario_minimo = float('inf')
    salario_maximo = float('-inf')
    edad_minima = float('inf')
    edad_maxima = float('-inf')

    # estadísticas
    for empleado in empleados:
        salario = float(empleado.get('employee_salary', 0))
        edad = int(empleado.get('employee_age', 0))

        total_salario += salario
        total_edad += edad

        salario_minimo = min(salario_minimo, salario)
        salario_maximo = max(salario_maximo, salario)

        edad_minima = min(edad_minima, edad)
        edad_maxima = max(edad_maxima, edad)

    # promedios
    promedio_salario = total_salario / total_empleados
    promedio_edad = total_edad / total_empleados

    # resultados
    print(f'A continuacion informacion de los empleados:')
    print(f"Numero de empleados: {total_empleados}")
    print(f"Promedio de salario: {promedio_salario:.2f}")
    print(f"Promedio de edad: {promedio_edad:.2f}")
    print(f"Salario mínimo: {salario_minimo:.2f}")
    print(f"Salario máximo: {salario_maximo:.2f}")
    print(f"Edad mínima: {edad_minima}")
    print(f"Edad máxima: {edad_maxima}")
