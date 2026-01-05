import java.io.*;

public class Main {
    static long[] t;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        t = new long[n+1];

        System.out.println(cal(n));
    }

    public static long cal(int n){
        if(n == 0){
            return 1;
        }

        t[0] = 1;

        for(int i = 1; i <= n; i++){
            for(int j=0; j<i; j++){
                t[i] += t[j] * t[i-1-j];
            }
        }

        return t[n];
    }
}