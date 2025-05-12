from typing import Any, Optional
from smolagents.tools import Tool

class PartyThemeTool(Tool):
    name = "party_theme_generator"
    description = """
    This tool suggests creative party ideas based on MBTI. 
    It returns a unique party theme idea.
    """
    inputs = {'mbti': {'type': 'string', 'description': 'MBTI type (e.g. INFP, ESTJ)'}}
    output_type = "string"

    def forward(self, mbti: str): 
        themes = {
            "INFP": "Dreamy Vaporwave",
            "ENFJ": "Charity Gala",
            "INTJ": "Futuristic Tech Expo",
            "ENTP": "Debate Night",
            "ISFJ": "Cozy Book Club",
            "ESTP": "Adventure Sports Day",
            "INFJ": "Mystical Masquerade",
            "ENTJ": "Corporate Networking Mixer",
            "ISTP": "DIY Workshop",
            "ENFP": "Carnival of Colors",
            "ISFP": "Artistic Retreat",
            "ESTJ": "Classic Elegance Ball",
            "INTP": "Science Fiction Convention",
            "ESFJ": "Community Potluck",
            "ISTJ": "Vintage Tea Party",
            "ESFP": "Beach Party Extravaganza"
        }

        return themes.get(
            mbti.upper(), 
            f"Invalild MBTI type: {mbti}.upper()."
        )

    def __init__(self, *args, **kwargs):
        self.is_initialized = False
