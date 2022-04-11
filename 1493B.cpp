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
int s[10] = {0, 1, 5, -1, -1, 2, -1, -1, 8, -1};

bool correct(int valh, int valm, int h, int m)
{
    if (s[valh % 10] == -1 || s[valh / 10] == -1 || s[valm % 10] == -1 || s[valm / 10] == -1)
        return false;
    return (s[valh % 10] * 10 + s[(valh / 10)] < m) && (s[valm % 10] * 10 + s[(valm / 10)] < h);
}

int32_t main()
{
    fastIO int T;

    cin >> T;
    while (T--)
    {
        int h, m;
        char col;
        cin >> h >> m;

        int valh, valm;
        cin >> valh >> col >> valm;
        while (correct(valh, valm, h, m) == false)
        {
            valm = (valm + 1) % m;
            if (valm == 0)
            {
                valh = (valh + 1) % h;
            }
        }
        cout << valh / 10 << valh % 10 << ":" << valm / 10 << valm % 10 << endl;
    }
}