#!/usr/bin/python


import matplotlib
import matplotlib.pyplot as plt
from student_regression import student_reg
from class_vis import output_image
from ages_net_worths import age_net_worth_data

matplotlib.use('agg')

ages_train, ages_test, net_worths_train, net_worths_test = age_net_worth_data()

reg = student_reg(ages_train, net_worths_train)

print(f'Net Worth prediction for 47 year old: {reg.predict(47)}')
print(f'Slope: {reg.coef_}')
print(f'Intercept: {reg.intercept_}')

print('\n########## Stats on Test Dataset ##########')
print(f'r-squared score: {reg.score(ages_test, net_worths_test)}')
print('\n########## Stats on Training Dataset ##########')
print(f'r-squared score: {reg.score(ages_train, net_worths_train)}\n')

plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")

plt.show()

plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
