package baekjoon_2217;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/a334ac368b9b42b9a9cb34e313c6cd3b

import java.util.*;
import java.io.*;

public class Main {
	
	static Vector<Integer> rope =  new Vector<Integer>();

	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		int N = rd.nextInt();
		for(int i = 0;i < N; i++) rope.add(rd.nextInt());
		
		Collections.sort(rope); //������������ ����
		
		//�⺻���� ���� ���� ���� * N�� �� �����ϰ�
		int weight = rope.get(0) * N; 
		for(int i = 1;i < N;i++) {
			if(rope.get(i) * (N - i) > weight) 
				weight = rope.get(i) * (N - i);
		} // 1���� rope�� �ٿ����� �� ���� �� �� �ִ� ��츦 ����.
		System.out.print(weight);
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