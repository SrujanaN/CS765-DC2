import sys
import Product_lowRating_highCount

product = sys.argv[1]
product_meta = sys.argv[2]
product_count = sys.argv[3]
worst_rating = sys.argv[4]


exec(Product_lowRating_highCount, product, product_meta, product_count, worst_rating)
