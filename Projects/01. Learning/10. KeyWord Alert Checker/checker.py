print('\n\tKeyWord Alert Checker') # Project Name
print('\nScanning for \'Error\' or \'Zone\'...') # Process Info

message = input('\nPaste the exact message you got from SEIM: ').lower() # Used .lower() to avoid caseSensitive issue

error_index = message.find('error')
zone_index = message.find('zone')

print('\nMessage Analyzed and printing Result...') # Process Completion

if error_index >= 0: # If Error keyword exist in message
    print('\nComunication Problem between SEIM agent and server\n')

if zone_index >= 0: # If Zone keyword exist in message
    print('\nThere is something wrong in your InfraStruture Zones\n')

if error_index < 0 and zone_index < 0: # If neither Zone nor Error exist in message
    print('\nYour are Safe!!\n')
