from tkinter import *
import numpy as np
import os, sys


class Lgs_guesser():
    def __init__(self) -> None:
        self.root = Tk()
        self.root.title('LGS Guesser')
        self.root.geometry("450x350")
        self.root.resizable(0,0)
        self.frame = Frame(self.root)
        self.frame.pack(side="top", expand=True, fill="both")
        self.years, self.points , self.percentages = extracter('train.csv')
        self.calibrate()
        self.root.mainloop()


    def calibrate(self):
        for widgets in self.frame.winfo_children():
                widgets.destroy()

        # declearing text variables
        self.l19p = StringVar()
        self.l20p = StringVar()
        self.l21p = StringVar()

        # initializing labels for years and entries and button and frame
        l19 = Label(self.frame, text='2019')
        l20 = Label(self.frame, text='2020')
        l21 = Label(self.frame, text='2021')
        self.lre = Label(self.frame, text='')
        e19 = Entry(self.frame, textvariable=self.l19p, width=7, bg="White", borderwidth=2)
        e20 = Entry(self.frame, textvariable=self.l20p, width=8, bg="White", borderwidth=2)
        e21 = Entry(self.frame, textvariable=self.l21p, width=7, bg="White", borderwidth=2)
        b = Button(self.frame, text='Submit', command=self.button_calibrate)
        d = Button(self.frame, text='Done', command=self.calculator_page)
        l19.place(x=50, y=30)
        l20.place(x=200, y=30)
        l21.place(x=350, y=30)
        self.lre.place(x=50, y=180)
        e19.place(x=30, y=60)
        e20.place(x=180, y=60)
        e21.place(x=330, y=60)
        b.place(x=175, y=130)
        d.place(x=180, y=300)

        
    def button_calibrate(self):
        self.lre['text'] = ''
        p19 = float(self.l19p.get()) / 100
        p20 = float(self.l20p.get()) / 100
        p21 = float(self.l21p.get()) / 100

        if p19+p20+p21 == 1:
            p1, p2 = 0, 0
            last_average = 0
            average = []
            average_n = [(500.0, 0.01)]
            size = len(self.years)
            for i in range(size):
                p1 = self.points[i]
                y1 = self.years[i]
                for j in range(i, size):
                    p2 = self.points[j]
                    y2 = self.years[j]
                    if (p1 + 0.5 >= p2 >= p1 - 0.5) and y1 != y2:
                        for k in range(j, size):
                            p3 = self.points[k]
                            y3 = self.years[k]
                            if ((p1 + 0.5 >= p3 >= p1 - 0.5) and (p2 + 0.5 >= p3 >= p2 - 0.5)) and y2 != y3:
                                curr_average = (p19*self.percentages[i] + p20*self.percentages[j] + p21*self.percentages[k])
                                if curr_average > last_average:
                                    average.append(f'{p1} -> {curr_average:.3f}')
                                    average_n.append((p1, curr_average))
                                last_average = curr_average
            average_n.append((193.0, 99.0))
            average_n = np.array(average_n)
            cf = np.polyfit(average_n[:,0],average_n[:,1], 5) # coefficents of the function has been created
            self.f = lambda x: cf[0]*x**5+cf[1]*x**4+cf[2]*x**3+cf[3]*x**2+cf[4]*x+cf[5] # function has been defined
            range_of_sample_data = np.arange(500, 299, -50)
            sample_data = self.f(range_of_sample_data)
            for i in range(len(sample_data)):
                self.lre['text'] += f'A student with a point {range_of_sample_data[i]} is in {sample_data[i]:0.2f} percentile group. \n'
        else:
            self.lre['text'] = 'Please reenter the percentages and be sure that their sum\n          is equal to 100.'
    
    def calculator_page(self):
        self.lre['text'] = ''
        p19 = float(self.l19p.get()) / 100
        p20 = float(self.l20p.get()) / 100
        p21 = float(self.l21p.get()) / 100
        self.button_calibrate()
        if p19+p20+p21 == 1:
            for widgets in self.frame.winfo_children():
                widgets.destroy()
            self.root.geometry('460x340')

            # setting variables for each lectures entry
            self.T_W = StringVar() # turkish
            self.T_E = StringVar() # turkish
            self.I_W = StringVar() # history
            self.I_E = StringVar() # history
            self.R_W = StringVar() # religion
            self.R_E = StringVar() # religion
            self.E_W = StringVar() # english
            self.E_E = StringVar() # english
            self.M_W = StringVar() # math
            self.M_E = StringVar() # math
            self.S_W = StringVar() # science
            self.S_E = StringVar() # science
            self.T_P = StringVar() # total point

            # entries
            t_w = Entry(self.frame, textvariable=self.T_W, width=5, bg="White", borderwidth=2)
            t_e = Entry(self.frame, textvariable=self.T_E, width=5, bg="White", borderwidth=2)
            i_w = Entry(self.frame, textvariable=self.I_W, width=5, bg="White", borderwidth=2)
            i_e = Entry(self.frame, textvariable=self.I_E, width=5, bg="White", borderwidth=2)
            r_w = Entry(self.frame, textvariable=self.R_W, width=5, bg="White", borderwidth=2)
            r_e = Entry(self.frame, textvariable=self.R_E, width=5, bg="White", borderwidth=2)
            e_w = Entry(self.frame, textvariable=self.E_W, width=5, bg="White", borderwidth=2)
            e_e = Entry(self.frame, textvariable=self.E_E, width=5, bg="White", borderwidth=2)
            m_w = Entry(self.frame, textvariable=self.M_W, width=5, bg="White", borderwidth=2)
            m_e = Entry(self.frame, textvariable=self.M_E, width=5, bg="White", borderwidth=2)
            s_w = Entry(self.frame, textvariable=self.S_W, width=5, bg="White", borderwidth=2)
            s_e = Entry(self.frame, textvariable=self.S_E, width=5, bg="White", borderwidth=2)
            t_p = Entry(self.frame, textvariable=self.T_P, width=10, bg="White", borderwidth=2)

            # labels
            lw = Label(self.frame, text='W')
            le = Label(self.frame, text='E')

            llt = Label(self.frame, text='Turkish')
            lli = Label(self.frame, text='Social S.')
            llr = Label(self.frame, text='Religion')
            lle = Label(self.frame, text='English')
            llm = Label(self.frame, text='Mathematic')
            lls = Label(self.frame, text='Science')

            lts = Label(self.frame, text='Total Score')
            self.lresult =Label(self.frame, text='Your percentage is ')

            # button
            b_show = Button(self.frame, text='Show', command=self.result)
            b_recalibrate = Button(self.frame, text='Recalibrate', command=self.calibrate)

            # placements
            lw.place(x=130,y=40)
            le.place(x=190,y=40)
            llt.place(x=30, y=60)
            lli.place(x=30, y=90)
            llr.place(x=30, y=120)
            lle.place(x=30, y=150)
            llm.place(x=30, y=180)
            lls.place(x=30, y=210)
            lts.place(x=320, y=60)
            self.lresult.place(x=35, y=260)

            t_w.place(x=110, y=60)
            i_w.place(x=110, y=90)
            r_w.place(x=110, y=120)
            e_w.place(x=110, y=150)
            m_w.place(x=110, y=180)
            s_w.place(x=110, y=210)
            t_e.place(x=170, y=60)
            i_e.place(x=170, y=90)
            r_e.place(x=170, y=120)
            e_e.place(x=170, y=150)
            m_e.place(x=170, y=180)
            s_e.place(x=170, y=210)
            t_p.place(x=300, y=90)

            b_show.place(x=315, y=125)
            b_recalibrate.place(x=300, y=155)


        else:
            self.lre['text'] = 'Please make sure that you have done yearly distributions correctly.'
        
    def result(self):
        t_w = self.T_W.get()
        t_e = self.T_E.get()
        i_w = self.I_W.get()
        i_e = self.I_E.get()
        r_w = self.R_W.get()
        r_e = self.R_E.get()
        e_w = self.E_W.get()
        e_e = self.E_E.get()
        m_w = self.M_W.get()
        m_e = self.M_E.get()
        s_w = self.S_W.get()
        s_e = self.S_E.get()
        t_p = self.T_P.get()
        total_point = 0

        if (t_w!='' and t_e!='' and i_w!='' and i_e!='' and r_w!='' and r_e!='' and e_w!='' and e_e!='' and m_w!='' and m_e!='' and s_w!='' and s_e!=''):
            total_point = 200.004394 + 3.44603333*(20-float(t_w)*1.33-float(t_e)) + 1.47508889*(10-float(i_w)*1.33-float(t_e)) + 1.59244444*(10-float(r_w)*1.33-float(r_e)) + 1.33975278*(10-float(e_w)*1.33-float(e_e)) + 5.78783333*(20-float(m_w)*1.33-float(m_e)) + 3.56228333*(20-float(s_w)*1.33-float(s_e))
        elif (t_p != ''):
            total_point = float(t_p)
        else:
            self.lresult['text'] = 'Come on man check your inputs :/'
        if 193 < total_point < 505:
            self.lresult['text'] = f'Your total point is {total_point:0.2f}, approximate percentage is {self.f(total_point):0.2f}'
        else:
            self.lresult['text'] = 'Come on man check your inputs :/'

        self.T_W.set('')
        self.T_E.set('')
        self.I_W.set('')
        self.I_E.set('')
        self.R_W.set('')
        self.R_E.set('')
        self.E_W.set('')
        self.E_E.set('')
        self.M_W.set('')
        self.M_E.set('')
        self.S_W.set('')
        self.S_E.set('')
        self.T_P.set('')



        

def extracter(name):
    new_file = open(name, 'r')
    difficulty, total_points, percentage = [], [], []
    new_file.readline()
    for line in new_file:
        line = line.split(',')
        line[-1] = line[-1].strip()
        difficulty.append(line[0])
        total_points.append(float(line[1]))
        percentage.append(float(line[2]))
    return difficulty, total_points ,percentage
    
if __name__=='__main__':
    guesser = Lgs_guesser()