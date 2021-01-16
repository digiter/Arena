// 1224. Maximum Equal Frequency

class Solution {
 public:
  int maxEqualFreq(vector<int>& nums) {
    if (nums.size() <= 1) {
      return nums.size();
    }

    int ans = 1;
    unordered_map<int, int> cnt;
    map<int, int> freq; // freq is the frequency of cnt.

    for (int i = 0; i < nums.size(); i++) {
      int x = nums[i];
      int old = cnt[x];
      cnt[x]++;

      if (old != 0) {
        if (--freq[old] == 0) freq.erase(old);
      }
      freq[old + 1]++;

      // Pattern 1
      // nums: a, a, a, a, ...
      // cnt: a: k
      if (cnt.size() == 1) {
        ans = max(ans, i + 1);
      }

      // Pattern 2
      // nums: a, b, c, d, ...
      // cnt: a:1, b:1, c:1, d:1, ...
      // freq: 1:k where k >= 1
      if (freq.size() == 1 && freq.count(1)) {
        ans = max(ans, i + 1);
      }

      // Pattern 3
      // nums: a, b, b, c, c, d, d, ...
      // cnt: 1, k, k, k, ... where k > 1
      // freq: 1:1, k:v
      if (freq.size() == 2 && freq.count(1) && freq.at(1) == 1) {
        ans = max(ans, i + 1);
      }

      // Pattern 4
      // nums: a, a, a, b, b, c, c, d, d, ...
      // cnt: b:k, c:k, d:k, a:(k+1), ...
      // freq: k:v, (k+1):1 where k >= 1
      if (freq.size() == 2) {
        int k = freq.begin()->first;
        int v = freq.begin()->second;
        auto other = freq.rbegin();
        if (k + 1 == other->first && other->second == 1) {
          ans = max(ans, i + 1);
        }
      }
    }
    return ans;
  }
};
