from vocobularium import *
import random

while True:
    print("1 - start test by number of words")
    print("2 - add word")
    print("3 - exit")
    print("4 - info")
    a=int(input())
    if a==1:
        n=input("введите количество слов к повторениюх(10)")
        if not n:
            n=10
        words = open_vocobularic()
        ids=create_list_of_id(int(n),words)
        random.shuffle(ids)
        
        for i in ids:
            words[i].print_word()
            r=input("make guess and pres ENTER")
            words[i].print_translate()
            r=input("correct guess? 1/0:")
            if not r:
                r=0
            words[i].update_word_status(r)
        dump_vocobularic(words)
        
    if a==2:
        s=input("введите слово:перевод")
        s=s.split(":")
        w=wt()
        w.word=s[0]
        w.translate=s[1]
        words = open_vocobularic()
        words.append(w)
        dump_vocobularic(words)
        print("done")
        
        
    if a==3:
        #dump_vocobularic(words)
        break

    if a==4:
        words = open_vocobularic()
        for el in words:
            el.print()

    if a==5:
        words = open_vocobularic()
        s=input("какое слово удалить?")
        for i in range(len(words)):
            if words[i].word==s:
                t=i
        words.pop(i)
        print("done")
        dump_vocobularic(words)

            
