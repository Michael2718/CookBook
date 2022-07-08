from flask import Blueprint, render_template, request
import api_module


# CONFIG
API_KEY = open("../api_key", 'r').read()

api = api_module.API(API_KEY)

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("Home.html")


@views.route('/<int:id>')
def show_recipe(id):
    recipe = api.recipe_info(id)
    instruction = api.get_instruction(id)
    card = api.get_card(id)
    return render_template("RecipePage.html", recipe=recipe, instruction=instruction, card=card)


@views.route('/general-search', methods=['POST', 'GET'])
def general_search():
    if request.method == "POST":
        if request.form.getlist('diet').__len__() != 0 and request.form.getlist('intolerances').__len__() != 0:
            response = api.complex_search(request.form['query'],
                                          diet=request.form['diet'],
                                          intolerances=request.form['intolerances'],
                                          addRecipeInformation=True)
        elif request.form.getlist('diet').__len__() != 0:
            response = api.complex_search(request.form['query'],
                                          diet=request.form['diet'],
                                          addRecipeInformation=True)
        elif request.form.getlist('intolerances').__len__() != 0:
            response = api.complex_search(request.form['query'],
                                          intolerances=request.form['intolerances'],
                                          addRecipeInformation=True)
        else:
            response = api.complex_search(request.form['query'], addRecipeInformation=True)
        return render_template("GeneralSearch.html", recipes=response['results'])
    else:
        return render_template("GeneralSearch.html")


@views.route('/search-by-ingredients', methods=['POST', 'GET'])
def search_by_ingredients():
    if request.method == "POST":
        ingredients = request.form['query'].split()
        recipes = api.search_by_ingredients(ingredients, number=20, ranking=1)
        # recipes_info = [api.recipe_info(recipe['id']) for id, recipe in recipes]
        return render_template("SearchByIngredients.html",
                               ingredients=ingredients,
                               recipes=recipes)
    else:
        return render_template("SearchByIngredients.html")


@views.route('/search-history')
def search_history():
    return render_template("SearchHistory.html")


@views.route('/favorites')
def favorites():
    return render_template("Favorites.html")
