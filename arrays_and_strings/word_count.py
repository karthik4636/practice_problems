#https://leetcode.com/problems/word-frequency/

def update_count(words, freq):
    for word in words:
        if word in freq:
            freq[word]+=1
        else:
            freq[word] = 1



with open("words.txt","r") as f:
    freq = {}
    for line in f.readlines():
        words = line.split()
        update_count(words, freq)
    a=sorted(freq.items(),reverse=True, key=lambda k:k[1])
    for key, vale in a:
        print(key, vale)




