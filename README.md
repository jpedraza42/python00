# Python 00 — Primeros pasos con Python / Python Fundamentals

[Español](#español--primeros-pasos-con-python) · [English](#english--python-00)

## Español · Primeros pasos con Python

Ejercicios de iniciación a Python realizados durante mi formación en **42 Málaga Fundación Telefónica**.

Este repositorio reúne ejercicios breves ambientados en un jardín. Su objetivo es practicar conceptos fundamentales del lenguaje y avanzar desde la entrada y salida de datos hasta las funciones, condiciones, iteración y recursividad.

## Ejercicios

| Carpeta | Archivo | Qué practica |
|---|---|---|
| `ex0` | [`ft_hello_garden.py`](ex0/ft_hello_garden.py) | Definir una función y mostrar un mensaje con `print()`. |
| `ex1` | [`ft_garden_name.py`](ex1/ft_garden_name.py) | Leer texto con `input()` y mostrarlo por pantalla. |
| `ex2` | [`ft_plot_area.py`](ex2/ft_plot_area.py) | Convertir entradas a enteros y calcular el área de una parcela. |
| `ex3` | [`ft_harvest_total.py`](ex3/ft_harvest_total.py) | Sumar las cosechas introducidas para tres días. |
| `ex4` | [`ft_plant_age.py`](ex4/ft_plant_age.py) | Utilizar `if/else` para comprobar si una planta supera los 60 días. |
| `ex5` | [`ft_water_reminder.py`](ex5/ft_water_reminder.py) | Utilizar una condición para recordar el riego cuando han pasado más de dos días. |
| `ex6` | [`ft_count_harvest_iterative.py`](ex6/ft_count_harvest_iterative.py) | Contar días mediante un bucle `for` y gestionar entradas no numéricas con `try/except`. |
| `ex6` | [`ft_count_harvest_recursive.py`](ex6/ft_count_harvest_recursive.py) | Resolver el mismo conteo mediante una función recursiva, con caso base y manejo de `ValueError`. |
| `ex7` | [`ft_seed_inventory.py`](ex7/ft_seed_inventory.py) | Usar parámetros, anotaciones de tipo y condiciones para mostrar un inventario en paquetes, gramos o superficie. |

## Cómo ejecutarlos

**Importante:** los archivos contienen definiciones de funciones; ejecutarlos directamente con `python3 archivo.py` no muestra nada hasta que se invoque la función. Se pueden probar importándolas desde la raíz del repositorio.

Ejemplo para `ex0`:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

Ejemplo para `ex2` (pedirá longitud y anchura):

```bash
python3 -c "from ex2.ft_plot_area import ft_plot_area; ft_plot_area()"
```

Ejemplo para `ex7` (la función recibe argumentos):

```bash
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 12, 'packets')"
```

Requieren **Python 3** y no se observan dependencias externas en los archivos de estos ejercicios.

## Qué estoy aprendiendo

- Funciones, parámetros y salida por consola.
- Entrada de usuario, conversión de tipos y operaciones aritméticas básicas.
- Condicionales y decisiones sencillas.
- Bucles y recursividad como dos formas de abordar un mismo problema.
- Tratamiento básico de entradas incorrectas en `ex6`.
- Anotaciones de tipos en `ex7`.

**Estado:** ejercicios formativos de nivel inicial; no constituyen una aplicación completa ni un proyecto de producción. Este repositorio muestra una etapa concreta de mi aprendizaje de programación.

---

## English · Python 00

Introductory Python exercises completed as part of my studies at **42 Málaga Fundación Telefónica**.

These short garden-themed exercises introduce core programming concepts, from input/output and arithmetic to conditionals, iteration, recursion, and type annotations.

### Exercises

| Folder | File | What it practices |
|---|---|---|
| `ex0` | [`ft_hello_garden.py`](ex0/ft_hello_garden.py) | Defining a function and printing a message with `print()`. |
| `ex1` | [`ft_garden_name.py`](ex1/ft_garden_name.py) | Reading text with `input()` and displaying it. |
| `ex2` | [`ft_plot_area.py`](ex2/ft_plot_area.py) | Converting input to integers and calculating the area of a garden plot. |
| `ex3` | [`ft_harvest_total.py`](ex3/ft_harvest_total.py) | Adding harvest quantities entered for three days. |
| `ex4` | [`ft_plant_age.py`](ex4/ft_plant_age.py) | Using `if/else` to check whether a plant is more than 60 days old. |
| `ex5` | [`ft_water_reminder.py`](ex5/ft_water_reminder.py) | Using a condition to remind the user to water plants after more than two days. |
| `ex6` | [`ft_count_harvest_iterative.py`](ex6/ft_count_harvest_iterative.py) | Counting days with a `for` loop and handling non-numeric input via `try/except`. |
| `ex6` | [`ft_count_harvest_recursive.py`](ex6/ft_count_harvest_recursive.py) | Solving the same countdown recursively, with a base case and `ValueError` handling. |
| `ex7` | [`ft_seed_inventory.py`](ex7/ft_seed_inventory.py) | Using parameters, type annotations and conditions to display inventory in packets, grams or area. |

### How to run

**Note:** these files define functions but do not call them automatically. Running a script directly with `python3 file.py` will produce no output until its function is invoked. From the repository root, import and call the relevant function:

Example for `ex0`:

```bash
python3 -c "from ex0.ft_hello_garden import ft_hello_garden; ft_hello_garden()"
```

Example for `ex2` (prompts for length and width):

```bash
python3 -c "from ex2.ft_plot_area import ft_plot_area; ft_plot_area()"
```

Example for `ex7` (requires arguments):

```bash
python3 -c "from ex7.ft_seed_inventory import ft_seed_inventory; ft_seed_inventory('tomato', 12, 'packets')"
```

The exercises require **Python 3**. No external package dependencies are evident in the submitted files.

### Learning outcomes

- Writing functions, passing arguments and printing output.
- Receiving user input, converting values and performing basic arithmetic.
- Using conditionals to make simple decisions.
- Comparing iteration and recursion to solve the same task.
- Handling invalid numeric input in `ex6`.
- Adding parameter and return type annotations in `ex7`.

**Status:** early-stage educational exercises, not a complete application or production project. This repository documents a specific stage of my programming studies.

---

## Autor / Author

**Juan A. Pedraza** · [GitHub](https://github.com/jpedraza42) · [Portfolio](https://jpedraza42.github.io/Jpedraza42/)
