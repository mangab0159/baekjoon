package baekjoon_5430;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/fc75d4683aa44fd5be618ed3934ac634

/*�ð��� �����ؼ� ������ ������, �����ϱ⸦ �����ϸ� �ȵ˴ϴ�.
������� ������ ������ ���� �ƴ� �տ��� �ڷ� �д°� �ڿ��� ������ �а� �Ͽ���
�����ϱ�� ���� ������ �ƴ� front�����͸� �ϳ� ������Ű�� ������ �����߽��ϴ�.
��µ� ���� ����� �ؾ� �ð��ʰ��� ���� �ʽ��ϴ�. */

import java.util.*;
import java.io.*;

public class Main {
	static ArrayList <String> numlist = new ArrayList<String>();
	static boolean reverse = false;
	static int front, end; //list�� ó���� ���� ����Ű�� index��ȣ
	static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
	//���� ���
	public static void main(String[] args) throws IOException {
		FastReader rd = new FastReader();

		int T = rd.nextInt();//�׽�Ʈ���̽�
		
		for(int i = 0;i < T;i++) {
			String p = rd.nextLine(); // ������ �Լ�
			int n = rd.nextInt(); // �迭�� ������ ��
			
			//inputString => tokenizer�� ������ ���� �� list�� ����
			InputString(rd.nextLine());
			
			boolean error = false;
			for(int j = 0;j < p.length();j++) {
				if(p.charAt(j) == 'R')  
					ReverseList(); //ListReverse => ������
				
				else {
					if(front > end) {//������Ȳ
						//front�� end���� ū ��Ȳ�� 
						//front == end == 1 �� ��Ȳ(list�� ���� �ϳ�)����
						//�ϳ��� ���� �� ��Ȳ�̴�. �� ���� ���� ���� ����
						bw.write("error\n");
						bw.flush();
						error = true;
						break;
					}
					else //���� �� �ִ� ���ڰ� ���� ��
						DeleteList(); //DeleteList => 0�� �ε��� ����
				}
			}
			if(error == false) OutputList();
			numlist.clear();
			reverse = false;
		}
		bw.close();
	}
	static void OutputList() throws IOException{
		bw.write("[");
		//reverse�� false�� ������� => ��(front) ��(end)�������� ���
		if(reverse == false) {
			for(int i = front;i <= end;i++) {
				if(i == end) bw.write(numlist.get(i));
				else bw.write(numlist.get(i) + ","); 
			}
		}
		//reverse�� true�� ������ ���� => ��(end) ��(front)�������� ���
		else {
			for(int i = end;i >= front;i--) 
				if(i == front) bw.write(numlist.get(i));
				else bw.write(numlist.get(i) + ",");
		}
		bw.write("]\n");
		bw.flush();
	}
	
	static void DeleteList() {
		if(reverse == false) front++;
		else end--;
		//������ ����� ���� �ƴ� ����Ű�� �ε����� ����, ���ҽ�Ŵ
		//���� �����̸� �� �ε����� ����(���� �����ϰ� �ǹǷ�)
		//������ �����̸� �� �ε����� ����(�ڰ� ���� ���� �ǹǷ�) 
	}
	
	static void ReverseList() {
		if(reverse == true) reverse = false;
		else reverse = true;
		//������ ������ ���� �ƴ� �������ִ��� �ƴ����� �Ǵ�
		//�Ŀ� ����Ҷ� ��� ������ �ٲ۴�
	}
	
	static void InputString(String numstr) {
		StringTokenizer st = new StringTokenizer(numstr, "[ | , | ]");
		
		while(st.hasMoreTokens()) 
			numlist.add(st.nextToken());
		
		front = 0;
		end = numlist.size() - 1;
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