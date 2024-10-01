def compressed(s):
    count = 1
    compress = ""
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compress += s[i - 1] + (str(count) if count > 1 else '')
            count = 1
    compress += s[-1] + (str(count) if count > 1 else '')
    return compress

n = "aaaabbbccc"
res = compressed(n)
print(res)
