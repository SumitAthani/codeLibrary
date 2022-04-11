#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define int long long

int32_t main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> a, b(2 * n + 1);
        for (int i = 0; i < n; i++)
        {
            int val;
            cin >> val;
            a.push_back(val);
            b[val] = i + 1;
        }
        sort(a.begin(), a.end());
        int c = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if ((a[i] * a[j]) > (2 * n))
                    break;
                if (a[i] * a[j] == (b[a[i]] + b[a[j]]))
                    c++;
            }
        }
        cout << c << "\n";
    }
    return 0;
}