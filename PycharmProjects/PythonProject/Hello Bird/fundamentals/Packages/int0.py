
#another way to organize code
#a package is a directory or folder

import ecommerce.shipping
from ecommerce.shipping import calculate_shipping # specific f(n)
from ecommerce import shipping

ecommerce.shipping.calculate_shipping()
calculate_shipping()
shipping.calculate_shipping()
