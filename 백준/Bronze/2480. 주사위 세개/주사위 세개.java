import java.util.*;
import java.io.*;

class Main {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();


        if(a!=b && b!=c && c!=a){
            int max = 0;
            //a가 b보다 큰경우
            if(a>b){
                //a가 c보다 큰경우
                if(a>c){
                    max = a;
                }//c가 a보다 큰경우
                else{
                    max = c;
                }
            }
            //b가 a보다 큰경우
            else{
                //b가 c보다 큰 경우
                if(b>c){
                    max = b;
                }//c가 b보다 큰경우
                else{
                    max = c;
                }
            }
            System.out.println(max*100);
        }// 같은게 있는경우
        else{
            if(a==b && b==c){
                System.out.println(10000+ a*1000);
            }
            else{
                if(a==b || a==c){
                    System.out.println(1000 + a*100);
                }else{
                    System.out.println(1000+ b*100);
                }
            }
        }


    }
}