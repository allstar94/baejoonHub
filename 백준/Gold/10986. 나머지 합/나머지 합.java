import java.util.*;

public class Main {
	public static void main(String[] args) {
		Scanner in=new Scanner(System.in);
		int n=in.nextInt();
		int m=in.nextInt();
		
		int sum=0;
		long mod[]=new long[m];
		long ans=0;
		
		for(int i=0;i<n;i++) {
			int input=in.nextInt();
			sum+=input;
			sum%=m;
			mod[sum]++;
			
			if(sum==0) {
				ans++;
			}
		}
		
		for(int i=0;i<m;i++) {
			long value = mod[i];
			long combination = value*(value-1)/Long.valueOf(2);
			ans+=combination;
		}
		System.out.println(ans);
	}
}