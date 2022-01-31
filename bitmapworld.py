#!/usr/bin/env python

import sys

# bitmap to be displayed
bitmap = """
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
...................................................................."""

message = input('Enter the message to display with the bitmap: ')
# quit program if no message supplied
if message == '':
    sys.exit()

# for each line in bitmap
for line in bitmap.splitlines():
    # iterate through each bit per line
    for i, bit in enumerate(line):
        if bit == " ":
            print('_', end='')
        else:
            # prints out each individual character of the message.
            # i % len of message = remainder: always within length of message
            print(message[i % len(message)], end='')
    print()
