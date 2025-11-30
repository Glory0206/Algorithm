import java.util.*;
import java.io.*;

public class Main{
  // 동서남북
  static int[] dx = {0, 0, 1, -1};
  static int[] dy = {1, -1, 0, 0};
  
  static int[][] map;
  static boolean[][] visited;
  static int N;
  
  public static void main(String args[]) throws IOException{
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    N = Integer.parseInt(br.readLine());

    // 지도 정의
    map = new int[N][N];
    visited = new boolean[N][N];
    List<Integer> apartSizes = new ArrayList<>();
    
    for(int i=0; i<N; i++){
      String arr = br.readLine();
      for(int j=0; j<N; j++){
        map[i][j] = arr.charAt(j) - '0';
      }
    }

    for(int i=0; i<N; i++){
      for(int j=0; j<N; j++){
        if(map[i][j] == 1 && !visited[i][j]){
          apartSizes.add(dfs(i, j));
        }
      }
    }

    Collections.sort(apartSizes);

    System.out.println(apartSizes.size());
    
    for(int apartSize: apartSizes){
      System.out.println(apartSize);
    }
  }

  static int dfs(int i, int j){
    // 방문 완료
    visited[i][j] = true;
    int apart = 1;

    for(int z=0; z<4; z++){
      // 현재 위치 기준 동서남북 이동
      int nx = i + dx[z];
      int ny = j + dy[z];

      // map 밖을 벗어난다면
      if(nx < 0 || ny < 0 || nx >= N || ny >= N){
        continue;
      }
      // 방문했던 곳이라면
      if(visited[nx][ny]){
        continue;
      }
      // 아파트가 존재하지 않는다면
      if(map[nx][ny] != 1){
        continue;
      }

      apart += dfs(nx, ny);
    }

    return apart;
  }
}
