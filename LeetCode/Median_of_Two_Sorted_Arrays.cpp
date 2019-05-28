class Solution {
public:
	double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
		vector<int> add;
		while (!nums1.empty() && !nums2.empty())
		{
			if (nums1[0] < nums2[0])
			{
				add.push_back(nums1[0]);
				nums1.erase(nums1.begin());
			}
			else
			{
				add.push_back(nums2[0]);
				nums2.erase(nums2.begin());
			}
		}
		while (!nums1.empty())
		{
			add.push_back(nums1[0]);
			nums1.erase(nums1.begin());
		}
		while (!nums2.empty())
		{
			add.push_back(nums2[0]);
			nums2.erase(nums2.begin());
		}
		int len = add.size();
		double median = 0;
		if (len % 2 == 0)
			median = (add[len / 2] + add[len / 2 - 1]) / 2.0;
		else
			median = add[len / 2];
		return median;
	}
};
