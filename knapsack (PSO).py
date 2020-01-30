#Define Item class
class Item:
    #each with a weight and a value
  def __init__(self, weight, value):
    self.weight = weight
    self.value = value
 	
def Bounded_Knapsack(items, capacity):
	knapsack = [] #knapsack container
	knapsack_weight = [] #array save all item value's kept in knapsack
	knapsack_value = [] #array save all item weight's kept in knapsack
	#initialization part,put into knapsack items ,constrained by knapsack weight
	while len(items) > 0:
		item = items.pop(0) 
		if item.weight +sum(knapsack_weight )<= capacity:
			#if adding new item,doesn't make total weight greater than the knapsack weight
             #then add it and update total current weight,value
			knapsack.append(item)#item complete object
			knapsack_weight.append( knapsack[knapsack.index(item)].weight)
			knapsack_value.append( knapsack[knapsack.index(item)].value)
		else:
			#fitness evaluations
			#if the other item has value greater than item's value in the knapsack and it's weight
			#less than the weight of the item's weight in the knapsack then remove old item from 
			#knapsack and append the new item with the new value and weight 
		 for t in items:
				for kt in knapsack:
					if(t.value>kt.value and t.weight<=min(knapsack_weight)and t.weight<kt.weight):
								knapsack_value.remove(kt.value)
								knapsack_weight.remove(kt.weight)
								knapsack.remove(kt)
								knapsack.append(t)
								knapsack_value.append(t.value)
								knapsack_weight.append(t.weight)
								items.pop(0)
								
   			                
							   
					else:
								continue

	
	return knapsack,sum(knapsack_weight),sum(knapsack_value)
   #experiment 1
items = [
  Item(5,800)	
,Item(5,700)
,Item(60,100)
,Item(2,300)
,Item(10,400)
,Item(100,200)
,Item(20,500)    
,Item(15,400)
,Item(5,620)
]
   #experiment 2
'''
items=[
Item(3,50)
,Item(5,10)
,Item(4,40)
,Item(6,30)
,
]'''
   #experiment 3
'''
items=[
Item(20,30)
,Item(10,55)
,Item(35,20)
,Item(45,30)
,Item(30,35)
,Item(20,15)
,Item(15,15)

]
'''
capacity=50
knapsack,weight,value=Bounded_Knapsack(items,capacity)
print("Bounded knapsack")
for item in knapsack:
	print("weight:",item.weight,"value:",item.value)
print("Total Allocated Weight:",weight,"\n","Max Value",value)	



#--------------------------------------------------------------------------------------
#the same concept put we can put unlimited number of the same item in the knapsack

def Unbounded_Knapsack(items, capacity):
	knapsack = []
	knapsack_weight = []
	knapsack_value = []
	while len(items) > 0:
		item = items.pop()
		if item.weight +sum(knapsack_weight )<= capacity:
			knapsack.append(item)
			knapsack_weight.append( knapsack[knapsack.index(item)].weight)
			knapsack_value.append( knapsack[knapsack.index(item)].value)
		else:
		 for t in items:
				for kt in knapsack:
					if((t.value>kt.value and t.weight<kt.weight ) or sum(knapsack_weight)<capacity):
								knapsack_value.remove(kt.value)
								knapsack_weight.remove(kt.weight)
								knapsack.remove(kt)
								knapsack.append(t)
								knapsack_value.append(t.value)
								knapsack_weight.append(t.weight)
								
								
   			                
							   
					else:
								continue

	
	return knapsack,sum(knapsack_weight),sum(knapsack_value)
	#experiment 1
items = [
  Item(10,800)	
,Item(5,700)
,Item(60,100)
,Item(2,300)
,Item(5,620)
,Item(100,200)
,Item(20,500)    
,Item(15,400)
,Item(10,400)
]
   #experiment 2
'''
items=[
Item(3,50)
,Item(5,10)
,Item(4,40)
,Item(6,30)
,
]'''
   #experiment 3
'''
items=[
Item(20,30)
,Item(10,55)
,Item(35,20)
,Item(45,30)
,Item(30,35)
,Item(20,15)
,Item(15,15)

]
'''
capacity=50

knapsack,i,j=Unbounded_Knapsack(items,capacity)
print("Unbounded knapsack")
for item in knapsack:
	print("weight:",item.weight,"value:",item.value)
print("Total Allocated Weight:",i,"\n","Max Value",j)	


