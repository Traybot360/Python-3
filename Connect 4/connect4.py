def main():  
  row_1 = [0,0,0,0,0,0]
  
  row_2 = [0,0,0,0,0,0]
  
  row_3 = [0,0,0,0,0,0]
  
  row_4 = [0,0,0,0,0,0]
  
  row_5 = [0,0,0,0,0,0]
  
  row_6 = [0,0,0,0,0,0]
  
  row_7 = [0,0,0,0,0,0]
  
  
  print(row_1)
  
  print(row_2)
  
  print(row_3)
  
  print(row_4)
  
  print(row_5)
  
  print(row_6)
  
  print(row_7)
  
  
  
  def check_won(row_1,row_2,row_3,row_4,row_5,row_6,row_7):
      #win detection algs
      #directley across
      for p in range(7):
        if(p <= 3):
          #same row detection
          if(row_1[p] == 1 and row_1[p + 1] == 1 and row_1[p + 2] == 1 and row_1[p + 3] == 1):
             
             print("player 1 won")
             return(True)
          if(row_2[p] == 1 and row_2[p + 1] == 1 and row_2[p + 2] == 1 and row_2[p + 3] == 1):
            print("player 1 won")
            return True
  
             
          if(row_3[p] == 1 and row_2[p + 1] == 1 and row_3[p + 2] == 1 and row_3[p + 3] == 1):
            print("player 1 won")
            return True
             
  
          if(row_4[p] == 1 and row_4[p + 1] == 1 and row_4[p + 2] == 1 and row_4[p + 3] == 1):
             
             print("player 1 won")
             return True
          if(row_5[p] == 1 and row_5[p + 1] == 1 and row_5[p + 2] == 1 and row_5[p + 3] == 1):
             
             print("player 1 won")
             return(True)
          if(row_6[p] == 1 and row_6[p + 1] == 1 and row_6[p + 2] == 1 and row_6[p + 3] == 1):
             
             print("player 1 won")
             return(True)
          if(row_7[p] == 1 and row_7[p + 1] == 1 and row_7[p + 2] == 1 and row_7[p + 3] == 1):
            
             print("player 1 won")
             return True
  
  
          if(row_1[p] == 2 and row_1[p + 1] == 2 and row_1[p + 2] == 2 and row_1[p + 3] == 2):
          
             print("player 2 won")
             return True
          if(row_2[p] == 2 and row_2[p + 1] == 2 and row_2[p + 2] == 2 and row_2[p + 3] == 2):
          
             print("player 2 won")
             return True
          if(row_3[p] == 2 and row_2[p + 1] == 2 and row_3[p + 2] == 2 and row_3[p + 3] == 2):
     
             print("player 2 won")
             return True
          if(row_4[p] == 2 and row_4[p + 1] == 2 and row_4[p + 2] == 2 and row_4[p + 3] ==2):
             
             print("player 2 won")
             return True
          if(row_5[p] == 2 and row_5[p + 1] == 2 and row_5[p + 2] == 2 and row_5[p + 3] == 2):
  
             print("player 2 won")
             return True
          if(row_6[p] == 2 and row_6[p + 1] == 2 and row_6[p + 2] == 2 and row_6[p + 3] == 2):
             print("player 2 won")
             return True
          if(row_7[p] == 2 and row_7[p + 1] == 2 and row_7[p + 2] == 2 and row_7[p + 3] == 2):
             print("player 2 won")
             return True
          
        #other column detection
          if(row_1[p] == 1 and row_2[p] == 1 and row_3[p] == 1 and row_4[p] == 1):
            print("player 1 won")
            return True
          if(row_2[p] == 1 and row_3[p] == 1 and row_4[p] == 1 and row_5[p] == 1):
            print("player 1 won")
            return True
          if(row_3[p] == 1 and row_4[p] == 1 and row_5[p] == 1 and row_6[p] == 1):
  
            print("player 1 won")
            return True
          if(row_4[p] == 1 and row_5[p] == 1 and row_6[p] == 1 and row_7[p] == 1):
            print("player 1 won")
            return True
         
          #diagonal checker
          
      for i in range(6):
          if(i <= 3):
        
            if(row_1[i] == 1 and row_2[i + 1] == 1 and row_3[i + 2] == 1 and row_4[i + 3] == 1):
  
              print("player 1 won")
              return True
          if(i <= 4):
            if(row_2[i] == 1 and row_3[i + 1] == 1 and row_4[i + 2] == 1 and row_5[i + 3] == 1):
              print("player 1 won")
              return True          
          if(i <= 3):
            if(row_3[i] == 1 and row_4[i + 1] == 1 and row_5[i + 2] == 1 and row_6[i + 3] == 1):
        
              print("player 1 won")
              return True
          if(i <= 3):
            if(row_4[i] == 1 and row_5[i + 1] == 1 and row_6[i + 2] == 1 and row_7[i + 3] == 1):
           
              print("player 1 won")
              return True  
            if(i <= 3):
              if(row_7[i] == 1 and row_6[i + 1] == 1 and row_5[i + 2] == 1 and row_4[i + 3] == 1):
     
                print("player 1 won")
                return True         
          if(i <= 4):
            if(row_6[i] == 1 and row_5[i + 1] == 1 and row_4[i + 2] == 1 and row_3[i + 3] == 1):
            
              print("player 1 won")
              return True
          if(i <= 3):
            if(row_5[i] == 1 and row_4[i + 1] == 1 and row_3[i + 2] == 1 and row_2[i + 3] == 1):
             
              print("player 1 won")
              return True 
          if(i <= 3):
            if(row_4[i] == 1 and row_3[i + 1] == 1 and row_2[i + 2] == 1 and row_1[i + 3] == 1):
              
              print("player 1 won")
              return True  
            
          if(i <= 3):
            if(row_1[i] == 2 and row_2[i + 1] == 2 and row_3[i + 2] == 2 and row_4[i + 3] == 2):
  
              print("player 2 won")
              return True
          if(i <= 4):
            if(row_2[i] == 2 and row_3[i + 1] == 2 and row_4[i + 2] == 2 and row_5[i + 3] == 2):
         
              print("player 2 won")
              return True          
          if(i <= 3):
            if(row_3[i] == 2 and row_4[i + 1] == 2 and row_5[i + 2] == 2 and row_6[i + 3] == 2):
           
              print("player 2 won")
              return True
          if(i <= 3):
            if(row_4[i] == 2 and row_5[i + 1] == 2 and row_6[i + 2] == 2 and row_7[i + 3] == 2):
              
              print("player 2 won")
              return True 
            if(i <= 3):
              if(row_7[i] == 2 and row_6[i + 1] == 2 and row_5[i + 2] == 2 and row_4[i + 3] == 2):
        
                print("player 2 won")
                return True       
          if(i <= 4):
            if(row_6[i] == 2 and row_5[i + 1] == 2 and row_4[i + 2] == 2 and row_3[i + 3] == 2):
         
              print("player 2 won")
              return True 
          if(i <= 3):
            if(row_5[i] == 2 and row_4[i + 1] == 2 and row_3[i + 2] == 2 and row_2[i + 3] == 2):
            
              print("player 2 won")
              return True
          if(i <= 3):
            if(row_4[i] == 2 and row_3[i + 1] == 2 and row_2[i + 2] == 2 and row_1[i + 3] == 2):
        
              print("player 2 won")
              return True 
  
    
  
  while (True):
  
      row_p1 = int(input("Player 1 :What row"))
      
      
      
      for i in range(6):
        
  
        
       if(row_p1 == 1):
          if(row_7[0] <= 0):
            row_7[0] = 1
            break
          elif(row_6[0] <= 0):
            row_6[0] = 1 
            break
          elif(row_5[0] <= 0):
            row_5[0] = 1 
            break
          elif(row_4[0] <= 0):
            row_4[0] = 1 
            break
          elif(row_3[0] <= 0):
            row_3[0] = 1 
            break
          elif(row_2[0] <= 0):
            row_2[0] = 1 
            break
          elif(row_1[0] <= 0):
            row_1[0] = 1 
            break
          
       if(row_p1 == 2):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break
            
       if(row_p1 == 3):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break
            
       if(row_p1 == 4):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break

       if(row_p1 == 5):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break
            
            
       if(row_p1 == 6):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break
        
            
       if(row_p1 == 7):
          if(row_7[row_p1 - 1] <= 0):
            row_7[row_p1 - 1] = 1
            break
          elif(row_6[row_p1 - 1] <= 0):
            row_6[row_p1 - 1] = 1 
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p1 - 1] = 1 
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p1 - 1] = 1 
            break
          elif(row_3[row_p1 - 1] <= 0):
            row_3[row_p1 - 1] = 1 
            break
          elif(row_2[row_p1 - 1] <= 0):
            row_2[row_p1 - 1] = 1 
            break
          elif(row_1[row_p1 - 1] <= 0):
            row_1[row_p1 - 1] = 1 
            break
        
        
      print(row_1)
      
      print(row_2)
      
      print(row_3)
      
      print(row_4)
      
      print(row_5) 
      
      print(row_6)
      
      print(row_7)
      
  
      
      if(check_won(row_1,row_2,row_3,row_4,row_5,row_6,row_7) == True):
        break
    #player 2's turn
      row_p2 = int(input("Player 2"))
      
      
      
  
      
      for i in range(6):
        
  
        
       if(row_p2 == 1):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
          
       if(row_p2 == 2):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
            
       if(row_p2 == 3):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
            
       if(row_p2 == 4):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
            
            
       if(row_p2 == 6):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
        
            
       if(row_p2 == 7):
          if(row_7[row_p2 - 1] <= 0):
            row_7[row_p2 - 1] = 2
            break
          elif(row_6[row_p2 - 1] <= 0):
            row_6[row_p2 - 1] = 2
            break
          elif(row_5[row_p1 - 1] <= 0):
            row_5[row_p2 - 1] = 2
            break
          elif(row_4[row_p1 - 1] <= 0):
            row_4[row_p2 - 1] = 2
            break
          elif(row_3[row_p2 - 1] <= 0):
            row_3[row_p2 - 1] = 2
            break
          elif(row_2[row_p2 - 1] <= 0):
            row_2[row_p2 - 1] = 2
            break
          elif(row_1[row_p2 - 1] <= 0):
            row_1[row_p2 - 1] = 2
            break
          
        
      print(row_1)
      
      print(row_2)
      
      print(row_3)
      
      print(row_4)
      
      print(row_5) 
      
      print(row_6)
      
      print(row_7)
      if(check_won(row_1,row_2,row_3,row_4,row_5,row_6,row_7) == True):
        break 
  
  
main()
