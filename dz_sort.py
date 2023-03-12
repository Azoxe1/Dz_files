book = {}

import os


f =open('1.txt','rt', encoding='utf-8')
res1 = f.readlines()
with open ('1.txt', 'rt', encoding='utf-8') as text_1:
    # full_text = text_1.readlines()   Если добавить сюда - счетчик не считает. если ниже - то не считывает текст.      
    counter_1 = 0
    for c in text_1:
        if c != '\n':
            counter_1 = counter_1 + 1 
    x = os.path.basename('1.txt')
    coun_plus = {}
    coun_plus.update({x: res1})
    book[counter_1] = coun_plus
    # print(book)    

i =open('2.txt','rt', encoding='utf-8')
res2 = i.readlines()    
with open ('2.txt', 'rt', encoding='utf-8') as text_2:
    counter_2 = 0
    # full_text = text_2.read()
    
    for c in text_2:
        if c != '\n':
            counter_2 = counter_2 + 1 
    x = os.path.basename('2.txt')
    coun_plus = {}
    coun_plus.update({x: res2})
    book[counter_2] = coun_plus
    # print(book)

j =open('3.txt','rt', encoding='utf-8')
res3 = j.readlines()      
with open ('3.txt', 'rt', encoding='utf-8') as text_3:
    counter_3 = 0
    # full_text = text_3.read()
    x = os.path.basename('3.txt')
    for c in text_3:
        if c != '\n':
            counter_3 = counter_3 + 1 
    x = os.path.basename('3.txt')
    coun_plus = {}
    coun_plus.update({x: res3})
    book[counter_3] = coun_plus
    # print(book)
    


def sort_colv (spis):
    with open('4.txt', 'w', encoding='utf-8') as doc:
        sort_list = sorted(spis.items())
        sort_dict = dict(sort_list)
        for num, text in sort_dict.items():
            for name, full_text in text.items():
                doc.write(name)
                doc.write('\n') #не нашел как делать отступы. наверняка есть варианты поумнее. подскажите плиз
                doc.write(str(num))
                doc.write('\n')
                doc.write(' '.join(full_text))
                doc.write('\n')
            
    
                
                
            
            
            
            
            
            
            
    

  
sort_colv (book)