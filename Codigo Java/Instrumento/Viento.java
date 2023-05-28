package Instrumento;

public class Viento extends InstrumentoMusical{
    private String sonido;

    public Viento(String nombre, String sonido){
        super(nombre);
        this.sonido=sonido;
    }
}
