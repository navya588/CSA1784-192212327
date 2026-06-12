% Facts

fruit_color(apple, red).
fruit_color(banana, yellow).
fruit_color(grapes, green).
fruit_color(orange, orange).
fruit_color(mango, yellow).
fruit_color(strawberry, red).

% Rule

color(Fruit, Color) :-
    fruit_color(Fruit, Color).
