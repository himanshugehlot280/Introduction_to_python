# Nested if statement
# if inside if, you can hae it statements inside if statments: this is called nested if statement

if True:
    print('first block is running')
    if True:
        print('second block is running')
        if True:
            print('third block is running')
            if False:  #this statement  is not execute
                print('fourth block is running')
