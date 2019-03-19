//假设日期1969.01.01用0表示，请开发一个函数输出任意日期的整数表示（日期小于1969.01.01的用负数表示）。反过来，给定日期的整数表示，开发一个函数求日期对应的年月日
#include<iostream>
#include<vector>

#define START 19690101//定义基准为0的日期

using namespace std;

int MONTH[13] = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };

bool judge(int year);//判断一年是否是闰年
int cal(int data);//计算这一天的日期的整数表示，以公元0年1月1日为0；
void data_int();//输出任意日期的整数表示
void int_data();//求日期对应的年月日

int main()
{
	data_int();
	int_data();
	return 0;
}

bool judge(int year)
{
	if (year % 400 == 0)return true;//是400的倍数表示是闰年
	if (year % 4 == 0 && year % 100 != 0)return true;//是4的倍数但是不是100的倍数也是闰年
	else return false;
}

int cal(int data)//计算八位整数日期的整数表示
{
	int n = 0;
	int year = data / 10000;
	int month = (data - 10000 * year) / 100;
	int day = data - 10000 * year - 100 * month;
	for (int i = 0; i < year; i++)
	{
		if (judge(i))n += 366;
		else n += 365;
	}
	for (int i = 0; i < month; i++)
	{
		n += MONTH[i];
	}
	if (judge(year) && month > 2)n++;//该年超过2月，日期数要多加1
	for (int i = 0; i < day; i++)
	{
		n++;
	}
	return n;
}

void data_int()
{
	int y, m, d;
	cout << "请输入一个日期，以小数点为间隔" << endl;
	while (1)
	{
		scanf("%d.%d.%d", &y, &m, &d);
		if (y < 0)
		{
			printf("请检查日期是否输入正确！\n");
			continue;
		}
		if (m < 1 || m>12)
		{
			printf("请检查日期是否输入正确！\n");
			continue;
		}
		if (judge(y) && m == 2 && d == 29)break;//如果是闰年2月29是正确日期，结束输入
		if (d>0&&d<=MONTH[m])
		{
			break;//如果d在该月的日期范围内 表示是正确日期，结束输入
		}
		else
		{
			printf("请检查日期是否输入正确！\n");
			continue;
		}
	}
	int result = cal(y * 10000 + m * 100 + d) - cal(START);
	printf("%04d年%02d月%02d日的整数表示为：%d\n", y,m,d,result);
	return;
}

void int_data()
{
	int y = 0, m = 1;
	int n,N;//日期的整数
	printf("请输入一个日期的整数表示：\n");
	scanf("%d", &N);
	n = cal(START) + N;//计算以0000年1月1日为基准的日期
	while (n>=365)//计算年份
	{
		n -= 365;
		if (judge(y))n--;//如果是闰年再减一天
		y++;
	}
	for (int i = 1; i <= 12; i++)
	{
		if (judge(y) && i == 2 && n > 29)//如果是闰年2月且大于29天的情况特殊处理
		{
			n -= 29; m++; continue;
		}
		if (n > MONTH[i])//计算月份
		{
			n -= MONTH[i];
			m++;
		}
		else
		{
			break;
		}
	}
	printf("整数%d对应的日期为：%04d年%02d月%02d日\n", N, y, m, n);
	return;
}
