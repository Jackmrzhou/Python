# 有很多能大量减少代码量的地方为什么我不优化？
# 因为我写了几处才意识到-。-!!  就懒得改了
import random
class livingthing(object):
    def __init__(self, name, HP, MP, backpack, defend, attack):
        self.name = name
        self.HP = HP
        self.MP = MP
        self.backpack = backpack
        self.defend = defend
        self.attack = attack
        self.dead = False
        self.weapon_place = []
        self.judge_weapon = {'head': 0, 'hand': 0, 'sword': 0, 'boots': 0, 'armor': 0}

    def hero_detail(self):
        print('Name:%s HP:%s MP:%s backpack:%s defend:%s attack:%s' %
              (Hero.name, Hero.HP, Hero.MP, Hero.backpack, Hero.defend, Hero.attack))

    def judge_HP(self):
        if self.HP <= 0:
            self.dead = True
            if 'reborn_pill' in self.backpack:
                print('You use a reborn-pill!')
                Hero.dead = False
            else:
                print('%s is dead!' % self.name)

    def use_stuff(self, choose_stuff):
        the_stuff = self.backpack[choose_stuff]
        if the_stuff == 'HP_small_pill':
            self.HP += 25
        elif the_stuff == 'HP_large_pill':
            self.HP += 50
        elif the_stuff == 'MP_small_pill':
            self.MP += 25
        elif the_stuff == 'MP_large_pill':
            self.MP += 50
        Hero.backpack.remove(the_stuff)

    def fall_into_trap(self):
        self.HP -= 30
        self.judge_HP()

    def recover(self):
        self.HP += 30
        self.MP += 30
        print('Your HP and MP increase 30!')

    def equip_weapon(self, weapon):
        if weapon in self.weapon_place:
            pass
        else:
            if weapon == 'old_sword' and not ('normal_sword' in self.weapon_place):
                self.attack += 20
                self.judge_weapon['sword'] = 1
            elif weapon == 'old_helmet' and not ('normal_helmet' in self.weapon_place):
                self.defend += 5
                self.judge_weapon['head'] = 1
            elif weapon == 'old_armor' and not ('normal_armor' in self.weapon_place):
                self.defend += 10
                self.judge_weapon['armor'] = 1
            elif weapon == 'old_boots' and not ('normal_boots' in self.weapon_place):
                self.defend += 5
                self.judge_weapon['boots'] = 1
            elif weapon == 'old_handguard' and not ('normal_handguard' in self.weapon_place):
                self.defend += 5
                self.judge_weapon['hand'] = 1
            elif weapon == 'normal_sword':
                if 'old_sword' in self.weapon_place:
                    self.weapon_place.remove('old_sword')
                    self.attack += 10
                else:
                    self.attack += 30
                    self.judge_weapon['sword'] = 1
            elif weapon == 'normal_helmet':
                if 'old_helmet' in self.weapon_place:
                    self.weapon_place.remove('old_helmet')
                    self.defend += 5
                else:
                    self.defend += 10
                    self.judge_weapon['head'] = 1
            elif weapon == 'normal_armor':
                if 'old_armor' in self.weapon_place:
                    self.weapon_place.remove('old_armor')
                    self.defend += 5
                else:
                    self.defend += 15
                    self.judge_weapon['armor'] = 1
            elif weapon == 'normal_boots':
                if 'old_boots' in self.weapon_place:
                    self.weapon_place.remove('old_boots')
                    self.defend += 5
                else:
                    self.defend += 10
                    self.judge_weapon['boots'] = 1
            elif weapon == 'normal_handguard':
                if 'old_handguard' in self.weapon_place:
                    self.weapon_place.remove('old_handguard')
                    self.defend += 5
                else:
                    self.defend += 10
                    self.judge_weapon['hand'] = 1
            self.weapon_place.append(weapon)

    def equip_dragon_weapon(self, dragon_weapon):
        if dragon_weapon == 'firesword':
            if 'old_sword' in self.weapon_place:
                self.attack += 55
            elif 'normal_sword' in self.weapon_place:
                self.attack += 45
            else:
                self.attack += 75
        elif dragon_weapon == 'helmet_of_Poseidon':
            if 'old_helmet' in self.weapon_place:
                self.defend += 10
            elif 'noemal_helmet' in self.weapon_place:
                self.defend += 5
            else:
                self.defend += 20
        elif dragon_weapon == 'armor_of_XuanWu':
            if 'old_armor' in self.weapon_place:
                self.defend += 10
            elif 'normal_armor' in self.weapon_place:
                self.defend += 5
            else:
                self.defend += 25
        else:
            self.weapon_place.append(dragon_weapon)

    def fight(self):
        print('Jack vs %s!' % The_monster.name)
        get_monster_HP = The_monster.HP
        round_fight = 1
        while True:
            print(round_fight)
            Hero.hero_detail()
            The_monster.monsters_detail()
            print('You can use pills in your backpack,or attck the monster!')
            print('1 for use, 2 for attack the monster!')
            while True:
                choice_fight = int(input())
                if choice_fight != 1 and choice_fight != 2:
                    print('You input a wrong number! Input again!')
                else:
                    break
            if choice_fight == 1:
                round_fight += 1
                print('Use the stuff in order!')
                while True:
                    choose_stuff = int(input())
                    if choose_stuff == '*':
                        break
                    elif Hero.backpack[choose_stuff] == 'reborn_pill':
                        print('You input a wrong number or you can not use that stuff!')
                        print('Input again or input * to not use stuff!')
                    elif choose_stuff > len(Hero.backpack):
                        print('You input a wrong number or you can not use that stuff!')
                        print('Input again or input * to not use stuff!')
                    else:
                        break
                if choose_stuff != '*':
                    Hero.use_stuff(choose_stuff)
            if choice_fight == 2:
                round_fight += 1
                Hero.HP -= The_monster.attack * Hero.defend // 100
                The_monster.HP -= Hero.attack * The_monster.defend // 100
                Hero.judge_HP()
                The_monster.judge_HP()
                Hero.hero_detail()
                The_monster.monsters_detail()
                if Hero.dead == True or The_monster.dead == True:
                    The_monster.dead = False
                    The_monster.HP = get_monster_HP
                    if Hero.dead == False:
                        Hero.backpack.append(The_monster.backpack[0])
                        print('You get an ' + The_monster.backpack[1] + '!')
                        print('Do you want to equip it?')
                        print('1 for equip it, 2 for throw it away.')
                        while True:
                            choice_weapon = int(input())
                            if choice_weapon != 1 and choice_weapon != 2:
                                print('You input a wrong number! Input again!')
                            else:
                                break
                        if choice_weapon == 1:
                            Hero.equip_weapon(The_monster.backpack[1])
                    break
                # 哎 为什么不把两种战斗设成同一种方法呢？ 都怪我设计方法时偷懒-。- 现在改改太麻烦-。-
                # （还好有ctrl键，逃

    def hero_fight_dragon(self, index):
        print('Jack VS %s!' % Dragon[index].name)
        round_fight = 1
        while True:
            print(round_fight)
            Hero.hero_detail()
            Dragon[index].dragons_detail()
            print('You can use pills in your backpack,or attck the dragon!')
            print('1 for use, 2 for attack the dragon!')
            while True:
                choice_fight = int(input())
                if choice_fight != 1 and choice_fight != 2:
                    print('You input a wrong number! Input again!')
                else:
                    break
            if choice_fight == 1:
                round_fight += 1
                print('Use the stuff in order!')
                while True:
                    choose_stuff = int(input())
                    if choose_stuff == '*':
                        break
                    elif Hero.backpack[choose_stuff] == 'reborn_pill':
                        print('You input a wrong number or you can not use that stuff!')
                        print('Input again or input * to not use stuff!')
                    elif choose_stuff > len(Hero.backpack):
                        print('You input a wrong number or you can not use that stuff!')
                        print('Input again or input * to not use stuff!')
                    else:
                        break
                if choose_stuff != '*':
                    Hero.use_stuff(choose_stuff)
            if choice_fight == 2:
                round_fight += 1
                if Dragon[index].MP >= 20:
                    print('The dragon use %s!' % Dragon[index].skill)
                    Dragon[index].skill_damage()
                else:
                	Hero.HP -= Dragon[index].attack * Hero.defend // 100
                Dragon[index].HP -= Hero.attack * Dragon[index].defend // 100
                Hero.judge_HP()
                Dragon[index].judge_HP()
                Hero.hero_detail()
                Dragon[index].dragons_detail()
                if Hero.dead == True or Dragon[index].dead == True:
                    if Hero.dead == False:
                        print('You get a' + Dragon[index].backpack[0] + '!')
                        print('Do you want to equip it?')
                        print('1 for equip it, 2 for throw it away.')
                        # 把equip方法再改写一个！妈蛋我的方法真是亡羊补牢！
                        while True:
                            choice_weapon = int(input())
                            if choice_weapon != 1 and choice_weapon != 2:
                                print('You input a wrong number! Input again!')
                            else:
                                break
                        if choice_weapon == 1:
                            Hero.equip_dragon_weapon(Dragon[index].backpack[0])
                    break


