#data structures
name_list = ["ankit", "janak", "sunil"]
name_tuple = ("ankit", "janak", "sunil")
name_set = {"ankit", "janak", "sunil"}
name_dictionary = {"ankit":24, "janak":23, "sunil":25}
name_list.remove("sunil")
name_set.remove("janak")
del name_dictionary["ankit"]
print(name_list)
print(name_tuple)
print(name_set)
print(name_dictionary)