def reverse_sentence(sentence):
  reversed_sentence = ""
  for i in range(len(sentence)):
    reversed_sentence += sentence[len(sentence) - i - 1] # インデックス溢れを防ぐための-1
  return reversed_sentence

target_sentence = "stressed"
answer_sentence = reverse_sentence(target_sentence)
print(answer_sentence)