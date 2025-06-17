# 加载机械臂库文件
#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

# 获取机械臂的对象
Arm = Arm_Device()
time.sleep(.1)
# 定义不同位置的变量参数
p_mould = [90, 130, 0, 0, 90]
p_top = [90, 80, 50, 50, 270]
p_Brown = [90, 53, 33, 36, 270]

p_layer_4 = [90, 76, 40, 17, 270]
p_layer_3 = [90, 65, 44, 17, 270]
p_layer_2 = [90, 65, 25, 36, 270]
p_layer_1 = [90, 48, 35, 30, 270]

p_move_layer_4 = [90, 72, 49, 13, 270]
p_move_layer_3 = [90, 66, 43, 20, 270]
p_move_layer_2 = [90, 63, 34, 30, 270]
p_move_layer_2 = [90, 53, 33, 36, 270]

p_Yellow = [65, 22, 64, 56, 270]
p_Red = [118, 19, 66, 56, 270]

p_Green = [136, 66, 20, 29, 270]
p_Blue = [44, 66, 20, 28, 270]
# 配置叠罗汉动作参数
# 定义夹积木块函数，enable=1：夹住，=0：松开
def arm_clamp_block(enable):
    if enable == 0:
        Arm.Arm_serial_servo_write(6, 60, 400)
    else:
        Arm.Arm_serial_servo_write(6, 135, 400)
    time.sleep(.5)

    
# 定义移动机械臂函数,同时控制1-5号舵机运动，p=[S1,S2,S3,S4,S5]
def arm_move(p, s_time = 500):
    for i in range(5):
        id = i + 1
        if id == 5:
            time.sleep(.1)
            Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.2))
        elif id == 1 :
            Arm.Arm_serial_servo_write(id, p[i], int(3*s_time/4))

        else:
            Arm.Arm_serial_servo_write(id, p[i], int(s_time))
        time.sleep(.01)
    time.sleep(s_time/1000)

