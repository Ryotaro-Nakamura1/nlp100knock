def cipher(sentence):
  changed_sentence = ""
  for i in range(len(sentence)):
    if sentence[i].islower():
      changed_sentence += chr(219 - ord(sentence[i]))
    else:
      changed_sentence += sentence[i]
  return changed_sentence

target_sentence = "I am an NLPer"
answer_sentence = cipher(target_sentence)
print(answer_sentence)
answer_sentence = cipher(answer_sentence)
print(answer_sentence)