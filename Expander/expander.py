def main():
  def expand(code,times):
    return times * code  
  
  def expandString(code):
    lbi = 0
    rbi = 0
    for i in range(len(code)):
      if(code[i] == "["):
        lbi = i
      if(code[i] == "]"):
        rbi = i
        break
    count = 1
    while code[lbi-count].isdigit():
      if(count == 1):
        mStr = code[lbi-count]
      else: 
        mStr = code[lbi-count] + mStr
      count += 1
    multiplier = int(mStr)
      
    code_inside = code[lbi + 1:rbi]
    code = code[0:lbi - len(mStr)] + expand(code_inside,multiplier) + code[rbi+1:] 
    if("[" not in code):
      return code
    else:
      return expandString(code)
  
  coded = input()
  a = (expandString(coded))
  print(a)
  
  
main()
