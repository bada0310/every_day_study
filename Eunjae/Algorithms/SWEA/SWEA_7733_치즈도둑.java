package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;


/* 
 1. 입력값 전부 받기(받으면서 입력값 중의 최대 값 찾기-> 이만큼까지만 for문 돌리면 되기때문)
 2. 해당일차일때, 그 일자보다 작은 값 방문체크, 큰 값 넘기면서 방문체크 초기화.
 3. 일차별로 해당일에 해당하는 맛 먹기-> 방문체크
3-1. 해당일자일때, 해당 맛 먹고, 먹지 않은 애를 시작점으로 삼음-> 큐에 넣기
3-2. 그 먹지 않은 애를 기준으로 사방탐색
3-3. 사방탐색하면서 찾은애들을 큐에 넣기
4. 조건 다 통과했으면, 그 애도 방문체크 상태변경
5. 해당일차 체크 다 끝났으면 최댓값갱신후, 다음 일차로 넘어감.
 */

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_7733_치즈도둑{
	static int N, ans;//한 변의 길이 2<=N<=100, ans:가장 많은 덩아리의 수
	static int[][] cheese;
	static boolean[][] eat;
	static int[] dr = {-1, 1, 0,0};
	static int[] dc = {0,0,-1,1};
	
	static class Pos{
		int r, c;

		public Pos(int r, int c) {
			super();
			this.r = r;
			this.c = c;
		}
	}// 위치 클래스
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt();
			cheese = new int[N][N];
			eat = new boolean[N][N];
			//1일차에는 치즈가 한덩이이니깐!
			ans =1; //0일차는 존재하는가? 고민해보기.
			
			int max = 1; //치즈 맛은 1~100이니까 1이하인 값이면 상관없다.
			for(int i=0; i<N; i++) {
				for(int j=0; j<N; j++) {
					cheese[i][j] = sc.nextInt();
					if(max<cheese[i][j]) {
						max = cheese[i][j];
					}	
				}
			}//치즈 입력과 가장 맛있는 맛도 알고 있음!! (최대값)
			
			//최고의 맛까지만 돌려보면 됨, 어짜피 그 초과값은 존재하지 않으니 의미없음
			//max<= 아닌 이유는 max날이 되면, 전부 다 먹어서 0이됨.
			for(int day =1; day<max; day++) {
				
				//2중 for문 돌려서 eat초기화하자
				for(int r=0; r<N; r++) {
					for(int c=0; c<N; c++) {
						//해당날짜보다 큰 맛은 방문안함.
						if(cheese[r][c] > day) {
							eat[r][c] =false;
						} else {
							eat[r][c] =true;
						}
					}
				}// 해당일자에 맞게 치즈는 다 먹은상태!
				
				//일자별로 치즈 다 먹은후, 덩어리 체크->bfs로 4방탐색하고, 덩어리 카운트
				int cnt =0; //이번 일차의 치즈 덩어리수
				Queue<Pos> q = new LinkedList<>();
				
				//행우선순회 방식으로 남은 치즈를 순회
				for(int i=0; i<N; i++) {
					for(int j=0; j<N; j++) {
						//먹었으면 넘어감.
						if(eat[i][j]) {
							continue;
						}
						
						//안 먹었으면 한덩이 가능범위 체크!
						q.add(new Pos(i,j));
						eat[i][j] = true; // 이제 이 부분은 먹은걸로 상태변경!
						cnt++; //한 번이라도 가능한 부분 나오면 그게 한덩이가 되기 때문에 카운트!
						
						//이제 이 덩이 첫부분에서 사방체크!
						while(!q.isEmpty()) { //큐가 비어있지 않으면 사방체크 고고
							Pos p = q.poll(); 
							//덩어리는 4방향으로 인접하면 +모양으로
							for(int d=0; d<4; d++) {
								//위치인덱
								int nr = p.r +dr[d];
								int nc = p.c +dc[d];
								
								//범위체크
								if(nr <0 || nc<0|| nr>= N || nc>=N) {
									continue;
								}
								
								//eat 체크 (이미 먹은 곳이면 넘어가
								if(eat[nr][nc]) {
									continue;
								}
								
								//위의 조건 다 통과했으면, 얘는 이제 먹은걸로 변경.
								eat[nr][nc] =true;
								q.add(new Pos(nr, nc));
								
							}//4방탐색.
							
						}//BFS 치즈덩어리 탐색.
						
					}//열for
					
				}//행for -> 안먹힌 치즈들 이중포문순회
				ans = Math.max(cnt, ans); //최대값 갱신. -> 해당일차의 덩어리가 최대덩어리가 되는가?
				
				
			}//일차별 for문.
			System.out.println("#"+tc+" "+ans);
		}//tc
	
	}//main
	
}
