
public class Password{
    public int Longitud;
    public String Contraseña;

    public Password(int Longitud, String Contraseña){
        this.Longitud=Longitud;
        this.Contraseña=Contraseña;
    }
    public int getLongitud() {
        return Longitud;
    }

    public String getContraseña() {
        return Contraseña;
    }
    public void setLongitud(int longitud) {
        this.Longitud = longitud;
    }

    public void setContraseña(String contraseña) {
        this.Contraseña = contraseña;
    }
}