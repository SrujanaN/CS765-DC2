import sys
import customer_reviews_rating

product = sys.argv[1]
product_meta = sys.argv[2]

exec(customer_reviews_rating, product, product_meta)
