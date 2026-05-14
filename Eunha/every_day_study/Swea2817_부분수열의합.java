package every_day_study;

import java.util.Scanner;

public class Swea2817_부분수열의합 {

	static int n, k, ans;//전역변수의 초기화 확인!
	static int[] row;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();//n개의 자연수
			k = sc.nextInt();//원하는 총 합계
			row = new int[n];
			ans=0;

			for (int i = 0; i < n; i++) {
				row[i] = sc.nextInt();
			} // 할당 완.

			dfs(0, 0);//메서드를 만들때 내가 만지고 싶은 인자의 갯수 생각하고 정하기

			System.out.println("#" + tc + " " + ans);
		} // 테케 끝
		
		sc.close();
	}// 메인 끝

	private static void dfs(int idx, int sum) {
		
		//종료조건
		if (sum == k) {// int형을 return하려면 어떻게 해야하지? 해결 return 1;
			ans++;
			return;
		} 
		
		//범위체크
		if(idx==n || sum>k) return;//범위가 넘어가면 return;
		//왜 여기 범위체크에서 idx=n이 되어야 하는거지? 지금 dfs로 들어오긴했지만 idx위치의 값을 더하지는 않은거라서 재취파트에서 현재 마지막 인덱스의 값을 더하고 나서 범위체크로 빼야하니까. 
		
		//재귀
		dfs(idx+1, sum+row[idx]);//현위치 숫자 더한거
		dfs(idx+1, sum);//현위치 숫자 안 더라고 넘어가

	}
}// 클래스 끝
//3시 25분
//결국 합이 k가 되는 묶음이 몇개인지 묻는 문제이기 때문에 boolean으로 check 할 필요는 없었다. 