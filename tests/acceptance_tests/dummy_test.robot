| *** Settings ***   |
| Documentation      | Example using the pipe separated plain text format.

| *** Variables ***  |
| ${MESSAGE}         | Hello, i am robo!

| *** Test Cases *** |                 |                   |
| My Test            | [Documentation] | Example robo test |
|                    | Log             | ${MESSAGE}        |
| Another Test       | Should Be Equal | ${MESSAGE}        | Hello, i am robo!