# with open("resource/学习计划.txt","r",encoding= "utf-8") as f:
#     # for line in f:
#     #     print(line.strip())
#     content = f.readlines()
#     print(content)

with open("resource/写入测试.txt","w",encoding= "utf-8") as f:
    f.write("hello world")
    f.write("静夜思（李白）\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

with open("resource/写入测试.txt","a",encoding= "utf-8") as f:
    f.write("com.abi.backpack.attack，这个包线上看广告比较少，重新改了看广告逻辑，但还是会有些慢这个游戏只有死亡的时候可以看广告，本地执行最快5分钟之后能看到一次广告，慢的话估计要十分钟，线上会更慢一些")