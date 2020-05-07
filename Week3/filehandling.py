
def main():
    f = open("demo.txt","r")
    g = open("demo1.txt","w+")
    if f.mode == 'r':
        contents =f.read()
        print(contents)
        g.write(contents)
    g.close
if __name__ == "__main__":
    main()