package baekjoon_1106;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/f27ceec311074b119fc847208aad7a4a

import java.util.*;
import java.io.*;

class Pair{
	private int cost, customer;
	Pair(int cost, int customer) {
		this.cost = cost;
		this.customer = customer;
	}
	public int getCo() { return cost; }
	public int getCu() { return customer; }
}

public class Main {
	
	static Pair[] city = new Pair[30]; // ������ ��
	static int[] dp = new int[100010]; 
	//dp[i]�� i�� ������� ����� ���� �ø� �� �ִ���
	//�ִ� : 100������ 1���� �ο��� �þ �� �ְ� 1000���� �����ؾ� �Ѵٸ�
	//100 * 1000 = 100000 ��ŭ �ʿ� 
	
	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		int C = rd.nextInt();
		int N = rd.nextInt();
		
		for(int i = 0;i < N;i++) {
			int x = rd.nextInt();
			int y = rd.nextInt();
			city[i] = new Pair(x,y);
		}
		
		for(int i = 1;i < 100001;i++) {
			for(int j = 0;j < N;j++) {
				if(city[j].getCo() <= i) 
					dp[i] = Math.max(dp[i], dp[i - city[j].getCo()] + city[j].getCu());
				//dp[i], �� i�� ������ ȫ�� �� �� �ִ� �ִ��� �ο��� �� ���ø� ���鼭 Ȯ���Ͽ� �ִ밪���� �����մϴ�.
			}
			if(dp[i] >= C) {//dp[i]�� ȫ�� �ؾ� �� �ο��� �����ϸ� i�� �ּҺ��
				System.out.println(i);
				break;
			}
		}
	}
	
	static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while(st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                }
                catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() { return Integer.parseInt(next()); }
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            }
            catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}