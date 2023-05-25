public class Periferico{
    private int id;
    private String marca;
    private String modelo;

    public Periferico(int id, String marca, String modelo){
        this.id = id;
        this.marca = marca;
        this.modelo = modelo;
    }

    public void getdatos(){
        System.out.println("el periferico tiene numero "+id+".");
        System.out.println("es de marca "+marca);
        System.out.println("y es del modelo "+modelo);   
    }
}
