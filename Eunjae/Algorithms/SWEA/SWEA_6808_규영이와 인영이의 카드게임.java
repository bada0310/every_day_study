package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;

//핵심 아이디어 1-18까지의 숫자를 인영이와 규영이가 나눠가지는 것임
// 둘중에 한 사람의 합이 큰경우 그 사람이 이기는 것
//즉 1-18까지의 합은 171이고 그중 86이상이면 그 사람이 이김

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class SWEA_6808_규영이와 인영이의 카드게임 {
	static int win, lose; // 규영이가 이기냐 지냐
	static int[] gyucards;
	static int[] incards;
	static boolean[] isgyucard;// 규영이가 해당 카드를 받았는지 확인해야 얘가 안받은 카드로 인영이 카드 할당 가능
	static boolean[] visited; // 규영이 카드는 어짜피 고정임. 내는 순서도, 그랬을때 그 카드 고정해두고, 인영이 값 포문 돌려가면서 경우의 수 따져보기
	// 인영이 카드 방문체크
	static int[] factorial = { 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880 }; // 매 계산마다 팩토리얼 계산 안하고 미리 리스트 만들어서 필요한 경우
																				// 가져다 쓰기
	// 3!은 factorial[3]

	public static void main(String[] args) throws Exception {

		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int T = Integer.parseInt(br.readLine());

		for (int tc = 1; tc <= T; tc++) {

			isgyucard = new boolean[19];
			gyucards = new int[9];
			incards = new int[9];
			visited = new boolean[9];

			StringTokenizer st = new StringTokenizer(br.readLine());

			// 규영이 값 받기
			for (int i = 0; i < 9; i++) {
				gyucards[i] = Integer.parseInt(st.nextToken());
				isgyucard[gyucards[i]] = true;
			} // 규영값

			// 인영이 값 결정
			int index = 0;
			for (int i = 1; i <= 18; i++) {
				if (!isgyucard[i]) {
					incards[index++] = i;
				}

			} // 인영값

			win = 0;
			lose = 0;

			dfs(0, 0, 0); // dfs(뎁스, 규영스코어, 인영스코어)????

			System.out.println("#" + tc + " " + win + " " + lose);

		} // 테케

	}// main

	static void dfs(int depth, int gyuscore, int inscore) {

		// 규영이 카드 고정된 채 인영이 카드 따져보기
		// 1. 재귀 탈출조건이자 가지치기
		// 앞에서 부터 해오다가 둘 중 한 사람이라도값이 86이상이 되면 뒤에는 안해봐도 어짜피 그 사람이 이기는 거기 때문에
		// 그 사람에게(즉 위너에게) 뒤의 경우의 수도 다 더해주면 됨
		if (gyuscore > 85) {
			win += factorial[9 - depth];
			return;
		}

		if (inscore > 85) {
			lose += factorial[9 - depth];
			return;
		}

		if (depth == 9) {
			return;
		}

		// 2.인영이 카드 포문돌리면서 경우의 수 따지기
		// depth 즉 실행라운드, 즉 규영이의 카드는고정된 채, 인영이의 카드 포문으로 돌려가며 경우의 수 따지기
		for (int i = 0; i < 9; i++) {

			if (!visited[i]) {
				visited[i] = true;

				int gyucard = gyucards[depth];
				int incard = incards[i];

				if (gyucard > incard) {
					dfs(depth + 1, gyuscore + gyucard + incard, inscore);
				}

				else if (incard > gyucard) {
					dfs(depth + 1, gyuscore, inscore + incard + gyucard);

				}

				// 복원과정이 있어야 다음 경우의 수에서 해당 카드도 고려될 수 있음
				visited[i] = false;
			}
		}

	}
}
