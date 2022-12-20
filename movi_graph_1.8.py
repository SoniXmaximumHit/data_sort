import numpy as np
from matplotlib import cm
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import PIL
from PIL import Image
import os
import itertools
import xlwt
fontsizes = itertools.cycle([16, 16, 24, 32])
class MakeGraph():
    """ Создаем график из данных файлов .dat """
    def __init__(self, r_list, path, w_list=[],  im=64, jm=64):
        self.r_list = r_list
        self.w_list = w_list
        self.path = path
        self.im = im
        self.jm = jm

    def creat_w_list(self):
        num_elem = (1/4)*len(self.r_list)
        num_elem=int(num_elem)
        # print("num_elem := "+str(num_elem))
        self.w_list=self.r_list[num_elem:num_elem*2]    
        # """ Записывает элементы в файл """
        # with open('file_1.txt', 'w') as fw:
        #     np.savetxt(fw, self.w_list, fmt='% .5f')
    def creat_w_mass(self):
        """ Организует 2мерный массив из данных одномерного """
        global w
        # print('im',self.im)
        w=np.zeros((self.im,self.jm))
        # print('wwww',len(w))
        for i in range(0,self.im-1):
            for j in range(0,self.jm-1):
                w[i][j]=self.w_list[i*(self.im+1)+j+1]
        print( np.shape(w),'ДЛИНА w')
        # """ Записывает элементы двумерного массива в файл """
        # with open('file.txt', 'w') as fw:
        #     np.savetxt(fw, w, fmt='% .5f') 
          
              
    def creat_graph(self,ti):
        self.creat_w_list()
        self.creat_w_mass()
        """ Строит график из данных массива """
        fig = plt.figure(figsize=plt.figaspect(0.5))
        # print(ti)
        plt.title(ti)
        # ax = fig.add_subplot(1, 2, 1, projection='3d')
        sx=np.zeros(len(w))
        sy=np.zeros(len(w))
        sz=np.zeros((self.im,self.jm))
        # print(len(sx),len(sy),len(sz),len(w))
        for i in range(len(w)):
            sx[i]=i/self.im
            for j in range(len(w[i])):
                sy[j]=j/self.jm
                sz[i][j]=w[i][j]
        # print(sx,sy)
        
        ##### график параболойд
        sx, sy = np.meshgrid(sx, sy)
        # surf = ax.plot_surface(sx, sy, w, cmap=cm.coolwarm,
        #                linewidth=0, antialiased=False)
        # fig.colorbar(surf, shrink=0.5, aspect=15)
        ########### график линии
        ax_1 = fig.add_subplot( 1, 1, 1)
        CS = ax_1.contour(sx, sy, w, 10,
                    colors='k',  # negative contours will be dashed by default)
                    )
        ax_1.clabel(CS, inline=1, fontsize=13, fmt='%1.2f')
        # ax_1.view_init(elev=-90)
        # plt.get_current_fig_manager().window.state('zoomed') 
        fig.set_size_inches(7.5, 7.5, forward=True)
        plt.savefig(self.path+'\\'+self.path+'_picture'+"\\"+self.path+'_'+ti+'.png', bbox_inches='tight')
        # plt.show()
        self.sect_graph(ti)

    def cycle_sect_graph(self,m):
        """ Строит массив для сектора"""
        sx1=np.zeros(len(m))
        sy1=np.zeros(len(m))
        sz1=np.zeros((len(m),len(m)))
        # print(len(sx1),len(sy1),len(sz1),len(m),'!!!!!!!!!!!!!!!!!!!!!!!')
        for ii in range(len(m)):
            sx1[ii]=ii/self.im
            for jj in range(len(m[ii])):
                sy1[jj]=jj/self.jm
                sz1[ii][jj]=m[ii][jj]

        return   sx1, sy1, sz1
             

    def sect_graph(self,ti):
        """ Строит сектор"""
        fig1 = plt.figure(figsize=plt.figaspect(0.5))
        # i1=int(len(w)/4); j1=int(len(w)/4)
        a=17; b=17

        i1=a; j1=b
        sx1, sy1, sz1 = self.cycle_sect_graph(w[:i1,:j1])
        ########### график линии
        ax_1 = fig1.add_subplot( 1, 4, 3)
        CS = ax_1.contour(sx1, sy1, sz1, 15,
                    colors='k',  # negative contours will be dashed by default)
                    )
        plt.title("Нижний левый угол")
        ax_1.clabel(CS, inline=1, fontsize=10)
        i1=-a; j1=-b
        sx1, sy1, sz1 = self.cycle_sect_graph(w[i1:,j1:])
        ax_1 = fig1.add_subplot( 1, 4, 2)
        CS = ax_1.contour(sx1, sy1, sz1, 15,
                    colors='k',  # negative contours will be dashed by default)
                    )
        plt.title("Верхний правый угол")
        ax_1.clabel(CS, inline=1, fontsize=10)
        i1=-a; j1=b
        sx1, sy1, sz1 = self.cycle_sect_graph(w[i1:,:j1])
        ax_1 = fig1.add_subplot( 1, 4, 1)
        CS = ax_1.contour(sx1, sy1, sz1, 15,
                    colors='k',  # negative contours will be dashed by default)
                    )
        plt.title("Верхний левый угол")
        ax_1.clabel(CS, inline=1, fontsize=10)
        i1=a; j1=-b
        sx1, sy1, sz1 = self.cycle_sect_graph(w[:i1,j1:])      
        ax_1 = fig1.add_subplot( 1, 4, 4)
        CS = ax_1.contour(sx1, sy1, sz1, 15,
                    colors='k',  # negative contours will be dashed by default)
                    )
        plt.title("Нижний правый угол")
        ax_1.clabel(CS, inline=1, fontsize=10)  
        # plt.get_current_fig_manager().window.state('zoomed')
        fig1.set_size_inches(11.5, 6.5, forward=True)
        plt.savefig(self.path+'\\'+self.path+'_picture'+"\\"+self.path+'_сектор_'+ti+'.png', bbox_inches='tight')  
        plt.cla()
        # plt.show()




