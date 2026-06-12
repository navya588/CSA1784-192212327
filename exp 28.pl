% Symptoms of patients

symptom(john, fever).
symptom(john, cough).
symptom(john, headache).

symptom(mary, fever).
symptom(mary, body_pain).

symptom(david, cough).
symptom(david, sore_throat).

% Diagnosis Rules

disease(Patient, flu) :-
    symptom(Patient, fever),
    symptom(Patient, cough),
    symptom(Patient, headache).

disease(Patient, viral_fever) :-
    symptom(Patient, fever),
    symptom(Patient, body_pain).

disease(Patient, cold) :-
    symptom(Patient, cough),
    symptom(Patient, sore_throat).
