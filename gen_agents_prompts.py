#system to attention to grab actions

actions = """
Given the following agent actions, extract the action itself and not any surrounding data, biases, or descriptive language.

{actions}

"""

## recognize entities
entities = """
Given the following agent actions, identify the entities mentioned.

{actions}
"""

## grab locations

locations = """

Given the following agent actions, identify the locations mentioned.

{actions}

"""

## Core rules prompt first (basic rules)

rules = """
Based on the CORE RULES, are the agent actions below acceptable?

Agent action:
{actions}

Return the following JSON object. Answer 0 for FALSE and 1 for TRUE:

"answer": 0 or 1
"explanation": Explanation for your answer.

"""

## If fail, auto regenerate

## Character profile prompt next (essential details)

character_profile = """
Based on {character} profile, are the agent actions below acceptable?

Agent action:
{actions}

Return the following JSON object. Answer 0 for FALSE and 1 for TRUE:

"answer": 0 or 1
"explanation": Explanation for your answer.

"""

# If fail, auto reboot

# Lore comes last (wider details)
lore = """
Based on Elordia lore, are the agent actions below acceptable?

Agent action:
{actions}

Return the following JSON object. Answer 0 for FALSE and 1 for TRUE:

"answer": 0 or 1
"explanation": Explanation for your answer.

"""
