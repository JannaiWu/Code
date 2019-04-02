//写出一个程序，接受一个十六进制的数值字符串，输出该数值的十进制字符串（多组同时输入 ）
#include<iostream>
#include<string>
#include<map>

using namespace std;

map<const char, int> m = { { '0', 0 }, { '1', 1 }, { '2', 2 }, { '3', 3 }, { '4', 4 }, { '5', 5 }, { '6', 6 }, { '7', 7 },
{ '8', 8 }, { '9', 9 }, { 'A', 10 }, { 'B', 11 }, { 'C', 12 }, { 'D', 13 }, { 'E', 14 }, { 'F', 15 } };

int hex_ten(string &s);

int main()
{
	//string s = "10E";
	//cout << m[s[0]];
	string s;
	while (cin>>s){
		cout << hex_ten(s) << endl;
	}
	return 0;
}

int hex_ten(string &s)
{
	int n = 0, mul = 1;
	int i = 0;
	s.erase(s.begin());
	s.erase(s.begin());
	for (i = s.length() - 1; i >= 0; i--)
	{
		n += (m[s[i]]*mul);
		mul *= 16;
	}
	return n;
}