def heap_up():
    # 让机械臂移动到一个准备抓取的位置
    arm_clamp_block(0)
    arm_move(p_mould, 1000)
    time.sleep(1)
    # 夹取黄色区域的方块堆叠到中间最底层的位置。
    arm_move(p_top, 1000)
    arm_move(p_Yellow, 1000)
    arm_clamp_block(1)

    arm_move(p_top, 1000)
    arm_move(p_layer_1, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move(p_mould, 1100)

    time.sleep(2)
    
    # 夹取红色区域的方块堆叠到中间第二层的位置。
    arm_move(p_top, 1000)
    arm_move(p_Red, 1000)
    arm_clamp_block(1)

    arm_move(p_top, 1000)
    arm_move(p_layer_2, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move(p_mould, 1100)

    time.sleep(2)
    
    # 夹取绿色区域的方块堆叠到中间第三层的位置。
    arm_move(p_top, 1000)
    arm_move(p_Green, 1000)
    arm_clamp_block(1)

    arm_move(p_top, 1000)
    arm_move(p_layer_3, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move(p_mould, 1100)

    time.sleep(2)
    
    # 夹取蓝色区域的方块堆叠到中间第四层的位置。
    arm_move(p_top, 1000)
    arm_move(p_Blue, 1000)

    arm_clamp_block(1)

    arm_move(p_top, 1000)
    arm_move(p_layer_4, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move(p_mould, 1100)

    time.sleep(1)
# 配置跳舞动作参数
time_1 = 500
time_2 = 1000
time_sleep = 0.5

def dance():
    Arm.Arm_serial_servo_write6(90, 90, 90, 90, 90, 90, 500)
    time.sleep(1)
    
    Arm.Arm_serial_servo_write(2, 180-120, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 120, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 60, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 180-135, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 135, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 45, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 180-120, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 120, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 60, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 90, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 180-80, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 80, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 80, time_1)
    time.sleep(time_sleep)



    Arm.Arm_serial_servo_write(2, 180-60, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 60, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 60, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 180-45, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 45, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 45, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(2, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(3, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 90, time_1)
    time.sleep(.001)
    time.sleep(time_sleep)



    Arm.Arm_serial_servo_write(4, 20, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(6, 150, time_1)
    time.sleep(.001)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(4, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(6, 90, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(4, 20, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(6, 150, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(4, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(6, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(1, 0, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(5, 0, time_1)
    time.sleep(time_sleep)



    Arm.Arm_serial_servo_write(3, 180, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 0, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(6, 180, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(6, 0, time_2)
    time.sleep(time_sleep)



    Arm.Arm_serial_servo_write(6, 90, time_2)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(1, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(5, 90, time_1)
    time.sleep(time_sleep)

    Arm.Arm_serial_servo_write(3, 90, time_1)
    time.sleep(.001)
    Arm.Arm_serial_servo_write(4, 90, time_1)
    time.sleep(time_sleep)
# 配置夹方块动作参数
# 定义移动机械臂函数,同时控制1-5号舵机运动，p=[S1,S2,S3,S4,S5]
def arm_move_clamp(p, s_time = 500):
    for i in range(5):
        id = i + 1
        if id == 5:
            time.sleep(.1)
            Arm.Arm_serial_servo_write(id, p[i], int(s_time*1.2))
        else :
            Arm.Arm_serial_servo_write(id, p[i], s_time)
        time.sleep(.01)
    time.sleep(s_time/1000)

# 机械臂向上移动
def arm_move_up():
    Arm.Arm_serial_servo_write(2, 90, 1500)
    Arm.Arm_serial_servo_write(3, 90, 1500)
    Arm.Arm_serial_servo_write(4, 90, 1500)
    time.sleep(.1)

def clamp_clock():
    # 让机械臂移动到一个准备抓取的位置
    arm_clamp_block(0)
    arm_move_clamp(p_mould, 1000)
    time.sleep(1)

    # 从灰色积木块位置抓取一块积木放到黄色积木块的位置上。
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Brown, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Yellow, 1000)
    arm_clamp_block(0)

    arm_move_clamp(p_mould, 1000)

    time.sleep(2)

    # 从灰色积木块位置抓取一块积木放到红色积木块的位置上。
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Brown, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Red, 1000)
    arm_clamp_block(0)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(2)

    # 从灰色积木块位置抓取一块积木放到绿色积木块的位置上。
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Brown, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Green, 1000)
    arm_clamp_block(0)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(2)

    # 从灰色积木块位置抓取一块积木放到蓝色积木块的位置上。
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Brown, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Blue, 1000)
    arm_clamp_block(0)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(1)
# 配置搬运动作参数
def move_block():
    # 让机械臂移动到一个准备抓取的位置
    arm_clamp_block(0)
    arm_move_clamp(p_mould, 1000)
    time.sleep(1)

    # 搬运第四层的积木块到黄色区域
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_move_layer_4, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Yellow, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(2)

    # 搬运第三层的积木块到红色区域
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_move_layer_3, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Red, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(2)

    # 搬运第二层的积木块到绿色区域
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_move_layer_2, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Green, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(2)

    # 搬运第一层的积木块到蓝色区域
    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_move_layer_2, 1000)
    arm_clamp_block(1)

    arm_move_clamp(p_top, 1000)
    arm_move_clamp(p_Blue, 1000)
    arm_clamp_block(0)

    time.sleep(.1)

    arm_move_up()
    arm_move_clamp(p_mould, 1100)

    time.sleep(1)
# 加载语音识别和语音播报库文件
import smbus
bus = smbus.SMBus(1)

i2c_addr = 0x0f   #Speech recognition module address
asr_add_word_addr  = 0x01   #Entry add address
asr_mode_addr  = 0x02   #Recognition mode setting address, the value is 0-2, 0: cyclic recognition mode 1: password mode, 2: button mode, the default is cyclic detection
asr_rgb_addr = 0x03   #RGB lamp setting address, need to send two bits, the first one is directly the lamp number 1: blue 2: red 3: green
                      #The second byte is brightness 0-255, the larger the value, the higher the brightness
asr_rec_gain_addr  = 0x04    #Identification sensitivity setting address, sensitivity can be set to 0x00-0x7f, the higher the value, the easier it is to detect but the easier it is to misjudge
                             #It is recommended to set the value to 0x40-0x55, the default value is 0x40
asr_clear_addr = 0x05   #Clear the operation address of the power-off cache, clear the cache area information before entering the information
asr_key_flag = 0x06  #Used in key mode, set the startup recognition mode
asr_voice_flag = 0x07   #Used to set whether to turn on the recognition result prompt sound
asr_result = 0x08  #Recognition result storage address
asr_buzzer = 0x09  #Buzzer control register, 1 bit is on, 0 bit is off
asr_num_cleck = 0x0a #Check the number of entries
asr_vession = 0x0b #firmware version number
asr_busy = 0x0c #Busy and busy flag

i2c_speech_addr = 0x30   #语音播报模块地址
speech_date_head = 0xfd
# 定义播报参数控制函数
def I2C_WriteBytes(str_):
    global i2c_speech_addr
    for ch in str_:
        try:
            bus.write_byte(i2c_speech_addr,ch)
            time.sleep(0.01)
        except:
            print("write I2C error")



EncodingFormat_Type = {
                        'GB2312':0x00,
                        'GBK':0X01,
                        'BIG5':0x02,
                        'UNICODE':0x03
                        }
def Speech_text(str_,encoding_format):
    str_ = str_.encode('gb2312')   
    size = len(str_)+2
    DataHead = speech_date_head
    Length_HH = size>>8
    Length_LL = size & 0x00ff
    Commond = 0x01
    EncodingFormat = encoding_format

    Date_Pack = [DataHead,Length_HH,Length_LL,Commond,EncodingFormat]

    I2C_WriteBytes(Date_Pack)

    I2C_WriteBytes(str_)

def SetBase(str_):
    str_ = str_.encode('gb2312')   
    size = len(str_)+2

    DataHead = speech_date_head
    Length_HH = size>>8
    Length_LL = size & 0x00ff
    Commond = 0x01
    EncodingFormat = 0x00

    Date_Pack = [DataHead,Length_HH,Length_LL,Commond,EncodingFormat]

    I2C_WriteBytes(Date_Pack)

    I2C_WriteBytes(str_)

def TextCtrl(ch,num):
    if num != -1:
        str_T = '[' + ch + str(num) + ']'
        SetBase(str_T)
    else:
        str_T = '[' + ch + ']'
        SetBase(str_T)


ChipStatus_Type = {
                    'ChipStatus_InitSuccessful':0x4A,#初始化成功回传
                    'ChipStatus_CorrectCommand':0x41,#收到正确的命令帧回传
                    'ChipStatus_ErrorCommand':0x45,#收到不能识别命令帧回传
                    'ChipStatus_Busy':0x4E,#芯片忙碌状态回传
                    'ChipStatus_Idle':0x4F #芯片空闲状态回传                  
                }

def GetChipStatus():
    global i2c_speech_addr
    AskState = [0xfd,0x00,0x01,0x21]
    try:
        I2C_WriteBytes(AskState)
        time.sleep(0.05)
    except:
        print("I2CRead_Write error")


    try:
        Read_result = bus.read_byte(i2c_speech_addr)
        return Read_result
    except:
        print("I2CRead error")

Style_Type = {
                'Style_Single':0,#为 0，一字一顿的风格
                'Style_Continue':1#为 1，正常合成
                }#合成风格设置 [f?]

def SetStyle(num):
    TextCtrl('f',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)   


Language_Type = {
                'Language_Auto':0,#为 0，自动判断语种
                'Language_Chinese':1,#为 1，阿拉伯数字、度量单位、特殊符号等合成为中文
                'Language_English':2#为 1，阿拉伯数字、度量单位、特殊符号等合成为中文
                }#合成语种设置 [g?]

def SetLanguage(num):
    TextCtrl('g',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)

Articulation_Type = {
                'Articulation_Auto':0,#为 0，自动判断单词发音方式
                'Articulation_Letter':1,#为 1，字母发音方式
                'Articulation_Word':2#为 2，单词发音方式
                }#设置单词的发音方式 [h?]

def SetArticulation(num):
    TextCtrl('h',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


Spell_Type = {
                'Spell_Disable':0,#为 0，不识别汉语拼音
                'Spell_Enable':1#为 1，将“拼音＋1 位数字（声调）”识别为汉语拼音，例如： hao3
                }#设置对汉语拼音的识别 [i?]

def SetSpell(num):
    TextCtrl('i',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


Reader_Type = {
                'Reader_XiaoYan':3,#为 3，设置发音人为小燕(女声, 推荐发音人)
                'Reader_XuJiu':51,#为 51，设置发音人为许久(男声, 推荐发音人)
                'Reader_XuDuo':52,#为 52，设置发音人为许多(男声)
                'Reader_XiaoPing':53,#为 53，设置发音人为小萍(女声
                'Reader_DonaldDuck':54,#为 54，设置发音人为唐老鸭(效果器)
                'Reader_XuXiaoBao':55#为 55，设置发音人为许小宝(女童声)                
                }#选择发音人 [m?]

def SetReader(num):
    TextCtrl('m',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


NumberHandle_Type = {
                'NumberHandle_Auto':0,#为 0，自动判断
                'NumberHandle_Number':1,#为 1，数字作号码处理
                'NumberHandle_Value':2#为 2，数字作数值处理
                }#设置数字处理策略 [n?]

def SetNumberHandle(num):
    TextCtrl('n',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)



ZeroPronunciation_Type = {
                'ZeroPronunciation_Zero':0,#为 0，读成“zero
                'ZeroPronunciation_O':1#为 1，读成“欧”音
                }#数字“0”在读 作英文、号码时 的读法 [o?]

def SetZeroPronunciation(num):
    TextCtrl('o',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)



NamePronunciation_Type = {
                'NamePronunciation_Auto':0,#为 0，自动判断姓氏读音
                'NamePronunciation_Constraint':1#为 1，强制使用姓氏读音规则
                }#设置姓名读音 策略 [r?]


def SetNamePronunciation(num):
    TextCtrl('r',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)

#设置语速 [s?] ? 为语速值，取值：0～10
def SetSpeed(speed):
    TextCtrl('s',speed)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


#设置语调 [t?] ? 为语调值，取值：0～10
def SetIntonation(intonation):
    TextCtrl('t',intonation)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)

#设置音量 [v?] ? 为音量值，取值：0～10
def SetVolume(volume):
    TextCtrl('v',volume)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


OnePronunciation_Type = {
                'OnePronunciation_Yao':0,#为 0，合成号码“1”时读成幺
                'OnePronunciation_Yi':1#为 1，合成号码“1”时读成一
                }#设置号码中“1”的读法 [y?]

def SetOnePronunciation(num):
    TextCtrl('y',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)


Rhythm_Type = {
                'Rhythm_Diasble':0,#为 0，“ *”和“#”读出符号
                'Rhythm_Enable':1#为 1，处理成韵律，“*”用于断词，“#”用于停顿
                }#是否使用韵律 标记“*”和“#” [z?]

def SetRhythm(num):
    TextCtrl('z',num)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)

#恢复默认的合成参数 [d] 所有设置（除发音人设置、语种设置外）恢复为默认值
def SetRestoreDefault():
    TextCtrl('d',-1)
    while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:
        time.sleep(0.002)
# 定义语音控制函数
#Write entry
def AsrAddWords(idnum,str):
    global i2c_addr
    global asr_add_word_addr
    words = []
    words.append(asr_add_word_addr)
    words.append(len(str) + 2)
    words.append(idnum)
    for  alond_word in str:
        words.append(ord(alond_word))
    words.append(0)
    print(words)
    for date in words:
        bus.write_byte (i2c_addr, date)
        time.sleep(0.03)

#Set RGB
def RGBSet(R,G,B):
    global i2c_addr
    global asr_rgb_addr
    date = []
    date.append(R)
    date.append(G)
    date.append(B)
    print(date)
    bus.write_i2c_block_data (i2c_addr,asr_rgb_addr,date)

#Read result
def I2CReadByte(reg):
    global i2c_addr
    bus.write_byte (i2c_addr, reg)
    time.sleep(0.05)
    Read_result = bus.read_byte (i2c_addr)
    return Read_result

#Wait busy
def Busy_Wait():
    busy = 255
    while busy != 0:
        busy = I2CReadByte(asr_busy)
        print(asr_busy)	
# 清除掉电缓存区中的词条和模块模式数据，这部分第一次使用写入即可，后续如果不需要在更改设置可以把1 设置为0，或者跳过，之后设置模块的灵敏度和识别提示声的开关，之后亮起模块的RGB 灯为白色1s 和鸣笛1s，并播报"初始化完成，请发布指令"。
'''
The mode and phrase have the function of power-down save, if there is no modification after the first entry, you can change 1 to 0
'''
cleck = 1

if 1:
    bus.write_byte_data(i2c_addr, asr_clear_addr, 0x40)#Clear the power-down buffer area
    Busy_Wait()#Wait for the module to be free
    print("Cache cleared")
    bus.write_byte_data(i2c_addr, asr_mode_addr, 1)
    Busy_Wait()
    print("The mode is set")
    AsrAddWords(0,"xiao ya")
    Busy_Wait()
    AsrAddWords(1,"die luo han")
    Busy_Wait()
    AsrAddWords(2,"tiao wu")
    Busy_Wait()
    AsrAddWords(3,"jia fang kuai")
    Busy_Wait()
    AsrAddWords(4,"ban yun")
    Busy_Wait()
    while cleck != 5:
        cleck = I2CReadByte(asr_num_cleck)
        print(cleck)

bus.write_byte_data(i2c_addr, asr_rec_gain_addr, 0x40)#Set the sensitivity, the recommended value is 0x40-0x55
bus.write_byte_data(i2c_addr, asr_voice_flag, 1)#Set switch sound
bus.write_byte_data(i2c_addr, asr_buzzer, 1)#buzzer
RGBSet(255,255,255)
time.sleep(1)
RGBSet(0,0,0)
bus.write_byte_data(i2c_addr, asr_buzzer, 0)#buzzer

SetReader(Reader_Type["Reader_XiaoPing"])#选择播音人晓萍
SetVolume(8)
Speech_text("初始化完成，请发布指令",EncodingFormat_Type["GB2312"])
while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:#等待当前语句播报结束
    time.sleep(0.1)  
# 循环检测声音
def main():
    while True:
        result = I2CReadByte(asr_result)
        print(f"result:{result}")
        #print(result)
        if result == 1:
            Speech_text("好的，开始叠罗汉",EncodingFormat_Type["GB2312"])
            while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:#等待当前语句播报结束
                time.sleep(0.1)  
            heap_up()
        elif result == 2:
            Speech_text("好的，开始跳舞",EncodingFormat_Type["GB2312"])
            while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:#等待当前语句播报结束
                time.sleep(0.1)  
            dance()
        elif result == 3:
            Speech_text("好的，开始夹方块",EncodingFormat_Type["GB2312"])
            while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:#等待当前语句播报结束
                time.sleep(0.1)  
            clamp_clock()
        elif result == 4:
            Speech_text("好的，开始搬运",EncodingFormat_Type["GB2312"])
            while GetChipStatus() != ChipStatus_Type['ChipStatus_Idle']:#等待当前语句播报结束
                time.sleep(0.1) 
            move_block()

        time.sleep(0.5)
        #print(" END OF LINE! ")
try :
    main()
except KeyboardInterrupt:
    # 释放Arm对象
    del Arm
    del bus
    print(" Program closed! ")
    pass


