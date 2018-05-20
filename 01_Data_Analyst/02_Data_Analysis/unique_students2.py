#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Trenton J. McKinney
#
# Created:     10/11/2015
# Copyright:   (c) Trenton J. McKinney 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------


enrollments = [{u'status': u'canceled', u'is_udacity': u'True', u'is_canceled': u'True',
                u'join_date': u'2015-01-27', u'account_key': u'448', u'cancel_date': u'2015-01-27',
                u'days_to_cancel': u'0'}, {u'status': u'canceled', u'is_udacity': u'False',
                u'is_canceled': u'True', u'join_date': u'2014-11-10', u'account_key': u'700',
                u'cancel_date': u'2014-11-16', u'days_to_cancel': u'6'}, {u'status': u'canceled',
                u'is_udacity': u'False', u'is_canceled': u'True', u'join_date': u'2014-11-10',
                u'account_key': u'429', u'cancel_date': u'2015-03-10', u'days_to_cancel': u'120'},
               {u'status': u'canceled', u'is_udacity': u'False', u'is_canceled': u'True',
                u'join_date': u'2015-03-10', u'account_key': u'429', u'cancel_date': u'2015-06-17',
                u'days_to_cancel': u'99'}]


def row_students(record):
    unique_students = dict()

    for line in record:
        try:
            unique_id = line['account_key']
        except:
            unique_id = line['acct']

        #creates a dict, adds key if it doesn't exist and counts the occurences
        unique_students[unique_id] = unique_students.get(unique_id,0) + 1

    #print 'poop', unique_students
    return len(unique_students), len(record), unique_students



print 'Total Rows:', row_students(enrollments)[1], '\n','Unique Students:', row_students(enrollments)[0], '\n'

unique_enrolled_students = row_students(enrollments)[2]

print 'Occurences:', unique_enrolled_students





