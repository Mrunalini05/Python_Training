'''ip:Placements
op:plAcEmEnts
ip:School
op:schOOl'''


a="School"
b=' '
for i in a:
    if i in 'AEIOUaeiou':
        b+=i.upper()
    else:
        b+=i.lower()
print(b)