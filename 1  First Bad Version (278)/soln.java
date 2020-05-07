/* The isBadVersion API is defined in the parent class VersionControl.
      boolean isBadVersion(int version); */

public class Solution extends VersionControl 
{
    public int firstBadVersion(int n) 
    {
        int lb=0;
        int ub=n-1;
        for (int i=0; i<=n; i++)
        {
        // System.out.println("lb = "+lb+",  ub="+ub);
            if (lb==ub)
                return lb+1;
            int mid = lb + (ub-lb)/2;
            if (isBadVersion(mid+1))             //it is True
                ub=mid;
            else                              //it is False
                lb=mid +1  ;
            
        }
        return -1;
    }
}