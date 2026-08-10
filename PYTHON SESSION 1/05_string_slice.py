r = "rituraz"

print(r[0:3])  # Output: rit
print(r[3:])   # Output: uraz
print(r[0:])     # Output: rituraz [0:len(r)]
print(r[:4])   # Output: ritu [0:4]

print(r[-5:-1]) # Output: tura
print(r[2:6])

# SLICING WITH SKIP VALUE
S = "JAFFERY"

print(S[0:6:2])  #skip value jumps 2 characters, Output: JFE eg. 123456789 [1:9:3] the skip value is 3, so it will jump 3 characters and print the next character