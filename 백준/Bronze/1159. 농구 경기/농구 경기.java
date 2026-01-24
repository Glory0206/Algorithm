import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[] count = new int[26];

        for(int i = 0; i < n; i++){
            String name = br.readLine();
            char firstName = name.charAt(0);
            count[firstName-'a']++;
        }

        boolean found = false;
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < 26; i++){
            if(count[i] >= 5){
                sb.append((char)(i+'a'));
                found = true;
            }
        }

        if(found){
            System.out.println(sb.toString());
        } else{
            System.out.println("PREDAJA");
        }
    }
}
