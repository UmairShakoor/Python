def myFunc():
    print('Hello World')

if __name__ == '__main__': # If file is in __main__
    print('We are directly running this code')
    myFunc()                                                                                                                                                           
    print(__name__) # Name of file from where it is executed                                                                                                      
    '''                                                                                                                                                                Explanation:                                                                                                                                                           if we executed file which has the actual source code then it returns __main__ and if we have imported source code from another file (module) then it will 
        print __module__ (Files Name)                                                                                                                             
    ''' 
