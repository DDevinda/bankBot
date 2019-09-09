# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.events import AllSlotsReset, Restarted, SlotSet
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction, REQUESTED_SLOT

import requests
import json
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message("Hello World!")
#
#         return []

class RestForm(FormAction):
    def name(self) -> Text:
        return "loan_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print('indside required slots')

        return ["type"]

    def slot_mappings(self):

        print('inside slot mappings')
        return {"type": self.from_entity(entity="type",
                                            not_intent="chitchat")}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        # firstName = tracker.get_slot('firstname')
        # secondName = tracker.get_slot('secondname')
        print('hi')
        # print(firstName)
        # print(secondName)
        dispatcher.utter_template('utter_submit', tracker)
        return []

class InterestForm(FormAction):
    def name(self) -> Text:
        return "interestRate_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        print('indside required slots')

        return ["amount", "time"]

    def slot_mappings(self):

        print('inside slot mappings')
        return {"amount": self.from_entity(entity="amount",
                                            not_intent="chitchat"),
                "time": [self.from_entity(entity="time",
                                                intent=["inform",
                                                        "ask_interest_rate"]),
                               self.from_entity(entity="number")]}

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict]:

        # firstName = tracker.get_slot('firstname')
        # secondName = tracker.get_slot('secondname')
        print('hi')
        # print(firstName)
        # print(secondName)
        dispatcher.utter_template('utter_submit', tracker)
        return []

class ResetSlot(Action):

    def name(self):
        return "action_reset_slot"

    def run(self, dispatcher, tracker, domain):
        dispatcher.utter_message("Have a nice day 😋")
        return [SlotSet("type", None)]