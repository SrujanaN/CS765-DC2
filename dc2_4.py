import sys
import category_rating_review

product = sys.argv[1]
product_meta = sys.argv[2]

exec(category_rating_review, product, product_meta)
