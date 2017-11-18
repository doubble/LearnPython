class MyClass:
    variable = "blah"

    def function(self):
        print("This is a message inside the class.")

    def my_function_with_args(self, username, greeting):
        print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))
        print (self)


MyClass().my_function_with_args("Mark", "greets")