class dragons(livingthing):
    def __init__(self, name, HP, MP, backpack, defend, attack, skill):
        self.skill = skill
        livingthing.__init__(self, name, HP, MP, backpack, defend, attack)

    def dragons_detail(self):
        print('Name:%s HP:%s' % (self.name, self.HP))

    def skill_damage(self):
        if len(self.skill) == 1:
            if self.skill[0] == 'dracarys':
                Hero.HP -= 35
                self.MP -= 25
            if self.skill[0] == 'water_boom':
                Hero.HP -= 30
                self.MP -= 25
            if self.skill[0] == 'earth_fall':
                Hero.HP -= 25
                self.MP -= 20
        else:
            choose_skill = random.randint(0, 2)
            if self.skill[choose_skill] == 'dracarys':
                Hero.HP -= 35
                self.MP -= 25
            if self.skill[choose_skill] == 'water_boom':
                Hero.HP -= 30
                self.MP -= 25
            if self.skill[choose_skill] == 'earth_fall':
                Hero.HP -= 25
                self.MP -= 20


class monsters(livingthing):
    def monsters_detail(self):
        print('Name:%s HP:%s' % (self.name, self.HP))


class floors(object):
    def __init__(self):
        self.floor = 1

    def floor_up(self):
        self.floor += 1

    def floor_down(self):
        if self.floor == 1:
            print('Nothing happen!')
        else:
            self.floor -= 1


