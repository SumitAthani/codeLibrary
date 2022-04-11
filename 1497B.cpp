#include <bits/stdc++.h>
using namespace std;
#define fastIO                        \
    ios_base::sync_with_stdio(false); \
    cin.tie(NULL);                    \
    cout.tie(NULL);
#define int long long int
#define fi first
#define se second
#define pub push_back
#define pi pair<int, int>
#define all(v) (v).begin(), (v).end()
#define rep(i, l, r) for (int i = (int)(l); i < (int)(r); i++)
#define repd(i, l, r) for (int i = (int)(l); i >= (int)(r); i--)
#define clrg(i, l, r)                         \
    for (int i = (int)(l); i < (int)(r); i++) \
        vis[i] = 0, v[i].clear();
int power(int x, unsigned int y)
{
    int res = 1;
    while (y > 0)
    {
        if (y & 1)
        {
            res = res * x;
        }
        y = y >> 1;
        x = x * x;
    }
    return res;
}
int powermod(int x, unsigned int y, int p)
{
    int res = 1;
    x = x % p;
    while (y > 0)
    {
        if (y & 1)
        {
            res = (res * x) % p;
        }
        y = y >> 1;
        x = (x * x) % p;
    }
    return res;
}
#define print2d(mat, n, m)                 \
    {                                      \
        for (int i = 0; i < (int)(n); i++) \
        {                                  \
            for (int j = 0; j < (m); j++)  \
            {                              \
                cout << mat[i][j] << " ";  \
            }                              \
            cout << endl;                  \
        }                                  \
    }
#define clr(a, x) memset(a, x, sizeof(a))
#define rr(v) for (auto &val : v)
#define print(v)             \
    for (const auto itr : v) \
    {                        \
        cout << itr << ' ';  \
    }                        \
    cout << "\n";
#define ln length()
#define sz size()
#define mod 1000000007
#define elif else if

// code

int32_t main()
{
    fastIO int T;
    cin >> T;
    while (T--)
    {
        int n, m;
        cin >> n >> m;
        map<int, int> c;
        rep(i, 0, n)
        {
            int x;
            cin >> x;
            c[x % m]++;
        }
        int c1 = 0;
        rr(c)
        {
            if (val.first == 0)
                c1++;
            elif (2 * val.first == m)
                c1++;
            elif (c.find(m - val.first) == c.end())
            {
                c1 += val.second;
            }
            elif (2 * val.first < m)
            {
                int y = 0;
                c1 += 1 + max(y, (val.second - c[m - val.first]) - 1);
            }
            //continue
        }
        cout << c1 << "\n";
    }
}