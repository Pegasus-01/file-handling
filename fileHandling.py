def main():
    file = open("file.txt", "w+")   #w+ is used for defining write mode
    for i in range(20):
        file.write("this is file handling sample %d \n" %(i))
    file.close()

    #for reading the file
    #file = open("file.txt", "r")
    #if file.mode == 'r':
    #    filecontent = file.read()
    #    print(filecontent)



if __name__ == '__main__':
    main()