# Expert-System

An expert system for propositional calculus. 

The program accept one parameter, which is the input file. It will contain a list of rules, then a list of initial facts, then a list of queries. For each of these queries, the programmust, given the facts and rules given, tell if the query is true, false, or undetermined.

## Symbols

The following symbols are defined, in order of decreasing priority:

- ( and ) which are fairly obvious. Example : A + (B | C) => D

-! which means NOT. Example : !B

- + which means AND. Example : A + B

- | which means OR. Example : A | B

- ˆ which means XOR. Example : A ˆ B

- => which means "implies". Example : A + B => C

- <=> which means "if and only if". Example : A + B <=> C

- ? stands for the query

- = stands for the initial fact

- # opens a commentary

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
