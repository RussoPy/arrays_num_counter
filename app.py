if __name__ == "__main__":

    array_1 =[ 1,2, 5, 9, 88, 777,1000]   
    array_2 = [2, 9,35, 55,88, 777] 
    i = 0
    res = []
    
    for num in array_1:
        while i<len(array_2) and num > array_2[i]:
            i += 1
        if  i < len(array_2) and num == array_2[i]:
            res.append(num)
    
    print(res)


   
