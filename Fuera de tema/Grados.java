// Grados.java
// Convierte grados Fahrenheit a Celsius según lo introducido por el usuario.

import java.util.Scanner;

public class Grados {
    public static double fToC(double fahrenheit) {
        return (fahrenheit - 32.0) * 5.0 / 9.0;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Introduce grados Fahrenheit (ej. 73.4): ");
        String raw;
        try {
            raw = sc.nextLine().trim();
        } catch (Exception e) {
            System.out.println("No se pudo leer la entrada.");
            sc.close();
            return;
        }
        raw = raw.replace(',', '.');
        try {
            double f = Double.parseDouble(raw);
            double c = fToC(f);
            System.out.printf("%.2f °F son %.2f °C%n", f, c);
        } catch (NumberFormatException e) {
            System.out.println("Entrada no válida. Introduce un número.");
        } finally {
            sc.close();
        }
    }
}
