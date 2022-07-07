import spoonacular
import requests
import socket
import time
import inspect

     def search_recipes_complex(self, query, **kwargs):
        """ Search through hundreds of thousands of recipes using advanced
            filtering and ranking. NOTE: This method combines searching by
            query, by ingredients, and by nutrients into one endpoint.
            https://spoonacular.com/food-api/docs#Search-Recipes-Complex
        """
        endpoint = "recipes/complexSearch"
        url_query = {}
        url_params = {"query": query, **kwargs}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)


     def search_recipes_by_ingredients(self, ingredients, fillIngredients=None, limitLicense=None, number=None, ranking=None):
        """ Find recipes that use as many of the given ingredients
            as possible and have as little as possible missing
            ingredients. This is a whats in your fridge API endpoint.
            https://spoonacular.com/food-api/docs#search-recipes-by-ingredients
        """
        endpoint = "recipes/findByIngredients"
        url_query = {}
        url_params = {"fillIngredients": fillIngredients, "ingredients": ingredients, "limitLicense": limitLicense, "number": number, "ranking": ranking}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)


     def get_recipe_information(self, id, includeNutrition=None):
        """ Get information about a recipe.
            https://spoonacular.com/food-api/docs#get-recipe-information
        """
        endpoint = "recipes/{id}/information".format(id=id)
        url_query = {}
        url_params = {"includeNutrition": includeNutrition}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)


     def get_analyzed_recipe_instructions(self, id, stepBreakdown=None):
        """ Get an analyzed breakdown of a recipe's instructions.
            Each step is enriched with the ingredients and the
            equipment that is used.
            https://spoonacular.com/food-api/docs#get-analyzed-recipe-instructions
        """
        endpoint = "recipes/{id}/analyzedInstructions".format(id=id)
        url_query = {}
        url_params = {"stepBreakdown": stepBreakdown}
        return self._make_request(endpoint, method="GET", query_=url_query, params_=url_params)