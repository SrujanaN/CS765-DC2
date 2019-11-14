import sys
import Category_Rating

product = sys.argv[1]
product_meta = sys.argv[2]

exec(Category_Rating, product, product_meta)
