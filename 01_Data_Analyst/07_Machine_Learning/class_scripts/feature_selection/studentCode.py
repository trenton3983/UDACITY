import pickle
from pprint import pprint as pp
from get_data import getData
import matplotlib.pyplot as plt


def compute_fraction(poi_messages, all_messages):
    """ given a number messages to/from POI (numerator)
        and number of all messages to/from a person (denominator),
        return the fraction of messages to/from that person
        that are from/to a POI
   """

    # you fill in this code, so that it returns either
    #     the fraction of all messages to this person that come from POIs
    #     or
    #     the fraction of all messages from this person that are sent to POIs
    # the same code can be used to compute either quantity

    # beware of "NaN" when there is no known email address (and so
    # no filled email features), and integer division!
    # in case of poi_messages or all_messages having "NaN" value, return 0.
    fraction = 0.

    if poi_messages != 'NaN' and all_messages != 'NaN':
        fraction = poi_messages/all_messages

    return fraction


data_dict = getData()

submit_dict = {}
for name in data_dict:
    data_point = data_dict[name]

    from_poi_to_this_person = data_point["from_poi_to_this_person"]
    to_messages = data_point["to_messages"]
    fraction_from_poi = compute_fraction(from_poi_to_this_person, to_messages)
    print('Fraction from POI: ', fraction_from_poi)
    data_point["fraction_from_poi"] = fraction_from_poi

    from_this_person_to_poi = data_point["from_this_person_to_poi"]
    from_messages = data_point["from_messages"]
    fraction_to_poi = compute_fraction(from_this_person_to_poi, from_messages)
    print('Fraction to POI: ', fraction_to_poi, '\n')
    submit_dict[name] = {"from_poi_to_this_person": fraction_from_poi,
                         "from_this_person_to_poi": fraction_to_poi}
    data_point["fraction_to_poi"] = fraction_to_poi


pp(submit_dict)

# x_val = []
# y_val = []
# poi_bool = []

for k, v in submit_dict.items():
    poi = data_dict[k]['poi']
    x, y = v.values()
    if poi:
        plt.scatter(x, y, c='r')
    else:
        plt.scatter(x, y, c='b')


#     x_val.append(x)
#     y_val.append(y)
#     if poi:
#         poi_bool.append(1)
#     else:
#         poi_bool.append(0)
#
# for i, v in enumerate(poi_bool):
#     if v == 1:
#         plt.scatter(x_val[i], y_val[i], c='r')
#     else:
#         plt.scatter(x_val[i], y_val[i], c='b')


plt.xlabel("Fraction of emails this person receives from POI's")
plt.ylabel("Fraction of emails this person sends to POI's")
plt.show()
