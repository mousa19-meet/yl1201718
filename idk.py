import random
class animal(object):
	def __init__ (self,sound,name,age,fav_color):
	    self.sound = sound
	    self.name = name
	    self.age = age
	    self.fav_color = fav_color
	def eat(self,food):
		print("yummy!!" +self.name + " is eating "+ food)
	def description(self):
		print(self.name + " is " + str(self.age) + " years old and loves the color "+ self.fav_color)
	def make_sound(self,number):
		print((self.sound +" ")*number)

#dog = animal("woof","max",10,"green")
#dog.eat("chocolate")
#dog.description()
#dog.make_sound(5)

class person(object):
	def __init__ (self,name,age,city,gender):
		self.name = name
		self.age = age
		self.city = city
		self.gender = gender
	def fav_food(self,food):
		self.food = food
		print(self.name + " is eating "+ food)
	def play(self,sport):
		self.sport = sport
		print(self.name + " loves playing "+ sport)
#p = person("shaq",100,"NY", 'female')
#p.fav_food("pancakes")
#p.play("football")

class song(object):
	def __init__ (self,lyrics):
		self.lyrics = lyrics
	def sing_me (self):
		a = 0
		for i in range (len(self.lyrics)):
			print(self.lyrics[a])
			a +=1
flower_song = song(["Roses are red,",
	         "Violets are blue,",
	         "I wrote this poem for you."])

another_song =song(["It's everyday bro,","with that disney channel flow", "5 mil"])
another_song1 = song(["lyrics1","lyrics2","lyrics3"])

song_list = [another_song,flower_song,another_song1]
random_song = random.randint(0,len(song_list)-1)
print(random_song)
song_list[random_song].sing_me()
