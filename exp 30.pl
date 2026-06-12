% Facts

raining.
cloudy.

% Rules

wet_ground :-
    raining.

carry_umbrella :-
    raining.

bad_weather :-
    cloudy,
    raining.
