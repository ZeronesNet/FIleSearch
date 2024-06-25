
with open(r"C:\Users\29470\Desktop\文件读取\writeDict.txt","a") as f1:

    while (True):

        BYTES = input("字节:")
        EXE = input("后缀:")

        if BYTES == "end":
            break

        BYTES = BYTES.replace(" ","")
        BYTES = "\"" + BYTES + "\""

        EXE = EXE.split(" ")

        exe_str = "["

        for i in EXE:

            i = "\"" + i + "\""
            exe_str = exe_str + i + ","

        exe_str = exe_str[0:len(exe_str)-1]
        exe_str = exe_str + "]"

        write_str = BYTES + ":" + exe_str + ","

        f1.write(write_str)
        f1.write("\n")
        