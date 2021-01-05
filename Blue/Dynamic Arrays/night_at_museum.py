txt = input()
new_txt = txt.lower()

current_ch = 'a'
sum_space = 0
for i in new_txt:
  space = abs(ord(i) - ord(current_ch))
  if space > 13:
    space = 26 - space
  sum_space += space
  
  current_ch = i
  
print(sum_space)