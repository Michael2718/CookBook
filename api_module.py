import spoonacular


class API:
    def __init__(self, api_key):
        self.api = spoonacular.API(api_key)

    def complex_search(self, query, **kwargs):
        return self.api.search_recipes_complex(query, **kwargs).json()

    def find_by_ingredients(self, ingredients, number, ranking=None):
        str_ingredients = ',+'.join(ingredients)
        return self.api.search_recipes_by_ingredients(ingredients=str_ingredients, number=number, ranking=ranking).json()

    def recipe_info(self, id):
        return self.api.get_recipe_information(id).json()

    def ingredient_search(self, query, number):
        return self.api.autocomplete_ingredient_search(query=query, number=number).json()
