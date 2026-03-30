/*
 1. 4방향 위치 정의
 2. 터널타입별로 정의: 2차원 배열로 터널번호-우하좌상 0,1,2,3
 3. 탈주범위 정보 클래스 만들기(현재위치 행,열, 소요시간)
 4. main에서 값다 받기
 - map: 번호정보
 - 각종 변수
 -방문체크 배열
 - 탈주범 있을수있는 위치 초기화
 -bfs()함수 실행
 5.bfs 함수 정의
-큐 만들기
-큐에 현재값 집어넣기- 탈주범정보 
-방문체크 현재위치 체크!
5-1. while문 시작!! 큐가비어있지 않는한 계속돌아!
-큐에서 하나 꺼내와서 Person p로 받아
-만약 범인의 최종 리밋시간과 소요시간이 같으면
*break하면 안됨!! 그러면 while문이 종료되는데, while문은 q에 들어있는 값 다 확인하면서 이동가능한지 보는건데,,, 뒤에있는 애들을 다 못봄..
**다음파이프와 나의 반대방향이 일치하는지 체크!!!!**
-현재 있는곳의 터널타입(번호)
-그 타입의 우상좌우 번호를 받아와서, 다음 행열정보(nr,nc) 알기
-범위체크&방문체크
-해당인덱스 값이 0이면 파이프 없어서 거기도 못감
- 다음타입은 다음 인덱스로
-반대 방향은 현재방향에서 2칸 더 가고 %4하기
- 다음타입과 반대방향 일치하는지 체크하는 함수 사용
- 모든조건 다 통과하면 그 위치 방문체크
-ans도 늘리고
-그 값을 q에 넣기!!! (그래야지 얘를 기준으로 또 다음진행 가능한지 확인 가능-> 계속 전진해야함!!)
6. 다음타입이랑 반대방향 체크 함수
-터널 타입번호로 부터 가져온 우하좌상 번호와 방향 일치하는지 
-일치하면 true반환.
 */




package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class SWEA_1953_탈주범검거 {
	static int N, M, R, C, L, ans; //행, 열, 좌표(R,C), 소요된. 시간, ans:있을 수 있는 장소
	static int[][] map;
	static boolean[][] visited; //갔던 길 또 가지않게 하기 위해
	
	//우하좌상
	static int[] dr = {0,1,0,-1};
	static int[] dc = {1,0,-1,0};
	
	//터널을 정의 (타입별로) 1: +, 2:ㅣ, 3:-
	static int[][] tunnel = {
			{}, //0번 터널은 없으니 버림.
			{0,1,2,3}, //1번:우하좌상.
			{1,3},//2번:하,상.
			{0,2},
			{0,3},
			{0,1},
			{1,2},
			{2,3}
	};
	
	//탈주범의 정보-좌표위치, 시간.
	static class Person{
		int r, c, time;

		public Person(int r, int c, int time) {
			super();
			this.r = r;
			this.c = c;
			this.time = time;
		}
		
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		for(int tc=1; tc<=T; tc++) {
			N = sc.nextInt(); //행.
			M = sc.nextInt(); //열.
			R = sc.nextInt(); //맨홀의 행좌표.
			C= sc.nextInt(); //맨홀의 열좌표.
			L=sc.nextInt(); //시간 1-20
			
			map = new int[N][M];
			visited = new boolean[N][M];
			for(int i=0; i<N; i++) {
				for(int j=0; j<M; j++) {
					map[i][j] = sc.nextInt();
				}
			}//입력끝
			ans =1; //탈주범이 있을 수 있는 위치.
			
			bfs();
			
			System.out.println("#"+tc+" "+ans);	
		}//tc
	}//main
	
	static void bfs() {
		Queue<Person> q = new LinkedList<>();
		q.offer(new Person(R, C, 1));
		visited[R][C] = true;
		
		while(!q.isEmpty()) {
			Person p = q.poll();
			
			//탈주범이 주어진 시간 만큼 이동했다. (break이면 안됨.. 큐에 들어있는 확인해야하는 애들 한가득인데, 종료시키면 안됨): 큐에 있는 애들은 탈주범의 현재 위치, 즉 탈주범은 이동하면서 다음으로 갈 수 있는지 계속 체크해여함.
			if(p.time ==L)
				continue;
			
			int type = map[p.r][p.c]; //현재 탈주범이 서있는 위치의 터널!
			//현재 터널에서 갈 수 있는 방향만 확인을 하면 되겠다.
			for(int dir : tunnel[type]) {
				int nr = p.r+ dr[dir];
				int nc =p.c + dc[dir];
				
				if(nr<0 || nc<0|| nr>=N|| nc>=M||visited[nr][nc])
					continue;
				
				if (map[nr][nc]==0)
					continue;//0의 값인 곳에는 터널이 없음.
				
				int nextType = map[nr][nc];
				int dir2 = (dir+2)%4; //우하좌상이면 반대방향이니깐 2칸 더 가는 거고, 4주기니깐 4로 나눠서 그 나머지가 방향이됨.
				
				//다음 타입이 현재있는 좌표와 연결이 되어있어야할듯!
				if(!canMove(nextType, dir2))
					continue;
				
				//모든 조건을 다 통과하면
				visited[nr][nc] = true;
				ans++;
				q.offer(new Person(nr,nc, p.time+1));
	
			}
	

		}
		

	}//bfs메서드.
	
	//type안에 dir이 있는지 체크.
	static boolean canMove(int type, int dir) {
		for(int d : tunnel[type]) {
			if(d == dir) return true;
		}
		return false;
	}
    
}
