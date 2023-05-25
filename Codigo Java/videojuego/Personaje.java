package videojuego;

public class Personaje {
    public int id;
    public String nombre;
    public int vida;
    public int exp;
    public int poder;

    public Personaje(int id, String nombre, int vida, int exp, int poder){
        this.id=id;
        this.nombre=nombre;
        this.vida=vida;
        this.exp=exp;
        this.poder=poder;
    }

    public void atacar(){
        System.out.println(nombre+ " esta atacando");
    }
}
