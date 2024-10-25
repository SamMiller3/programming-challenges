#24/10/2024
#Project Euler - Longest Collatz Sequence

longest_sequence=0
starting_number=0
for i in range(1,1000000):
    j=i 
    current_sequence=0
    while j!=1:
        if j%2==0:
            j/=2
        else:
            j=(3*j)+1
        current_sequence+=1
    if current_sequence>longest_sequence:
        longest_sequence=current_sequence
        starting_number=i
print(f"longest sequence: {longest_sequence}, starting numbers {starting_number}")
    
