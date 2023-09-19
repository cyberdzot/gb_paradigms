% Prolog - язык логического программирования

% вычислить суммму чисел в списке
sum_list([], 0):-!.
sum_list([Head|Tail], Sum):-
   sum_list(Tail, TailSum),
   Sum is TailSum + Head.

% пример:
% sum_list([1,2,5], Sum).