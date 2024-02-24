#!/usr/bin/env python3
menu = {
    'categories': [
        {
            'name': 'Drinks',
            'items': [ 'Tea', 'Coffee' ]
         },
        {
            'name': 'Snacks',
            'items': ['Brownie', 'Muffin' ]
        }
        ]
    }
import json
print(json.dumps(menu))
