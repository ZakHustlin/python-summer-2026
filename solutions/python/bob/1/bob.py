def response(hey_bob):
    s = hey_bob.strip()
    if s.endswith("?"):
        if s.isupper():
            return "Calm down, I know what I'm doing!"
              
        else:
            return "Sure."
                
    else:
        if s.isupper():
            return "Whoa, chill out!"
                
        elif s == "":
            return "Fine. Be that way!" 
                
        else:
            return "Whatever."
                
  
        
        
        
