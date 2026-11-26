def word_bi_gram(sentence):
  word_list = sentence.split()
  gram_list = []
  limit = len(word_list) - 1
  for i in range(limit):
    gram_list.append((word_list[i], word_list[i + 1]))
  return gram_list

def character_tri_gram(sentence):
  gram_list = []
  limit = len(sentence) - 3
  for i in range(limit):
    gram_list.append(sentence[i:i + 3])
  return gram_list

target_sentence = "I am an NLPer"
answer_tri_gram = character_tri_gram(target_sentence)
answer_bi_gram = word_bi_gram(target_sentence)
print("文字tri_gram:", answer_tri_gram)
print("単語bi-gram:", answer_bi_gram)