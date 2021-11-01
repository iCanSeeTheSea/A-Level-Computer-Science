def sum_array(array, total):
    if len(array) == 0:
        return total
    else:
        temp = array[0]; total+= temp; array.remove(temp)
        return sum_array(array, total)
        
print(sum_array([1,2,3,4,5,6,7,8], 0))

n = 149
def is_prime(n, i):
    if n % i != 0 and i == 2:
        return True
    elif n % i == 0:
        return False
    else:
        return is_prime(n, i-1)
    
print(is_prime(n, n-1))