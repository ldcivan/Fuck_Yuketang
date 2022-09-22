import pyautogui
import time
import pyscreeze
import cv2
screenWidth, screenHeight = pyautogui.size()

print(
    '''
      本程序由Yujio_Nako编写，基于opencv与pyautogui
    本程序仅供学习，请确保使用过程不会触犯当地法律与学校条规
             Yujio_Nako不对任何使用后果负责
    ——————————————————————————————————————————————
             本程序只支持了0-60页的自动翻页
         如有需要更多页数需要可自行在data文件夹中
     以PNG格式保存按钮截图，样式与文件名参考data内内容
    '''
)
time.sleep(3)

try:
    t = int(input("请输入翻页的间隔：") or 5)
except:
    print("乱填是吧？不会填我来给你填！")
    t = 5
    print("已设置间隔时间为 5 秒")
if (t < 5):
    t = 5
    print("间隔太小，到时候怕你被鼠标耍了关不掉程序，已自动调整间隔为 5 秒")
    time.sleep(1)
try:
    page = int(input("从第几页开始看(默认从0页开始)：") or 0)
except:
    print("乱填是吧？不会填我来给你填！")
    page = 0
    print("已设置起始页数为第 0 页")
print("将在 5 秒后开始运行，请确保将要预习的内容置于前台！！")
print("建议全屏，否则可能造成目录上的页码被下边框覆盖！！")
for i in range(5):
	print('剩余',5-i,'S')
	time.sleep(1)
print('开始执行')


screenScale = 1
loop = 1

while(loop == 1):

    # 事先读取按钮截图
    target = cv2.imread(r".//data//menu.png", cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot = pyscreeze.screenshot('.//data//my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'.//data//my_screenshot.png', cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    print("目标图宽高：" + str(twidth) + "-" + str(theight))
    print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if (max_val >= 0.6):
        # 计算出中心点
        top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)
        tagHalfW = int(twidth / 2)
        tagHalfH = int(theight / 2)
        tagCenterX = top_left[0] + tagHalfW
        tagCenterY = top_left[1] + tagHalfH
        # 左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX, tagCenterY, button='left')
    else:
        print("没找到")

    # 事先读取按钮截图
    target = cv2.imread(r".//data//"+str(page)+".png", cv2.IMREAD_GRAYSCALE)
    # 先截图
    screenshot = pyscreeze.screenshot('.//data//my_screenshot.png')
    # 读取图片 灰色会快
    temp = cv2.imread(r'.//data//my_screenshot.png', cv2.IMREAD_GRAYSCALE)

    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    print("目标图宽高：" + str(twidth) + "-" + str(theight))
    print("模板图宽高：" + str(tempwidth) + "-" + str(tempheight))
    # 先缩放屏幕截图 INTER_LINEAR INTER_AREA
    scaleTemp = cv2.resize(temp, (int(tempwidth / screenScale), int(tempheight / screenScale)))
    stempheight, stempwidth = scaleTemp.shape[:2]
    print("缩放后模板图宽高：" + str(stempwidth) + "-" + str(stempheight))
    # 匹配图片
    res = cv2.matchTemplate(scaleTemp, target, cv2.TM_CCOEFF_NORMED)
    mn_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(max_val)
    if (max_val >= 0.985):
        # 计算出中心点
        top_left = max_loc
        bottom_right = (top_left[0] + twidth, top_left[1] + theight)
        tagHalfW = int(twidth / 2)
        tagHalfH = int(theight / 2)
        tagCenterX = top_left[0] + tagHalfW
        tagCenterY = top_left[1] + tagHalfH
        # 左键点击屏幕上的这个位置
        pyautogui.click(tagCenterX, tagCenterY, button='left')
    else:
        print("----------------------------------------")
        print("没找到目标页数，可能是已经看完或页数被遮挡，请手动接管")
        print("结束页数是：%s 页" %(page - 1))
        loop = 0

    page = page + 1

    time.sleep(t)