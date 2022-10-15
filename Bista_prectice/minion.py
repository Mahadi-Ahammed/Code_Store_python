play_word='BANANA'
v='AEIOU'
save=[]
cnt=0
kevin=0
Sturt=0
for i in range(len(play_word)):
    if play_word[i] in v:
        kevin+=len(play_word[i:])
    else:
        Sturt+=len(play_word[i:])
        
if kevin>Sturt:
    print("Kevin",kevin)
else:
    print("Sturt",Sturt)
        