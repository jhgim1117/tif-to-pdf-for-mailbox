import img2pdf
import os
import datetime

filenames = os.listdir('./')
for direc in filenames:
    if '.py' not in direc:
        imgs = os.listdir('./'+direc)
        real_imgs = []
        flag = 0
        for img in imgs:
            if '.pdf' in img:
                flag = 1
                break
            real_imgs.append(f'./{direc}/{img}')
        if flag:
            continue
        try:
            with open(f"./{direc}/{datetime.datetime.now().strftime('%Y%m%d %H%M%S')}.pdf","wb") as f:
                f.write(img2pdf.convert(real_imgs))
        except:
            continue