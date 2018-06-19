# Expert-System

An expert system for propositional calculus. 

The program accepts one parameter, which is the input file. It will contain a list of rules, a list of initial facts and a list of queries. For each of these queries, the program will tell if the fact is true, false, or undetermined.

## Symbols

The following symbols are defined, in order of decreasing priority:

- '(' and ')' work like normal parentheses . Example : A + (B | C) => D

- '!' means NOT. Example : !B

- '+' means AND. Example : A + B

- '|' means OR. Example : A | B

- 'ˆ' means XOR. Example : A ˆ B

- '=>' means "implies". Example : A + B => C

- '<=>' means "if and only if". Example : A + B <=> C

- '?' stands for the query

- '=' stands for the initial fact

- '#' opens a commentary

## Example

C => E # C implies E

A + B + C => D # A and B and C implies D

A | B => C # A or B implies C

A + !B => F # A and not B implies F

C | !G => H # C or not G implies H

V ^ W => X # V xor W implies X

A + B => Y + Z # A and B implies Y and Z

C | D => X | V # C or D implies X or V

E + F => !V # E and F implies not V

A + B <=> C # A and B if and only if C

A + B <=> !C # A and B if and only if not C

=ABG # Initial facts : A, B and G are true. All others are false.

?GVX # Queries : What are G, V and X ?
