data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."
                    #  ^   ^                           ^
                    # Order of %s is also the index of data in tuple so,
                    # 1st %s is 1st ele in tuple
print(format_string % data)