student(ravi,cs101).
student(sita,cs102).
student(rahul,cs103).

teacher(smith,cs101).
teacher(john,cs102).
teacher(kumar,cs103).

subject(cs101,'AI').
subject(cs102,'DBMS').
subject(cs103,'CN').

student_teacher(S,T):-
    student(S,C),
    teacher(T,C).