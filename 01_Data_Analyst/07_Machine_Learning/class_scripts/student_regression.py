from sklearn.linear_model import LinearRegression


def student_reg(ages_train, net_worths_train):

    reg = LinearRegression()
    reg.fit(ages_train, net_worths_train)

    return reg
