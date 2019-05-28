class Solution
{
public:
	int lengthOfLongestSubstring(string s)
	{
		if (s.length() == 0)
			return 0;
		int b, e;//记录循环查找的字符串的开头结尾
		int max=1,temp=1;
		int store[128] = { 0 };
		for (b = 0; b < s.length();)
		{
			temp = 1;
			store[int(s[b])]++;//记录一下这个字符出现过
			for (e = b + 1; e < s.length(); e++)
			{
				if (!store[int(s[e])])//如果没出现过
				{
					temp++;
					store[int(s[e])]++;//标记出现过
				}
				else
				{
					clearstore(store);
					break;
				}
			}
			b++;
			max = max > temp ? max : temp;
		}
		return max;
	}
	void clearstore(int* st)//清空储存是否出现过的数组
	{
		for (int i = 0; i < 128; i++)
		{
			st[i] = 0;
		}
		return;
	}
};

/*
网上大神的解法，可以从40ms的运算速度降低到8ms，提高了一个数量级
class Solution
{
public:
	int lengthOfLongestSubstring(string s)
	{
		if (s.length() == 0)
			return 0;
		vector<int> store(128, -1);//记录每一个字符出现的位置；一开始都设置为-1是为了之后好比较位置
		int left = -1;
		int max = 0;
		for (int right = 0; right < s.length(); right++)
		{
			if (store[s[right]] > left)
				left = store[s[right]];
			max = max > right - left ? max : right - left;
			store[s[right]] = right;//记录该字符最后出现的位置
		}
		return max;
	}
};
*/
