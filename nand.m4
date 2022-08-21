.PS

log_init

del = linewid/4

Or1: Autologix(
  Or(A,B),
  N
)

N1: Autologix(
  Not(A),
  N
)
line from (Or1.Out) to (N1.In1)

OrTop: Autologix(
  Or(A,B),
  N
) with .sw at N1.ne + (1.65*del, 1.65*del)
line from (OrTop.In2) to (OrTop.In2, N1.Out) then to (N1.Out,  N1.Out)
line from (OrTop.In1) to (Or1.In1, OrTop.In1) then to (Or1.In1,Or1.In1)
line from (Or1.In1, OrTop.In1) to (Or1.In1, OrTop.In1)+(-2*del, 0)

OrBot: Autologix(
  Or(A,B),
  N
) with .nw at N1.se + (1.65*del, -1.65*del)
line from (OrBot.In1) to (OrBot.In1, N1.Out) then to (N1.Out,  N1.Out)
line from (OrBot.In2) to (Or1.In2, OrBot.In2) then to (Or1.In2,Or1.In2)
line from (Or1.In2, OrBot.In2) to (Or1.In2, OrBot.In2)+(-2*del, 0)

And1: Autologix(
  And(A,B),
  N
) with .center at N1.Out + (10*del, 0)
line from (And1.Out) to (And1.Out, And1.Out) + (1.2*del, 0)
line from (OrTop.Out) to (And1.In1, OrTop.Out) then to (And1.In1, And1.In1)
line from (OrBot.Out) to (And1.In2, OrBot.Out) then to (And1.In2, And1.In2)

# Autologix(Nand(Nand(Nand(Nand(A,B), Nand(C,D)),Nand(Nand(C,D),Nand(E,F))), Nand(F,G)));

.PE