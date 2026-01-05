import java.io.*;
import java.util.*;

public class Main {
    static int[][] map = new int[5][5];
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static boolean possible = false;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 맵 초기화
        // 사과: 1, 빈칸: 0, 장애물: -1
        for(int i = 0; i < 5; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j = 0; j < 5; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        // 시작 위치
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        dfs(r, c, 0, 0);

        System.out.println(possible ? 1 : 0);
    }

    public static void dfs(int x, int y, int depth, int apples){
        // 위치에 사과가 있다면 1 증가
        if(map[x][y] == 1){
            apples++;
        }
        // 사과가 2개 이상이라면 3번안에 먹기 가능
        if(apples >=2){
            possible = true;
            return;
        }
        // 3번의 이동에도 사과를 2개 먹지 못함
        if(depth == 3){
            return;
        }
        
        // 방문했다면 장애물로 바뀜
        int temp = map[x][y];
        map[x][y] = -1;

        for(int i = 0; i < 4; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];

            if(nx >= 0 && nx < 5 && ny >= 0 && ny < 5 && map[nx][ny] != -1){
                dfs(nx, ny, depth + 1, apples);
                if(possible){
                    return;
                }
            }
        }
        map[x][y] = temp;
    }
}
