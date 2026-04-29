package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;

import java.util.Scanner;

public class SWEA_2105_디저트카페 {
	static int N; // NxN크기의 정사각형 맵 4 <= N <= 20
	static int[][] map;
	// 우상, 우하, 좌하, 좌상
	static int[] dr = { -1, 1, 1, -1 };
	static int[] dc = { 1, 1, -1, -1 };
	static int ans;

	static class Cafe {
		int r, c; // 현재 카페의 위치

		public Cafe(int r, int c) {
			this.r = r;
			this.c = c;
		}
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for (int tc = 1; tc <= T; tc++) {
			N = sc.nextInt();
			map = new int[N + 2][N + 2]; // 디저트의 종류는 1이상 100이하의 정수
			// 따로 벽으로 처리할 필요는 없다. 0이 아니면 갈거야!
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j <= N; j++) {
					map[i][j] = sc.nextInt();
				}
			} // 입력 끝
			ans = 0;

			// 디저트투어!
			for (int i = 1; i < N + 1; i++) {
				for (int j = 1; j < N + 1; j++) {
					boolean[] eat = new boolean[101];
					eat[0] = true;
					Cafe start = new Cafe(i, j);
					move(start, start, eat, 0);
				}
			}

			System.out.println("#" + tc + " " + (ans == 0 ? -1 : ans));

		} // tc
	}// main

	// start의 위치로 dir 3인채로 들어가야 투어가 마무리가 되었다.
	static void move(Cafe st, Cafe curr, boolean[] eat, int dir) {
		// 종료파트
		if (st.r == curr.r && st.c == curr.c && dir == 3) {
			// 투어를 마쳤다!
			// 실제로 먹었던 디저트의 종류를 쳌
			// 아래의 cnt 부분은 인자로 누적으로 들고다니면 줄일 수 있음!
			int cnt = 0;
			for (int i = 1; i <= 100; i++) {
				if (eat[i])
					cnt++;
			}
			ans = Math.max(ans, cnt);
			return;
		}
		// 재귀파트
		// 0방향일떄는 0,1
		// 1방향일때는 1,2
		// 2방향일떄는 2,3
		// 3방향일때는 3
		for (int i = dir; i < dir + 2 && i < 4; i++) {
			int nr = curr.r + dr[i];
			int nc = curr.c + dc[i];

			// 벽으로 둘러쌓인 상태 범위체크를 할필요는 없다!
			// 내가 안먹은 디저트인지, 0은 아닌지
			int dessert = map[nr][nc];
//			if(!eat[dessert] && map[nr][nc] != 0) {
			// 벽인 0번을 먹었다라고 체크를 미리 해두면 조거쳌을 줄일 수 있을거 같다.
			if (!eat[dessert]) {
				eat[dessert] = true;
				move(st, new Cafe(nr, nc), eat, i);
				eat[dessert] = false;
			}
		}

	}

}

