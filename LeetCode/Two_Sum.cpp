class Solution
{
public:
	vector<int> twoSum(vector<int> v, int sum)
	{
		unordered_map<int, int> m;
		for (int i = 0; i < v.size(); i++)
		{
			m[v[i]]=i;
		}
		for (int i = 0; i < v.size(); i++)
		{
			if (m.count(sum-v[i])&&m[sum-v[i]]!=i)
			{
				return{ i, m[sum - v[i]] };
			}
		}
		return{};
	}
};
