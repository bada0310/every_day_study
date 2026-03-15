package Daily_Study.every_day_study.Eunjae.Algorithms.SWEA;


//그리디로 푸는 것이 정석이지만 디피로 풀면 이러하다..

import java.util.Arrays;
import java.util.Scanner;

public class swea_쉬운거스름돈 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		
		//돈종류.
		int[] coins = {50000, 10000, 5000, 1000, 500, 100, 50, 10};
		
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			//1. dp배열 초기화(N원을 만드는데 필요한 최소.동전개수)
			int[] dp = new int[N+1];
			
			//초기값은 무한대로 설정(오버플로우 방지를 위해 적당히 큰 값)
			Arrays.fill(dp, 987653838);
			dp[0] =0; //0원을 만드는데 필요한 동전은 0개.
			
			//2.역추적을 위한 배열(해당 금액을 만들 때, '마지막으로 사용한 동전의 인덱스 저장)
			int[] lastCoin = new int[N+1];
			Arrays.fill(lastCoin, -1);
			
			//3. DP실행- 하향식 방식
			for(int i=0; i< coins.length; i++) {
				for(int j=coins[i]; j<=N; j++) {
					//기존 방식보다 i번째 동전을 하나 더 쓰는 것이 이득이라면 갱신
					if(dp[j-coins[i]]+1 <dp[j]) {
						dp[j] = dp[j-coins[i]]+1;
						lastCoin[j] = i;
					}
				}
			}
			
			//4.역추적하여 각 동전이 몇개 쓰였는지 카운트
			int[] counts = new int[coins.length];
			int currentAmount = N;
			
			while(currentAmount>0) {
				int coinIndex = lastCoin[currentAmount];
				counts[coinIndex]++;
				currentAmount -= coins[coinIndex];
			}
			
			//5. 출력
			System.out.println("#" +tc);
			for(int i=0; i< counts.length; i++) {
				System.out.print(counts[i]+ " ");
			}
			System.out.println();
			
		}
		
	}

}

