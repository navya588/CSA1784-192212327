% Facts

person(john, 25).
person(mary, 30).
person(david, 22).
person(susan, 28).

% Rule for Pattern Matching

find_person(Name, Age) :-
    person(Name, Age).
