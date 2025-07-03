# range(7) gives numbers from 0 to 6 inclusive
for i in range(7):  
    if i == 3 or i == 6:
        
# skip the rest of the loop body for these values
        continue  
    print(i, end=' ')
