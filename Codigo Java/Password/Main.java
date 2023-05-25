public class Main {
    public static void main(String[] args) {
        Contraseña password = new Contraseña(8, "miContraseña");
        System.out.println("Longitud de la contraseña: " + password.getLongitud());
        System.out.println("Contraseña: " + password.getContraseña());

        password.setContraseña("nuevaContraseña");
        System.out.println("Contraseña actualizada: " + password.getContraseña());
    }
}

