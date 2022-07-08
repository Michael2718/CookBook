import spoonacular, requests


class API:
    def __init__(self, api_key):
        self.api = spoonacular.API(api_key)

    def complex_search(self, query, **kwargs):
        return self.api.search_recipes_complex(query, **kwargs).json()

    def search_by_ingredients(self, ingredients, number, ranking=None):
        str_ingredients = ',+'.join(ingredients)
        return self.api.search_recipes_by_ingredients(ingredients=str_ingredients, number=number, ranking=ranking).json()

    def recipe_info(self, id):
        return self.api.get_recipe_information(id).json()

    def ingredient_search(self, query, number):
        return self.api.autocomplete_ingredient_search(query=query, number=number).json()

    def get_instruction(self, id):
        return self.api.get_analyzed_recipe_instructions(id, False).json()

    def get_card(self, id):
        url = f"https://api.spoonacular.com/recipes/{id}/card?apiKey={self.api.api_key}"
        response = requests.get(url)
        return response.json()['url']
