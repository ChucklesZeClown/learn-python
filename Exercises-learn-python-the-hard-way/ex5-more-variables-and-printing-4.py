name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
inch_to_centimeter_conversion_rate = 2.54
pound_to_kg_conversion_rate = 0.453592
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Lets talk about %s." % name
print "He's %d inches tall." % height
print "Which is %2f cm." % (height * inch_to_centimeter_conversion_rate)
print "He's %d pounds heavy." % weight
print "Which is %2f kg." % (weight * pound_to_kg_conversion_rate)
print "Which is also %+2.2f kg." % (weight * pound_to_kg_conversion_rate)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %r." %(
    age, height, weight, age + height + weight
)