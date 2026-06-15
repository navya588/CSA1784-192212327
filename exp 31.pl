% Facts

student(ravi).
student(sita).
student(rahul).

% Pattern Matching Rule
match(X) :-
    student(X).
