# Run-Length Encoding

# Running time O(n)| space 0(n) where n is the length of input string
def runLengthEncoding(string):
    newstring = []
    cnt = 0
    start = string[0]
    for i in range(len(string)):

        if string[i] != start or cnt == 9:
            newstring.append(f'{cnt}{start}')
            start = string[i]
            cnt = 0

        cnt += 1

    newstring.append(f'{cnt}{string[i]}')

    return "".join(newstring)


print(runLengthEncoding("AAAAAAAAAAAAABBCCCCDD"))
