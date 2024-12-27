import webbrowser
import allel
import myvariant
from tkinter import Tk, Toplevel, messagebox, ttk
from tkinter import *
import csv
import database_interface
from PIL import ImageTk, Image
from tkinter.filedialog import asksaveasfile
rsid_list = []
id = []
mv = myvariant.MyVariantInfo()


# f = database_interface.database_window


def main():
    main_window = Tk()
    app = info(main_window, '')
    main_window.mainloop()


class info:

    def __init__(self, root, f):
        search_id = f.get_id()
        self.error_str = ''
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)

        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=120, y=60)

        progress = ttk.Progressbar(self.root1, style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        i = 20

        progress['value'] = i

        self.root1.update_idletasks()

        # time.sleep(0.1)
        self.root1.after(100)  # Delay in millisecs.
        i = i + 40

        try:
            m = mv.getvariant(search_id)
            self.m = m
            id.append(search_id)

            if m == None:
                rsid_list.append('.')
            else:
                if m.get('dbsnp'):
                    dbsnp = m['dbsnp']
                    if dbsnp.get('rsid'):
                        rsid = dbsnp['rsid']

                        rsid_list.append(rsid)
                        print(f"rsid:{rsid}")
                    else:
                        rsid_list.append('.')

                else:
                    rsid_list.append('.')

        except Exception as es:
            self.error_str = es


        self.root = root
        self.root.title('dbSNP window')
        self.root.overrideredirect(False)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        # setting window to the center
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        # self.root.geometry('1350x700+0+0')
        # self.root.resizable(width=False, height=False)

        # set window icon
        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        frame1 = Frame(self.root, bg='#dacc1f')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#dacc1f',
                      fg='white')
        title.place(x=380, y=45)
        frame2 = Frame(self.root, bg='orange')
        frame2.place(x=0, y=150, width=width, height=15)

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1, padx=0, pady=0)
        main_frame.place(x=0, y=165, width=width, height=height - 150)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

        self.frametwo = Frame(my_canvas, bg='white')

        my_canvas.create_window((0, 0), window=self.frametwo, anchor='nw')

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')

        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 13, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=95, y=42)
        url = 'https://www.ncbi.nlm.nih.gov/snp/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/snp/",
                     font=("Times New Roman", 14, 'italic'), command=openweb, bg='white', fg='Blue',
                     activeforeground='white', cursor='hand2',
                     activebackground='white', bd=0)
        Btn.grid(padx=0, pady=0)
        Btn.place(x=int(width / 2) - 200, y=20, width=400)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width() // 40
                y1 = canvas.winfo_height()
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", 0, -2)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############
        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)
        text = canvas.create_text(0, -2000,
                                  text=f'dbSNP contains human single nucleotide variations, \n'
                                       f'microsatellites among human and small-scale insertions\n'
                                       f'and deletions along with publication, population frequency,\n'
                                       f'molecular consequence, and genomic and RefSeq mapping \n'
                                       f'information for both common variations and clinical \nmutations.',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 235, y=50, width=470, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        try:

            if self.m == None:

                no_id = Label(self.frametwo, text='No Data available for this ID', font=("Times New Roman", 14, 'bold'),
                              bg='white', fg='black')
                no_id.place(x=60, y=65)


            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
            table = ttk.Treeview(table1, height="50")  #################

            table['columns'] = ['ID', 'rsID']
            table.column('#0', width=200, minwidth=105)
            table.column('ID', width=200, minwidth=105)
            table.column('rsID', anchor=W, width=200)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('ID', text='ID', anchor=W)
            table.heading('rsID', text='rsID', anchor=W)

            for i in range(len(rsid_list)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(id[i], rsid_list[i]))
            table.place(x=0, y=0)  ##########################
            # VERTICAL SCROLLBAR
            yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
            yscrollbar.pack(side=RIGHT, fill='y')  ##################

            # HORIZONTAL SCROLLBAR
            xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
            xscrollbar.pack(side=BOTTOM, fill='x')  #######################

            table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
            table.pack(side=LEFT)
            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=620, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=620, width=100)
        except Exception as es:

            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nEnter values again    ', font=("Times New Roman", 12),
                           bg='white',
                           fg='black')
            error2.grid(padx=0, pady=0)
            error2.place(x=550, y=280)

            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=370, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=370, width=100)


    def exit(self):
        self.root.destroy()

    def search_window(self):
        rsid_list.clear()
        id.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()


