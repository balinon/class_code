my_dictionary = {}
print(type(my_dictionary))
my_dictionary["gigE0"] = "Link to ISP"
my_dictionary["gigE1"] = "DNS is the root of all problems"
my_dictionary["gigE2"] = "An IPv4 address walks into the barand yells, 'Bartender! Give me a cider, I'm exhausted!"
my_dictionary["gigE3"] = "You know the think about NTP jokes? Its all about the timing"
print (my_dictionary["gigE2"])
my_list = [3, 2, 1]
my_other_dictionary = {}
my_other_dictionary["thisisakey"] = "thisisavalue"
my_dictionary["nested_list"] = my_list
my_dictionary["nested_dict"] = my_other_dictionary
print(my_dictionary["nested_dict"]["thisisakey"])
