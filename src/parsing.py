
# IMPORTANT NOTE
# syntaxCheck is awfully designed.
# My bad
# The algorithm works but the code is not maintainable
# and is hard to follow
# plus there's a better way of performing the syntax check
# I WILL rewrite a version of the algorithm, pinky promise.



'''Syntax is HTML-like. If you want a line or a word or simply a character to be of a certain color, you have to enclose it, within <colorName> and also close the the clause </colorName>.
colorName can be any 6-hex value (has to be a string starting with #) or a valid HTML 5 exact color name.Check PIL documentation. 
You guessed it, characters like <, >, / are reserved. But what if you want to use one of them. 
Prepend an ampersand (&) before the character. For e.g if you want to use < you have to write &<.
If you want to use an ampersand, write &&. Not doing so will result in unexpected behaviour from parse.
Also, the alogorithm is not designed to handle nested clauses. Do not do this:
<red>Hello <blue>world</blue> </red>.
Instead do this:
<red>Hello /red><blue>world </blue>
'''

def parse(exp):
    startIndex = None
    endIndex = None

    skip = False
    capture = False

    startTag = ''
    endTag = ''
    end = False
    virgin_string = ''
    i = 0
    params = []
    for index, c in enumerate(exp):

        if skip:
            skip = False
            continue

        if c == '&':
            
            virgin_string += exp[index+1]
            i+=1
            skip = True
            continue

        if c == '<':
            if startIndex != None:
                # endIndex = index-1
                endIndex = i - 1

            capture  = True
            continue


        elif c == "/":
            end = True

            
            continue
        


        elif capture:

            if c == '>':
                capture = False

                

                if end:
                    end = False

                    if startTag == endTag:
                       
                        params.append((startIndex,endIndex,startTag))

                        # startTag = ''
                        # endTag = ''
                        # startIndex = None
                        # endIndex = None

                    else:
                        print('\t--- WARNING ---')
                        print(f'\t<{startTag}> and </{endTag}> do not match. Text enclosed by these tags will be rendered in black.')
                        print('\t' + '-' * 15 + '\n')

                        params.append((startIndex,endIndex,'black'))

                    startTag = ''
                    endTag = ''
                    startIndex = None
                    endIndex = None

                else:

                    # startIndex = index + 1
                    startIndex = i 

                continue
                

            if end:
                endTag += c

            else:
                startTag+=c

        else:
            i += 1
            virgin_string+=c


    return params, virgin_string






def syntaxCheck(test):
    '''
    NOTE
    The algorithm below is awfully built.
    I will rewrite it.
    '''
    skip = False
    second = False
    once = False

    nL,nR,slash = 0,0,0

    for i, c in enumerate(test):

        if skip:
            skip = False
            continue

        if c == '&':
            if i < len(test) - 1:
                if test[i+1] not in ['<', '>', '/', '&']:
            
                    return False
            else:
                return False

            skip = True
            continue

        


        if c == '/':

            
            slash+=1

            if not second:
                # print('error2')
                return False

                

            else:

                if test[i-1] != '<':
                    # print('error69')
                    return False

                # t = i - 1

                # while test[t] != '<':

                #     if test[t] == ' ':
                #         t -= 1 

                #     else:
                #         print("error90")
                #         break




        if c == '<':

            nL += 1

            if not once:

                once = True

            else:
                once = False
                if  test[i+1] != '/':
                    print('here')

                    return False

                
                    



        if c == '>':

            nR +=1

            if once:

                second = True

            elif second:

                second = False

            else:
                # print('Missing <')
                return False


    if nR != nL or nR//2 != slash or nL//2 != slash or nR % 2 !=0 or nL % 2 !=0 :

        # print('Bad Syntax')
        return False

    return True

  



