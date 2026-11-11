
% FACTS

person(john, 30).
person(lisa, 25).
person(mike, 35).
person(sarah, 28).
person(david, 40).
person(emma, 22).
person(alex, 32).

hobby(john, reading).
hobby(lisa, painting).
hobby(mike, hiking).
hobby(sarah, cooking).
hobby(david, gardening).
hobby(emma, photography).
hobby(alex, hiking).

friend(john, lisa).
friend(lisa, sarah).
friend(sarah, mike).
friend(david, emma).
friend(alex, mike).

% RULES

is_adult(Name) :-
    person(Name, Age),
    Age >= 18.

has_hobby(Name, Hobby) :-
    hobby(Name, Hobby).

similar_hobbies(Name1, Name2) :-
    hobby(Name1, Hobby),
    hobby(Name2, Hobby),
    Name1 \= Name2.

are_friends(Name1, Name2) :-
    friend(Name1, Name2);
    friend(Name2, Name1).

oldest_person(Name) :-
    person(Name, Age),
    \+ (person(_, OtherAge), OtherAge > Age).

friends_of(Person, Friends) :-
    findall(Friend, are_friends(Person, Friend), Friends).

hobbies_of_adults_with_hobby(Hobby, Adults) :-
    findall(Name,
            (is_adult(Name), has_hobby(Name, Hobby)),
            Adults).
