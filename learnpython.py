'''
INDENTATION 
leading whitespace before any statements
improves readability
Helps in indicating a block of code

= assignment operator
== equality operator


'''
name = "sam"
if name == "sam":
    print("Hello Sam")
else:
    print('Hello Dude')
print('How are you?')

'''
REPL read evaluate print loop thus python interactive shell
as a calculator
Arithmetic operations
** exponent power
% modulus/remainder
// integer division ans is integer
/ division ans is floating point
* multiplication
- subtraction
/ division

PRECEDENCE OF ARITHMETIC OPERATORS
**
%, //, /, *
-, +
'''

'''
int DATA TYPE
decimal integer representation normal numbers
result will be an integer

non-decimal integers base is not 10
thus adding prefixes
0b or 0B for binary
0o or 0O for octal
0x or 0X for hexadecimal

converting non decimal to decimal
refer from notes
you can use print for conversion

float DATATYPE
xE or xe  for number with decimal point where x is no.

Boolean DATA TYPE
for true or false

STRING DATA TYPE
single quotes inside double quotes
escaping quotes we use a 
when multi-line stringing we  use

ACCESSING INDIVIDUAL CHARACTERS IN A STRING
each character receives a positive number

ACCESSING INDIVIDUALS FROM THE LAST
each character receives a negative number

ACCESSING THE SUBSTRING
or range of characters in string
[name_of_variable][start_index:end_index]

STRING CONCATENATE OPERATOR
combining strings using (+)

STRING REPETITION OPERATOR
Creates multiple copies of the string
if (n) is integer and (s) string then (n*s) order does not matter thus copies created

STRING COMPARISON OPERATORS

compare two strings at a time thus a binary operator
comparisons are caseSensitive
ASCII VALUE
Each character has unique ASCII value thus compared. 
ASCII values of capital letters have smaller value compared to smaller letters
ASCII values are incrimental in nature

string comparison operator
== operator
if two strings are equal then TRUE
else FALSE

the not equal operator
!= operator
if two strings are unequal then TRUE
else FALSE

the < operator
returns TRUE if first string is smaller than the second string
else FALSE

The <= operator
Returns TRUE if the first string is smaller or equal to the second string
else FALSE

The > operator
Returns TRUE if the string is greater than the second string,
else FALSE
The >= operator
Returns TRUE if the first string is greater or equal to the second string
else FALSE

MEMBERSHIP OPERATORS

the in operator
returns TRUE if the first operand is contained within the second operand

the not in operator
returns TRUE if the first operand is not contained within the second
operand

ESCAPE SEQUENCE OPERATOR

escape character
is used to insert a non-allowed character in a string
consists of escape operator (\) followed by a non-allowed character

\n
\b
\t
\\
\000
\xhh

STRING FORMATTING OPERATOR
% is used to format a string also format specifiers
%d decimal val
%c external character
%s sub-string
%f floating val

STRING SLICING
used to access a substring of string

SLICING WITH THE THIRD PARAMETER
also calLed step value thus val 1

step val-1
specifies the number of elements to skip when slicing the string

elininating the first parameter and the second parameter is allowed

keeping the first parameter and eliminating the second parameter or vice versa is allowed

NEGATIVE THIRD PARAMETER
also called step value. Defaults to 1
'''



'''

print (0b0101)
print (173e5)

name = 'sam'
if True:
    print('Hello Sam')
else:
    print("Hello Dude")

'''
'''
VARIABLES IN PYTHON
name attached to a value which can be changed later
Thus variables are dynamic
no need of declaration unlike other programming languages
no need of semicolon
no need to specify the variable

VARIABLE NAMING CONVENTIONS rules
using letter, numbers and underscores.
cannot start with a number
to space use underscore
should be short and descriptive
are case sensitive

FOR MULTI-WORD 
camelCase
PascalCase
snake_case

CHAINED ASSIGNMENT OF VARIABLES
X = Y =  Q = 2

VARIABLES IN C
a name of a memory location / container where you can store value

thus
[data_type] [variable_name] = value;
int x = 10;
int y = x;


'''




