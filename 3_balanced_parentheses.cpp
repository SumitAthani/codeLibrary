#include <bits/stdc++.h>
using namespace std;
bool checkBalancedBrackets(string expr)
{
	stack<char> s;
	char x;
	for (int i = 0; i < expr.length(); i++)
	{
		if (expr[i] == '(' || expr[i] == '['
			|| expr[i] == '{')
		{
			s.push(expr[i]);
			continue;
		}
		if (s.empty())
			return false;

		switch (expr[i])
		{
		  case ')':
			x = s.top();
			s.pop();
			if (x == '{' || x == '[')
				return false;
			break;

		case '}':
			x = s.top();
			s.pop();
			if (x == '(' || x == '[')
				return false;
			break;

		case ']':
			x = s.top();
			s.pop();
			if (x == '(' || x == '{')
				return false;
			break;
		}
	}

	return (s.empty());
}

int main()
{
	string expr;
	cout<<"Enter the expression : ";
	cin>>expr;
	if (checkBalancedBrackets(expr))
		cout << "Parentheses Balanced"<<endl;
	else
		cout << "Parentheses not Balanced"<<endl;
	return 0;
}
