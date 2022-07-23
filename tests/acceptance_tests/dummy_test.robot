| *** Settings ***   |
| Documentation      | Example using the pipe separated plain text format.

| *** Variables ***  |
| ${MESSAGE}         | Hello, i am robo!

| *** Test Cases *** |                 |                   |
| accseptance test 1 | [Documentation] | Example robo test |
|                    | Log             | ${MESSAGE}        |
| accseptance test 2 | Should Be Equal | ${MESSAGE}        | Hello, i am robo!