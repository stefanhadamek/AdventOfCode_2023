#A

f = open("AdventOfCode_2023/04/input.txt","r")
lines = f.readlines()
total_score =0
for l in lines:
    
    l=l[:-1]
    
    
    ids,cards = l.split(":")
    winning_cards,our_cards = cards.split("|")
    #assert False
    winning_cards = winning_cards.split(" ")
    winning_cards =[item for item in winning_cards if item != '']
    our_cards = our_cards.split(" ")
    our_cards =[item for item in our_cards if item != '']
    print(winning_cards,our_cards)
    matches = 0 
    for card in our_cards:
        if card in winning_cards:
            matches+=1
    if matches >0:
        total_score += 2**(matches-1)

print(total_score)  


number_copies = []
for l in lines:
    l = l[:-1]
    ids,cards = l.split(":")
    winning_cards,our_cards = cards.split("|")
    #assert False
    winning_cards = winning_cards.split(" ")
    winning_cards =[item for item in winning_cards if item != '']
    our_cards = our_cards.split(" ")
    our_cards =[item for item in our_cards if item != '']
    print(winning_cards,our_cards)
    matches = 0 
    for card in our_cards:
        if card in winning_cards:
            matches+=1

number_of_cards = [1]*220

for i,l in enumerate(lines):
    l=l[:-1]
    ids,cards = l.split(":")
    winning_cards,our_cards = cards.split("|")
    #assert False
    winning_cards = winning_cards.split(" ")
    winning_cards =[item for item in winning_cards if item != '']
    our_cards = our_cards.split(" ")
    our_cards =[item for item in our_cards if item != '']
    print(winning_cards,our_cards)
    matches = 0 
    for card in our_cards:
        if card in winning_cards:
            matches+=1
    
    for j in range(matches):
        number_of_cards[i+j+1] += number_of_cards[i]

print(sum(number_of_cards))