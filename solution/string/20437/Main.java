package baekjoon_20437;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/0d345a8508a74a1fbf363c6719797709

/* 3. ����ڸ� ��Ȯ�� k�� �����ϴ� ���� ª�� ���ڿ�
      == ���۰� ���� � ������ ���� ª�� ���ڿ�
   4. ��Ȯ�� k�� �����ϴ� ���� �� ���ڿ�
      == ���۰� ���� � ������ ���� �� ���ڿ�  */

import java.util.*;
import java.io.*;

public class Main {
	static int[] alpha = new int[26];
	
	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		int T = rd.nextInt();
		
		for(int i = 0;i < T;i++) {
			
			for(int j = 0;j < 26;j++) // �ʱ�ȭ 
				alpha[j] = 0;

			String W = rd.nextLine();
			int K = rd.nextInt();
			
			//�� ���ĺ��� ��� ���Դ��� ����
			for(int j = 0;j < W.length();j++) 
				alpha[W.charAt(j) - 'a']++;
			
			int min = Integer.MAX_VALUE, max = 0;
			for(int j = 0;j < W.length();j++) {
				if(alpha[W.charAt(j) - 'a'] < K) continue;
				
				//K���� ũ�ų� ���� �󵵷� ���� ���ڸ� ����
				//�� ���ڰ� ���ڿ��� ���۰� ��
				char ch = W.charAt(j);
				int count = 0;
				for(int l = j;l < W.length();l++) {
					if(ch != W.charAt(l)) continue;
					else count++;
						
					//��Ȯ�� K���� �Ǵ� ���� min, max�� ����
					if(count == K) {
						min = Math.min(min, l - j + 1);
						max = Math.max(max, l - j + 1);
						break;
					}
				}
			}
	
			if(min == 10001 || max == 0) System.out.println("-1");
			else System.out.println(min + " " + max);
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