# coding=utf-8

name = raw_input("What is your name?")        #如果是在Python 3中，更换为input()
age = raw_input("How old are you?")

print "Your name is: ", name                                 #Python 3: print("Your name is: ",  name)
print "You are " + age + " years old."                #Python 3: print("You are " + age + " years old.")

after_ten = int(age) + 10
print "You will be " + str(after_ten) + " years old after ten years."
