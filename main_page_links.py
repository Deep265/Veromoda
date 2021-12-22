dress = [
'all-dresses-vm',
'shirt-vm',
'bodycon-vm',
'fit-flare-vm',
'jumpsuit-vm',
'maxi-vm',
'midi-vm',
'mini-vm',
'playsuit-vm',
'sheath-vm',
'shift-vm',
'skater-vm',
]

t_shirts = [
't-shirts-vm',
'tops-vm']
links = []
for i in dress:
    links.append('https://www.veromoda.in/dresses-jumpsuits-vm/dresses-jumpsuits-'+i)

t_shirts_links = []
for i in t_shirts:
    t_shirts_links.append('https://www.veromoda.in/tops-t-shirts-vm/tops-t-shirts-'+i)

winter_wear = [
  'outerwear-vm-jacket',
   'outerwear-vm-sweatshirt',
   'blazers-vm',
    'cardigans-pullovers-vm',
   'coats-vm',
   'shrugs-vm',
   'outerwear-sweater-61525'
]
winter_wear_links = []
for i in winter_wear:
    winter_wear_links.append('https://www.veromoda.in/fashion-vm/fashion-outerwear-vm/fashion-'+i)
winter_wear_links += ['https://www.veromoda.in/fashion-vm/fashion-outerwear-vm/fashion-outerwear-sweater-61525']


jeans = [
  'anti-fit-vm',
  'boot-cut-vm',
  'joggers-vm',
   'regular-vm',
  'skinny-vm',
   'slim-vm'
]

jeans_links = []
for i in jeans:
    jeans_links.append('https://www.veromoda.in/fashion-vm/fashion-jeans-vm/fashion-'+i)
jeans_links += ['https://www.veromoda.in/fashion-vm/fashion-jeans-vm/fashion-vm-fashion-jeans-jegging-61955']

bottom_wear = [
  'culottes-vm',
   'leggings-vm',
   'pants-vm',
   'shorts-vm',
   'trousers-vm',
]

bottom_wear_links = []
for i in bottom_wear:
    bottom_wear_links.append('https://www.veromoda.in/fashion-vm/fashion-'+i)


shirts = ['https://www.veromoda.in/fashion-vm/fashion-shirts-vm']

accessories = [
  'vm-belt',
  'fashion-bags-belts-wallets-vm',
   'fashion-caps-vm',
   'fashion-jewellery-vm',
   'veromoda-58487',
    'fashion-scarves-vm',
   'fashion-sunglasses-vm'
]

accessories_links = []
for i in accessories:
    accessories_links.append('https://www.veromoda.in/fashion-vm/fashion-accessories-vm/'+i)

footwear = [
  'fashion-heels-vm',
  'fashion-sandals-vm',
  'fashion-slip-ons-vm',
  'fashion-wedges-vm',
]

footwear_links = []
for i in footwear:
    footwear_links.append('https://www.veromoda.in/fashion-vm/fashion-footwear-vm/'+i)

athe = ['https://www.veromoda.in/new-arrivals-vm/new-arrivals-athleisure-vm/new-arrivals-sweatpants-vm','https://www.veromoda.in/fashion-vm/fashion-athleisure-vm/fashion-sweatshirts-vm']

jackets = [
 'fashion-biker-jackets-vm',
 'fashion-bomber-jackets-cm',
  'fashion-casual-jackets-vm',
  'fashion-denim-jackets-vm',
  'fashion-leather-jackets-vm',
]

jackets_links = []
for i in jackets:
    jackets_links.append('https://www.veromoda.in/fashion-vm/fashion-jackets-vm/'+i)

ease = ['https://www.veromoda.in/vm-ease/vm-ease-loungewear/vm-ease-bomber-jackets',
'https://www.veromoda.in/vm-ease/vm-ease-loungewear/vm-ease-lounge-pants',
'https://www.veromoda.in/vm-ease/vm-ease-loungewear/vm-ease-lounge-tops-and-t-shirts',
'https://www.veromoda.in/vm-ease/vm-ease-sleepwear-/vm-ease-night-dresses',
'https://www.veromoda.in/vm-ease/vm-ease-sleepwear-/vm-ease-night-suits'
        ]

links = t_shirts_links+winter_wear_links+jackets_links+athe+footwear_links+ease+accessories_links+shirts+bottom_wear_links+jackets_links
print(len(links))