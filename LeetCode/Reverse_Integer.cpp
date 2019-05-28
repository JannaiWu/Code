class Solution {
public:
	int reverse(int x)
	{
		if (x <= INT_MIN || x >= INT_MAX)return 0;
		int flag = 0;
		if (x > 0)
		{
			flag = 1;
		}
		else
			x *=-1;
		stringstream ss; string s; int res;
		ss << x; ss >> s; ss.clear();
		string sss(s.rbegin(), s.rend());
		ss << sss; ss >> res;
		if (res <= INT_MIN || res >= INT_MAX)return 0;
		if (flag)
			return res;
		else
			return -1 * res;
	}
};
