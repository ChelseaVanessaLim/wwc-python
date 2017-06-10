""" Aling Nena's Reward System Challenge
Author:
Description: This summer, Aling Nena’s Sari-sari store wants to implement a
reward system where customers can redeem a reward by texting the following:
<Reward number 1-9> <Customer’s name> <Gender f or m>

>> Please enter text: 1 nicole i. tibay f

The system will then reply the following:
Hi <Customer’s name first letters upper case>! You have successfully redeem
reward #<reward number> - <reward>! Thank you for choosing Aling Nena’s
Sari-sari store.

>> Hi Nicole I. Tibay! You have successfully redeem reward #1 - Coke sakto!
Thank you for choosing Aling Nena’s Sari-sari store.
"""

# You can access this by: rewards[<index>]
# Just like strings the index starts with 0
rewards = [
     "Coke sakto",  # index 0
     "Boy Bawang",  # index 1
     "15pcs. Yucky candy",  # index 2
     "15pcs. Pintura candy",  # index 3
     "15PHP load",  # index 4
     "3 pcs. Dove conditioner",  # index 5
     "Cottonbuds",  # index 6
     "One sheet of Biogesic",  # index 7
     "100mL Pepper/Pintura",  # index 8
]

text = input("Please enter text:")
elements = text.split()
customer = elements[1:len(elements)-1]
name=[]
for i in customer:
    a=i.title()
    name.append(a)
final_name = ' '.join(name)
reward_index = int(elements[0])-1
reward = rewards[reward_index]

print('Hi {}! You have successfully redeem reward #{} - {}! Thank you for choosing Aling Nena\'s sari-sari store.'.format(final_name, reward_index, reward))
