package every_day_study;

import java.util.ArrayDeque;
import java.util.Queue;
import java.util.Scanner;

public class Swea1267_작업순서 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		StringBuilder sb = new StringBuilder();

		for (int tc = 1; tc <= 10; tc++) {
			int v = sc.nextInt();
			int e = sc.nextInt();

			int[][] box = new int[v + 1][v + 1];// 인접행렬
			int[] check = new int[v + 1];// 진입차수 저장

			for (int i = 1; i <= e; i++) {
				int from = sc.nextInt();
				int to = sc.nextInt();

				box[from][to] = 1;// 유향이니까
				check[to]++;
			} // 입력완료

			Queue<Integer> q = new ArrayDeque<>();
			Queue<Integer> ans = new ArrayDeque<>();

			for (int i = 1; i < v+1; i++) {//*check의 크기가 v+1.
				if (check[i] == 0) {
					q.add(i);
				}
			} // 처음에 deque에 들어가야하는 숫자 넣기

			while (!q.isEmpty()) {
				int tmp = q.poll();
				ans.add(tmp);

				for (int to = 1; to < v + 1; to++) {
					if (box[tmp][to] == 1) {//*인접행렬에서 둘이 인접한건지 확인하고
						check[to]--;

						if (check[to] == 0) {
							q.add(to);
						}
					}

				}
			}
			
			sb.append("#").append(tc);
			while(!ans.isEmpty()) {
				sb.append(" ").append(ans.poll());
			}
			sb.append("\n");//*각 테케 끝나고 줄바꿈
			
		}//테케 끝
		
		System.out.println(sb);//*테케 다 끝나고 마지막에 출력해야지. 
	}//메인 끝
}//클래스 끝
//12시 7분
