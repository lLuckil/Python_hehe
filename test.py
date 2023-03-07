L = [1.1,'2.2', 'hi', 3.3, 'beluga', 4.4, 'hmmm', 'interesting', '8.8', 8.88, [12.1, '12.2', 14.3, '15.4']]

def listsum(lst):
    l = []
    s = []
    txt = ""
    for num in lst:
        if type(num) == float:
            l.append(num)
        elif type(num) == str:
            s.append(num)
        elif type(num) == list:
            for numbers in num:
                if type(numbers) == float:
                    l.append(numbers)
                elif type(numbers) == str:
                    s.append(numbers)
    
    print(l)
    print(s)

listsum(L)