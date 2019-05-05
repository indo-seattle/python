

def vowelCount(_input_str):

    # Create a array of vowel count in the order aeiou
    aeiou = [0, 0, 0, 0, 0]

    _input_str = str(_input_str)
    if _input_str != "" and _input_str is not None:
        #
        for my_char in _input_str:
            #
            if my_char.upper() == 'A':
                aeiou[0] = aeiou[0]+1
            elif my_char.upper() == 'E':
                aeiou[1] = aeiou[1] + 1
            elif my_char.upper() == 'I':
                aeiou[2] = aeiou[2]+1
            elif my_char.upper() == 'O':
                aeiou[3] = aeiou[3]+1
            elif my_char.upper() == 'U':
                aeiou[3] = aeiou[3] + 1

            char_index += 1
    return aeiou



def chocolateFeast(n, c, m):
    # This function is used recursively

    wrapper_count = int(n/c)
    return wrapper_count+calculateBars(wrapper_count,m)

def calculateBars(n,m):
    bars = int(n/m)
    left_over_wrappers = int(n % m)
    if bars == 0:
        return 0
    else:
        return bars + calculateBars(bars + left_over_wrappers, m)


if __name__=='__main__':

    '''myStr = "I'm super smart but only thing is that I always take things for granted"
    print(vowelCount(myStr))'''
    print(chocolateFeast(15,3,2))
    print(chocolateFeast(10, 2, 5))
    print(chocolateFeast(12, 4, 4))
    print(chocolateFeast(6, 2, 2))
