2
import argparse
import csv
import random
import uuid
from datetime import datetime, timedelta

LIKERT_LABELS = [
    "Totalmente en desacuerdo",
    "En desacuerdo",
    "Ni de acuerdo ni en desacuerdo",
    "De acuerdo",
    "Totalmente de acuerdo",
]

GENDERS = ["Femenino", "Masculino"]

EXAMPLE_LABEL = "EJEMPLO DE ITEM"

ITEM_TEXTS = [
    "Considero que las personas del otro género suelen cumplir lo que prometen.",
    "Percibo que el género contrario acostumbra mostrar respeto hacia los demás.",
    "El género opuesto tiene habilidad para resolver problemas.",
    "El género opuesto suele expresar sus opiniones con firmeza.",
    "En mi experiencia, el género contrario respeta los compromisos que asumen.",
    "Atribuyo al género opuesto una actitud empática.",
    "Creo que el sexo opuesto es competente en su ámbito laboral o académico.",
    "Socialmente percibo que el sexo opuesto defiende sus ideas sin temor.",
    "Es común que perciba que el sexo opuesto no falla cuando asume una responsabilidad.",
    "El género opuesto suele mostrarse menos comprensivo en la convivencia diaria.",
    "Pienso que el género opuesto no sabe desempeñarse con eficacia.",
    "El género opuesto se asocia con la capacidad de expresar desacuerdos.",
    "En general, se cree que las personas del género opuesto son confiables.",
    "Creo que el género opuesto no demuestra interés por ayudar a los demás.",
    "Considero que quienes pertenecen al sexo contrario cuentan con recursos para enfrentar desafíos en la vida diaria.",
    "Siento que el género opuesto no sabe poner límites de manera clara.",
    "Pienso que el género opuesto no es sincero",
    "La imagen social del género opuesto está asociada con la amabilidad.",
    "A menudo se considera que el género opuesto tiene preparación suficiente para lograr buenos resultados.",
    "En general, el género opuesto se le atribuye seguridad al comunicarse.",
    "Al género opuesto se le reconoce constancia en los compromisos.",
    "Socialmente creo que el género opuesto refleja sensibilidad hacia las necesidades ajenas.",
    "Al género opuesto se le reconoce preparación para alcanzar objetivos.",
    "Pienso que el género opuesto manifiesta sus desacuerdos de manera adecuada.",
]


def generate_row_numeric():
    """Genera una fila con respuestas numéricas (1-5) internamente.

    La marca de tiempo se deja como `None` y se rellenará después.
    """
    edad = random.randint(18, 28)
    genero = random.choice(GENDERS)
    example_resp = random.randint(1, 5)
    responses = [random.randint(1, 5) for _ in range(len(ITEM_TEXTS))]
    return [None, edad, genero, example_resp] + responses


