
def solution(n, k):
    answer=[]
    k-=1
    avail_num_arr = [i for i in range(1,n+1)]
    case_num_arr = [1]
    case_num=1
    for i in range(2,n):
        case_num*=i
        case_num_arr.append(case_num)
    
    for i in case_num_arr[-1::-1]:
        #print(k/i)
        answer.append(avail_num_arr.pop(int(k/i))) 
        k%=i
    answer.append(avail_num_arr.pop(0))
    
    
    return answer
