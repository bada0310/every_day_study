package every_day_study;

import java.util.Scanner;

public class SecondSwea2817_부분수열의합 {
	static int n, k, count;
	static int[]row;
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();
			k = sc.nextInt();
			row = new int[n];

			for (int i = 0; i < n; i++) {
				row[i] = sc.nextInt();

			} // 할당 끝
			
			count =0;
			solve(0, 0);//0번 인덱스부터, 현재 합 0으로 시작.
			
			System.out.println("#" + tc+ " "+count);
		}
	}
	
	private static void solve(int idx, int sum) {
		if(idx ==n) {//인덱스를 끝까지 돌아도 그 전에 부분수열이 된 애들이 밑의 재귀식에 걸려서 결국엔 남아 있을 것.
			if(sum==k) count++;
			return;
		}
		
		solve(idx +1, sum + row[idx]);//인덱스는 넘어가는데 그 값을 더하는 경우
		solve(idx+1, sum);//인덱스는 넘어가지만 지금 해당 값은 제외하고.
	}
}
//8시 27분
