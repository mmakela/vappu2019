*** Settings ***
Library    MultiplesLib    ${INFILE}    ${OUTFILE}
Variables    MultiplesVariables.py
Suite Teardown    Remove Files    ${INFILE}    ${OUTFILE}


*** Variables ***
${INFILE}    roboin.txt
${OUTFILE}    roboout.txt


*** Test cases ***
Sunnyday test
    Create Input File    ${VALID_DATA}[in]
    ${output}    Run Successful Script
    Should Be Equal    ${output}    ${VALID_DATA}[out]
    Verify Output File    ${VALID_DATA}[out]

Bad Input File
    Create Input File    ${INVALID_DATA}[in]
    ${output}    Run UnSuccessful Script
    Should Be Equal    ${output}    ${INVALID_DATA}[out]


*** Keywords ***
Create Input File
    [Arguments]    ${content}
    Create File    ${INFILE}    ${content}

Verify Output File
    [Arguments]    ${content}
    ${output}    Get File    ${OUTFILE}
    Should Be Equal    ${output}    ${content}
