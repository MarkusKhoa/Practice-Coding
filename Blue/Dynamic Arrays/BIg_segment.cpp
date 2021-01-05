#include <iostream>
using namespace std;
int l_seg[100000], r_seg[100000], min_l = 1000000000, max_r = -1, pos = -2, n;
int main()
{
  cin >> n;
  for(int i = 0; i < n; i++)
  {
    cin>>l_seg[i]>>r_seg[i];
  }
  for(int i=0; i<n; i++)
  {
    if(l_seg[i] < min_l)
    {
      min_l = l_seg[i];
    }
    if(r_seg[i] > max_r)
    {
      max_r = r_seg[i];
    }
  }
  for(int i = 0; i < n; i++)
  {
    if(l_seg[i] == min_l && r_seg[i] == max_r)
    {
      pos = i;
      break;
    }
  }
  cout << pos+1 << endl;
  return 0;
}