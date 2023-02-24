def GetRhythm (text):                                   
    vowels = ["а", "и", "о", "у", "ы", "э"]             #Комментарий в окне сдачи задания не актуален. Заккоментированный способ это который не получился,
    count = map(str, text[0])                           # а первый основной, чуть допилил его.
    count = filter(lambda x: x in vowels, count)        
    count = list(map(lambda x: x, count))
    maxCount = len(count); count = len(count)
    for i in range(1, len(text)):
        if maxCount != count:
            break
        count = 0
        for j in range(len(text[i])):
            if text[i][j] in vowels:
                count +=1
    if maxCount == count:
        print("Ритм есть")                    
    else:
        print("Ритма нет")
                         
            
                                           
    
          
text = input("Введите текст: ").split(" ")
GetRhythm(text)            



'''def printRes (res):
    if len(res) % 2 > 0:
        return print("Ритма нет")
    elif len(res)  % 2 == 0:
        return print("Ритм есть")
    
        

vowels = ["а", "и", "о", "у", "ы", "э"]            
text_insert = input("Введите текст: ")
res = map(str, text_insert)
res = filter(lambda x: x in vowels, res)
res = list(map(lambda x: x, res))
print(printRes(res))'''







