#Debugging exercise # 1
product = {
    "name": 'small gumball', 
    "price": 0.49
}

tax_rate = 0.045

total = round(product["price"] + product["price"] * tax_rate, 2)

print(f"A {product["name"]} costs ${total:.2f}")
