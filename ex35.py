from sys import exit

def gold_room():
    print ("这房间里全是金子。你要拿多少？")
    next = input(">")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("伙计，要学会打一个数字。")

    if how_much < 50:
        print ("不错，你不贪心，你赢了。")
        input(">>>>>>>>>>>>")
    else:
        dead("你这个贪婪的家伙！")


def bear_room():
    print ("这里有只熊。")
    print ("这只熊有一堆蜂蜜。")
    print ("肥熊在另一扇门前。")
    print ("你打算怎样行动去引走熊，吃蜂蜜还是嘲讽熊又或者是直接开门？")
    bear_moved = False

    while True:
        next = input(">")
        if next == "吃蜂蜜":
            dead("熊看着你，然后拍打你的脸。说道：小伙子，胆挺肥的！")
        elif next == "嘲讽熊" and not bear_moved:
            print ("熊已经离开了门，你现在可以进去了。")
            bear_moved = True
        elif next == "开门" and bear_moved:
            gold_room
        else:
            print ("我不知道你这是什么意思？")




def cthulhu_room():
    print ("在这里你看到了邪恶的克苏鲁。")
    print ("作为旧日支配者的一员，克苏鲁的形象粗糙地带有一些章鱼、蝙蝠和人类的特征，他全身绿色，身躯极其巨大，据说有一座山那样高;他柔软的头部生有无数的触须，身体肥胖并长着鳞片，前肢生有软塌塌的类似爪状物，背后有一对破破烂烂、似乎没有长成形的翅膀。")
    print ("你是选择逃命还是头给他吃？")

    next = input("请输入逃命或者头>")
    if "逃命" in next:
        start()
    elif "头" in next:
        dead("嗯，克鲁苏看着你空空的头，摇了摇头。你幸运的活了下来。")
    else:
        print ("脑袋一阵眩晕，你又回来了。")
        cthulhu_room()




def dead(why):
    print (why,"Good job!")
    input(">>>>>>>>>>>>")

def start():
    print ("你在一个小黑屋里。嘿嘿嘿~~~")
    print ("你的左手和右手边各有一扇门。")
    print ("请问你要选择那一扇门？")

    next = input("请输入左或者右，>")
    if next == "左":
        bear_room()
    elif next == "右":
        cthulhu_room()
    else:
        dead("我让你输左或者右，你都输了些什么。所以你最后在房间里一直转悠，然后饿死了。")



start()






