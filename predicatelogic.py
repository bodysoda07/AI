% Facts

male(ravi).
male(kumar).

female(priya).
female(anita).

parent(ravi, kumar).
parent(ravi, priya).
parent(kumar, anita).

% Rules

father(X,Y) :- parent(X,Y), male(X).

mother(X,Y) :- parent(X,Y), female(X).

sibling(X,Y) :- parent(Z,X), parent(Z,Y), X \= Y.

grandparent(X,Y) :- parent(X,Z), parent(Z,Y).
