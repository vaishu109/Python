# f=open("poem.txt")
# content=f.read()
# if("twinkle"in content):
#     print("the word is present")
# else:
#     print("not present")
#     f.close

# game

# import random
# def game():
#     print("you are playing a game...")
#     score = random.randint(1,61)
#     with open("hiscore.txt") as f:
#         hiscore=f.read()
#         if(hiscore !=""):
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0
#     print(f"your score:{score}")
#     if(score > hiscore):
#         with open("hiscore.txt","w") as f:
#             f.write(str(score))

#     return score
        
# game()

# table print

# def generatetable(n):
#     table="" 
#     for i in range(2,21):
#         table+=f"{n}X{i}={n*i}\n"
#     with open(f"tables/table_{n}.txt","w") as f:
#         f.write(table)
# for i in range(2,21):
#     generatetable(i)

# replace word

# word="donkey"
# with open("files.txt","r") as f:
#     content=f.read()
# contentnew=content.replace(word,"######")
# with open("files.txt","w") as f:
#     f.write(contentnew)

# list of censored word


# words=["donkey","ganda","animal","domestic"]
# with open("files.txt","r") as f:
#     content=f.read()
#     for word in words:
#        content=content.replace(word,"#"*len(word))
# with open("files.txt","w") as f:
#     f.write(content)

# log file and find python

# with open("log.txt") as f:
#     content=f.read()
# if("python" in content):
#     print("yes")
# else:
#     print("no")

# log file and find python and print line no

# with open("log.txt") as f:
#     lines=f.readlines()
# lineno=1
# for line in lines:
#     if("python" in line):
#         print(f"yes.line no:{lineno}")
#         break
#     lineno+=1
# else:
#      print("no")

# make a copy of a text file

# with open("file.txt") as f:
#     content=f.read()
# with open("this_copy.txt","w") as f:
#     f.write(content)

# file is identical and matches the content of another file

# with open("file.txt") as f:
#     content1=f.read()
# with open("poem.txt") as f:
#     content2=f.read()
# if(content1==content2):
#     print("yes")
# else:
#     print("no")

# wipe out a prrogram

# with open("this_copy.txt","w") as f:
#     f.write("")

# rename

with open("old.txt") as f:
    content=f.read()
with open("renamed_by_python.txt","w") as f:
     f.write(content)