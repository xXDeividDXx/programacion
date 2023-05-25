public class Pantalla extends Periferico {
    private String resolucion;
    private int dimension;
    private int frecuencia;

    public Pantalla(int id, String marca, String modelo, String resolucion, int dimension, int frecuencia){
        super(id, marca, modelo);
        this.dimension=dimension;
        this.frecuencia=frecuencia;
        this.resolucion=resolucion;
    }

    public void mostrardatos(){
        System.out.println("la pantalla es de resolucion: "+resolucion);
        System.out.println("tiene una frecuencia de "+frecuencia);
        System.out.println("y es de "+dimension+" pulgadas.");
    }
}
