"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise directions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

# -------------------------------------------------------------------
# Start here.


# Part 2: Write queries

# Get the brand with the **id** of 8.
q1 = Brand.query.get(8)
# Get all models with the **name** Corvette and the **brand_name** Chevrolet.
q2 = Model.query.filter_by(name='Corvette', brand_name='Chevrolet').all()

# Get all models that are older than 1960.
q3 = Model.query.filter(Model.year < 1960).all()
# this is what the solutuon said but it gave me me models younger than 1960 ie. founded after 19602222
q3 = Model.query.filter(Model.year > 1960).all()

# Get all brands that were founded after 1920.
q4 = Brand.query.filter(Brand.founded > 1920).all()

# Get all models with names that begin with "Cor".
q5 = Model.query.filter(Model.name.like('Cor%'))).all()

# Get all brands with that were founded in 1903 and that are not yet discontinued.
q6 = Brand.query.filter_by(founded=1903, discontinued=None).all()
# Get all brands with that are either discontinued or founded before 1950.
q7 = Brand.query.filter(db.or_(Brand.founded < 1950, Brand.discontinued != None)).all()
# Get any model whose brand_name is not Chevrolet.
q2 = Model.query.filter(Model.brand_name != "Chevrolet").all()

# Fill in the following functions. (See directions for more info.)

def get_model_info(year):
    '''Takes in a year, and prints out each model, brand_name, and brand
    headquarters for that year using only ONE database query.'''
    models = Model.query.filter_by(year=year).all()

   	for model in models:
   		print "Model: %s, Brand Name: %s, Headquarters: %s" % (model.name, model.brand_name, model.Brand.headquarters)
   

def get_brands_summary():
    '''Prints out each brand name, and each model name for that brand
    using only ONE database query.'''
    # computer was having troubles and coun't check  against db
    brands = Brand.query.all()

    
    for brand in brands:
    	statement = ""
    	statement + "\n Brand:" + brand + "Models: "
    	for model in brand.models:
    		statement + model.name ", "
    	print statement

    

    

# -------------------------------------------------------------------


# Part 2.5: Advanced and Optional
def search_brands_by_name(mystr):
    pass


def get_models_between(start_year, end_year):
    pass

# -------------------------------------------------------------------

# Part 3: Discussion Questions (Include your answers as comments.)

# 1. What is the returned value and datatype of ``Brand.query.filter_by(name='Ford')``?
#Would return a db object of the Ford brand. 


# 2. In your own words, what is an association table, and what *type* of relationship
# does an association table manage?
# An associate table manages how the tables connect and allows you to easily get information of multiple tables.

