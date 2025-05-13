from smolagents import Tool
from typing import Any, Optional

class SimpleTool(Tool):
    name = "convert_unit"
    description = "Convert a value from one unit to another."
    inputs = {'value': {'type': 'number', 'description': 'The numerical value to be converted.'}, 'from_unit': {'type': 'string', 'description': 'The unit of the input value (e.g., "cm", "kg").'}, 'to_unit': {'type': 'string', 'description': 'The target unit for conversion (e.g., "km", "lb").'}}
    output_type = "number"

    def forward(self, value: float, from_unit: str, to_unit: str) -> float:
        """
        Convert a value from one unit to another.

        Args:
            value: The numerical value to be converted.
            from_unit: The unit of the input value (e.g., "cm", "kg").
            to_unit: The target unit for conversion (e.g., "km", "lb").

        Returns:
            The converted value in the target unit.

        Raises:
            ValueError: If the conversion between the specified units is not supported.
        """

        # Define conversion rates
        conversion_rates = {
            # Length
            'mm': {'cm': 0.1, 'm': 0.001, 'km': 0.000001, 'in': 0.0393701, 'ft': 0.00328084},
            'cm': {'mm': 10, 'm': 0.01, 'km': 0.00001, 'in': 0.393701, 'ft': 0.0328084},
            'm': {'mm': 1000, 'cm': 100, 'km': 0.001, 'in': 39.3701, 'ft': 3.28084,},
            'km': {'mm': 1000000, 'cm': 100000, 'm': 1000, 'in': 39370.1, 'ft': 3280.84},
            'in': {'mm': 25.4, 'cm': 2.54, 'm': 0.0254, 'km': 0.0000254, 'ft': 0.0833333},
            'ft': {'mm': 304.8, 'cm': 30.48, 'm': 0.3048, 'km': 0.0003048, 'in': 12,},

            # Weight
            'mg': {'g': 0.001, 'kg': 0.000001, 'lb': 0.00000220462, 'oz': 0.000035274},
            'g': {'mg': 1000, 'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
            'kg': {'mg': 1000000, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
            'lb': {'mg': 453592, 'g': 453.592, 'kg': 0.453592, 'oz': 16},
            'oz': {'mg': 28349.5, 'g': 28.3495, 'kg': 0.0283495, 'lb': 0.0625},
        }

        # Convert `value` to float if it's a string
        if isinstance(value, str):
            try:
                value = float(value)
            except ValueError:
                raise ValueError("Value must be a number")
        
        # Check if the units are valid
        if from_unit not in conversion_rates or to_unit not in conversion_rates[from_unit]:
            raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported")

        # Debug error
        # print(f"Value: {value}, Type: {type(value)}")
        # print(f"From unit: {from_unit}, To unit: {to_unit}")
        # print(f"Conversion rate: {conversion_rates[from_unit][to_unit]}, Type: {type(conversion_rates[from_unit][to_unit])}")

        
        # Perform the conversion
        return value * conversion_rates[from_unit][to_unit]