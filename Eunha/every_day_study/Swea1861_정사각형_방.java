package every_day_study;

import java.util.Scanner;

public class Swea1861_정사각형_방 {
	
	static int[] dr = {-1, 0, 1, 0};
	static int[] dc = {0, 1, 0, -1};
	
	static int[][] box, store;
	static int n;
	
	public static void main(String[] args) {

		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		
		for(int tc=1;tc<=T;tc++) {
			
		n = sc.nextInt();
		
		box = new int[n][n];
		store = new int[n][n];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				box[i][j] = sc.nextInt();
			}
		} // 할당 끝
		
		int answerRoom = Integer.MAX_VALUE;//얘를 sysout할거야
		int maxLength=0;//얘도
		
		for(int i=0;i<n;i++) {
			for(int j=0;j<n;j++) {
				
				int length = dfs(i, j);
				
				if(length>maxLength) {
					maxLength = length;
					answerRoom = box[i][j];
				} else if(length==maxLength && box[i][j] < answerRoom){
					answerRoom = box[i][j];
				}
			}
		}
			System.out.println("#"+ tc + " "+answerRoom +" "+ maxLength);
	}
	}//메인 끝

	private static int dfs(int i, int j) {
		
		if(store[i][j]!=0) {
			return store[i][j];//이미 방문한 곳이라면 return하라.
		}
		
		store[i][j] =1;//일단 본인 방 하나는 무조건 포함하게.
		
		for(int k=0;k<4;k++) {
			
			int nextR = i+dr[k];
			int nextC = j + dc[k];
			
			//조건1
			if(nextR<0 || nextR>=n || nextC<0 || nextC>=n) continue;//*or로 연결해야해 
			
			//조건2
			if(box[nextR][nextC] - box[i][j] == 1) {
				store[i][j] = dfs(nextR, nextC) +1; //뒤에 더하는 1은 현재 본인 방.
				break;//4방향을 모두 탐색하지 않았는데도 break할 수 있는 이유는 방 번호는 중복이 되지 않으니까 
				//다음 차례에 갈 수 있는 길은 오직 하나다. 그걸 찾았으니 break해야한다.
			}
		}
		return store[i][j];
		
	}

}//클래스 끝
//3시 22분