class Graphs():
    """ Создаем график управляющих параметров из данных файлов spis списка """
    def __init__(self,path,dat,list=[]):
        self.list = list
        self.path = path
        self.dat = dat


    def graph_draw(self):
        """ Рисует график из управляющих параметров"""
        for elem in self.list:
            gr.append(elem[0])
            wc.append(elem[3])
        
        fig, ax = plt.subplots()
        plt.plot(gr, wc, 'o')
        ax.set_xlabel('Gr', fontsize=next(fontsizes))
        ax.set_ylabel('W', fontsize=next(fontsizes))
        ax.set_title('W от Gr', fontsize=next(fontsizes))
        # plt.savefig(self.path+'\\'+self.path+'_picture'+"\\"+'W от Gr.png', bbox_inches='tight')
        plt.cla()
        # plt.show()

    def exel(self,sheet):
        """Создаем ексель файл и записываем туда значения"""
        # Заполняем ящейку (Строка, Колонка, Текст, Шрифт)
        val=['gr',"re",'e_kin','wc','wm2','wsum']
        for i in range(len(val)):
                sheet.write(0,i,val[i])
        for i in range(len(self.list)):
            for j in range(len(self.list[i])):
                sheet.write(i+1,j,self.list[i][j])
        self.list.clear()
                

    def open_read_file(self,file):
        """Открывает картинку"""
        # titl=pic
        # img = Image.open(pic)
        # img.show()
        """ Открывает файл и считывает из него данные, переводит их в float """
        data = []
        mdata = []
        pic=''
        with open(file) as f:
            for line in f:
                mdata.append([x for x in line.split()])
        for m in mdata:
            for n in m:
                if n == 'E_KIN':
                    e_ = m[2]
                    e_kin = float(e_[0:-1])
                    # print('E_KIN'+str(e_kin))
                if n == 'G':
                    gr = m[2]
                    pic= n + " = "+ gr + " " 
                    gr = float(gr[0:-1])
                    # print('G',gr)
                if n == 'RE':
                    re = m[2]
                    pic += n + " = "+ re[0:-1]+ " " 
                    re = float(re[0:-1])
                    # print('RE',re)
                if n == 'WC':
                    wc = m[2]
                    pic += n + " = "+ wc[0:-1]
                    wc = float(wc[0:-1])
                    # print('wc',wmax)
                if n == 'WM2':
                    wmax2 = m[2]
                    wmax2 = float(wmax2[0:-1])
                    # print('WM2',wmax2)
                if n == 'WSUM':
                    wsum = m[2]
                    wsum = float(wsum[0:-1])
                    print(pic)
        # ['E_KIN', '=', '3.1437451E-04,']
        # wc = wc*wsum/abs(wsum)
        lt=[gr,re,e_kin,wc,wmax2,wsum]
        self.list.append(lt)
        # print(lt) 
        try:
            with open(file) as f:
                for line in f:
                    data.append([float(x) for x in line.split()])
            self.element(data,pic, self.path)
        except ValueError:
            self.element(data,pic, self.path)   
        

    def obxodFile(self,path,level=1):
        """ Обходит все файлы в папке path"""
        # print("Level= ",level,'Conter: ',os.listdir(path) )

        try:
            for i in os.listdir(self.path):
                print(i)
                if os.path.isdir(self.path+'\\'+i):
                    print('Cпускаемся', self.path+'\\'+i)
                    a=self.path+'\\'+i+'\\'+ self.dat
                    if a:
                        print('a = ',a)
                        self.open_read_file(a)
                #     self.obxodFile(self.path+'\\'+i,level+1)
                #     print('Возвращаемся', path)
        except FileNotFoundError:
            pass 
        

    def element(self, data, pic, path):
            """ Делает поэлементный список """    
            text=[]
            for x in data:
                for y in x:
                    text.append(y)
            graph = MakeGraph(text, self.path)
            graph.creat_graph(pic)






lt=[]
path=''

# print(spis)
gr=[]
wc=[]

# path='dir_gr_re'
# p=['Gr=7000','Gr=10000','Gr=15000','Gr=25000','Gr=15000_синий','Gr=25000_синий']
# d=['7092.dat','7092.dat','7092.dat','7092.dat','7092.dat','7092.dat']
# p=['Re=1','Re=4','Re=10']
# d=['7092.dat','7092.dat','7092.dat']
p=['new']
d=['7092.dat']

# Создаем книку
book = xlwt.Workbook('utf8')

for i in range(len(p)):
    graphs = Graphs(p[i],d[i])
    graphs.obxodFile(p[i])
    graphs.graph_draw()

    # Добавляем лист
    sheet = book.add_sheet(p[i])
    graphs.exel(sheet)
# Сохраняем в файл
book.save('значения энергии,ф-ии тока.xls')

# for i in range(len(p)):
#     print(p[i],dat[i])
# [gr,re,e_kin,wmax,wmax2,WSUM]
# print(spis)









