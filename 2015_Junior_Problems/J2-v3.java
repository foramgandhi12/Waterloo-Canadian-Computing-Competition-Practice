/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

package happy.or.sad;

/**
 * Foram Gandhi
 * Happy or Sad
 */
import java.util.Scanner;
public class HappyOrSad {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        
        String sentence, sentence_sub, sentence_sub2;
        int happy, sad, numhappy, numsad;
        
        Scanner input= new Scanner(System.in);
        
        System.out.print("Enter the text message: ");
            sentence=input.nextLine();
            
        numhappy=0;
        numsad=0;
        
        for (int counter=0; counter>=0; counter++)
        {
        happy=sentence.indexOf(":-)");
        sad=sentence.indexOf(":-(");
           
        sentence_sub=sentence.substring(happy);
            numhappy+=1;
        
        sentence_sub2=sentence.substring(sad);
            numsad+=1;
        }
        
        if (numhappy>numsad)
         {
            System.out.print("happy");
         }
        
        else if (numhappy==numsad)
         {
            System.out.print("unsure");
         }
        
        else if (numhappy==0 && numsad==0)
         {
            System.out.print("none");
         }
        
        else 
         {
            System.out.print("sad");
         }
        
    }
    
}
