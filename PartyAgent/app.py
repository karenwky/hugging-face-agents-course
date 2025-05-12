import yaml
import os
from smolagents import GradioUI, CodeAgent, LiteLLMModel

# Get current directory path
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

from tools.web_search import DuckDuckGoSearchTool as WebSearch
from tools.visit_webpage import VisitWebpageTool as VisitWebpage
from tools.suggest_drinks import SimpleTool as SuggestDrinks
from tools.get_store_price import SimpleTool as GetStorePrice
from tools.party_theme_generator import PartyThemeTool as PartyThemeGenerator
from tools.final_answer import FinalAnswerTool as FinalAnswer



model = LiteLLMModel(
num_ctx=8192,
model_id='ollama_chat/qwen3:8b',
api_base='http://127.0.0.1:11434',
)

web_search = WebSearch()
visit_webpage = VisitWebpage()
suggest_drinks = SuggestDrinks()
get_store_price = GetStorePrice()
party_theme_generator = PartyThemeGenerator()
final_answer = FinalAnswer()


with open(os.path.join(CURRENT_DIR, "prompts.yaml"), 'r') as stream:
    prompt_templates = yaml.safe_load(stream)

agent = CodeAgent(
    model=model,
    tools=[web_search, visit_webpage, suggest_drinks, get_store_price, party_theme_generator],
    managed_agents=[],
    #class='CodeAgent',
    max_steps=20,
    verbosity_level=2,
    grammar=None,
    planning_interval=None,
    name=None,
    description=None,
    executor_type='local',
    executor_kwargs={},
    max_print_outputs_length=None,
    prompt_templates=prompt_templates
)
if __name__ == "__main__":
    GradioUI(agent).launch()
