# Select Related Examples
from mainapp.models import Restaurant, Topping, Pizza



# Prefetch_related Example :

resturants = Restaurant.objects.prefetch_related('best_pizza__toppings')

# In the above query we fetched all the resturants and their related pizzas and all pizzas with their related toppings

# This will be done in 3 db queries - one for the restaurants, one for the pizzas, and one for the toppings.


#Optimization :

Restaurant.objects.select_related('best_pizza').prefetch_related('best_pizza__toppings')

#here we are hitting db two times as  prefetch_related is hitted after the main query , and it has the precalculated result for best pizza , so it will avoid calculating them again


#SELECT RELATED

best_pizza = Restaurant.objects.select_related('best_pizza')
# select related basicaly we are using for when we have Forigenkey or one to one relation between the tables

'''

select_related works by creating an SQL join  thats why, select_related gets the related objects
  in the same database query. However, to avoid the much larger result set that would result
   from joining across a ‘many’ relationship, select_related is limited to single-valued
    relationships - foreign key and one-to-one.
'''



#Prefetch_Related

'''
prefetch_related, does a separate lookup for each relationship, 
and does then it do ‘joining’ in Python. This allows it to prefetch many-to-many and 
many-to-one objects, which cannot be done using select_related, .'''

.