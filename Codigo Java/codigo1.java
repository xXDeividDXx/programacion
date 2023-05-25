import java.util.Scanner;
public class codigo1{

    public static void imprimirMatriz(int[][]m){
        Scanner lector = new Scanner(System.in);
        for(int i=0;i<3;i++)
           for(int j=0;j<3;j++){
            System.out.println(m[i][j] + " ");
           }
           System.out.println(" ");
    }
    public static void main(String[] args){
        int[][]cubo =new int[3][3];
        imprimirMatriz(cubo);
    }
}