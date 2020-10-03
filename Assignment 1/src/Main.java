import java.nio.charset.Charset;
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
        System.out.println("KeyMap formatted as follows: ");
        System.out.println(keyMap);
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
        String[] key = createKey();
        System.out.print("Randomly generated key: ");
        for(String c : key){
            System.out.print(c);
        }
        System.out.println("");
        String cipher = myEncrypt("hello there", key);
        String decode = decrypt(cipher, key);

        System.out.println("Ciphertext: " + cipher);
        System.out.println("Plaintext: " + decode);
    }
}
