import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Stack<Character> stack = new Stack<>();

        String str = br.readLine();
        String boom = br.readLine();
        int boomLen = boom.length();

        // Deque에 문자별로 넣기
        for(char c : str.toCharArray()) {
            stack.push(c);

            if(stack.size() >= boomLen) {
                boolean like = true;

                for(int i = 0; i < boomLen; i++) {
                    if(stack.get(stack.size() - boomLen + i) != boom.charAt(i)) {
                        like = false;
                        break;
                    }
                }

                if(like) {
                    for(int i=0; i<boomLen; i++) {
                        stack.pop();
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(char c : stack){
            sb.append(c);
        }
        System.out.println(sb.length() == 0 ? "FRULA" : sb);
    }
}