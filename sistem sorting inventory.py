import pandas as pd

inventory = []
num_items = int(input("Greetings, brave adventurer! How many treasures have you unearthed today?: "))

for _ in range(num_items):
    name = input("What is this magnificent item's name?: ")
    strength = int(input("How powerful is this item? (Give me a number!): "))
    rarity = int(input("Rate its rarity for me! (1=Common, 2=Uncommon, 3=Rare, 4=Epic, 5=Legendary): "))
    weight = float(input("How much does this item weigh? (Enter a number, please!): "))
    value = int(input("What price would this item fetch? (Numbers, my friend!): "))
    inventory.append({"name": name, "strength": strength, "rarity": rarity, "weight": weight, "value": value})

df_inventory = pd.DataFrame(inventory)

rarity_labels = {1: "Common", 2: "Uncommon", 3: "Rare", 4: "Epic", 5: "Legendary"}
df_inventory["rarity"] = df_inventory["rarity"].map(rarity_labels)

criteria = input("How would you like it sorted? (name/strength/rarity/weight/value): ").lower()
order = input("Ascending or Descending order? (type 'ascending' or 'descending') ").lower()
ascending = True if order == "ascending" else False

def bubble_sort(df, key, ascending=True):
    data = df.to_dict('records')  
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and data[j][key] > data[j + 1][key]) or (not ascending and data[j][key] < data[j + 1][key]):
                data[j], data[j + 1] = data[j + 1], data[j]
    return pd.DataFrame(data)


if criteria in df_inventory.columns:
    df_inventory = bubble_sort(df_inventory, criteria, ascending)
else:
    print("Invalid sorting criteria! Choose from 'name', 'strength', 'rarity', 'weight', or 'value'.")

df_inventory.index = range(1, len(df_inventory) + 1)

print("\nYour Inventory:")
print(df_inventory)
