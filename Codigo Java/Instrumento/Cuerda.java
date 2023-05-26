package Instrumento;

public class Cuerda extends InstrumentoMusical {
    private String sonido;

    public Cuerda(String nombre, String sonido){
        super(nombre);
        this.sonido=sonido;
    }

    public void EmitirSonido(){
        System.out.println("El instrumento llamado "+super.getNombre()+" hace"+sonido);
    }

}
