//一个长度未知的巨型向量分布在n台机器上，如何快速找到(近似)中位数？
#include<iostream>
#include<unordered_map>

using namespace std;

int main()
{
	unordered_map<int,int> m;
	cout << "请输入整数向量，以空格分开，以回车结束："<<endl;
	int temp,Len=0;
	do
	{
		scanf("%d", &temp);
		m[temp]++;
		Len++;
	} while (getchar() != '\n');
	int cnt= 0;
	unordered_map<int, int> ::iterator it;
	for (it = m.begin(); ; it++)
	{
		cnt += it->second;
		if (cnt > Len / 2)break;//由于向量的长度很大，近似认为向量的排序的一半位置为近似中位数
	}
	printf("近似中位数为%d\n", it->first);
	return 0;
}