class info_hg38:

    def __init__(self, root, f):
        search_id = f.get_id()
        self.error_str = ''
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)

        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=120, y=60)

        progress = ttk.Progressbar(self.root1, style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        i = 20

        progress['value'] = i

        self.root1.update_idletasks()

        # time.sleep(0.1)
        self.root1.after(100)  # Delay in millisecs.
        i = i + 40

        try:
            m = mv.getvariant(search_id, assembly='hg38')
            self.m = m
            id.append(search_id)

            if m == None:
                rsid_list.append('.')
            else:
                if m.get('dbsnp'):
                    dbsnp = m['dbsnp']
                    if dbsnp.get('rsid'):
                        rsid = dbsnp['rsid']

                        rsid_list.append(rsid)
                        print(f"rsid:{rsid}")
                    else:
                        rsid_list.append('.')

                else:
                    rsid_list.append('.')

        except Exception as es:
            self.error_str = es


        self.root = root
        self.root.title('dbSNP window')
        self.root.overrideredirect(False)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        # setting window to the center
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
        # self.root.geometry('1350x700+0+0')
        # self.root.resizable(width=False, height=False)

        # set window icon
        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        frame1 = Frame(self.root, bg='#dacc1f')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#dacc1f',
                      fg='white')
        title.place(x=380, y=45)
        frame2 = Frame(self.root, bg='orange')
        frame2.place(x=0, y=150, width=width, height=15)

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1, padx=0, pady=0)
        main_frame.place(x=0, y=165, width=width, height=height - 150)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

        self.frametwo = Frame(my_canvas, bg='white')

        my_canvas.create_window((0, 0), window=self.frametwo, anchor='nw')

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')

        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 13, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=95, y=42)
        url = 'https://www.ncbi.nlm.nih.gov/snp/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/snp/",
                     font=("Times New Roman", 14, 'italic'), command=openweb, bg='white', fg='Blue',
                     activeforeground='white', cursor='hand2',
                     activebackground='white', bd=0)
        Btn.grid(padx=0, pady=0)
        Btn.place(x=int(width / 2) - 200, y=20, width=400)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width() // 40
                y1 = canvas.winfo_height()
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", 0, -2)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############
        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)
        text = canvas.create_text(0, -2000,
                                  text=f'dbSNP contains human single nucleotide variations, \n'
                                       f'microsatellites among human and small-scale insertions\n'
                                       f'and deletions along with publication, population frequency,\n'
                                       f'molecular consequence, and genomic and RefSeq mapping \n'
                                       f'information for both common variations and clinical \nmutations.',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 235, y=50, width=470, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        try:

            if self.m == None:

                no_id = Label(self.frametwo, text='No Data available for this ID', font=("Times New Roman", 14, 'bold'),
                              bg='white', fg='black')
                no_id.place(x=60, y=65)


            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG38)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
            table = ttk.Treeview(table1, height="50")  #################

            table['columns'] = ['ID', 'rsID']
            table.column('#0', width=200, minwidth=105)
            table.column('ID', width=200, minwidth=105)
            table.column('rsID', anchor=W, width=200)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('ID', text='ID', anchor=W)
            table.heading('rsID', text='rsID', anchor=W)

            for i in range(len(rsid_list)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(id[i], rsid_list[i]))
            table.place(x=0, y=0)  ##########################
            # VERTICAL SCROLLBAR
            yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
            yscrollbar.pack(side=RIGHT, fill='y')  ##################

            # HORIZONTAL SCROLLBAR
            xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
            xscrollbar.pack(side=BOTTOM, fill='x')  #######################

            table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
            table.pack(side=LEFT)
            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=620, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=620, width=100)
        except Exception as es:

            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nEnter values again    ', font=("Times New Roman", 12),
                           bg='white',
                           fg='black')
            error2.grid(padx=0, pady=0)
            error2.place(x=550, y=280)

            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=370, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=370, width=100)


    def exit(self):
        self.root.destroy()

    def search_window(self):
        rsid_list.clear()
        id.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()



