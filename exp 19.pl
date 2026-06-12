% Facts

record(ravi,   smith,  mathematics, cs101).
record(priya,  johnson, physics,     ph102).
record(arun,   williams, chemistry,  ch103).
record(neha,   brown,   biology,     bi104).
record(kiran,  davis,   computer_science, cs105).

% Rules

student_subject(Student, Subject) :-
    record(Student, _, Subject, _).

teacher_subject(Teacher, Subject) :-
    record(_, Teacher, Subject, _).

subject_code(Subject, Code) :-
    record(_, _, Subject, Code).