Hero = livingthing('Jack', 100, 100, [], 25, 50)

Dragon = [dragons('firedragon', 150, 50, ['firesword'], 10, 75, ['dracarys']),
          dragons('waterdragon', 150, 50, ['helmet_of_Poseidon'], 25, 50, ['water_boom']),
          dragons('earthdragon', 100, 60, ['armor_of_XuanWu'], 50, 35, ['earth_fall']),
          dragons('king_of_dragon', 250, 100, ['key'], 75, 100, ['dracarys', 'water_boom', 'earth_fall'])]

old_weapon = ['old_sword', 'old_armor', 'old_helmet', 'old_handguard', 'old_boots']

monsters = [monsters('goblin', 20, 0, ['HP_small_pill', 'old_armor'], 10, 20, ),
            monsters('doom', 60, 0, ['HP_large_pill', 'old_sword'], 25, 30, ),
            monsters('tank', 30, 0, ['MP_small_pill', 'old_helmet'], 15, 20, ),
            monsters('wizard', 60, 60, ['MP_large_pill', 'old_boots'], 20, 25, )]
rooms = ['monster', 'nothing', 'box', 'trap', 'recover']

normal_weapon = ['normal_sword', 'normal_armor', 'normal_helmet', 'normal_handguard', 'normal_boots']

box = ['normal_sword', 'normal_armor', 'normal_helmet', 'normal_handguard', 'normal_boots', 'portal'
                                                                                            'HP_small_pill',
       'HP_large_pill', 'MP_small_pill', 'MP_large_pill', 'reborn_pill']
floors = floors()

