package videojuego;

public class Heroe extends Personaje {
    public int sanacion;

    public Heroe(int id, String nombre, int vida, int exp, int poder, int sanacion){
        super(id, nombre, vida, exp, poder);
        this.sanacion=sanacion;
    }

    public void atacar(v:Villano){
        
    }
}
