Understanding Python Dictionaries (The "Folder" Concept)

A Dictionary is a way to store data where every piece of information has a Name (Key) and a Value.

1. The Anatomy

In a List, you only have values: [5, 2, 3]
In a Dictionary, you have labels: {"law": 5, "shorthand": 2, "coding": 3}

Key: The label (e.g., "law") — Always a string in quotes.

Value: The data (e.g., 5) — Can be a number, string, or even another list.

The "Colon Rule": Always use a : between the label and the data.
The "Comma Rule": Use a , to separate different pairs.

2. Why we put the Dictionary INSIDE the loop

Think of it like this:

The Scenario: You are at a store checkout.

Before the loop: The cashier gets a Bag (The List: history = []).

Inside the loop:

The cashier picks up an Item (The Dictionary: entry = {...}).

The cashier puts that Item into the Bag (history.append(entry)).

Next turn of the loop:

The cashier picks up a NEW Item.

By creating the dictionary inside the loop, we make a fresh, new folder for every day.

3. Srujana's Practice Challenge (Completed! ✅)

To master the "Manual" dictionary, try to write the code for these two examples. Use the syntax: name = {"key": value}

Task A: A Book Dictionary

Create a dictionary named my_book.

It should have a title: "Constitution"

It should have pages: 448

SOL: my_book = {"title": "Constitution", "pages": 448}

Task B: A Student Dictionary

Create a dictionary named student.

It should have a name: "Srujana"

It should have a status: "Learning"

SOL: student = {"name": "Srujana", "status": "Learning"}

Summary

List ([]): A collection of many things.

Dictionary ({}): One thing with many details.

Note from Gemini: Great job completing these, Srujana! Your syntax is perfect. You've mastered the foundation of dictionaries.