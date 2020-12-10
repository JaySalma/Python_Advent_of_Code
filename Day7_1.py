rules_input=open("Day7_input.txt","r").readlines()
my_bag="shiny gold"
containing_rules=[]

all_found=False

def rules_check(rules,bags):
    search_in=[]
    for lines in rules:
        for bag in bags:
            if bag in lines and not lines.startswith(bag):
                search_in.append(lines)
        next
    next
    return(search_in)


def separate_containing_bag(rule):
    bag_containing_my_bag=rule.split(' bags contain ')[0]
    return(bag_containing_my_bag)

search_in=rules_check(rules_input,[my_bag])
appropriate_bags=[]
for rule in search_in:
    new_bag=separate_containing_bag(rule)
    appropriate_bags.append(new_bag)
next

while not all_found:
    number_bugs_start=len(appropriate_bags)
    search_in=rules_check(rules_input,appropriate_bags)
    for rules in search_in:
        new_bag=separate_containing_bag(rules)
        if not new_bag in appropriate_bags:
            appropriate_bags.append(new_bag)
    next
    if not number_bugs_start<len(appropriate_bags):
        all_found=True

print("I could use %d different bags:\n" %len(appropriate_bags))