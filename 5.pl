move(1,A,B,_):-
    write('Move disk from '),write(A),
    write(' to '),write(B),nl.

move(N,A,B,C):-
    N>1,
    N1 is N-1,
    move(N1,A,C,B),
    move(1,A,B,C),
    move(N1,C,B,A).