public class ejercicio1 {
    public static String reemplazarLetra(String cadena) {
    char[] chars = cadena.toCharArray();
    for (int i = 0; i < chars.length; i++) {
        chars[i]++;
    }
    return new String(chars);
}

public static void main(String[] args) {
    String cadena = "Hola";
    System.out.println(reemplazarLetra(cadena));
}
}