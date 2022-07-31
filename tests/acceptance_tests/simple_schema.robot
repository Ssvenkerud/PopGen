| *** Settings ***      |
| Documentation         | Accseptance tests cases for creating data with the simple schma type.
| Library               | OperatingSystem
| Library               | Process


| *** Variables ***     |
| ${stdout}
| ${SCHEMA}

| *** Test Cases ***    |

| Test I can read schema
| | # read the raw data
| | ${SCHEMA}= | Get file | tests/acceptance_tests/simple_schema.json
| |
| | # convert the data to a python object
| | ${object}= | Evaluate | json.loads('''${SCHEMA}''') | json
| |
| | # log the data
| | log | Schema is read:  ${object["filename"]} ${object["fileformat"]}

| Generate Simple data
| | ${SCHEMA}= | Get file | tests/acceptance_tests/simple_schema.json
| | ${object}= | Evaluate | json.loads('''${SCHEMA}''') | json
| | ${result}= | run process | python |  main.py
| | File Should Not Be Empty | output/${object["filename"]}.${object["fileformat"]}