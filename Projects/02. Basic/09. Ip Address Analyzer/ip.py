print('\n\tIp Address Analyzer') # Project Name

ip = input('\nIPv4 Address: ') # Input IPv4

if ip.count('.') != 3: # If IPv4 address not contain 3 periods
    print('\nIPv4 Address Invalid\n')

else:
   dot1_index = ip.find('.')
   octet1 = ip[0:dot1_index] # First Octet

   last3_octet = ip[(dot1_index+1):]
   dot2_index = last3_octet.find('.')
   octet2 = last3_octet[0:dot2_index] # Second Octet

   last2_octet = last3_octet[(dot2_index+1):]
   dot3_index = last2_octet.find('.')
   octet3 = last2_octet[0:dot3_index] # Third Octet

   octet4 = last2_octet[(dot3_index+1):] # Fourth Octet

   print('\nIPv4 Address Analyzed, Successfuly and printing Result...') # Process Completion

   print(f'\nOctet1: {octet1}')
   print(f'Octet2: {octet2}')
   print(f'Octet3: {octet3}')
   print(f'Octet4: {octet4}\n')
