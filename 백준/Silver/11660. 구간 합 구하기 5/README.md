bufferedreader scanner 차이

![image](https://user-images.githubusercontent.com/42260010/182291315-aaeb2ebf-8778-4de6-882c-4e6ecaeb672f.png)

package milk;

import java.util.Scanner;

public class study {

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);

		System.out.println("원하는 숫자를 입력하세요");
		String input = scanner.nextLine();
		int num = Integer.parseInt(input);

		System.out.println(num);
	}

}


우리는 보통 자바를 처음 배울때 콘솔에서 입력을 받기 위해 이러한 방식을 많이 사용했을 것이다. 하지만 Scanner는 편리하지만 속도가 느리다는 단점이 있어 특히 알고리즘 문제를 풀때 시간초과 에러를 내는 치명적인 단점이 있습니다. 하하지만  BufferedReader 를 아래와 같이 사용한다면 버퍼를 사용하기 때문에 입력 속도에서 확연히 줄일 수 있습니다.

package milk;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class study {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in)); // 선언
		String s = br.readLine(); 
		int i = Integer.parseInt(br.readLine()); 
		
		System.out.println("String : " + s);
		System.out.println("Int : " + i);
		
	}
}

![image](https://user-images.githubusercontent.com/42260010/182293826-e750cd85-a60d-4fde-a686-01de85a3a028.png)


# [Silver I] 구간 합 구하기 5 - 11660 

[문제 링크](https://www.acmicpc.net/problem/11660) 

### 성능 요약

메모리: 123748 KB, 시간: 1344 ms

### 분류

다이나믹 프로그래밍(dp), 누적 합(prefix_sum)

### 문제 설명

<p>N×N개의 수가 N×N 크기의 표에 채워져 있다. (x1, y1)부터 (x2, y2)까지 합을 구하는 프로그램을 작성하시오. (x, y)는 x행 y열을 의미한다.</p>

<p>예를 들어, N = 4이고, 표가 아래와 같이 채워져 있는 경우를 살펴보자.</p>

<table class="table table-bordered" style="line-height:20.8px; width:158px">
	<tbody>
		<tr>
			<td style="text-align:center">1</td>
			<td style="text-align:center">2</td>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
		</tr>
		<tr>
			<td style="text-align:center">2</td>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
		</tr>
		<tr>
			<td style="text-align:center">3</td>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
			<td style="text-align:center">6</td>
		</tr>
		<tr>
			<td style="text-align:center">4</td>
			<td style="text-align:center">5</td>
			<td style="text-align:center">6</td>
			<td style="text-align:center">7</td>
		</tr>
	</tbody>
</table>

<p>여기서 (2, 2)부터 (3, 4)까지 합을 구하면 3+4+5+4+5+6 = 27이고, (4, 4)부터 (4, 4)까지 합을 구하면 7이다.</p>

<p>표에 채워져 있는 수와 합을 구하는 연산이 주어졌을 때, 이를 처리하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 표의 크기 N과 합을 구해야 하는 횟수 M이 주어진다. (1 ≤ N ≤ 1024, 1 ≤ M ≤ 100,000) 둘째 줄부터 N개의 줄에는 표에 채워져 있는 수가 1행부터 차례대로 주어진다. 다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2 가 주어지며, (x1, y1)부터 (x2, y2)의 합을 구해 출력해야 한다. 표에 채워져 있는 수는 1,000보다 작거나 같은 자연수이다. (x1 ≤ x2, y1 ≤ y2)</p>

### 출력 

 <p>총 M줄에 걸쳐 (x1, y1)부터 (x2, y2)까지 합을 구해 출력한다.</p>

