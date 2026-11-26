def mix_sentences(sentence1, sentence2):
# この関数内では、両文の長さは同一であると仮定する。
  mixed_sentence = ""
  for i in range(len(sentence1)):
    mixed_sentence += sentence1[i]
    mixed_sentence += sentence2[i]
  return mixed_sentence

target_sentence1 = "パトカー"
target_sentence2 = "タクシー"
answer_sentence = mix_sentences(target_sentence1, target_sentence2)
print(answer_sentence)