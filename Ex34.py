def Count (text_insert):
    global count
    count = 1
    for i in range(len(text_insert)):
        if text_insert[i] == " ":
            count += 1
            
    

def printRes (res, count):
    if len(res) % 2 != 0:
        return print("Ритма нет")
    elif len(res)  % 2 == 0:
        return print("Ритм есть")
    
        

vowels = ["а", "и", "о", "у", "ы", "э"]            
text_insert = input("Введите текст: ")
res = map(str, text_insert)
res = filter(lambda x: x in vowels, res)
res = list(map(lambda x: x, res))
Count(text_insert)
print(printRes(res, count))






# Когда java головного мозга:
'''def GetRhythm (text):
    maxCount = 0
    count = 0
    vowels = ["а", "и", "о", "у", "ы", "э"]
    i = 0; j = 0
    while i < len(text[j]):
        if text[j][i] in vowels:
            count += 1
            i+=1
        i+=1    
    maxCount = count
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
            '''

          
