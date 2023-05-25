package EjemploGato;

public class Gato {
    String name;
    String sex;
    int age;
    int weight;
    String color;
    String texture;

    Gato(String name, String sex, int age, int weight, String color, String texture){
        this.name=name;
        this.sex=sex;
        this.age=age;
        this.weight=weight;
        this.color=color;
        this.texture=texture;
    }
    void eat(){
        System.out.println(this.name + " esta comiendo");
    }
}
