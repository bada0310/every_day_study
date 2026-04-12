package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;

//N퀸의 핵심 원리는 한행씩 내려가면서 퀸을 놓는것
//그렇기 때문에 내가 지금 퀸을 놓을지 말지 고려중인 row보다 밑에있는 row+1부터의 행에는
//어짜피 퀸이 없기 때문에 고려하지 않아도 됨. 즉 그 전의 선배퀸(?)들의 i<row만 확인해보면 됨
import java.util.Scanner;

public class SWEA_2806_N-Queen {
	static int N;
	static int[] col;
	static int ans;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N= sc.nextInt();
			col = new int[N];
			ans =0;
			make(0);
			System.out.println("#"+tc+" "+ ans);
		}
	}
	
	static void make (int row) {
		//탈출조건
		if(row == N) {
			ans++;
			return;
			
			
		}
		
		
		//받은 row값에 대해서 열을 이동시키면서 c값 배치시키기
		for(int c=0; c<N; c++) {
			col[row] =c;
			
			if(isPossible(row)) {
				make(row+1);
			}
		}
	}
	
	static boolean isPossible(int row) {
		
		for(int i=0; i<row; i++) {
			//col 배열의 값자체가 열의 위치 이니까 즉, 인덱스는 행, 값은 열인
			if(col[i] ==col[row]) {
				return false;
			}
			
			//같은 대각선이면 안됨
			//기울기 공식: x변화량과 y의 변화량이 같으면 즉, 대각선이 1이거나 -1이면
			//대각선임
			if(Math.abs(row-i) == Math.abs(col[row] - col[i])){
				return false;
				
			} 
			
		}
		return true;
		
	}
	

}