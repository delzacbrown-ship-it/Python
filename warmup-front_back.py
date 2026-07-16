def front_back(str):
  if len(str) > 1:
    # first letter [0]
    first = str[0]
    
    # last letter [-1]
    last = str[-1]
    
    # middle letter [1:-1]
    middle = str[1:-1]
    
    new = last+middle+first
    
    return new
  
  else:
    return str