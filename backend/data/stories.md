## happy path
* greet
  - utter_greet
* mood_great
  - utter_happy

## sad path 1
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* affirm
  - utter_happy

## sad path 2
* greet
  - utter_greet
* mood_unhappy
  - utter_cheer_up
  - utter_did_that_help
* deny
  - utter_goodbye

## say goodbye
* goodbye
  - utter_goodbye

## ask for loan
* greet
  - utter_greet
* request_loan
  - loan_form
  - form{"name": "loan_form"}
  - form{"name": null}
  - utter_slots_values
* thank
  - action_reset_slot

## ask for loanAgain
* request_loan
  - loan_form
  - form{"name": "loan_form"}
  - form{"name": null}
  - utter_slots_values
* thank
  - action_reset_slot

## ask for interest rate
* greet
  - utter_greet
* ask_interest_rate
  - interestRate_form
  - form{"name": "interestRate_form"}
  - form{"name": null}
  - utter_slots_values_interests
