class person(object):
    def __init__(self, name, sex, HP, backpack, health):
        self.name = name
        self.sex = sex
        self.HP = HP
        self.backpack = backpack
        self.health = health
    def attack__zombie(self, attackway):
        while self.HP > 0 and monster.HP > 0:
            if attackway == "1":
                self.HP -= monster.attack
                monster.HP -= 35
            elif attackway == "2":
                self.HP -= monster.attack
                monster.HP -= 50
            elif attackway == "3":
                self.HP -= monster.attack
                monster.HP -= 20
        if attackway == "1":
            self.backpack.remove('knife')
        elif attackway == "2":
            self.backpack.remove('gun')
        if self.HP <= 0:
            print("You are dead!")
            daily.day = 15
        if monster.HP <= 0:
            print("%s is killed!" % monster.name)
            if monster.name == 'Doom!':
                if len(self.backpack) == 3:
                    print("Sorry!You backpack is full and you can't get anything!")
                else:
                    self.backpack.append('gun')
                self.HP += 50
                self.health += 10
                print("Your HP increase 50,your health increase 10")
                monster.HP = 100
            if monster.name == 'Tank!':
                if len(zhujue.backpack) == 3:
                    print("Sorry!You backpack is full and you can't get anything!")
                else:
                    self.backpack.append('knife')
                self.HP += 40
                self.health += 5
                print("Your HP increase 40,your health increase 5")
                monster.HP = 55
            if monster.name == 'zombie':
                self.HP += 30
                monster.HP = 35
                print("Your HP increase 30")
    def detail(self):
        temp = "name:%s  sex:%s HP:%s backpack:%s health:%s" % (
        self.name,self.sex,self.HP,self.backpack,self.health)
        print(temp)
    def search(self):
        goods = ['water', 'bread', 'gun', 'knife', 'pill']
        import random
        wupin = random.choice(goods)
        if len(self.backpack) == 3:
            print("Backpack is full!")
        else:
            self.backpack.append(wupin)
    def rest(self):
        self.HP += 20
    def study_map(self):
        import random
        out = random.randint(0, 15)
        if out == 7:
            print("You find a secret way out!You survive!")
            daily.day = 15
class monsters(person):
    def __init__(self, name, sex, HP, backpack, health, attack):
        person.__init__(self, name, sex, HP, backpack, health,)
        self.attack = attack
    def detail1(self):
        temp = "name:%s  sex:%s HP:%s backpack:%s health:%s" % (
        self.name, self.sex, self.HP, self.backpack, self.health, self.attack)
        print(temp)
class routine(object):
    def __init__(self, day=1):
        self.day = day
    def tomorrow(self):
        self.day += 1
        zhujue.health -= 5
        if zhujue.health < 0:
            zhujue.HP -= 20
            if zhujue.HP <= 0:
                print("You are dead!")
                self.day = 15
        elif self.day == 15:
            print("You survive!")
    def plus_health(self, choice):
        if choice == "1" and 'water' in zhujue.backpack:
            zhujue.health += 5
            zhujue.backpack.remove('water')
        elif choice == "2" and 'bread' in zhujue.backpack:
            zhujue.health += 10
            zhujue.backpack.remove('bread')
        elif choice == "3" and 'pill' in zhujue.backpack:
            zhujue.HP += 35
            zhujue.backpack.remove('pill')
        elif choice != "4":
            print("Such thing don't exist in your backpack!")
print("You are now in ZJU,the school is dangerous and you are alone.Try to survive two weeks!")
print("Everyday you can only do on thing:1.search ZJU,and you may find something useful")
print("2.sleep,you can recover 20HP. 3.study map,you may find a secret way out or maybe")
print("you will find nothing!You may face zombies everyday,and search is more likely to meet zombies!")
print("When you facing a zombie,you can choose to kill it and get some useful things or you can run!")
print("But you can use what in your backpack before doing the thing!")
name = input("Enter you name!")
sex = input("Are you male or female?")
zhujue = person(name, sex, 100, ['water', 'bread', 'knife'], 10)
daily = routine()
zombies = [monsters("Doom!", "unknown", 100, None, None, 40),
           monsters("zombie", "unknown", 35, None, None, 20),
           monsters("Tank!", "unknown", 55, None, None, 30)]
while daily.day != 15:
    flag = 0
    print("day:%s" % daily.day)
    zhujue.detail()
    print("Do you want to use what in your backpack?")
    print("1 for water,2 for bread,3 for pill.4 for NO USE!")
    use = input()
    if use != "3":
        daily.plus_health(use)
    act = input("Enter 1 for search ZJU,2 for rest,3 for study map")
    if act == "1":
        zhujue.search()
    elif act == "2":
        zhujue.rest()
    elif act == "3":
        zhujue.study_map()
    import random
    op = random.randint(1, 10)
    choose = random.randint(0, 2)
    monster = zombies[choose]
    if act == "1":
        if op >= 3:
            print("You meet a zombie!")
            monster.detail()
            flag = 1
    elif op >= 8:
        print("You meet a zombie!")
        monster.detail1()
        flag = 1
    if flag == 1:
        choice = input("Run or fight? 1 for run,2 for fight!")
        if choice == "1":
            if op >= 5:
                print("You run away!")
            else:
                print("You are caught by the zombie!Get ready to fight!")
        if choice == "2" or (choice == "1" and op < 5):
            attackway = input("Choose weapon to fight:1 for knife,2 for gun,3 for no weapon!")
            zhujue.attack__zombie(attackway)
    if daily.day == 15:
        break
    print("Today is over,please enter anything to continue!")
    dayover = input()
    daily.tomorrow()
print("***************************滑稽分割线****************************************")
print("感谢你对本游戏的体验，因为水平问题，游戏肯定有不少BUG，请多包含。（我也不会去优化的！）")
print("                                                                Made By Jack__Zhou")