while floors.floor != 20:
    print('This is floor %s' % floors.floor)
    if floors.floor <= 15:
        choose_room = random.randint(0, 4)
        room = rooms[choose_room]
    if floors.floor == 16:
        room = 'Fireroom'
    elif floors.floor == 17:
        room = 'Waterroom'
    elif floors.floor == 18:
        room = 'Earthroom'
    elif floors.floor == 19:
        room = 'Hell'
    else:
        pass
    # 进房间前询问是否使用物品
    print('Would you like use something in you backpack? 1 for YES,2 for NO!')
    while True:
        choice = int(input())
        if choice != 1 and choice != 2:
            print('You input a wrong number! Input again!')
        else:
            break
    if choice == 2:
        pass
    elif choice == 1:
        print('Use the stuff in order!')
        while True:
            choose_stuff = int(input())
            if choose_stuff == '*':
                break
            elif Hero.backpack[choose_stuff] == 'reborn_pill':
                print('You input a wrong number or you can not use that stuff!')
                print('Input again or input * to not use backpack!')
            elif choose_stuff > len(Hero.backpack):
                print('You input a wrong number or you can not use that stuff!')
                print('Input again or input * to not use backpack!')
            else:
                break
        if choose_stuff != '*':
            Hero.use_stuff(choose_stuff)
    print('There 5 rooms before you.Please choose one!')

    # 其实room根本就不是你选的（滑稽）
    #但是我还是要判断用户有没有合法输入  ！——。——！
    while True:
    	nonsense = int(input())
    	if nonsense >= 1 and nonsense <= 5:
    		break
    	else:
    		print('You input a wrong number!Input again!')

    # 进房间
    if room == 'nothing':
        print('The room is empty!')
        print('Input anything to go to next floor!')
        nonsense = input()

    if room == 'trap':
        print('You fall into a trap!And you get hurt!')
        Hero.fall_into_trap()
        if Hero.dead == True:
            break
        print('Input anything to go to next floor!')
        nonsense = input()

    if room == 'recover':
        print('The room can treat some of your wounds!')
        Hero.recover()
        print('Input anything to go to next floor!')
        nonsense = input()

    if room == 'box':
        print('There is a box in this room!')
        print('Do you like open it? 1 for YES,2 for NO!')
        while True:
            choice_box = int(input())
            if choice_box != 1 and choice_box != 2:
                print('You input a wrong number! Input again!')
            else:
                break
        if choice_box == 2:
            print('Input anything to go to next floor!')
            nonsense = input()
        elif choice_box == 1:
            choose_box = random.randint(0, 10)
            box_stuff = box[choose_box]

            if box_stuff == 'portal':
                random_up_down = random.randint(1, 2)
                if random_up_down == 1:
                    floors.floor_up()
                    floors.floor_up()
                    print('You meet a portal and you get 2 floors up!')
                else:
                    floors.floor_down()
                    print('You meet a portal and you get 2 floor down!')
                print('Input anything to go to next floor!')
       			nonsense = input()

            if box_stuff in normal_weapon:
                print('You find an %s' % box_stuff)
                print('1 for equip it, 2 for throw it away.')
                while True:
                    choice_weapon = int(input())
                    if choice_weapon != 1 and choice_weapon != 2:
                        print('You input a wrong number! Input again!')
                    else:
                        break
                if choice_weapon == 1:
                    Hero.equip_weapon(box_stuff)
               	print('Input anything to go to next floor!')
        		nonsense = input()
            
            else:
                Hero.backpack.append(box_stuff)
                print('Input anything to go to next floor!')
        		nonsense = input()

    if room == 'monster':
        choose_monster = random.randint(0, 3)
        The_monster = monsters[choose_monster]
        print('This room have a monster!Do you want to fight?')
        print('1 for fight,2 for run 1 floor down.')
        while True:
            choice_fight = int(input())
            if choice_fight != 1 and choice_fight != 2:
                print('You input a wrong number! Input again!')
            else:
                break
        if choice_fight == 2:
            if Hero.MP >= 20:
                Hero.MP -= 20
                print('You use 20MP to escape!')
                succeed_fail = random.randint(1, 10)
                if succeed_fail >= 8:
                    floors.floor_down()
                    print('You succeed in running!')
                else:
                    print('You failed in running!Get ready to fight!')
                    Hero.fight()
            else:
                print('You do not have enough MP!Get ready to fight!')
                Hero.fight()
        else:
            Hero.fight()
        if Hero.dead == True:
            break

    i = 0
    if not (room in rooms):
        print('You enter the %s' % room)
        print('%s watch the door up,kill it!' % Dragon[i].name)
        Hero.hero_fight_dragon(i)
        i += 1
    if Hero.dead == True:
        break

    floors.floor_up()

