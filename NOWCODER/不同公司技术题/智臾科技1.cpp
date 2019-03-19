//给定一百万个0到255之间的整数，与出复杂度为O(n)的排序算法
#include<iostream>
#include<vector>

#define MAX 1000000//题目要求对一百万个数进行排序

using namespace std;

vector<int> v(256,0);

void input(vector<int> &v);
void output(vector<int> v);

int main()
{
	cout << "请输入"<< MAX <<"个整数,范围[0,255]："<< endl;
	input(v);
	cout << "排序结果为：" << endl;
	output(v);
	return 0;
}

void input(vector<int> &v)
{
	int temp;
	for (int i = 0; i < MAX; i++)
	{
		scanf("%d", &temp);//读入数据
		if (temp > 255 || temp < 0)
		{
			cout << temp << "不合理，请重新输入！" << endl;
			i--;
			continue;
		}
		v[temp]++;//记录每一个数字出现的次数
	}
	return;
}

void output(vector<int> v)
{
	for (int i = 0; i < 256; i++)
	{
		for (int j = 0; j < v[i]; j++)
		{
			printf("%d ", i);//根据数字出现的个数按照顺序输出
		}
	}
	return;
}
