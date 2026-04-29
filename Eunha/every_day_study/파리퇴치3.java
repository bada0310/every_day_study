package every_day_study;

import java.util.Scanner;

public class 파리퇴치3 {

	static int[][] box;// 근데 box크기를 정의 할 때 n을 넣어야 하는데 n은 static으로 안빼도 되나?
	static int n, m;

	static int[] plusDr = { -1, 0, 1, 0 };
	static int[] plusRow = { 0, 1, 0, -1 };

	static int[] axDr = { -1, 1, 1, -1 };
	static int[] axRow = { 1, 1, -1, -1 };

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();

		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();
			m = sc.nextInt();

			box = new int[n][n];

			for (int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					box[i][j] = sc.nextInt();
				}
			} // 할당 끝

			int ans=0;//초기화는 어떨때 하는거더라
			
			for (int x = 0; x < n; x++) {//스프레이 난사 중심을 for문 두개로 옮겨줘야해. 
				for (int y = 0; y < n; y++) {
					int plusSum = plus(x, y);
					int axSum = ax(x, y);
					
					ans =Math.max(ans, Math.max(plusSum, axSum));
				}
			}

			System.out.println("#"+tc+ " "+ans);

		} // 테케 끝
		sc.close();
	}// 메인 끝

	private static int plus(int i, int j) {
		int sum = box[i][j]; // 지금 중심 포함

		for (int x = 0; x < 4; x++) {// 뱡향 탐색
			for (int y = 1; y < m; y++) {// 얼마나?
				int plusR = i + plusDr[x] * y;
				int plusC = j + plusRow[x] * y;

				if (plusR >= 0 && plusC >= 0 && plusR < n && plusC < n) {
					sum += box[plusR][plusC]; // 넘어가라.가 아니고 이런 경우에만 sum에 담자
					//갱신하는게 아니라 누적하려면 연산자를 += 사용해야 해. 
				}
			}
		}
		return sum;
	}

	private static int ax(int i, int j) {
		int sum = box[i][j]; // 지금 중심 포함

		for (int x = 0; x < 4; x++) {// 뱡향 탐색
			for (int y = 1; y < m; y++) {// 얼마나?
				int plusR = i + axDr[x] * y;
				int plusC = j + axRow[x] * y;

				if (plusR >= 0 && plusC >= 0 && plusR < n && plusC < n) {
					sum += box[plusR][plusC]; // 넘어가라.가 아니고 이런 경우에만 sum에 담자
				}
			}
		}
		return sum;
	}
}// 클래스 끝
