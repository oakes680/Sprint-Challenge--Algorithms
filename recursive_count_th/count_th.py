'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# count = 0
# def count_th(word):
#     target = 'th'
#     global count
    
#     for i in range(len(word) - 1 ):
#         if word[i:i+2] == target:
#             count += 1  

#     return count


def count_th(word):
    count = 0
    if word == '':
        print(count)
        return count
    target='th'
    
    if len(word) < 2:
        print('hi', count)
        return count

    if word[0:2] == target:
        count = count + 1
    # print(len(word))
    # print(word)
    word = word[1:]
    return count + count_th(word)
        
        




word = 'abcthefthghith'
print(count_th(word))
