package baekjoon_16954;

//Authored by : suin8
//Co-authored by : -
//Link : http://boj.kr/b8fc50e235a44c1a9cfd95e860c9f8be

import java.util.*;
import java.io.*;

class Point{
	int y, x;
	Point(int y, int x){
		this.y = y;
		this.x = x;
	}
}

public class Main {
	static char[][] chess;
	static boolean[][] visited;
	static int wall_count = 0;
	static int[] dx = {1, 0, -1, 0, 1, -1, 1, -1, 0};
	static int[] dy = {0, 1, 0, -1, -1, 1, 1, -1, 0};
	
	public static void main(String[] args) {
		FastReader rd = new FastReader();
		
		chess = new char[10][10];
		visited = new boolean[10][10];
		
		//�Է��� �����鼭 �� ������ ����
		for(int i = 1;i <= 8;i++) {
			String str = rd.nextLine();
			for(int j = 1;j <= 8;j++) {
				chess[i][j] = str.charAt(j - 1);
				if(chess[i][j] == '#') wall_count++;
			}
		}
		
		if(bfs() == true) System.out.println("1");
		else System.out.println("0");
	}
	
	static boolean bfs() {
		Queue<Point> q = new LinkedList<>();
		q.add(new Point(8, 1));
		
		while(!q.isEmpty()) {
			int check = q.size();
			
			/*������ġ���� ���� ��ġ�� �� �� �ִ� ���� ť�� ���� �ְ�
			 ���� while roop�� ť���� ��� ������ �˻��� �Ŀ� ���� �������� �Ѵ�.
			 �׷��� ������ ���� ��� �̵��ϴ� ��Ȳ�� ��������.*/
			for(int i = 0;i < check;i++) {
				Point cur = q.poll();
				//���� ��ġ�� ���� ���� ��ġ(�� ���� �� ��Ȳ)��� �Ѿ��.
				if(chess[cur.y][cur.x] == '#') continue;
				
				//������ �Ǵ� ���� ��� �ݵ�� �������� ������ �� �ִ� ��Ȳ.
				if(cur.y == 1 && cur.x == 8 || wall_count == 0) return true;
				
				//8���� + ���ڸ� ��ġ���� �� 9������ �˻��Ͽ� ť�� �ִ´�.
				for(int j = 0;j < 9;j++) {
					int nexty = cur.y + dy[j];
					int nextx = cur.x + dx[j];	
					
					if(nextx <= 0 || nexty <= 0 || nextx > 8 || nexty > 8) continue;
					if(visited[nexty][nextx] == true || chess[nexty][nextx] == '#') continue;
					
					visited[nexty][nextx] = true;
					q.add(new Point(nexty, nextx));
				}
			}
			//�̵��Ͽ��ٰ� �ٽ� �ǵ��� �� �� �ֱ� ������ �ʱ�ȭ.
			for(int i = 0;i < 10;i++)
				Arrays.fill(visited[i], false);
			
			//���� �������� �� ���� �ű��.
			if(wall_count > 0) moveWall();
		}
		
		return false;
	}
	
	static void moveWall() {
		for(int i = 8;i > 0;i--) {
			for(int j = 1;j <= 8;j++) {
				if(chess[i][j] != '#') continue;
				
				int nextwall = i + 1;
				if(nextwall <= 8) {
					chess[nextwall][j] = '#';
					chess[i][j] = '.';
				}
				else {
					chess[i][j] = '.';
					wall_count--;
				}
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