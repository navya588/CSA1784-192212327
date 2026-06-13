% Facts: planet(Name, Type, Moons)

planet(mercury, terrestrial, 0).
planet(venus, terrestrial, 0).
planet(earth, terrestrial, 1).
planet(mars, terrestrial, 2).
planet(jupiter, gas_giant, 95).
planet(saturn, gas_giant, 146).
planet(uranus, ice_giant, 27).
planet(neptune, ice_giant, 14).

% Rule to find planets with moons
has_moons(Planet) :-
    planet(Planet, _, Moons),
    Moons > 0.

% Rule to find terrestrial planets
terrestrial_planet(Planet) :-
    planet(Planet, terrestrial, _).

% Rule to find gas giant planets
gas_giant(Planet) :-
    planet(Planet, gas_giant, _).

% Rule to find planets having more than N moons
more_moons_than(Planet, N) :-
    planet(Planet, _, Moons),
    Moons > N.
