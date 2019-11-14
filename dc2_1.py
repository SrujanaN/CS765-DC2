import sys
import product_price_count

product = sys.argv[1]
product_meta = sys.argv[2]

exec(product_price_count, product, product_meta)
