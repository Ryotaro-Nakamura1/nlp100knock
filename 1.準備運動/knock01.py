def filter_sentence_even(sentence):
  filtered_sentence = ""
  for i in range(len(sentence)):
    if 1 == (i % 2):
      filtered_sentence += sentence[i]
  return filtered_sentence

target_sentence = "パタトクカシーー"
answer_sentence = filter_sentence_even(target_sentence)
print(answer_sentence)