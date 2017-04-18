# Write code in your favorite language (scripting language preferred) to "flatten" a dictionary. A dictionary can contain any number of nested dictionaries. A flattened dictionary has no nesting and instead contains a list of paths to leaf data (with a period representing edges of the path). For instance,

nested_dictionary = {
  'a': 5,
  'b': 6,
  'c': {
    'f': 9,
    'g': {
      'm': 17,
      'n': 3
    }
  }
}

# flatten(nested_dictionary) = {
#   'a': 5,
#  'b': 6,
#  'c.f': 9,
#  'c.g.m': 17,
#  'c.g.n': 3,
# }

def flatten(n_dict, result_dict={}, ancestors=''):
    # for item in n_dict:
    #     if type(n_dict[item]) == int:
    #         result_dict[item] = n_dict[item]
    #     else: 
    #         key = item
    #         while type(n_dict[item]) != int:
    #             n_dict = n_dict[item]
    for item in n_dict:            
        if type(n_dict[item]) == int: 
            if ancestors == '': 
                result_dict[item] = n_dict[item]
            else:
                new_key = ancestors+'.'+item
                result_dict[new_key] = n_dict[item]

        else:
            if ancestors == '':
                flatten(n_dict[item], result_dict, item)
            else: 
                new_key = ancestors +'.'+ item
                flatten(n_dict[item], result_dict, new_key)

    return result_dict
            
print flatten(nested_dictionary)