public class Teclado extends Periferico {
    private String material;
    private String tiposwitch;
    private String conectividad;

    public Teclado(int id, String marca, String modelo, String material, String tiposwitch, String conectividad) {
        super(id, marca, modelo);
        this.material = material;
        this.tiposwitch = tiposwitch;
        this.conectividad = conectividad;
    }

    public void mostrardatos(){
        System.out.println("el teclado es de material "+material);
        System.out.println("tiene switch tipo "+tiposwitch);
        System.out.println("y tiene conectividad de tipo "+conectividad);
    }
}
