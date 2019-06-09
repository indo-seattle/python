def vowels():
    vowels = 'aeiou'
    ip_str = 'Hello, have you tried our turorial section yet?'
    ip_str = ip_str.casefold()
    count = {}.fromkeys(vowels, 0)
    for lt in ip_str:
        if lt in count.keys():
            count[lt] = count[lt] + 1
    print(count)

vowels()