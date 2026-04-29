package every_day_study;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Swea1219_길찾기 {
	
	static List<Integer>[] graph;//배열한칸에 리스트가 들어 있는 형태
	static boolean[] visited;
	
	
public static void main(String[] args) {
	
	Scanner sc = new Scanner(System.in);
	
	for(int tc=0;tc<10;tc++) {
		
		int T = sc.nextInt();
		int line = sc.nextInt();
		
		graph = new ArrayList[100];
		visited = new boolean[100];
		
		for(int i=0;i<100;i++) {
			graph[i] = new ArrayList<>();
		}
		
		for(int i=0;i<line;i++) {
			int from = sc.nextInt();
			int to = sc.nextInt();
			
			graph[from].add(to);//리스트에 넣으려면 .add()로
		}//할당 끝
		
		boolean dap = dfs(0);//dfs(0)으로 나온 답을 바로 dap에 넣어버리기
		
		System.out.println("#"+T+" "+(dap ? 1: 0));//sysout안에 삼항연산자 바로 넣어도 되네 굿
		
	}
}

private static boolean dfs(int start) {
	//종료
	if(start==99) return true;
	visited[start] = true;
	
	for(int next : graph[start]) {//for(int i=0;i<graph[start].size();i++) 
										//int next = graph[start].get(i);랑 동일
										//graph[start]사이즈를 모르지만 모두 돌아야할 때 사용하면 유용
		if(!visited[next]) {			
			if(dfs(next)) return true;
		}//next에서 99까지 갈 수 있으면 true를 전달하는거야. (아직 잘 모르겠음)
	}
	return false;
	
}
}
