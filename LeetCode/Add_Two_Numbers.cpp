class Solution {
public:
	ListNode* addTwoNumbers(ListNode* l1, ListNode* l2)
	{
		ListNode *l = new ListNode(0);
		ListNode *s = l,*p=l1,*q=l2;
		int plus = 0;
		while (p||q)
		{
			int x = p ? p->val : 0;
			int y = q ? q->val : 0;
			int sum = (x + y + plus) % 10;
			plus = (x + y + plus) / 10;
			s->next = new ListNode(sum);
			s = s->next;
			if (p)p = p->next;
			if (q)q = q->next;
		}
		if (plus)
			s->next = new ListNode(plus);
		return l->next;
	}
};
