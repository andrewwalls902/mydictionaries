# Below is a dictionary that contains information about real estate space for
# a doctor's office. Using the dictionary, create a csv file that has details
# for each space represented as rows. Name your file 'retail_space.csv.


'''
Your final output should look like:

room-number,use,sq-ft,price
100,reception,50,75
101,waiting,250,75
102,examination,125,150
103,examination,125,150
104,office,150,100

'''




datastore = { "medical":[
      { "room-number": 100,
        "use": "reception",
        "sq-ft": 50,
        "price": 75
      },
      { "room-number": 101,
        "use": "waiting",
        "sq-ft": 250,
        "price": 75
      },
      { "room-number": 102,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 103,
        "use": "examination",
        "sq-ft": 125,
        "price": 150
      },
      { "room-number": 104,
        "use": "office",
        "sq-ft": 150,
        "price": 100
      }

      ]
}
import csv
outfile = open('retail_space.csv','w')
outfile.write('room-number,use,sq-ft,price\n')

for l in datastore['medical']:
  roomno = l['room-number']
  use = l['use']
  sqft = l['sq-ft']
  price = l['price']

  outfile.write(f"{roomno},{use},{sqft},{price}\n")

outfile.close()


#import csv
#datastore = {
    
    #"medical":[
        #{"room-number": 100,"use": "reception", "sq-ft": 50, "price": 75},
        #{"room-number": 101,"use": "waiting", "sq-ft": 250, "price": 75},
       # {"room-number": 102,"use": "examination", "sq-ft": 125, "price": 150},
        #{"room-number": 103,"use": "examination", "sq-ft": 125,"price": 150},
        #{"room-number": 104,"use": "examination", "sq-ft": 50, "price": 100},
        ##]
        #}

#file_path = 'retail_space.csv'

#with open (file_path, 'w') as file:
    #file.write("room-number,use,sp-ft,price\n")
  


    #for room in datastore["medical"]:
       # row = f'{room["room-number"]},{room["use"]},{room["sq-ft"]},{room["price"]}\n'
       # file.write(row)

