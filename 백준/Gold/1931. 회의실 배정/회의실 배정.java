import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        List<int[]> list = new ArrayList<>();
        for(int i=0; i<N; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            list.add(new int[]{start, end});
        }

        // 끝나는 시간을 기준으로 오름차순 정렬, 끝나는 시간이 같을 경우 시작 시간을 기준으로 오름차순 정렬
        // return값이 -인 경우 a가 좌측, +인 경우 b가 좌측(오름차순 정렬)
        list.sort((a, b) -> {
            if(a[1] == b[1]){ // 끝나는 시간이 같은 경우
                return a[0] - b[0];
            } else{
                return a[1] - b[1];
            }
        });

        int count = 0;
        int temp = 0;

        for(int i=0; i<N; i++){
            int getStart = list.get(i)[0];
            int getEnd = list.get(i)[1];

            if(getStart >= temp){
                count++;
                temp = getEnd;
            }
        }
        System.out.println(count);
    }
}