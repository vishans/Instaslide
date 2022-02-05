# add maxlength i.e if article length is greater than max length return false
# add special character support i.e &<..

def formatParagraph(exp, width=15):
    exp+='\n'

    length = len(exp)
    i = 0
    currentLineWidth = width
    word = ''
    wordLen = 0
    result = ''

    while i < length:

        c = exp[i]

        if c == '&':
            c = exp[i+1]
            word += '&' + c
            wordLen +=1
            i+=2
            continue


        if c == '<':
           
            word+= c
            i+=1

            while exp[i] != '>':
                
                word+=exp[i]
                i+=1

            word+=exp[i]
           

            i+=1
            continue

            



        if c == ' ':
            word += c # append the space to the word

            if wordLen > width:
                return False

            if wordLen < currentLineWidth:

                result += word

                word = ''
                currentLineWidth -= wordLen
                wordLen = 0

            else:

                result += '\n'
                result += word

                word = ''
                currentLineWidth = width - wordLen
                wordLen = 0

        elif c == '\n':
            if wordLen > width:
                return False

            if wordLen < currentLineWidth:

                result += word

                

            else:

                result += '\n'
                result += word

       
            word = ''
            wordLen = 0
            currentLineWidth = width
            result+='\n'
           

        else:
            # character is normal text
            word +=c
            wordLen +=1

        i+=1


    
    return result[:-1]


if __name__ == '__main__':
    article = '''hello wordffff &<hello&> this 
    is me whidsa dgkldaa
    bla bla fkjgou ouyfouig oif iugfoyg of9uofyu oyfyt
    hehe hi'''

    print(formatParagraph(article))

