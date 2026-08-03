# Python - Test-driven development

Writing doctests alongside implementations so that behavior is specified
before and verified after the code is written.

## Description

Each module pairs a function with a plain-text doctest file under
tests/, covering normal use, edge cases, and the exceptions raised on
invalid input.

## Running the tests

    python3 -m doctest -v ./tests/*

## Author

Noxus - Holberton School
