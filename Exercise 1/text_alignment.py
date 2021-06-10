#!python
import time

# This script is going to do some alignment of text
# which is provided by the user.  At the moment we're
# collecting the data in a fairly crude way where we
# put the inputs into 5 separate variables, but we 
# will soon see how we could extend this to use an 
# arbitrary number of inputs 

# Collect 5 pieces of text from the user

text1 = input("Text1: ")
text2 = input("Text2: ")
text3 = input("Text3: ")
text4 = input("Text4: ")
text5 = input("Text5: ")

# For each of the pieces of text we want to put them
# into all uppercase and remove any spaces from the
# front and back.  Again, looking at help(str) we find
#
# strip(self, chars=None, /)
#   Return a copy of the string with leading and trailing 
#   whitespace removed.
#
# ...and also...
#
# upper(self, /)
#    Return a copy of the string converted to uppercase.

# Since each of these returns a modified string we
# can chain the two operatations together.

text1 = text1.strip().upper()
text2 = text2.strip().upper()
text3 = text3.strip().upper()
text4 = text4.strip().upper()
text5 = text5.strip().upper()

# We're also going to want to add the current time and
# date at the bottom of the output.  We need to find a 
# way to get this from the time package
#
# asctime(...)
#   asctime([tuple]) -> string
#
#   Convert a time tuple to a string, e.g. 
#   'Sat Jun 06 16:26:11 1998'. When the time tuple is 
#   not present, current time as returned by localtime()
#   is used.

time_text = time.asctime()


# Now we can print this all out.  We want the output to be
# centered in a 40 character block.  Again the str package 
# has a method which can help us.
#
# center(self, width, fillchar=' ', /)
#   Return a centered string of length width.
#
#   Padding is done using the specified fill character 
#   (default is a space).

# We can now print the output.  Since I want all of the 
# different pieces of text on different lines I'm setting
# the sep argument of print to be "\n", ie a newline.

print(
    text1.center(40),
    text2.center(40),
    text3.center(40),
    text4.center(40),
    text5.center(40),
    time_text.center(40),
    sep="\n"
)

