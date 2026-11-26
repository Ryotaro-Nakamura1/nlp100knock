import random

def randomize_sentence(word_list):
  randomed_sentence = ""
  for i in range(len(word_list)):
    if 5 > len(word_list[i]):
      randomed_sentence += word_list[i]
    else:
      head = word_list[i][:1]
      mid = word_list[i][1:(len(word_list[i]) - 1)]
      tail = word_list[i][(len(word_list[i]) - 1):]
      randomed_sentence += head
      mid_list = list(mid)
      random.shuffle(mid_list)
      for k in range(len(mid_list)):
        randomed_sentence += mid_list[k]
      randomed_sentence += tail
    if "." != word_list[i]:
        randomed_sentence += " "
  return randomed_sentence


target_sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
target_list = target_sentence.split()
answer_sentence = randomize_sentence(target_list)
print(answer_sentence)