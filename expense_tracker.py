#讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8')as f:
	for line in f:
		if '商品, 價格' in line:
			continue
		name, price = line.strip().split(',')
		products.append([name, price])
print(products)

#輸入商品
while True:
	name = input('請輸入商品名稱 :')
	if name == 'q' or name =='Q':
		print('程式結束')
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	products.append([name, price])

#印出所有商品價格
for p in products:
	print(p[0],'的價格是', p[1])

#寫入商品
with open('products.csv', 'w', encoding= 'utf-8')as f:
	f.write('商品, 價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')

