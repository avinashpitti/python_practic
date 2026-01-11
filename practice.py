# 10

def count_vowels(word):
    count=0
    for ch in word.lower():
        if ch in 'aeiou':
            count+=1

    return count

text ='I am learning python stack development'
print(count_vowels(text))