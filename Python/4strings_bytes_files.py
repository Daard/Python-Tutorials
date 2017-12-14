print('foobar' == "foobar")
#True
print('"Where are you?"')
#"Where are you?"
print("I'm here!")
#I'm here!
print("""foo
bar""")
# foo
# bar
print("foo""bar")
#foobar

# \'
# \"
# \t
# \n
# \xhh

print("\tell me")
#    ell me

#raw strings
print(r"\tell me")
# \tell me

s = "I am string"
print(list(s))
# ['I', ' ', 'a', 'm', ' ', 's', 't', 'r', 'i', 'n', 'g']

print(s[0], type(s[0]))
# I <class 'str'>
print(list(s[0]))
# ['I']

#register modifications
print('foor bar'.capitalize())
# Foor bar
print('foor bar'.title())
# Foor Bar
print('foor bar'.upper())
# FOOR BAR
print('OOR BAR'.lower())
# oor bar
print("foo bar".title().swapcase())
# fOO bAR

#tabing

print('foo bar'.ljust(16, "±"))
# foo bar±±±±±±±±±
print('foo bar'.rjust(16, "±"))
# ±±±±±±±±±foo bar
print('foo bar'.center(16, "±"))
# ±±±±foo bar±±±±±

#Stripping

print(']>>foo bar<<['.lstrip(']>'))
# foo bar<<[
print(']>>foo bar<<['.rstrip('<['))
# ]>>foo bar
print(']>>foo bar<<['.strip('<[]>'))
#foo bar

print('\t   foo bar \r\n'.strip())
# foo bar

#Splitting
print('foo,bar'.split(','))
# ['foo', 'bar']
print('foo,,,bar'.split(','))
# ['foo', '', '', 'bar']
print('\t foo bar \r\n'.split())
# ['foo', 'bar']
print('foo, bar, baz'.partition(','))
# ('foo', ',', ' bar, baz')
print('foo, bar, baz'.rpartition(','))
# ('foo, bar', ',', ' baz')

#Joining
print(", ".join(['foo', 'bar', 'baz']))
# foo, bar, baz
print(', '.join(filter(None, ['','foo'])))
# foo
print(', '.join('bar'))
# b, a, r

#Containing
print('foo' in 'foobar')
# True
print('foobar'.startswith('foo'))
#True
print('foobar'.endswith('bar'))
#True

#Replacing
print('abracadadbra'.replace('ra', '***'))
# ab***cadadb***
print('abracadadbra'.replace('ra', '***', 1))
# ab***cadadbra
tr_map = {ord('a'):'*', ord('b'):'+'}
print('abracadadbra'.translate(tr_map))
# *+r*c*d*d+r*

#Predicates
print('100500'.isdigit())
#True
print('foo100500'.isalnum())
#True
print('foobar'.isalpha())
#True
print('foobar'.islower())
#True
print('FOOBAR'.isupper())
#True
print('Foo Bar'.istitle())
#True

#Formatting
print("{}, {}, how are you?".format('Hello', 'Sally'))
# Hello, Sally, how are you?
print('Today is November, {}th'.format(5))
# Today is November, 5th

#object2str
print(str("I am string"))
# I am string
print('{:-^16}'.format('foo bar'))
# ----foo bar-----
print('int: {0:d}, hex: {0:x}'.format(42))
# int: 42, hex: 2a
print('oct: {0:o}, bin:{0:b}'.format(42))
# oct: 52, bin:101010

#Positioning
print('{0}, {1}, {0}'.format('hello', 'kitty'))
# hello, kitty, hello
print('{0}, {who}, {0}'.format('hello', who='kitty'))
# hello, kitty, hello

#BYTES
#..........

#FILES