class info2:
    def __init__(self, root, f):
        self.error_str = ''


        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)




        ##############################################################################
        ##################################################
        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)
        progress = ttk.Progressbar(self.root1, style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        i = 20


        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=120, y=60)


        try:
            for Id in vcf:
                id.append(Id)
                index_id=id.index(Id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                progress['value'] = i
                self.root1.update_idletasks()

                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                i = i + 40

                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(Id)
                print(Id)

                if m == None:
                    rsid_list.append('.')


                else:
                    if m.get('dbsnp'):
                        dbsnp = m['dbsnp']

                        if dbsnp.get('rsid'):
                            rsid = dbsnp['rsid']

                            rsid_list.append(rsid)

                            print(f"rsid:{rsid}")
                        else:
                            rsid_list.append('.')

                    else:
                        rsid_list.append('.')


        except Exception as es:
            self.error_str = es

        self.root = root
        self.root.title('dbSNP window')
        self.root.overrideredirect(False)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        # self.root.geometry('1350x700+0+0')
        # self.root.resizable(width=False, height=False)





        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        Frame1 = Frame(self.root, bg='#cb525d')
        Frame1.place(x=0, y=0, width=width, height=150)
        title = Label(Frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#cb525d',
                      fg='white')
        title.place(x=380, y=45)
        frame2 = Frame(self.root, bg='orange')
        frame2.place(x=0, y=150, width=width, height=15)

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1, padx=0, pady=0)
        main_frame.place(x=0, y=165, width=width, height=height - 150)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

        self.frametwo = Frame(my_canvas, bg='white')

        my_canvas.create_window((0, 0), window=self.frametwo, anchor='nw')

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)
        self.root.configure(background='White')
        url = 'https://www.ncbi.nlm.nih.gov/snp/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/snp/",
                     font=("Times New Roman", 14, 'italic'), command=openweb, bg='white', fg='Blue',
                     activeforeground='white', cursor='hand2',
                     activebackground='white', bd=0)
        Btn.grid(padx=0, pady=0)
        Btn.place(x=int(width / 2) - 200, y=20, width=400)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width() // 40
                y1 = canvas.winfo_height()
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", 0, -2)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############
        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)
        text = canvas.create_text(0, -2000,
                                  text=f'dbSNP contains human single nucleotide variations, \n'
                                       f'microsatellites among human and small-scale insertions\n'
                                       f'and deletions along with publication, population frequency,\n'
                                       f'molecular consequence, and genomic and RefSeq mapping \n'
                                       f'information for both common variations and clinical \nmutations.',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 235, y=50, width=470, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(rsid_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(rsid_list) == len(id):
                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID', 'rsID']
                table.column('#0', width=200, minwidth=105)
                table.column('ID', width=200, minwidth=105)
                table.column('rsID', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)

                for i in range(len(rsid_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(id[i], rsid_list[i]))
                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)

                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)

                btn_back = Button(self.frametwo, text='Go Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=600, y=640, width=120)
                btn_exit = Button(self.frametwo, text='Exit', command=self.exit,
                                  font=("Times New Roman", 15, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=730, y=640, width=120)
            ######################################
            elif len(rsid_list) != len(id) and(len(rsid_list) and len(id))!=0:
                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID', 'rsID']
                table.column('#0', width=200, minwidth=105)
                table.column('ID', width=200, minwidth=105)
                table.column('rsID', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)

                for i in range(len(rsid_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(id[i], rsid_list[i]))
                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)


                btn_back = Button(self.frametwo, text='Go Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=600, y=640, width=120)

            ######################################
                btn_exit = Button(self.frametwo, text='Exit', command=self.exit,
                                  font=("Times New Roman", 15, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=730, y=640, width=120)


                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again   ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=600, y=740)

            else:
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=550, y=250)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again    ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=550, y=280)
                btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=660, y=370, width=100)

                btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                                  font=("Times New Roman", 15, 'bold'), bd=3,
                                  relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=780, y=370, width=100)


        except Exception as  es:
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload File Again    ', font=("Times New Roman", 12),
                           bg='white',
                           fg='black')
            error2.grid(padx=0, pady=0)
            error2.place(x=550, y=280)

            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=370, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=370, width=100)




    def exit(self):
        self.root.destroy()

    def search_window(self):
        rsid_list.clear()
        id.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()

    def get_file(self):
        reverse_file = self.file[::-1]
        pos = reverse_file.find('/', 0)
        path = reverse_file[pos + 1:]
        path = path[::-1]
        header = ['HGVS_id', 'rs_ID']
        l1 = []
        data1 = []

        for i in range(len(rsid_list)):
            data = []
            data.append(id[i])
            data.append(rsid_list[i])
            data1.append(data)
        for row in data1:
            print(row)
            d1 = {header[0]: row[0], header[1]: row[1]}
            print(d1)
            l1.append(d1)

        print(l1)
        try:
            EWT = messagebox.askquestion('File Level', 'Would you like to save')
            if EWT == 'yes':
                files = [('CSV File', '*.csv')]
                savefile = asksaveasfile(mode='w',defaultextension=".csv",filetypes = files)
                print(savefile)
                if savefile!= None:
                    with open(savefile.name, "w", newline='') as f1:


                        writer = csv.DictWriter(f1, fieldnames=header)
                        writer.writeheader()
                        for row in l1:
                            writer.writerow(row)
                        messagebox.showinfo("Success", "File saved Successfully", parent=self.root)
                else:
                    messagebox.showerror("Error", "File not saved. Please Try again"
                                         , parent=self.root)




        except Exception as es:
            print(es)
            messagebox.showerror("Error", "File open in other Program"
                                 , parent=self.root)

