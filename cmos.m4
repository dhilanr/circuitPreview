.PS
cct_init

G: ground
Q1: c_fet(up_,,N) with .S at G + (-dimen_*1.25,0); "sp_$\overline{\textsc{B}}$" rjust at Q1.G
Q2: c_fet(up_,,N) with .S at G; "sp_$\overline{\textsc{D}}$" rjust at Q2.G
Q3: c_fet(up_,R,N) with .S at G + (dimen_*0.75,0); "sp_$\overline{\textsc{C}}$" ljust at Q3.G
    line from Q1.S to Q3.S

Q4: c_fet(up_,,N) with .S at Q1.D; "sp_$\overline{\textsc{A}}$" rjust at Q4.G
Q5: c_fet(up_,,N) with .S at Q2.D; "sp_$\textsc{A}$" rjust at Q5.G 
Q6: c_fet(up_,R,N) with .S at Q3.D; "sp_$\overline{\textsc{A}}$" ljust at Q6.G
    line from Q4.D to Q6.D

P1: c_fet(up_,,P) with .S at Q5.Channel+(-dimen_*0.5,dimen_); "sp_$\overline{\textsc{A}}$" rjust at P1.G
P2: c_fet(up_,R,P) with .S at Q5.Channel+(dimen_*0.5,dimen_); "sp_$\overline{\textsc{C}}$" ljust at P2.G
    line from P1.D to P2.D

Midline: line from P1.S to P2.S
NetworkConnect: line from Q5.Channel + (0, dimen_*0.5) to Midline.c
    line from NetworkConnect.c to NetworkConnect.c + (dimen_*2, 0)
    { "sp_$\textbf{Y}$" ljust}
    
    

P3: c_fet(up_,,P) with .S at P1.D; "sp_$\textsc{A}$" rjust at P3.G
P4: c_fet(up_,R,P) with .S at P2.D; "sp_$\overline{\textsc{\textsc{D}}}$" ljust at P4.G
    line from P3.D to P4.D 
P5: c_fet(up_,,P) with .S at P3.D; "sp_$\overline{\textsc{A}}$" rjust at P5.G
P6: c_fet(up_,R,P) with .S at P4.D; "sp_$\overline{\textsc{C}}$" ljust at P6.G
    line from P5.D to P6.D
    line from last line.c to last line.c + (0, dimen_*0.3); Rail: Here
    line right dimen_/2 with .c at Here; "$V_{DD}$" above at Here + (-dimen_*0.22,0)
    

.PE