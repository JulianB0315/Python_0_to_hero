# Grados.py
# Convierte grados Fahrenheit a Celsius según lo introducido por el usuario.

def f_to_c(fahrenheit: float) -> float:
    return (fahrenheit - 32.0) * 5.0 / 9.0

def main():
    raw = input("Introduce grados Fahrenheit (ej. 73.4): ").strip()
    raw = raw.replace(",", ".")
    try:
        f = float(raw)
    except ValueError:
        print("Entrada no válida. Introduce un número.")
        return
    c = f_to_c(f)
    print(f"{f:.2f} °F son {c:.2f} °C")

if __name__ == "__main__":
    main()