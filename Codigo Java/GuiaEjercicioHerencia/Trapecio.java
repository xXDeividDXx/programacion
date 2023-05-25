package GuiaEjercicioHerencia;

public class Trapecio extends Cuadrilatero {
    public int ladoA;
    public int ladoB;
    public int ladoC;
    public int ladoD;
    public int ladoH;

    public Trapecio(int vertice1, int vertice2, int vertice3, int vertice4, int coordenadaX, int coordenadaY, int ladoA, int ladoB, int ladoC, int ladoD, int ladoH){
        super(vertice1, vertice2, vertice3, vertice4, coordenadaX, coordenadaY);
        this.ladoA=ladoA;
        this.ladoB=ladoB;
        this.ladoC=ladoC;
        this.ladoD=ladoD;
        this.ladoH=ladoH;
    }

    public void CalcularArea(){
        
    }
}
