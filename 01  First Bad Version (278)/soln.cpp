// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) 
    {
        long lb=0;
        long ub=n-1;
        for (int i=0; i<=n; i++)
        {
            if (lb==ub)
                return (int(lb+1));
            int mid = (lb + ub)/2;
            if (isBadVersion(mid+1))             //it is True
                ub=mid;
            else                              //it is False
                lb=mid +1  ;            
        }
        return -1;
    }
};