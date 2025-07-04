""" A spam comment is defined as a text containing following keywords: 
'Make a lot of money', 'buy now', 'subscribe this', 'click this'. Write a program
to detect these spams. """

print('\n\tComment Spammy ??') # Project Name

comment = input('\nPaste exact comment you got from unknown number: ').lower()

spam_key1 = 'Make a lot of money'.lower()
spam_key2 = 'Buy Now'.lower()
spam_key3 = 'subscribe this'.lower()
spam_key4 = 'click this'.lower()

if spam_key1 in comment:
    print('\nAlert!!, Someone is trying you to trap in Money Greed.\n')

elif spam_key2 in comment:
    print('\nBeAware, Someone is trying you to trap in Urgency-Case.\n')

elif spam_key3 in comment:
    print('\nBeAware, There is a marketing trick in this comment.\n')

elif spam_key4 in comment:
    print('\nSpammy!!, Don\'t click on the link . First, Verify it from `virustotal.com`.\n')

else:
    print('\nSafe.\n')
