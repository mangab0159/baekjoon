package baekjoon_1912;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/788f5770927f4da79551c4bc06c3351b

import java.util.*;
import java.io.*;

public class Main {
	
	static int[] arr = new int[100010];
	static int[] dp = new int[100010];
 	
	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		int n = rd.nextInt();
		for(int i = 0;i < n;i++) 
			arr[i] = rd.nextInt();
		
		//�ʱ�ȭ
		int max = arr[0];
		dp[0] = arr[0];
		
		//dp[i]�ȿ��� arr[0~i]������ �� �� �ִ밪�� ������.
		//max�� dp���� �ִ밪�� ������.=> �����
		for(int i = 1;i < n;i++) {
			dp[i] = Math.max(dp[i - 1] + arr[i], arr[i]);
			max = Math.max(dp[i], max);
		}
		
		System.out.println(max);
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