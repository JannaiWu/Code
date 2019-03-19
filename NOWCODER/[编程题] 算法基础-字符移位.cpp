#include<iostream>
#include<string>

using namespace std;

int main()
{
    string s;
    while(cin>>s)
    {
        string s1="",s2="";
        for(int i=0;i<s.length();i++)
            {
                if(s[i]>='a'&&s[i]<='z')s1+=s[i];
                else if(s[i]>='A'&&s[i]<='Z') s2+=s[i];
            }
        s=s1+s2;
        cout<<s<<endl;
    }
    return 0;
}
