import re

some_string = input()

found_words_regex = r"#[A-Z][a-z]+#[0-9]{2}/[0-9]{2}/[0-9]{2}#[[0-9]+#|#[A-Z][a-z]+\s[A-Z][a-z]+#[0-9]{2}/[0-9]{2}/[" \
                    r"0-9]{2}#[[0-9]+#|\|[A-Z][a-z]+\|[0-9]{2}/[0-9]{2}.[0-9]{2}\|[0-9]+\||\|[A-Z][a-z]+\s[A-Z][" \
                    r"a-z]+\|[0-9]{2}/[0-9]{2}.[0-9]{2}\|[0-9]+\|"
find_words = re.findall(found_words_regex, some_string)
sum_nutrition = 0
words = []
for word in find_words:
    if "#" in word:
        words = word.split("#")
    elif "|" in word:
        words = word.split("|")
    nutrition = int(words[3])
    sum_nutrition += nutrition
sum_nutrition = sum_nutrition // 2000
print(f"You have food to last you for: {sum_nutrition} days!")
for word in find_words:
    if "#" in word:
        words = word.split("#")
    elif "|" in word:
        words = word.split("|")

    print(f"Item: {words[1]}, Best before: {words[2]}, Nutrition: {words[3]}")

