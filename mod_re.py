import re

phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('Cell: (415) 555-4242 Work: (212) 555-0000')
print(mo.groups())
print(mo.groups()[0])
print(mo.group(1))
print(mo.group())
print(phoneNumRegex.findall('Cell: (415) 555-4242 Work: (212) 555-0000'))

print()

# named groups
nameRegex = re.compile(r'(?P<first>\d+) (?P<second>[a-z]+)')
mo = nameRegex.search('33 fefe 555 awaaa 222 12 piyo')
print(mo)
print(mo.groups())
print(mo.groupdict())

print()

heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tina Fey.')
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman.')
print(mo2.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile lost a wheel Batbat')
print(mo.group())
print(mo.group(1))

print()

no_match = re.compile(r"hoge")
mo = no_match.search("fuga")
print(mo)

print()

# difference between match() and search()
print(re.match(r'Hello', 'Hello World!'))
print(re.search(r'Hello', 'Hello World!'))
print(re.match(r'World', 'Hello World!'))
print(re.search(r'World', 'Hello World!'))

print()

# sub()
namesRegex = re.compile(r'Agent (\w+)')
print(namesRegex.sub(r'\1CENSORED', 'Agent Alice gave the secret documents to Agent Bob.'))

print()

# split()
middle = re.compile('[A-Z]\.')
print(middle.split('Hoge X. Fefe'))

# flags
# re.I, re.IGNORECASE
# re.S, re.DOTALL
# re.M, re.MULTILINE
regex1 = re.compile('RoboCop', re.I | re.S | re.M)

# re.X, re.VERBOSE
phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?            # area code
        (\s|-|\.)?                    # separator
        \d{3}                         # first 3 digits
        (\s|-|\.)                     # separator
        \d{4}                         # last 4 digits
        (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)
