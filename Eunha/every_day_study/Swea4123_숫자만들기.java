package every_day_study;

import java.util.Scanner;

public class Swea4123_숫자만들기 {

	static int n, min, max;
	static int[] yun, num;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			n = sc.nextInt();

			yun = new int[4];
			for (int k = 0; k < 4; k++) {
				yun[k] = sc.nextInt();
			}

			num = new int[n];
			for (int i = 0; i < n; i++) {
				num[i] = sc.nextInt();
			} // 할당 끝

			max = Integer.MIN_VALUE;//*전역 변수로 쓰려는걸 static에 올려놓고도 여기서 자료형까지 쓰면 지역변수로 하나 또 생성된거고, dfs메서드에서 바꾸는 max나 min 영향 X
			min = Integer.MAX_VALUE;

//			int tmp = dfs(0, 0);//이렇게 변수 하나에 담는건 메서드의 return값이 하나일 때 가능하다. 아니면 덮어씌워지는 대참사.
			dfs(1, num[0]);// 여기에는 인덱스가 아닌데 어떻게 넣어버리지? *숫자의 순서는 안바뀌니까 일단 첫 숫자는 넣어두기!

			int dap = max - min;//+-상관없이 두 숫자의 차를 구하는거면 빼기로도 충분.

			System.out.println("#" + tc + " " + dap);
		}
		sc.close();
	}

	private static void dfs(int idx, int sum) {// 여기 인덱스는 다음번에 들어올 숫자를 말하고 있다. sum은 지금 까지의 합.
		//*숫자를 마지막까지 쓴다면 max랑 min에 일단 갖다 대보기
		if (idx == n) {
			max = Math.max(max, sum);
			min = Math.min(min, sum);
			return;
		}
		
		//우리가 돌려봐야하는건 연산자.
		for (int i = 0; i < 4; i++) {
			if (yun[i] > 0) {
				yun[i]--;

				if (i == 0) {
					dfs(idx + 1, sum + num[idx]);
				} else if (i == 1) {
					dfs(idx + 1, sum - num[idx]);
				} else if (i == 2) {
					dfs(idx + 1, sum * num[idx]);
				} else if (i == 3) {
					dfs(idx + 1, sum / num[idx]);
				}
				yun[i]++;
			}
		}

	}// dfs메서드 끝

}// 클래스 끝
//8시 7분
//10시 23분 축적이 안되는 문제 찾기 시작