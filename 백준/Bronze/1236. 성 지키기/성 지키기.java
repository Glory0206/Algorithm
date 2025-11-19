import java.util.*;
import java.io.*;

public class Main{
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    boolean[] hasGuardRow = new boolean[N];
    boolean[] hasGuardCol = new boolean[M];

    for (int i = 0; i < N; i++) {
        String line = br.readLine();
        for (int j = 0; j < M; j++) {
            if (line.charAt(j) == 'X') {
                hasGuardRow[i] = true;
                hasGuardCol[j] = true;
            }
        }
    }
    
    int rowNeed = 0;
    
    for (boolean b : hasGuardRow) {
        if (!b) rowNeed++;
    }

    int colNeed = 0;
    for (boolean b : hasGuardCol) {
        if (!b) colNeed++;
    }

    System.out.println(Math.max(rowNeed, colNeed));
  }
}
