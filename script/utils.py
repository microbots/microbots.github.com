# Create your views here.
# coding=utf-8

import qrcode  
import Image  
import os  

def gen_ecard(vstr,path):
    # print vstr
    qr = qrcode.QRCode(
        # version值为1~40的整数,控制二维码的大小,(最小值是1,是个12*12的矩阵)
        # 如果想让程序自动确定,将值设置为 None 并使用 fit 参数即可
        version=2,
        # error_correction: 控制二维码的错误纠正功能,可取值下列4个常量
        #   ERROR_CORRECT_L: 大约7%或更少的错误能被纠正
        #   ERROR_CORRECT_M(默认): 大约15%或更少的错误能被纠正
        #   ERROR_CORRECT_Q: 大约25%或更少的错误能被纠正
        #   ERROR_CORRECT_H: 大约30%或更少的错误能被纠正
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        # 控制二维码中每个小格子包含的像素数
        box_size=2,
        # 控制边框(二维码与图片边界的距离)包含的格子数(默认为4,是相关标准规定的最小值)
        border=3,
    )

    # 将vCard数据填入qr
    qr.add_data(vstr)

    qr.make(fit=True)

    # 生成图片
    img = qr.make_image()

    # 将图片存入指定路径文件
    img.save(path)

def change_color(rgb_value,path):
    current_path= os.getcwd()
    file_path =  current_path+"/test.png"
    im = Image.open(file_path)
    image = im.convert('RGB')
    pixs = image.load()
    (row,col) = image.size
    print rgb_value
    for x in range(0,row):
        for y in range(0,col):
            if pixs[x,y] == (0,0,0):
                pixs[x,y] = rgb_value

    image.save("test.png")

def get_ecard_path(name,phone,tel,email,address,url,position,rgb_value):
    begin = "BEGIN:VCARD\n"
    ename = ephone = eemail = eaddress = eurl = etitle = etel =""
    if name:
        ename = "FN:%s\n" % name
    if phone:
        ephone = "TEL;TYPE=cell:%s\n" % phone
    if email: 
        eemail = "EMAIL:%s\n" % email
    if address:
        eaddress = "ADR;TYPE=WORK:;%s\n" % address
    if url:
        eurl = "URL:%s\n" % url
    if position:
        etitle = "TITLE:%s\n" % position
    if tel:
        etel =  "TEL:%s\n" % tel
    end = "END:VCARD\n"

    current_root = os.path.dirname(__file__)

    vstr = begin + ename + etel  + ephone + eemail + eaddress + eurl + etitle +end
   
    current_path= os.getcwd()
    path =  current_path+ "/test.png"  
    gen_ecard(vstr,path)
    change_color(rgb_value,path)
    return path

if __name__ == "__main__":
    name = "杨宝玲"
    tel = "15212345678"
    phone = "6656123"
    email = "yang.bl@qq.com"
    address = "上海"
    url = "http://oriental13.lofter.com"
    position = "东南大学学生"
    #rgb_list = [(1,1,1),(46,111,188),(48,161,212),(10,158,80),(229,137,5),(249,97,21),(140,19,27)]
    rgb_value = (140,19,27)
    get_ecard_path(name,tel,phone,email,address,url,position,rgb_value)
