#include<iostream>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

int main()
{
	int K;
	while (cin >> K)
	{
		vector<int> v(K);
		for (int i = 0; i < K; i++)
		{
			cin >> v[i];
		}
		sort(v.begin(), v.end());
		int min = v[0], max = v[K - 1];
		int cntmin = 1, cntmax = 0;
		int mindiff = max - min;
		if (mindiff == 0)
		{
			cout << K*(K - 1) / 2 << ' ' << K*(K - 1) / 2 << endl;
			continue;
		}
		map<int, int> m1, m2;
		m2[v[0]]++;
		for (int i = 1; i < K; i++)
		{
			if (v[i] == min)cntmin++;
			else if (v[i] == max)cntmax++;
			mindiff = v[i] - v[i - 1] < mindiff ? v[i] - v[i - 1] : mindiff;
			m1[v[i] - v[i - 1]]++;
			m2[v[i]]++;
		}
		int minpair = 0;
		if (mindiff == 0)
		{
			for (auto it = m2.begin(); it != m2.end(); it++)
			{
				if (it->second > 1)minpair += (it->second)*(it->second - 1) / 2;
			}
		}
		else
		{
			minpair = m1[mindiff];
		}
		cout <<minpair<< ' ' << cntmin*cntmax << endl;
	}
	return 0;
}
