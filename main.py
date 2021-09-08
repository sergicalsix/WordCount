file_path="inputFiles/"

word_count = 0
flag = True
with open(file_path + "demo1.txt","r") as f:
    while flag:
        line = f.readline()
        #print(a,len(a))
        line_len =  len(line)
        if line_len == 0:
            flag=False
        word_count += line_len-1 #-1は改行文字の削除
        

print(word_count)
