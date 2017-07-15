import pythonwhois , json , sys

url = sys.argv[1]

a= open(url,'r')

a = a.readlines()

print(a)

result = []

for i in range(0, len(a)):
    a[i] = a[i].replace("\n","")
    data = pythonwhois.get_whois(a[i])
    result.append(data)

b = open('result.txt','w')

b.write(result)
