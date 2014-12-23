import sys, math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

L = int(raw_input())
H = int(raw_input())
T = raw_input()
ROW = ""

for i in xrange(H):
    ROW += raw_input()

# Write an action using print
# To debug: print >> sys.stderr, "Debug messages..."

len_T = len(T)
out_T = list(T)

chr2 = []

for i in range(ord('A'), ord('Z') + 1 ):
    chr2 += chr(i)
chr2 += '?'


for i in xrange(H):
    answer = ""
    for j in xrange(len_T):
        
        hitnum = -1
        for k in xrange(len(chr2)):
            if chr2[k] == T[j:j+1]:
                hitnum = k
        
        if hitnum > 0:
            answer += ROW[(i*L*27)+L*(hitnum):(i*L*27)+L*(hitnum+1)]
    print answer

