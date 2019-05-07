def longest_substr(s):
    alphas = {}
    subs = {}
    start_index = 0
    index = 0
    while index < len(s):
        char = s[index]
        if char in alphas:
            current_sub = s[start_index:index]
            len_subs = subs.get(len(current_sub), [])
            len_subs.append(current_sub)
            subs[len(current_sub)] = len_subs
            index = alphas[char] + 1
            start_index = index
            alphas = {}
        else:
            alphas[char] = index
            index += 1
    return subs[max(subs)]


s = "ABDEFGABEF"
print(longest_substr(s))
