from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "get_store_price"
    description = "Returns store price text description based on store name, description includes discounts details."
    inputs = {'store': {'type': 'string', 'description': 'Store name. Allowed values are: "Store A", "Store B", "Store C".'}}
    output_type = "object"

    def forward(self, store: str) -> dict:
        """
        Returns store price text description based on store name, description includes discounts details. 
        Args:
            store (str): Store name. 
            Allowed values are: "Store A", "Store B", "Store C". 
        """
        store_price_desc = {
            "Store A": {"apple": "$2 each", "orange": "$5 each, buy 5 get 1 free", "banana": "$5.5 each, 10% off for $15 and higher in total"}, 
            "Store B": {"apple": "$3 each, buy 3 get 1 free", "orange": "$4 each", "banana": "$6 each, buy 4 get 1 free"},      
            "Store C": {"apple": "$2.5 each", "orange": "$4.5 each, 10% off for $15 and higher in total", "banana": "$5 each"}
        }

        return store_price_desc[store]