import pprint

kid = ['Amber', 'Eli', 'Nyssa', 'Devin']
for first_kid in kid:
    for second_kid in kid:
        if first_kid != second_kid:
            pprint.pprint( first_kid + " | " + second_kid)