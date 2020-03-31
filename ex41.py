# -- coding: utf-8 --
from sys import exit
from random import randint

def death():
    quips = ["你死了。你的技术有点烂！",
    "好样的，你死了，哈哈哈！",
    "GAME OVER！",
    "我劝你再来一次！"]

    print (quips[randint(0,len(quips)-1)])
    exit(1)
    a = input ('<<<<<<')

def central_corridor():
	print ("珀卡尔星球的哥顿人入侵了你的船。在船中大开杀戒。")
	print ("你是最后一个幸存的成员。")
	print ("任务是从武器库中取出中子炸弹")
	print ("把它放在舰桥上，然后把船摧毁。")
	print ("\n")
	print ("你正沿着中央走廊向武器库跑去")
	print ("一只有着红色带鳞的皮肤，黑色的肮脏的牙齿，穿着邪恶的小丑服装的哥顿跳了出来，。")
	print ("在他充满仇恨的身体里流淌。他堵住了通往")
	print ("军械库的门，准备拔出武器来炸你。")

	print ("请输入射击or躲避or讲一个笑话。")

	action = input (">")

	if action == "射击":
		print ("你拔出你的爆能枪向哥顿星人开火")
		print ("他的小丑服装在他的身体周围形成了保护罩，这使他")
		print ("躲开了你的攻击。你的激光击中了他的保护罩，但却完全失去了他本体的影子。这个")
		print ("但是，这也使得他母亲送给他的衣服完全的破碎了。")
		print ("然后，他勃然大怒，朝你开了无数枪。")
		return ("death")

	elif action == "躲避":
		print ("""你就像一个世界级的拳击手，左躲右避，
			巧妙的避开了哥顿的攻击。但在你巧妙的闪避过程中，
			你的脚却绊到了消防栓，你的头撞在金属墙上，
			然后昏过去。哥特趁机向你射击。
			""")
		return ('death')

	elif action == "讲一个笑话":
		print ("""幸运的是，你知道一个很好笑的笑话。
			你对哥顿讲了一个笑话：
			我中午去ATM存钱，排队时后面的美女问我：“存钱是吗？”
			 “嗯” 
			 “我正好要取钱，反正你要存，不如把钱给我，咋俩就不用排队了” 
			 我一想觉得挺有道理，就把钱给她了。
			 哥顿停下来，先是憋住不笑，然后放声大笑。
			 当他在笑的时候，你跑起来，朝他头部的方向开枪，把他放下，然后跑到了激光武器库。
			 """)
		return ('laser_weapon_armory')


	else:
		print ("请输入射击or躲避or讲一个笑话。")
		return "central_corridor"


def laser_weapon_armory():
	print ("""你进入武器库，蹲下扫视了一遍房间，寻找更多可能隐藏起来的哥顿。
		你站起来，跑到房间的另一边，在里面找到了中子弹。盒子上有个键盘锁，
		你需要密码才能把炸弹拿出来。
		如果你把密码搞错3次，锁就会永远关上，你就不能拿到炸弹。
		代码为3位。”
		""")

	code = "3"
	guess = input('请输入一个一位数')
	guesses = 0


	while guess != code and guesses < 2:
		print ("输入错误")
		guesses = guesses + 1
		guess = input('请输入一个一位数')

	if guess == code:
		print ("密码输入正确。")
		print ("""容器咔嚓一声打开,密封件破裂，气体泄漏。
			你抓起中子弹，以最快的速度跑到桥上，你必须把它放在正确的位置。
			""")

		return ('the_bridge')

	else:
		print ("""
			锁最后一次发出嗡嗡声，然后当机械装置转动的声音。然后发出了一声轻微的撕裂声。
			这意味着你已经不能将炸弹取出。你决定坐在那里，然后听天由命。
			最后哥特人从船上炸毁了船，你就死了。
			""")

		return ('death')

def the_bridge():
	print ("""你胳膊下夹着中子炸弹冲进了舰桥，
		让5个试图控制飞船的哥特人大吃一惊。
		他们看到你胳膊下的炸弹，不想主动引爆它。所以他们还没有拔出他们的武器。
		""")

	action = input ('请输入扔炸弹还是放置炸弹')

	if action == '扔炸弹':

		print ("""在恐慌中，你向哥顿投掷了炸弹，然后朝门那边跳去。
			就在你跳的过程中，一个哥顿人从你的背后射杀了你。当你死的时候，
			你看到另一个哥顿人正疯狂地试图解除炸弹。
			你知道他们是不可能拆掉的，最后的结果是同归于尽。
			""")
		return "death"

	elif action == '放置炸弹':

		print ("""你用爆破枪指着你胳膊下面的炸弹，哥特人举起了手，并开始冒冷汗。
			你后退一步，打开门，然后小心地把炸弹放在地上，用爆破枪指着它。
			然后你跳回到门前，按一下“关闭”按钮，关上了门，
			这样哥顿就出不去了。你就可以坐逃生舱离开了。
			""")

		return 'escape_pod'

	else :
		print ('错误')

		return 'the_bridge'

def escape_pod():
	print ("""在整艘船爆炸之前，你拼命地跑着，想尽快赶到逃生舱。船上已经几乎没有哥顿人了，
		所以你一路都没有受到干扰。然后你到了有逃生舱的房间，
		现在需要选择一个逃生舱。这些逃生舱中有些可能已经损坏，
		但你没有时间仔细检查。有5个逃生舱，你要选择几号？”
		""")

	good_pod = "2"
	guess = input ('逃生舱 >')


	if guess != good_pod:
		print ("""你跳进逃生舱，按下弹出按钮。太空舱飞到了太空中，
			然后随着船体破裂而内爆，把你的身体压成果酱状。
			""")
		return('death')
	else:
		print("""你跳进了太空舱，按下弹出按钮，太空舱很容易滑出太空，进入下面的星球。当它飞到行星上时，
			你回头看，你的飞船内爆，然后像明亮的恒星一样爆炸，同时带走了哥顿飞船。你赢了！
			""")
		exit(0)
		a = input ('<<<<<<')

ROOMS ={
'death':death,
'central_corridor':central_corridor,
'laser_weapon_armory':laser_weapon_armory,
'the_bridge':the_bridge,
'escape_pod':escape_pod
		}


def runner(map,start):
	next = start
	while True:
		room = map[next]
		print ("\n---------------")
		next = room()

runner(ROOMS,'central_corridor')
