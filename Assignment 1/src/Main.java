/*Jessie Lazo ID: 017165640
CECS 378 Sec 11
02 October 2020*/
import java.util.*;

public class Main {
    static String alphabet = "abcdefghijklmnopqrstuvwxyz";

    /**
     * Returns a modified version of the lowercase alphabet by randomly scrambling a string of the alphabet
     * @return String, for use as a key
     */
    public static String[] createKey(){
        String key = "abcdefghijklmnopqrstuvwxyz";
        String[] alphaCopy = key.split("");//easier than manually filling out the array
        List<String> alphaList = Arrays.asList(alphaCopy);
        Collections.shuffle(alphaList);
        alphaList.toArray(alphaCopy);
        return(alphaCopy);
    }

    /**
     * Former half of the simple-substition cipher process which operates via replacing each character by another
     * one character relative to a key, assumes the given text is lowercase
     * @param plaintext the phrase entered to be encrypted into a cipher text
     * @param key the certain modified version of the alphabet for the encryption to base of, same key to be used in
     *            decryption
     * @return String, the encrypted message of the inputted phrase
     */
    public static String myEncrypt(String plaintext, String[] key){
        String cipher = "";
        Map<Character, String> keyMap = new HashMap<Character, String>();
        //Iterate through the alphabet and key simultaneously to create a map of the two in which the plaintext
        //can substitute letters of the original alphabet to the modified alphabet aka the key
        for(int i = 0; i < alphabet.length(); i++){
            keyMap.put(alphabet.charAt(i), key[i]);
        }
        for(int i = 0; i < plaintext.length(); i++){
            //to retain formatting only perform substitution to alphabetical characters
            if(Character.isAlphabetic(plaintext.charAt(i))){
                char temp = plaintext.charAt(i);
                cipher = cipher + keyMap.get(temp);
            }
            else{
                cipher += plaintext.charAt(i);
            }
        }
        return cipher;
    }

    /**
     * Latter half of the simple-substition cipher process, reverse substitution is used by comparing the ciphertext
     * to the key to return the original text, ciphertext should remain lowercase
     * @param cipher the desired ciphertext to be decrypted accordingly with the proper key
     * @param key the certain modified version of the alphabet for the decryption to utilize, same key as was used in
     *            the encryption process
     * @return String, the plaintext message which the ciphertext is based off
     */
    public static String decrypt(String cipher, String[] key){
        String pText = "";
        Map<Character, Character> keyMap = new HashMap<Character, Character>();
        //Similar creation of a map as in the encryption process however as the desired value desired is the original
        //alphabet, the key and values of the map are switched
        for(int i = 0; i < alphabet.length(); i++){
            keyMap.put((key[i].charAt(0)), alphabet.charAt(i));
        }
        for(int i = 0; i < cipher.length(); i++){
            //for formatting retention
            if(Character.isAlphabetic(cipher.charAt(i))){
                pText = pText + keyMap.get(cipher.charAt(i));
            }
            else{
                pText += cipher.charAt(i);
            }
        }
        return pText;
    }


    public static void main(String args[]){
        String first = "He who fights with monsters should look to it that he himself does " +
                "not become a monster . And if you gaze long into an abyss , the abyss " +
                "also gazes into you .";
        String second = "There is a theory which states that if ever anybody discovers " +
                "exactly what the Universe is for and why it is here , it will " +
                "instantly disappear and be replaced by something even more bizarre " +
                "and inexplicable . There is another theory which states that this " +
                "has already happened.";
        String third = "Whenever I find myself growing grim about the mouth ; whenever it is " +
                "a damp , drizzly November in my soul ; whenever I find myself " +
                "involuntarily pausing before coffin warehouses , and bringing up the " +
                "rear of every funeral I meet ; and especially whenever my hypos get " +
                "such an upper hand of me , that it requires a strong moral principle " +
                "to prevent me from deliberately stepping into the street , and " +
                "methodically knocking people ’ s hats off - then , I account it high " +
                "time to get to sea as soon as I can .";
        ArrayList<String> phrases = new ArrayList<String>();
        phrases.add(first);
        phrases.add(second);
        phrases.add(third);
        String[] key = createKey();
        System.out.print("Randomly generated key: ");
        for(String c : key){
            System.out.print(c);
        }
        System.out.println("");
        for(String s : phrases){
            String cText = myEncrypt(s.toLowerCase(), key);
            System.out.println("Ciphertext: " + cText);
            String pText = decrypt(cText, key);
            System.out.println("Plaintext: " + pText);
        }
    }
}
