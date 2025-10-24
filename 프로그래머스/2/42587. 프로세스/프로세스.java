import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] priorities, int location) {
        Queue<Integer> queue = new LinkedList<>();
        
        for (int i = 0; i < priorities.length; i++) {
            queue.add(i);
        }
        
        int count = 0;
        
        while(!queue.isEmpty()){
            boolean has = false;
            
            int currentIndex = queue.poll();
            int currentProcess = priorities[currentIndex];
                
            for(int indexQueue : queue){
                if(currentProcess < priorities[indexQueue]){
                    has = true;
                    break;
                }
            }
            if(has){
                queue.add(currentIndex);
            } else{
                count++;
                
                if (currentIndex == location){
                    return count;
                }
            }
        }
        return -1;
    }
}