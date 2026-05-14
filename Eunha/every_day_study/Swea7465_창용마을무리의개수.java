package every_day_study;

import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;
import java.util.Stack;

public class Swea7465_창용마을무리의개수 {

	static List<Integer>[] bestie;
	static boolean[] visited;
	static int n, count;

	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();// n명이 있고
			int m = sc.nextInt();// m개의 관계를 말해줄거야.
			count=0;

			bestie = new LinkedList[n + 1];// 난 그걸 리스트에 담는거지 LinkedList를 배열 한칸에 넣을거니까 이렇게 작성하는거다. 1번부터 사용할거야.
			visited = new boolean[n + 1];

			for (int i = 1; i <= n; i++) {// 인덱스 1부터 넣어.
//				bestie = new LinkedList<>();//이렇게 생성하면서 갯수를 확보해두는게 맞나? 놉 이렇게 되면 bestie를 덮어쓰는거 밖에 안됨.
				bestie[i] = new LinkedList<>();// 배열 각 칸에 LinkedLsit를 넣어준다.
			}

			for (int j = 0; j < m; j++) {
				int a = sc.nextInt();
				int b = sc.nextInt();

				bestie[a].add(b);// a랑 b가 친하다 저장
				bestie[b].add(a);// b랑 a가 친하다 저장
			} // 할당 끝

			for(int i=1;i<=n;i++) {//n명 모두 방문.
				
				if(!visited[i]) {
					count++;
					dfs(i);
				}
			}

			System.out.println("#" + tc + " " + count);

		}
		sc.close();
	}

	private static void dfs(int start) {//*방문체크 관리하는 메서드 *stack or 재귀

//		for (int i = 1; i <= n; i++) {//메서드 안에 i가 없어서 쓰이지 않음. 지금 반복하는게 아니라 인덱스 접근을 위해 사용하는거였잖아.

			Stack<Integer> stack = new Stack<>();
			
			visited[start] = true;
			stack.push(start);
			
			while(!stack.isEmpty()) {
				int now = stack.pop();
				
				for(int tmp : bestie[now]) {
					
					if(!visited[tmp]) {
						visited[tmp] = true;
						stack.push(tmp);
					}
				}
			}
						

	}

}
