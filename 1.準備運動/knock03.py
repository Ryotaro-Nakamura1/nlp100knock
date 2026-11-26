def count_character(sentence):
  if sentence.endswith((".", ",")):
    return len(sentence) - 1
  else:
    return len(sentence)

def create_count_list(list):
  created_count_list = []
  for i in range(len(list)):
    created_count_list.append(count_character(list[i]))
  return created_count_list

target_sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
target_list = target_sentence.split()
answer_list = create_count_list(target_list)
print(answer_list)