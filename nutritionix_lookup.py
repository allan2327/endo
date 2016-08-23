from nutritionix import Nutritionix
import sys

def search(s):
	val = nix.search(s).json()[u'hits'][0]
	item_id = val[u'fields'][u'item_id']
	name = val[u'fields'][u'item_name']
	carbs = nix.item(id=item_id).json()[u'nf_total_carbohydrate']
	print name, carbs, 'carbs'

nix = Nutritionix(app_id="89b2a057", api_key="8bdfcf6398c7c4d6ab6407b92826264a")
query = raw_input()

print search(query)
sys.stdout.flush()
