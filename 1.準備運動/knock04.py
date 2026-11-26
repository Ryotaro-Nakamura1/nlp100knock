target_sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
target_list = target_sentence.split()
answer_dict = {}

for i in range(len(target_list)):
  if i in (0, 4, 5, 6, 7, 8, 14, 15, 18):
    answer_sentence = target_list[i][:1]
  else:
    answer_sentence = target_list[i][:2]
  answer_dict[answer_sentence] = i + 1

print(answer_dict)