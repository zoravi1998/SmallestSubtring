from collections import defaultdict 
  
MAX_CHARS = 256
  
def findSubString(strr): 
      
    n = len(strr) 
      
    # Count all distinct characters. 
    dist_count = len(set([x for x in strr])) 
      
    crtcount = defaultdict(lambda: 0) 
    count = 0
    start = 0
    min_len = n 
      
    for j in range(n): 
        crtcount[strr[j]] += 1
          
        # distinct character matched, 
        # then increment count 
        if crtcount[strr[j]] == 1: 
            count += 1
              
        # count the character which occured more than one
        # then remove it from starting and also remove 
        # the useless characters. 
        if count == dist_count: 
            while crtcount[strr[start]] > 1: 
                if crtcount[strr[start]] > 1: 
                    crtcount[strr[start]] -= 1
                      
                start += 1
                  
            # Update window size 
            len_window = j - start + 1
              
            if min_len > len_window: 
                min_len = len_window 
                start_index = start 
  
    #retrun miminum length
    return min_len 
                                   
# Driver code 
if __name__=='__main__': 
    st=input()  
    print(findSubString(st))