print('You use the key and open the door!')
print('You see the beauty and release her!')
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
print('感谢您对本游戏的体验！因为水平问题本游戏一定有不少BUG！（但是我不会去优化的！）')
print('                                                      Made by Jack_Zhou')

'''
Once I was seven years old my momma told me
	那年我七岁 妈妈就对我说
Go make yourself some friends or you'll be lonely
	去交些朋友 不然你会孤独寂寞
Once I was seven years old
	那年我七岁
It was a big big world but we thought we were bigger
	这个辽阔的大千世界 总以为我们也会变得更加强大
Pushing each other to the limits we were learning quicker
	将彼此逼到绝境 我们得以更快的成长
By eleven smoking herb and drinking burning liquor
	十一岁那年 我吸大麻 喝烈性酒
Never rich so we were out to make that steady figure
	生活捉襟见肘 我们离家奋斗只为有个稳定收入
Once I was eleven years old my daddy told me
	十一岁那年 爸爸对我说
Go get yourself a wife or you'll be lonely
	给自己找个妻子 否则你会空虚寂寞
Once I was eleven years old
	那年我十一岁
I always had that dream like my daddy before me
	我常梦想着有朝一日能像爸爸一样成为一个歌手
So I started writing songs I started writing stories
	所以我开始写歌 开始写不同的故事
Something about the glory just always seemed to bore me
	曾经的光辉岁月 对我来说也已厌倦
Cause only those I really love will ever really know me
	因为只有那些我真正爱的人才真的懂我
Once I was 20 years old my story got told
	二十岁那年 我的故事广为流传
Before the morning sun when life was lonely
	黎明还未照耀前 孤独的我无人相伴
Once I was 20 years old
	那年我二十岁
I only see my goals I don't believe in failure
	我一心实现梦想 从不相信失败
Cause I know the smallest voices they can make it major
	因为我知道蝼蚁也能成就不朽
I got my boys with me at least those in favor
	我找到一群志同道合的伙伴
And if we don't meet before I leave I hope I'll see you later
	如果我离开前 我们无缘碰面 就让我们后会有期
Once I was 20 years old my story got told
	二十岁那年 我的故事广为流传
I was writing about everything I saw before me
	我写下每一个亲眼所见的故事
Once I was 20 years old
	那年我二十岁
Soon we'll be 30 years old our songs have been sold
	很快我们三十而立 我们的歌也是人尽皆知
We've traveled around the world and we're still rolling
	我们游遍世界 我们不曾止步
Soon we'll be 30 years old
	很快我们就三十了
I'm still learning about life
	我依旧在领悟人生真谛
My woman brought children for me
	爱人为我生了几个孩子
So I can sing them all my songs
	所以我可以为他们唱我的歌
And I can tell them stories
	我可以为他们讲我的故事
Most of my boys are with me
	昔日兄弟仍跟有联络
Some are still out seeking glory
	有些仍在追名逐利
And some I had to leave behind
	有些已被我遗忘脑海
My brother I'm still sorry
	兄弟们 我仍心怀歉意
Soon I'll be 60 years old my daddy got 61
	很快我就年过花甲 我父亲也年逾古稀
Remember life and then your life becomes a better one
	时刻感恩 生活就会更加美好
I made the man so happy when I wrote a letter once
	又一次给老爸写信 他高兴不已
I hope my children come and visit once or twice a month
	我希望我的孩子偶尔也来看望一下我
Soon I'll be 60 years old will I think the world is cold
	很快我将年逾六十 不知是否还会觉得人世冷漠
Or will I have a lot of children who can warm me
	还是会拥有一群温暖我心的孩子
Soon I'll be 60 years old
	#很快我将年逾六十
Soon I'll be 60 years old will I think the world is cold
	很快我将年逾六十 不知是否还会觉得人世冷漠
Or will I have a lot of children who can warm me
	还是拥有一群温暖我心的孩子
Soon I'll be 60 years old
	#很快我将年逾六十
Once I was seven years old my momma told me
	那年我七岁 妈妈就对我说
Go make yourself some friends or you'll be lonely
	去交些朋友 不然你会孤独寂寞
Once I was seven years old
	那年我七岁
Once I was seven years old
	那年我七岁
'''
