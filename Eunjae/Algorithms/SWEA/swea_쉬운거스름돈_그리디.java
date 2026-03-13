//큰 금액이 작은 금액으로 나누어 떨어지면 그리디 풀이로

import java.util.Scanner;

public class swea_쉬운거스름돈_그리디{
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T = sc.nextInt();
		
		for(int tc=1; tc<=T; tc++) {
			int N = sc.nextInt();
			
			//그리디로 풀려 내림차순으로 되어있어야함.
			int[] coins = {50000,10000, 5000, 1000, 500,100, 50,10};
			
			int[] count = new int[coins.length];
			for(int i=0; i<coins.length; i++) {
				count[i] = N/coins[i];
				N = N % coins[i];
			}
			
			//출력.
			System.out.println("#"+tc);
			for(int i=0; i<count.length; i++) {
				System.out.print(count[i]+ " ");
			}
			
			System.out.println();
			
			
		}
	}
}