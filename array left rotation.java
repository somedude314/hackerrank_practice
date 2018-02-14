import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;


public class MyClass {
    public static void main(String args[]) {
        
        // int[] array = {1,2,3,4,5};
        // rotate(array, 4);
        
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        int k = in.nextInt();
        int a[] = new int[n];
        for(int a_i=0; a_i < n; a_i++){
            a[a_i] = in.nextInt();
        }
      
        rotate(a, k);
      
        System.out.println();
    }
    
    public static void rotate(int[] array, int shiftCount) {
        for (int i = 0; i<shiftCount; i++){
            shift(array);
        } 
	printArray(array);
    }
    
    public static void shift(int[] array) {
        int size = array.length;
        int temp;
        temp = array[0];
        for(int i = 1 ; i <= size -1 ; i++) {
           array[i-1] = array[i];
        }
        array[size-1] = temp;
    }
    
    public static void printArray(int[] array) {
        for(int i = 0 ; i < array.length ; i++) {
           System.out.print(array[i] + " ");
        }
    }
}
