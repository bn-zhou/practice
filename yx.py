class Creature():
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp
    def say(self):
        print ("我的名字是",name,"我接下去去打小怪兽")










name = input ("请输入你的名字 <")

player = Creature(name,100)
maste = Creature("暗黑破坏兽",100)

print (name,"你好，我是天使。现在地球遇上了危机，正是需要英雄的时候。你愿意为了地球去天马座星系打败怪兽，保护地球吗？")
select = input ("请输入是or否 <")


while select == "是" and select == "否":
    if select == "是":
        print ("好的，我将送你到天马座星系。")
        print ("."*20)
        print ("你现在已经到了天马座星系。")
        print ("出现在你面前的是敌人的大BOOS——暗黑破坏兽")
        break
    elif select == "否":
        print ("砰！！！")
        print ("出现在你面前的是敌人的大BOOS——暗黑破坏兽")
        print ("它叫嚣道:没想到吧！！！")
        break
    else:
        print ("请重新输入")



















