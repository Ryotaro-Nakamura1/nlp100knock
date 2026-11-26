def character_bi_gram(sentence):
  gram_list = []
  limit = len(sentence) - 2
  for i in range(limit):
    gram_list.append(sentence[i:i + 2])
  return gram_list

target_sentence1 = "paraparaparadise"
target_sentence2 = "paragraph"
X = set(character_bi_gram(target_sentence1))
Y = set(character_bi_gram(target_sentence2))
print("集合X:", X)
print("集合Y:", Y)
print("集合X∪Y:", X | Y)
print("集合X∩Y:", X & Y)
print("集合X∖Y:", X - Y)
target_word = "se"
if target_word in X:
  print("Xに", target_word, "は含まれている。")
else:
  print("Xに", target_word, "は含まれていない。")
if target_word in Y:
  print("Yに", target_word, "は含まれている。")
else:
  print("Yに", target_word, "は含まれていない。")