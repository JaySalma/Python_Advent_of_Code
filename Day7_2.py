rules_input=open("Day7_input.txt","r").readlines()
my_bag=["shiny gold",1]
number_bags=0

def rules_for_bag(bag):
    #list of rules concerning this bag
    applicable_rules=[]
    bag_color=bag[0]
    for rule in rules_input:
        if rule.startswith(bag_color):
            applicable_rules.append(rule)
    return applicable_rules

def find_colorandamount(phrase):
    #remove unnessasary characters
            phrase=phrase.removeprefix(" ")
            phrase=phrase.removesuffix(".\n")
            
            try:
                amount=int(phrase[0])
            except ValueError:
                amount=0
            color=phrase[2:phrase.find(" bag")]
            return(color,amount)

def get_inner_bags(rule):
    inner_bags=[]
    inner_bags_string=rule.split(" contain ")[1]
    inner_bags_raw=inner_bags_string.split(",")
    
    for items in inner_bags_raw:
        if "bag" in items:
            if not items.startswith("no other"):
                new_bag=find_colorandamount(items)
                inner_bags.append(new_bag)
    return inner_bags

#higher_instance gives multiplicator for the bags of the lower levels
def check_bag(bag,higher_instance): #bag=[color,amount]
    #set number of bags 0 for highest instance
    if bag!=my_bag:
        number_bags=higher_instance*bag[1]
    else:
        number_bags=0
    
    rules=rules_for_bag(bag) #get rules concerning the current bag
    for rule in rules:
        inner_bags=get_inner_bags(rule) #bags mentioned in the rules
        for items in inner_bags:
            #sum up the backs, by recalling this function we get to the lowest instance
            number_bags+=check_bag(items,higher_instance*bag[1])
        next
    next
    
    return number_bags

print(check_bag(my_bag,1))

