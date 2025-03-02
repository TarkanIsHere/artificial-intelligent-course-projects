package sifrekirici;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;
import java.util.List;
import java.lang.System;

public class sifreBulucu {          
    private String sifre;
    private List<Kromozom> population;
    private int kromozomCount;
    private int geneCount;
    public int generationCount;
    public int time;
    private boolean found = false;
    
    
    public sifreBulucu(String sifre,int kromozomCount){
        this.sifre = sifre;
        this.geneCount = sifre.length();
        this.kromozomCount = kromozomCount;
        this.population = new ArrayList<>();

        
    }
    
    public class Kromozom implements Comparable<Kromozom>{
        public String kromozom;
        public int fitness;
        
        public Kromozom(String x){
            this.kromozom = x;
        }
        @Override
        public int compareTo(Kromozom y){
                return Integer.compare(this.fitness, y.fitness);
        }
    }
    
    public void sifreKir(){
        long start = System.nanoTime();                         //geçen zamanı ölçmek için başlangıç noktası
        
        for (int i = 0; i < kromozomCount; i++) {
            Kromozom x = new Kromozom(createGnome(geneCount));
            population.add(x);
        }
        while(!found){
            List<Kromozom> newPopulation = new ArrayList<>();
            
            fitness();                                      //FITNESS
            
            Collections.sort(population);
            if (population.get(0).fitness == 0) {
                found = true;
                break;
            }
            
            for(int i =0;i<population.size();i++){           //CROSSOVER & MUTATION
                
                Kromozom parent1 = selection();
                Kromozom parent2 = selection();
                Kromozom child = new Kromozom(crossOver(parent1.kromozom, parent2.kromozom, geneCount));
                newPopulation.add(child);
            }
            
            System.out.print("Generasyon:" + generationCount + "|\t|"); 
            System.out.print("Cozume en yakin:" + population.get(0).kromozom + "|\t|");
            System.out.println("Farklilik:" + population.get(0).fitness); 
            population = newPopulation;
            generationCount++; 
        }
        
        long finish = System.nanoTime();                        //geçen zamanı ölçmek için bitiş noktası
        long gecenZaman = finish - start;
        
        System.out.print("Generasyon:" + generationCount + "|\t|");
        System.out.print("Bulunan sifre:" + population.get(0).kromozom + "|\t|"); 
        System.out.println("Farklilik:" + population.get(0).fitness); 
        System.out.println("Harcanan Zaman(ms):" + gecenZaman/1000000 + "ms");
        

    }
    
    public void fitness(){                                      //bütün popülsayonun skorunu hesaplayan kod(yüksek skor = kötü)
        
        for (int i = 0; i < population.size(); i++) {
            int score = 0;
            for (int j = 0; j < geneCount; j++) {
                if (population.get(i).kromozom.charAt(j) != sifre.charAt(j)) {
                   score++;
                }
            }
            population.get(i).fitness = score;
        }
    }
    
    public Kromozom selection(){
        int r = randomInt(50);
        return population.get(r);
    }
    
    private int randomInt(int size) {                           //rastgele sayı yaratıcı
        Random random = new Random();
        return random.nextInt(0, size);
    }

    private char newMutatedGen() {                              //rastgele bir char seçip returnlemek için
        final String GENES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890,.-;:_!\"#%&/()=?@${[]}";
        int index = randomInt(GENES.length());
        return GENES.charAt(index);
    }

    private String createGnome(int size) {                      //kromozom yaratıcı
        StringBuilder gnome = new StringBuilder();
        for (int i = 0; i<size; i++) {
            gnome.append(newMutatedGen());
        }
        return gnome.toString();
    }

    private String crossOver(String parent0, String parent1, int size) {        //CROSSOVER & MUTATION
        StringBuilder crossedGnome = new StringBuilder();
        for (int i = 0; i<size; i++) {
            int parentNum = randomInt(100);
            if (parentNum < 45) {
                crossedGnome.append(parent0.charAt(i));
            }
            else if (parentNum < 90) {
                crossedGnome.append(parent1.charAt(i));
            }
            else {                                                              //MUTATION
                crossedGnome.append(newMutatedGen());
            }
        }
        return crossedGnome.toString();
    }
}
