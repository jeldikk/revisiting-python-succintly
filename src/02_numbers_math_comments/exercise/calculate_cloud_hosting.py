'''
In this exercise let's assume that you are planning to build a social networking service using your new 
Python skills. You make the decision to host your application on servers running in the cloud. Once you’ve selected a hosting provider, you want to know how much it will cost to operate per day and per 
month. You will launch your service using one server, and your provider will charge $1.02 per hour. 

Try to write a Python program that will display the answers to the following questions: 
1. How much will it cost to operate one server per day? 
2. How much will it cost to operate one server per month? 

'''

cost_per_hour = 1.02

cost_per_day = 24 * cost_per_hour
cost_per_month = 30 * cost_per_day

print("Cost to operate one server per day ${:.2f} when cost per hour is ${:.2f}".format(cost_per_day, cost_per_hour))
print("Cost to operate one server per month ${:.2f} when cost per hour is ${:.2f}".format(cost_per_month, cost_per_hour))