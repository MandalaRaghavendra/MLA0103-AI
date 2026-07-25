bird(parrot).
bird(crow).
bird(penguin).

can_fly(X):-
    bird(X),
    X \= penguin.