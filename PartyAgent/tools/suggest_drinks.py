from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "suggest_drinks"
    description = "Suggests drinks based on the taste preference."
    inputs = {'taste': {'type': 'string', 'description': 'The drink taste preference. Allowed values are: - "sweet": Drink menu for sweet taste. - "sour": Drink menu for sour taste. - "spicy": Drink menu for spicy taste. - "custom": Custom drink menu suggested by assistant.'}}
    output_type = "string"

    def forward(self, taste: str) -> str:
        """
        Suggests drinks based on the taste preference.
        Args:
            taste (str): The drink taste preference. Allowed values are:
                - "sweet": Drink menu for sweet taste.
                - "sour": Drink menu for sour taste.
                - "spicy": Drink menu for spicy taste.
                - "custom": Custom drink menu suggested by assistant.
        """
        if taste == "sweet":
            return "Espresso Martini, Piña Colada, White Russian"
        elif taste == "sour":
            return "Whiskey Sour, Margarita, Sidecar"
        elif taste == "spicy":
            return "Spicy Margarita, Mezcal Mule, Spicy Paloma"
        else:
            return "Custom drink menu suggested by assistant"