class info2_hg38:
    def __init__(self, root, f):
        self.error_str = ''

        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)

        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=120, y=60)

        progress = ttk.Progressbar(self.root1, style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)

        i = 20

        ##############################################################################

        ##################################################

        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)

        try:
            for Id in vcf:
                id.append(Id)
                index_id=id.index(Id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                progress['value'] = i

                self.root1.update_idletasks()

                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                i = i + 40
                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(Id, assembly='hg38')
                (Id)

                if m == None:
                    rsid_list.append('.')


                else:
                    if m.get('dbsnp'):
                        dbsnp = m['dbsnp']

                        if dbsnp.get('rsid'):
                            rsid = dbsnp['rsid']

                            rsid_list.append(rsid)

                            (f"rsid:{rsid}")
                        else:
                            rsid_list.append('.')

                    else:
                        rsid_list.append('.')


        except Exception as es:
            self.error_str = es
        self.root = root
        self.root.title('dbSNP window')
        self.root.overrideredirect(False)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        # self.root.geometry('1350x700+0+0')
        # self.root.resizable(width=False, height=False)

        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        Frame1 = Frame(self.root, bg='#cb525d')
        Frame1.place(x=0, y=0, width=width, height=150)
        title = Label(Frame1, text="VCESS Retrieving Data from dbSNP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#cb525d',
                      fg='white')
        title.place(x=380, y=45)
        frame2 = Frame(self.root, bg='orange')
        frame2.place(x=0, y=150, width=width, height=15)

        main_frame = Frame(self.root)
        main_frame.pack(fill=BOTH, expand=1, padx=0, pady=0)
        main_frame.place(x=0, y=165, width=width, height=height - 150)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scroll = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scroll.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scroll.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.config(scrollregion=my_canvas.bbox(ALL)))

        self.frametwo = Frame(my_canvas, bg='white')

        my_canvas.create_window((0, 0), window=self.frametwo, anchor='nw')

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)
        self.root.configure(background='White')
        url = 'https://www.ncbi.nlm.nih.gov/snp/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/snp/",
                     font=("Times New Roman", 14, 'italic'), command=openweb, bg='white', fg='Blue',
                     activeforeground='white', cursor='hand2',
                     activebackground='white', bd=0)
        Btn.grid(padx=0, pady=0)
        Btn.place(x=int(width / 2) - 200, y=20, width=400)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width() // 40
                y1 = canvas.winfo_height()
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", 0, -2)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############
        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)
        text = canvas.create_text(0, -2000,
                                  text=f'dbSNP contains human single nucleotide variations, \n'
                                       f'microsatellites among human and small-scale insertions\n'
                                       f'and deletions along with publication, population frequency,\n'
                                       f'molecular consequence, and genomic and RefSeq mapping \n'
                                       f'information for both common variations and clinical \nmutations.',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 235, y=50, width=470, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(rsid_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)


        try:
            if len(rsid_list) == len(id):
                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID', 'rsID']
                table.column('#0', width=200, minwidth=105)
                table.column('ID', width=200, minwidth=105)
                table.column('rsID', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)

                for i in range(len(rsid_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(id[i], rsid_list[i]))
                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)

                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)

                btn_back = Button(self.frametwo, text='Go Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=600, y=640, width=120)
                btn_exit = Button(self.frametwo, text='Exit', command=self.exit,
                                  font=("Times New Roman", 15, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=730, y=640, width=120)
            ######################################
            elif len(rsid_list) != len(id) and(len(rsid_list) and len(id))!=0:
                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 300, y=180, width=600, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID', 'rsID']
                table.column('#0', width=200, minwidth=105)
                table.column('ID', width=200, minwidth=105)
                table.column('rsID', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)

                for i in range(len(rsid_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(id[i], rsid_list[i]))
                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)


                btn_back = Button(self.frametwo, text='Go Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=600, y=640, width=120)
                btn_exit = Button(self.frametwo, text='Exit', command=self.exit,
                                  font=("Times New Roman", 15, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=730, y=640, width=120)
                ######################################

                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again   ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=600, y=740)


            else:
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=550, y=250)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again    ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=550, y=280)
                btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                                  font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                  cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                  activebackground='#154857')
                btn_back.grid(padx=0, pady=0)
                btn_back.place(x=660, y=370, width=100)

                btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                                  font=("Times New Roman", 15, 'bold'), bd=3,
                                  relief=RIDGE,
                                  cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                                  activebackground='dark red')
                btn_exit.grid(padx=0, pady=0)
                btn_exit.place(x=780, y=370, width=100)


        except Exception as  es:
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload File Again    ', font=("Times New Roman", 12),
                           bg='white',
                           fg='black')
            error2.grid(padx=0, pady=0)
            error2.place(x=550, y=280)

            btn_back = Button(self.frametwo, text='Back', command=self.search_window,
                              font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                              cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                              activebackground='#154857')
            btn_back.grid(padx=0, pady=0)
            btn_back.place(x=660, y=370, width=100)

            btn_exit = Button(self.frametwo, command=self.exit, text='Exit',
                              font=("Times New Roman", 15, 'bold'), bd=3,
                              relief=RIDGE,
                              cursor='hand2', bg='dark red', fg='white', activeforeground='white',
                              activebackground='dark red')
            btn_exit.grid(padx=0, pady=0)
            btn_exit.place(x=780, y=370, width=100)

    def exit(self):
        self.root.destroy()

    def search_window(self):
        rsid_list.clear()
        id.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()

    def get_file(self):
        reverse_file = self.file[::-1]
        pos = reverse_file.find('/', 0)
        path = reverse_file[pos + 1:]
        path = path[::-1]
        header = ['HGVS_id', 'rs_ID']
        l1 = []
        data1 = []

        for i in range(len(rsid_list)):
            data = []
            data.append(id[i])
            data.append(rsid_list[i])
            data1.append(data)
        for row in data1:
            (row)
            d1 = {header[0]: row[0], header[1]: row[1]}
            (d1)
            l1.append(d1)

        (l1)
        try:
            EWT = messagebox.askquestion('File Level', 'Would you like to save')
            if EWT == 'yes':
                files = [('CSV File', '*.csv')]
                savefile = asksaveasfile(mode='w',defaultextension=".csv",filetypes = files)
                (savefile)
                if savefile!= None:
                    with open(savefile.name, "w", newline='') as f1:


                        writer = csv.DictWriter(f1, fieldnames=header)
                        writer.writeheader()
                        for row in l1:
                            writer.writerow(row)
                        messagebox.showinfo("Success", "File saved Successfully", parent=self.root)
                else:
                    messagebox.showerror("Error", "File not saved. Please Try again"
                                         , parent=self.root)
        except Exception as es:
            (es)
            messagebox.showerror("Error", "File open in other Program"
                                 , parent=self.root)

if __name__ == '__main__':
    main()
