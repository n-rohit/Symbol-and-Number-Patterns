def star_pattern_left(totalrows):
    for row in range(1,totalrows+1):                                    #    *
        for symbol in range(1, row+1):                                  #    **
            print('*', end='')                                          #    ***
        # for space in range(1, (totalrows-row)+1):                     #    ****
        #     print(' ', end='')                                        #    *****
        print()
    print('\n')

            #   OR   #
'''
def star_pattern_left(totalrows):
    list = []
    for row in range(1, totalrows+1):
        list.append('*')
        print(''.join(list))
    print('\n')
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_left(totalrows):
    for row in range(1,totalrows+1):                                    #    1
        for nums in range(1, row+1):                                    #    12
            print('{0}'.format(nums), end='')                           #    123
        # for space in range(1, row+1):                                 #    1234
        #     print(' ', end='')                                        #    12345
        print()
    print('\n')

            #   OR   #
'''
def num_pattern_left(totalrows):
    list = []
    for row in range(totalrows):
        list.append(str(row+1))
        print(''.join(list))
    print('\n')
'''
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_left_reverse(totalrows):
    for row in range(1,totalrows+1):                                    #    *****
        for symbol in range(1, (totalrows-row)+2):                      #    ****
            print('*', end='')                                          #    ***
        # for space in range(1, row+1):                                 #    **
        #     print(' ', end='')                                        #    *
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_left_reverse(totalrows):
    for row in range(1,totalrows+1):                                    #    12345
        for nums in range(1, (totalrows-row)+2):                        #    1234
            print('{0}'.format(nums), end='')                           #    123
        # for space in range(1, row+1):                                 #    12
        #     print(' ', end='')                                        #    1
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_right(totalrows):
    for row in range(1,totalrows+1):                                    #        *
        for space in range(1, (totalrows-row)+1):                       #       **
            print(' ', end='')                                          #      ***
        for symbol in range(1, row+1):                                  #     ****
            print('*', end='')                                          #    *****
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_right(totalrows):
    for row in range(1,totalrows+1):                                    #        1
        for space in range(1, (totalrows-row)+1):                       #       12
            print(' ', end='')                                          #      123
        for nums in range(1, row+1):                                    #     1234
            print('{0}'.format(nums), end='')                           #    12345
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_right_reverse(totalrows):
    for row in range(1,totalrows+1):                                    #    *****
        for space in range(2, row+1):                                   #     ****
            print(' ', end='')                                          #      ***
        for symbol in range(1, (totalrows-row)+2):                      #       **
            print('*', end='')                                          #        *
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_right_reverse(totalrows):
    for row in range(1,totalrows+1):                                    #    12345
        for space in range(2, row+1):                                   #     1234
            print(' ', end='')                                          #      123
        for nums in range(1, (totalrows-row)+2):                        #       12
            print('{0}'.format(nums), end='')                           #        1
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_center(totalrows): # Similar to --> star_pattern_right (change from end='' to end=' ')
    for row in range(1,totalrows+1):
        for space in range(1, (totalrows-row)+1):                       #        *
            print(' ', end='')                                          #       * *
        for symbol in range(1, row+1):                                  #      * * *
            print('*', end=' ')                                         #     * * * *
        print()                                                         #    * * * * *
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_center(totalrows): # Similar to --> num_pattern_right (change from end='' to end=' ')
    for row in range(1,totalrows+1):                                    #        1
        for space in range(1, (totalrows-row)+1):                       #       1 2
            print(' ', end='')                                          #      1 2 3
        for nums in range(1, row+1):                                    #     1 2 3 4
            print('{0}'.format(nums), end=' ')                          #    1 2 3 4 5
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_center_reverse(totalrows): # Similar to --> star_pattern_right_reverse (change from end='' to end=' ')
    for row in range(1,totalrows+1):
        for space in range(2, row+1):                                   #    * * * * *
            print(' ', end='')                                          #     * * * *
        for symbol in range(1, (totalrows-row)+2):                      #      * * *
            print('*', end=' ')                                         #       * *
        print()                                                         #        *
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_center_reverse(totalrows): # Similar to --> num_pattern_right_reverse (change from end='' to end=' ')
    for row in range(1,totalrows+1):
        for space in range(2, row+1):                                   #     1 2 3 4 5
            print(' ', end='')                                          #      1 2 3 4
        for nums in range(1, (totalrows-row)+2):                        #       1 2 3
            print('{0}'.format(nums), end=' ')                          #        1 2
        print()                                                         #         1
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def star_pattern_diamond(totalrows): # Combination of --> star_pattern_center & star_pattern_center_reverse (change in num_pattern_center_reverse part --> second half)
    for row in range(1,totalrows+1):
        for space in range(1, (totalrows-row)+1):                       #        *
            print(' ', end='')                                          #       * *
        for symbol in range(1, row+1):                                  #      * * *
            print('*', end=' ')                                         #     * * * *
        print()                                                         #    * * * * *
    for row in range(1,totalrows+1):                                    #     * * * *
        for space in range(2, row+2):                                   #      * * *
            print(' ', end='')                                          #       * *
        for symbol in range(1, (totalrows-row)+1):                      #        *
            print('*', end=' ')
        print()
    print('\n')
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def num_pattern_diamond(totalrows): # Combination of --> num_pattern_center & num_pattern_center_reverse (change in num_pattern_center_reverse --> lines 137, 139)
    for row in range(1,totalrows+1):
        for space in range(1, (totalrows-row)+1):                       #        1
            print(' ', end='')                                          #       1 2
        for nums in range(1, row+1):                                    #      1 2 3
            print('{0}'.format(nums), end=' ')                          #     1 2 3 4
        print()                                                         #    1 2 3 4 5
    for row in range(1,totalrows+1):                                    #     1 2 3 4
        for space in range(2, row+2):                                   #      1 2 3
            print(' ', end='')                                          #       1 2
        for nums in range(1, (totalrows-row)+1):                        #        1
            print('{0}'.format(nums), end=' ')
        print()
    print('\n')




star_pattern_left(5)
num_pattern_left(5)

star_pattern_left_reverse(5)
num_pattern_left_reverse(5)

star_pattern_right(5)
num_pattern_right(5)

star_pattern_right_reverse(5)
num_pattern_right_reverse(5)

star_pattern_center(5)
num_pattern_center(5)

star_pattern_center_reverse(5)
num_pattern_center_reverse(5)

star_pattern_diamond(5)
num_pattern_diamond(5)