def main():
    parser = argparse.ArgumentParser(description="Genera un CSV (solo con las preguntas que diste) con respuestas aleatorias para la encuesta.")
    parser.add_argument("--n", type=int, default=None, help="Número de filas/participantes a generar (si no se especifica, se pedirá interactivamente)")
    parser.add_argument("--out", type=str, default="datos_encuesta.csv", help="Ruta del archivo CSV de salida")
    parser.add_argument("--labels", dest="labels", action="store_true", help="Usar etiquetas textuales (por defecto)")
    parser.add_argument("--numeric", dest="labels", action="store_false", help="Usar respuestas numéricas 1-5 en lugar de etiquetas")
    parser.add_argument("--reverse", type=str, default="10,11,14,16,17",
                        help="Lista separada por comas de números de ítems que deben invertirse (p. ej. 10,11,14)")
    parser.add_argument("--error-prob", type=float, default=0.0,
                        help="Probabilidad (0.0-1.0) de introducir un error en cada respuesta (cambio a categoría adyacente)")
    parser.add_argument("--date-from", type=str, default=None, help="Fecha inicial (día/mes/año) para las marcas de tiempo, por ejemplo 9/11/2025")
    parser.add_argument("--date-to", type=str, default=None, help="Fecha final (día/mes/año) para las marcas de tiempo, por ejemplo 10/11/2025")
    parser.add_argument("--start", type=str, default=None, help="Hora inicial en cada día (HH:MM o HH:MM:SS), por ejemplo 10:00 o 10:00:00")
    parser.add_argument("--end", type=str, default=None, help="Hora final en cada día (HH:MM or HH:MM:SS), por ejemplo 11:30")
    parser.set_defaults(labels=True)
    args = parser.parse_args()

    if args.n is None:
        while True:
            try:
                raw = input("¿Cuántas filas quieres generar? ").strip()
                n = int(raw)
                if n <= 0:
                    print("Introduce un número entero mayor que 0.")
                    continue
                args.n = n
                break
            except ValueError:
                print("Entrada no válida. Escribe un número entero, por ejemplo 50.")

    if args.date_from is None:
        args.date_from = input("Introduce la fecha inicial (día/mes/año), por ejemplo 9/11/2025: ").strip()
    if args.date_to is None:
        args.date_to = input("Introduce la fecha final (día/mes/año), por ejemplo 10/11/2025: ").strip()
    if args.start is None:
        args.start = input("Hora de inicio en cada día (HH:MM o HH:MM:SS), por ejemplo 10:00: ").strip()
    if args.end is None:
        args.end = input("Hora de fin en cada día (HH:MM o HH:MM:SS), por ejemplo 11:30: ").strip()

    def parse_date(date_str):
        for dfmt in ["%d/%m/%Y", "%d/%m/%y"]:
            try:
                return datetime.strptime(date_str, dfmt).date()
            except Exception:
                pass
        raise ValueError(f"Formato de fecha no válido: {date_str}")

    def parse_time(time_str):
        for tfmt in ["%H:%M:%S", "%H:%M"]:
            try:
                return datetime.strptime(time_str, tfmt).time()
            except Exception:
                pass
        raise ValueError(f"Formato de hora no válido: {time_str}")

    try:
        date_from = parse_date(args.date_from)
        date_to = parse_date(args.date_to)
        start_time = parse_time(args.start)
        end_time = parse_time(args.end)
    except ValueError as e:
        print(f"Error al parsear fecha/hora: {e}")
        return

    # Construir datetimes de inicio y fin
    start_dt = datetime.combine(date_from, start_time)
    end_dt = datetime.combine(date_to, end_time)

    if end_dt <= start_dt:
        print("La fecha/hora final debe ser posterior a la inicial.")
        return

    numbered_items = [f"{i}. {text}" for i, text in enumerate(ITEM_TEXTS, start=1)]

    # parse reverse items (1-based indices)
    try:
        reverse_items = set()
        for part in args.reverse.split(","):
            raw = part.strip()
            if not raw:
                continue
            idx = int(raw)
            if idx < 1 or idx > len(ITEM_TEXTS):
                raise ValueError(f"Ítem de reversa fuera de rango: {idx}")
            reverse_items.add(idx)
    except Exception as e:
        print(f"Error al parsear --reverse: {e}")
        return

    # Header: sólo columnas raw (sin columnas de 'score')
    header = ["Marca de tiempo", "Edad (18 - 28 años)", "Género", EXAMPLE_LABEL]
    for i, text in enumerate(ITEM_TEXTS, start=1):
        header.append(f"{i}. {text} (raw)")

    # función para generar un timestamp aleatorio entre start_dt y end_dt
    def random_timestamp(start: datetime, end: datetime) -> datetime:
        total_seconds = int((end - start).total_seconds())
        offset = random.randint(0, total_seconds)
        return start + timedelta(seconds=offset)

    # Generar filas en memoria con timestamps (datetime), luego ordenarlas y escribirlas
    rows = []
    for _ in range(args.n):
        row = generate_row_numeric()
        ts = random_timestamp(start_dt, end_dt)
        # guardar el datetime en la primera posición por ahora
        row[0] = ts
        rows.append(row)

    # ordenar por marca de tiempo ascendente
    rows.sort(key=lambda r: r[0])

    with open(args.out, "w", newline='', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for r in rows:
            ts = r[0]
            ts_str = f"{ts.day}/{ts.month}/{ts.year} {ts.hour:02d}:{ts.minute:02d}:{ts.second:02d}"
            # r structure: [ts, edad, genero, example_resp, item1, item2, ...]
            base = [ts_str, r[1], r[2]]

            # example response: show labels if requested, otherwise numeric
            example_numeric = r[3]
            if args.labels:
                example_out = LIKERT_LABELS[example_numeric - 1]
            else:
                example_out = example_numeric

            out_row = base + [example_out]

            # iterate items and produce only raw (sin columna score)
            for idx in range(1, len(ITEM_TEXTS) + 1):
                raw_val = r[3 + idx]

                # simulate measurement error: change to an adjacent category with prob args.error_prob
                if args.error_prob > 0.0 and random.random() < args.error_prob:
                    neighbors = []
                    if raw_val > 1:
                        neighbors.append(raw_val - 1)
                    if raw_val < 5:
                        neighbors.append(raw_val + 1)
                    if neighbors:
                        raw_val = random.choice(neighbors)

                if args.labels:
                    raw_out = LIKERT_LABELS[raw_val - 1]
                else:
                    raw_out = raw_val

                out_row.append(raw_out)

            writer.writerow(out_row)

    print(f"Archivo generado: {args.out} ({args.n} filas). Rango usado: {start_dt} -> {end_dt}")


if __name__ == "__main__":
    main()
