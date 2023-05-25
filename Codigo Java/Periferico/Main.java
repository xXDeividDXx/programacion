public class Main {
    public static void main(String[] args){
        Periferico periferico = new Periferico(1234,"Logitech" , "G69");
        Teclado teclado = new Teclado(2, "Corsair", "K95 Platinum XT", "Aluminio", "Mecánico", "USB");
        Pantalla pantalla = new Pantalla(3, "ASUS", "TUPUTAMADRE", "4K Full HD", 32, 144);
    
        periferico.getdatos();
        teclado.mostrardatos();
        pantalla.mostrardatos();
    }
}
