#include <stdio.h>

int main(void)
{
	int n,i,sum=0;
	char s[105];

	scanf("%d%s",&n,s);
	for(i=0;i<n;i++)
	{
		sum+=s[i]-'0';
	}
	printf("%d", sum);
	return 0;
}