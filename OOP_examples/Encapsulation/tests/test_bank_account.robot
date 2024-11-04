*** Settings ***
Library           BankAccountLibrary.py

*** Variables ***
${ACCOUNT_NUMBER}   123456789
${INITIAL_BALANCE}  1000.0

*** Test Cases ***
Test Initial Balance
    [Documentation]   Verify the initial balance is correctly set
    Create Bank Account    ${ACCOUNT_NUMBER}    ${INITIAL_BALANCE}
    ${balance} =    Get Balance
    Should Be Equal As Numbers    ${balance}    ${INITIAL_BALANCE}

Test Deposit Positive Amount
    [Documentation]   Verify deposit increases balance correctly
    Create Bank Account    ${ACCOUNT_NUMBER}    ${INITIAL_BALANCE}
    Deposit Amount         500
    ${balance} =    Get Balance
    Should Be Equal As Numbers    ${balance}    1500.0

Test Deposit Negative Amount
    [Documentation]   Verify deposit does not change balance for negative amount
    Create Bank Account    ${ACCOUNT_NUMBER}    ${INITIAL_BALANCE}
    Deposit Amount         -100
    ${balance} =    Get Balance
    Should Be Equal As Numbers    ${balance}    ${INITIAL_BALANCE}

Test Withdraw Valid Amount
    [Documentation]   Verify withdraw decreases balance correctly
    Create Bank Account    ${ACCOUNT_NUMBER}    ${INITIAL_BALANCE}
    Withdraw Amount        200
    ${balance} =    Get Balance
    Should Be Equal As Numbers    ${balance}    800.0

Test Withdraw Insufficient Funds
    [Documentation]   Verify balance remains unchanged when withdrawing more than balance
    Create Bank Account    ${ACCOUNT_NUMBER}    100.0
    Withdraw Amount        200
    ${balance} =    Get Balance
    Should Be Equal As Numbers    ${balance}    100.0

Test Get Account Number
    [Documentation]   Verify account number is returned correctly
    Create Bank Account    ${ACCOUNT_NUMBER}    ${INITIAL_BALANCE}
    ${account_number} =    Get Account Number
    Should Be Equal        ${account_number}    ${ACCOUNT_NUMBER}
