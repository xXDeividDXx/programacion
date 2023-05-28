package Instrumento;

public class Percusion extends InstrumentoMusical {
    private String sonido;

    public Percusion(String nombre, String sonido){
        super(nombre);
        this.sonido=sonido;
    }

    public void emitirsonido(){
        System.out.println("El instrumento llamado " + super.getNombre() + " hace " + sonido);
    }
    
        
}
