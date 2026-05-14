package every_day_study;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SecondSwea1225_암호생성기 {
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		for (int tc = 1; tc <= 10; tc++) {
			int T = sc.nextInt();
			Queue<Integer> queue = new LinkedList<>();
			for(int i=0;i<8;i++) {
				queue.offer(sc.nextInt());
			}//row 큐에 할당 완료
			
			out://*이렇게 나가면 좋겠는 마지막 반복문에 이름을 붙이면 break 이름;했을때 원하는 반복문까지 빠져나옴. 
			while(true) {
				for(int j=1;j<6;j++) {
					int tmp = queue.poll();
					
					tmp = tmp-j;//뺀 걸 다시 tmp에 넣고
					
					if(tmp<=0) {
						tmp=0;
						queue.offer(tmp);//*이렇게 까지 해야지 0이 들어간 암호문 최종 완성
						break out;
					}
					queue.offer(tmp);//그 tmp를 맨 뒤로 다시 집어 넣는다. 
				}
			}
			
			System.out.print("#"+tc);
			for(int num : queue) {
				System.out.print(" "+ num);
			}
			System.out.println();
		}//tc끝
	}
}

