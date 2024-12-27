import webbrowser
from tkinter.filedialog import asksaveasfile
import allel
import myvariant
from tkinter import Tk, Toplevel, messagebox, ttk
from tkinter import *
import csv
import database_interface
from PIL import ImageTk, Image
from urllib.request import urlopen
import ast
import os

intervar_list = []
pvs1_list = []
ps1_list = []
ps2_list = []
ps3_list = []
ps4_list = []
pm1_list = []
pm2_list = []
pm3_list = []
pm4_list = []
pm5_list = []
pm6_list = []
pp1_list = []
pp2_list = []
pp3_list = []
pp4_list = []
pp5_list = []
ba1_list = []
bp1_list = []
bp2_list = []
bp3_list = []
bp4_list = []
bp5_list = []
bp6_list = []
bp7_list = []
bs1_list = []
bs2_list = []
bs3_list = []
bs4_list = []
searchId = []


def main():
    main_window = Tk()
    app = info(main_window, '')
    main_window.mainloop()


class info:
    def __init__(self, root, f):
        search_id = f.get_id()
        searchId.append(search_id)
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
        title = Label(frame1, text="VCESS Retrieving Data from InterVar",
                      font=("Times New Roman", 16, "bold", "italic"),
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
        prog = 20

        progress['value'] = prog

        self.root1.update_idletasks()

        # time.sleep(0.1)
        self.root1.after(100)  # Delay in millisecs.
        prog = prog+ 40

        link = "http://wintervar.wglab.org/api_new.php?queryType=position&chr=" + str(f.get_chr()) + "&pos=" + str(
            f.get_pos()) + "&ref=" + str(f.get_ref()) + "&alt=" + str(f.get_alt())

        try:
            page = urlopen(link)
            html_bytes = page.read()
            (html_bytes)

            html = html_bytes.decode("utf-8")

            (f"html is:{html}")

            if html == "":

                self.intervar = '.'
                pvs1 = '.'
                ps1 = '.'
                ps2 = '.'
                ps3 = '.'
                ps4 = '.'
                pm1 = '.'
                pm2 = '.'
                pm3 = '.'
                pm4 = '.'
                pm5 = '.'
                pm6 = '.'
                pp1 = '.'
                pp2 = '.'
                pp3 = '.'
                pp4 = '.'
                pp5 = '.'
                ba1 = '.'
                bp1 = '.'
                bp2 = '.'
                bp3 = '.'
                bp4 = '.'
                bp5 = '.'
                bp6 = '.'
                bp7 = '.'
                bs1 = '.'
                bs2 = '.'
                bs3 = '.'
                bs4 = '.'

            else:



               try:
                    index=html.index('}')
                    html=html[:index+1]
                    data = ast.literal_eval(html)

                    (data)
                    if data.get("Intervar"):
                        self.intervar = data['Intervar']
                    else:
                        self.intervar = '.'

                    if data.get("PVS1"):
                        pvs1 = data['PVS1']
                    else:
                        pvs1 = 0

                    if data.get("PS1"):
                        ps1 = data["PS1"]
                    else:
                        ps1 = 0

                    if data.get("PS2"):
                        ps2 = data["PS2"]
                    else:
                        ps2 = 0

                    if data.get("PS3"):
                        ps3 = data["PS3"]
                    else:
                        ps3 = 0

                    if data.get("PS4"):
                        ps4 = data["PS4"]
                    else:
                        ps4 = 0

                    if data.get('PM1'):
                        pm1 = data['PM1']
                    else:
                        pm1 = 0

                    if data.get('PM2'):
                        pm2 = data['PM2']
                    else:
                        pm2 = 0

                    if data.get('PM3'):
                        pm3 = data['PM3']
                    else:
                        pm3 = 0

                    if data.get('PM4'):
                        pm4 = data['PM4']
                    else:
                        pm4 = 0

                    if data.get('PM5'):
                        pm5 = data['PM5']
                    else:
                        pm5 = 0

                    if data.get('PM6'):
                        pm6 = data['PM6']
                    else:
                        pm6 = 0

                    if data.get('PP1'):
                        pp1 = data['PP1']
                    else:
                        pp1 = 0

                    if data.get('PP2'):
                        pp2 = data['PP2']
                    else:
                        pp2 = 0

                    if data.get('PP3'):
                        pp3 = data['PP3']
                    else:
                        pp3 = 0

                    if data.get('PP4'):
                        pp4 = data['PP4']
                    else:
                        pp4 = 0

                    if data.get('PP5'):
                        pp5 = data['PP5']
                    else:
                        pp5 = 0

                    if data.get('BA1'):
                        ba1 = data['BA1']
                    else:
                        ba1 = 0

                    if data.get('BP1'):
                        bp1 = data['BP1']
                    else:
                        bp1 = 0

                    if data.get('BP2'):
                        bp2 = data['BP2']
                    else:
                        bp2 = 0

                    if data.get('BP3'):
                        bp3 = data['BP3']
                    else:
                        bp3 = 0

                    if data.get('BP4'):
                        bp4 = data['BP4']
                    else:
                        bp4 = 0

                    if data.get('BP5'):
                        bp5 = data['BP5']
                    else:
                        bp5 = 0

                    if data.get('BP6'):
                        bp6 = data['BP6']
                    else:
                        bp6 = 0

                    if data.get('BP7'):
                        bp7 = data['BP7']
                    else:
                        bp7 = 0

                    if data.get('BS1'):
                        bs1 = data['BS1']
                    else:
                        bs1 = 0

                    if data.get('BS2'):
                        bs2 = data['BS2']
                    else:
                        bs2 = 0

                    if data.get('BS3'):
                        bs3 = data['BS3']
                    else:
                        bs3 = 0

                    if data.get('BS4'):
                        bs4 = data['BS4']
                    else:
                        bs4 = 0
               except Exception as es:

                self.intervar = '.'
                pvs1 = '.'
                ps1 = '.'
                ps2 = '.'
                ps3 = '.'
                ps4 = '.'
                pm1 = '.'
                pm2 = '.'
                pm3 = '.'
                pm4 = '.'
                pm5 = '.'
                pm6 = '.'
                pp1 = '.'
                pp2 = '.'
                pp3 = '.'
                pp4 = '.'
                pp5 = '.'
                ba1 = '.'
                bp1 = '.'
                bp2 = '.'
                bp3 = '.'
                bp4 = '.'
                bp5 = '.'
                bp6 = '.'
                bp7 = '.'
                bs1 = '.'
                bs2 = '.'
                bs3 = '.'
                bs4 = '.'
        except Exception as es:
            self.error_str = es
            (es)

        self.root = root
        self.root.title('VCESS-InterVar')
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
        title = Label(frame1, text="VCESS Retrieving Data from InterVar",
                      font=("Times New Roman", 40, "bold", "italic"),
                      bg='#dacc1f',
                      fg='white')
        title.place(x=380, y=45)
        frame2 = Frame(self.root, bg='orange')
        frame2.place(x=0, y=150, width=width, height=15)

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='White')
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
        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID", font=("Times New Roman", 16, "bold"), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 14, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=95, y=42)

        url = 'https://wintervar.wglab.org/'
        new = 1

        def openweb():
            import webbrowser
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://wintervar.wglab.org/",
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
                                  text=f"InterVar is  a  bioinformatics  software  tool  for  clinical "
                                       f"  interpretation\nof  genetic  variants by the ACMG/AMP  2015"
                                       f"guideline.\nThe  input  to  InterVar  is  an  annotated  file"
                                       f" generated  from  ANNOVAR,\nwhile  the  output of  InterVar  is"
                                       f" the  classification  of  variants  into\n'Benign',  'Likely"
                                       f"benign', 'Uncertain significance', 'Likely pathogenic'"
                                       f"\nand  'Pathogenic'.",
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 225, y=50, width=450, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()

        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)

        try:
            self.html = html

            if self.html == "":
                no_id = Label(self.frametwo, text='No Data available for this ID',
                              font=("Times New Roman", 15, "bold"),
                              bg='white',
                              fg='black')
                no_id.grid(padx=0, pady=0)
                no_id.place(x=60, y=65)

            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################

            table = ttk.Treeview(table1, height="50")  #################

            table['columns'] = ["ID", 'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5',
                                'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5',
                                'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4']
            table.column('#0', width=120, minwidth=105)
            table.column('ID', width=120, minwidth=105)
            table.column('InterVar', width=120, minwidth=105)
            table.column('PVS1', anchor=W, width=120)
            table.column('PS1', anchor=W, width=120)
            table.column('PS2', anchor=W, width=120)
            table.column('PS3', anchor=W, width=120)
            table.column('PS3', anchor=W, width=120)
            table.column('PS4', anchor=W, width=120)
            table.column('PM1', anchor=W, width=120)
            table.column('PM2', anchor=W, width=120)
            table.column('PM3', anchor=W, width=120)
            table.column('PM4', anchor=W, width=120)
            table.column('PM5', anchor=W, width=120)
            table.column('PM6', anchor=W, width=120)
            table.column('PP1', anchor=W, width=120)
            table.column('PP2', anchor=W, width=120)
            table.column('PP3', anchor=W, width=120)
            table.column('PP4', anchor=W, width=120)
            table.column('PP5', anchor=W, width=120)
            table.column('BA1', anchor=W, width=120)
            table.column('BP1', anchor=W, width=120)
            table.column('BP2', anchor=W, width=120)
            table.column('BP3', anchor=W, width=120)
            table.column('BP4', anchor=W, width=120)
            table.column('BP5', anchor=W, width=120)
            table.column('BP6', anchor=W, width=120)
            table.column('BP7', anchor=W, width=120)
            table.column('BS1', anchor=W, width=120)
            table.column('BS2', anchor=W, width=120)
            table.column('BS3', anchor=W, width=120)
            table.column('BS4', anchor=W, width=120)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('ID', text='ID', anchor=W)
            table.heading('InterVar', text='InterVar', anchor=W)
            table.heading('PVS1', text='PVS1', anchor=W)
            table.heading('PS1', text='PS1', anchor=W)
            table.heading('PS2', text='PS2', anchor=W)
            table.heading('PS3', text='PS3', anchor=W)
            table.heading('PS4', text='PS4', anchor=W)
            table.heading('PM1', text='PM1', anchor=W)
            table.heading('PM2', text='PM2', anchor=W)
            table.heading('PM3', text='PM3', anchor=W)
            table.heading('PM4', text='PM4', anchor=W)
            table.heading('PM5', text='PM5', anchor=W)
            table.heading('PM6', text='PM6', anchor=W)
            table.heading('PP1', text='PP1', anchor=W)
            table.heading('PP2', text='PP2', anchor=W)
            table.heading('PP3', text='PP3', anchor=W)
            table.heading('PP4', text='PP4', anchor=W)
            table.heading('PP5', text='PP5', anchor=W)
            table.heading('BA1', text='BA1', anchor=W)
            table.heading('BP1', text='BP1', anchor=W)
            table.heading('BP2', text='BP2', anchor=W)
            table.heading('BP3', text='BP3', anchor=W)
            table.heading('BP4', text='BP4', anchor=W)
            table.heading('BP5', text='BP5', anchor=W)
            table.heading('BP6', text='BP6', anchor=W)
            table.heading('BP7', text='BP7', anchor=W)
            table.heading('BS1', text='BS1', anchor=W)
            table.heading('BS2', text='BS2', anchor=W)
            table.heading('BS3', text='BS3', anchor=W)
            table.heading('BS4', text='BS4', anchor=W)

            table.insert(parent='', index='end', iid=0, text=0 + 1,
                         values=(search_id,
                                 self.intervar, pvs1, ps1, ps2, ps3, ps4, pm1, pm2, pm3, pm4, pm5, pm6, pp1, pp2, pp3, pp4,
                                 pp5,
                                 ba1,
                                 bp1, bp2, bp3, bp4, bp5, bp6, bp7, bs1, bs2, bs3, bs4))
            table.place(x=0, y=0)

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
            (es)
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


        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()



class info2:
    def __init__(self, root, f):
        intervar_list.clear()
        pvs1_list.clear()
        ps1_list.clear()
        ps2_list.clear()
        ps3_list.clear()
        ps4_list.clear()
        pm1_list.clear()
        pm2_list.clear()
        pm3_list.clear()
        pm4_list.clear()
        pm5_list.clear()
        pm6_list.clear()
        pp1_list.clear()
        pp2_list.clear()
        pp3_list.clear()
        pp4_list.clear()
        pp5_list.clear()
        ba1_list.clear()
        bp1_list.clear()
        bp2_list.clear()
        bp3_list.clear()
        bp4_list.clear()
        bp5_list.clear()
        bp6_list.clear()
        bp7_list.clear()
        bs1_list.clear()
        bs2_list.clear()
        bs3_list.clear()
        bs4_list.clear()
        searchId.clear()

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
        title = Label(frame1, text="VCESS Retrieving Data from InterVar", font=("Times New Roman", 16, "bold", "italic"),
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
        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)

        try:
             for id in vcf:

                searchId.append(id)
                index_id=searchId.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                progress['value'] = i

                self.root1.update_idletasks()

                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                i = i + 40

                if '>' in id:
                    chr = id[0:id.index(':'):]
                    chr = chr.replace('chr', '')

                    pos = id[id.index('.') + 1:]
                    ref = pos
                    x = [i for i in pos if ord(i) < 48 or ord(i) > 57]
                    pos_index = pos.index(x[0])
                    pos = pos[:pos_index]

                    ref = ref[pos_index:ref.index('>')]

                    alt = id[id.index('>') + 1:]

                    link = "http://wintervar.wglab.org/api_new.php?queryType=position&chr=" + str(
                        chr) + "&pos=" + str(
                        pos) + "&ref=" + str(ref) + "&alt=" + str(alt)

                    (link)

                    page = urlopen(link)
                    html_bytes = page.read()
                    (f"html_bytes{html_bytes}")

                    html = html_bytes.decode("utf-8")
                    (f"htmlllllllllllllllllllllllllllllllllllll{html}")
                    if html == "":
                        # searchId.append(ID)
                        intervar_list.append('.')
                        pvs1_list.append('.')
                        ps1_list.append('.')
                        ps2_list.append('.')
                        ps3_list.append('.')
                        ps4_list.append('.')
                        pm1_list.append('.')
                        pm2_list.append('.')
                        pm3_list.append('.')
                        pm4_list.append('.')
                        pm5_list.append('.')
                        pm6_list.append('.')
                        pp1_list.append('.')
                        pp2_list.append('.')
                        pp3_list.append('.')
                        pp4_list.append('.')
                        pp5_list.append('.')
                        ba1_list.append('.')
                        bp1_list.append('.')
                        bp2_list.append('.')
                        bp3_list.append('.')
                        bp4_list.append('.')
                        bp5_list.append('.')
                        bp6_list.append('.')
                        bp7_list.append('.')
                        bs1_list.append('.')
                        bs2_list.append('.')
                        bs3_list.append('.')
                        bs4_list.append('.')

                    else:
                        # searchId.append(ID)

                        try:
                            index=html.index('}')
                            html=html[:index+1]
                            data = ast.literal_eval(html)
                            ("data", data)
                            if data.get("Intervar"):

                                self.intervar = data['Intervar']
                            else:
                                self.intervar = '.'

                            if data.get("PVS1"):
                                pvs1 = data['PVS1']
                            else:
                                pvs1 = 0

                            if data.get("PS1"):
                                ps1 = data["PS1"]
                            else:
                                ps1 = 0

                            if data.get("PS2"):
                                ps2 = data["PS2"]
                            else:
                                ps2 = 0

                            if data.get("PS3"):
                                ps3 = data["PS3"]
                            else:
                                ps3 = 0

                            if data.get("PS4"):
                                ps4 = data["PS4"]
                            else:
                                ps4 = 0

                            if data.get('PM1'):
                                pm1 = data['PM1']
                            else:
                                pm1 = 0

                            if data.get('PM2'):
                                pm2 = data['PM2']
                            else:
                                pm2 = 0

                            if data.get('PM3'):
                                pm3 = data['PM3']
                            else:
                                pm3 = 0

                            if data.get('PM4'):
                                pm4 = data['PM4']
                            else:
                                pm4 = 0

                            if data.get('PM5'):
                                pm5 = data['PM5']
                            else:
                                pm5 = 0

                            if data.get('PM6'):
                                pm6 = data['PM6']
                            else:
                                pm6 = 0

                            if data.get('PP1'):
                                pp1 = data['PP1']
                            else:
                                pp1 = 0

                            if data.get('PP2'):
                                pp2 = data['PP2']
                            else:
                                pp2 = 0

                            if data.get('PP3'):
                                pp3 = data['PP3']
                            else:
                                pp3 = 0

                            if data.get('PP4'):
                                pp4 = data['PP4']
                            else:
                                pp4 = 0

                            if data.get('PP5'):
                                pp5 = data['PP5']
                            else:
                                pp5 = 0

                            if data.get('BA1'):
                                ba1 = data['BA1']
                            else:
                                ba1 = 0

                            if data.get('BP1'):
                                bp1 = data['BP1']
                            else:
                                bp1 = 0

                            if data.get('BP2'):
                                bp2 = data['BP2']
                            else:
                                bp2 = 0

                            if data.get('BP3'):
                                bp3 = data['BP3']
                            else:
                                bp3 = 0

                            if data.get('BP4'):
                                bp4 = data['BP4']
                            else:
                                bp4 = 0

                            if data.get('BP5'):
                                bp5 = data['BP5']
                            else:
                                bp5 = 0

                            if data.get('BP6'):
                                bp6 = data['BP6']
                            else:
                                bp6 = 0

                            if data.get('BP7'):
                                bp7 = data['BP7']
                            else:
                                bp7 = 0

                            if data.get('BS1'):
                                bs1 = data['BS1']
                            else:
                                bs1 = 0

                            if data.get('BS2'):
                                bs2 = data['BS2']
                            else:
                                bs2 = 0

                            if data.get('BS3'):
                                bs3 = data['BS3']
                            else:
                                bs3 = 0

                            if data.get('BS4'):
                                bs4 = data['BS4']
                            else:
                                bs4 = 0
                            # searchId.append(ID)
                            intervar_list.append(self.intervar)
                            pvs1_list.append(pvs1)
                            ps1_list.append(ps1)
                            ps2_list.append(ps2)
                            ps3_list.append(ps3)
                            ps4_list.append(ps4)
                            pm1_list.append(pm1)
                            pm2_list.append(pm2)
                            pm3_list.append(pm3)
                            pm4_list.append(pm4)
                            pm5_list.append(pm5)
                            pm6_list.append(pm6)
                            pp1_list.append(pp1)
                            pp2_list.append(pp2)
                            pp3_list.append(pp3)
                            pp4_list.append(pp4)
                            pp5_list.append(pp5)
                            ba1_list.append(ba1)
                            bp1_list.append(bp1)
                            bp2_list.append(bp2)
                            bp3_list.append(bp3)
                            bp4_list.append(bp4)
                            bp5_list.append(bp5)
                            bp6_list.append(bp6)
                            bp7_list.append(bp7)
                            bs1_list.append(bs1)
                            bs2_list.append(bs2)
                            bs3_list.append(bs3)
                            bs4_list.append(bs4)
                        except Exception as es:
                            intervar_list.append('.')
                            pvs1_list.append('.')
                            ps1_list.append('.')
                            ps2_list.append('.')
                            ps3_list.append('.')
                            ps4_list.append('.')
                            pm1_list.append('.')
                            pm2_list.append('.')
                            pm3_list.append('.')
                            pm4_list.append('.')
                            pm5_list.append('.')
                            pm6_list.append('.')
                            pp1_list.append('.')
                            pp2_list.append('.')
                            pp3_list.append('.')
                            pp4_list.append('.')
                            pp5_list.append('.')
                            ba1_list.append('.')
                            bp1_list.append('.')
                            bp2_list.append('.')
                            bp3_list.append('.')
                            bp4_list.append('.')
                            bp5_list.append('.')
                            bp6_list.append('.')
                            bp7_list.append('.')
                            bs1_list.append('.')
                            bs2_list.append('.')
                            bs3_list.append('.')
                            bs4_list.append('.')
                else:
                    intervar_list.append('.')
                    pvs1_list.append('.')
                    ps1_list.append('.')
                    ps2_list.append('.')
                    ps3_list.append('.')
                    ps4_list.append('.')
                    pm1_list.append('.')
                    pm2_list.append('.')
                    pm3_list.append('.')
                    pm4_list.append('.')
                    pm5_list.append('.')
                    pm6_list.append('.')
                    pp1_list.append('.')
                    pp2_list.append('.')
                    pp3_list.append('.')
                    pp4_list.append('.')
                    pp5_list.append('.')
                    ba1_list.append('.')
                    bp1_list.append('.')
                    bp2_list.append('.')
                    bp3_list.append('.')
                    bp4_list.append('.')
                    bp5_list.append('.')
                    bp6_list.append('.')
                    bp7_list.append('.')
                    bs1_list.append('.')
                    bs2_list.append('.')
                    bs3_list.append('.')
                    bs4_list.append('.')


        except Exception as es:
            (es)
            self.error_str = es

        self.root = root
        self.root.title('Intervar')
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
        frame1 = Frame(self.root, bg='#7877a5')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from Intervar",
                      font=("Times New Roman", 40, "bold", "italic"),
                      bg='#7877a5',
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

        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#dacc1f', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='light grey')
        url = 'https://wintervar.wglab.org/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://wintervar.wglab.org/",
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
        ###############################################################################################
        text = canvas.create_text(0, -2000,
                                  text=f"InterVar is  a  bioinformatics  software  tool  for  clinical "
                                       f"  interpretation\nof  genetic  variants by the ACMG/AMP  2015"
                                       f"guideline.\nThe  input  to  InterVar  is  an  annotated  file"
                                       f" generated  from  ANNOVAR,\nwhile  the  output of  InterVar  is"
                                       f" the  classification  of  variants  into\n'Benign',  'Likely"
                                       f"benign', 'Uncertain significance', 'Likely pathogenic'"
                                       f"\nand  'Pathogenic'.",
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.grid(padx=0, pady=0)

        canvas.place(x=int(width / 2) - 375, y=50, width=900, height=200)

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
        idz_p= Label(self.frametwo, text=' '+str(len(intervar_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if (len(intervar_list)) == (len(searchId)):

                table1 = LabelFrame(self.frametwo, text="Retreived Data")  ################
                table1.grid(padx=50, pady=300)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4',
                                    'PM5',
                                    'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4',
                                    'BP5',
                                    'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4']
                table.column('#0', width=120, minwidth=105)
                table.column('ID', width=120, minwidth=105)
                table.column('InterVar', anchor=W, minwidth=105)
                table.column('PVS1', anchor=W, width=120)
                table.column('PS1', anchor=W, width=120)
                table.column('PS2', anchor=W, width=120)
                table.column('PS3', anchor=W, width=120)
                table.column('PS3', anchor=W, width=120)
                table.column('PS4', anchor=W, width=120)
                table.column('PM1', anchor=W, width=120)
                table.column('PM2', anchor=W, width=120)
                table.column('PM3', anchor=W, width=120)
                table.column('PM4', anchor=W, width=120)
                table.column('PM5', anchor=W, width=120)
                table.column('PM6', anchor=W, width=120)
                table.column('PP1', anchor=W, width=120)
                table.column('PP2', anchor=W, width=120)
                table.column('PP3', anchor=W, width=120)
                table.column('PP4', anchor=W, width=120)
                table.column('PP5', anchor=W, width=120)
                table.column('BA1', anchor=W, width=120)
                table.column('BP1', anchor=W, width=120)
                table.column('BP2', anchor=W, width=120)
                table.column('BP3', anchor=W, width=120)
                table.column('BP4', anchor=W, width=120)
                table.column('BP5', anchor=W, width=120)
                table.column('BP6', anchor=W, width=120)
                table.column('BP7', anchor=W, width=120)
                table.column('BS1', anchor=W, width=120)
                table.column('BS2', anchor=W, width=120)
                table.column('BS3', anchor=W, width=120)
                table.column('BS4', anchor=W, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('InterVar', text='InterVar', anchor=W)
                table.heading('PVS1', text='PVS1', anchor=W)
                table.heading('PS1', text='PS1', anchor=W)
                table.heading('PS2', text='PS2', anchor=W)
                table.heading('PS3', text='PS3', anchor=W)
                table.heading('PS4', text='PS4', anchor=W)
                table.heading('PM1', text='PM1', anchor=W)
                table.heading('PM2', text='PM2', anchor=W)
                table.heading('PM3', text='PM3', anchor=W)
                table.heading('PM4', text='PM4', anchor=W)
                table.heading('PM5', text='PM5', anchor=W)
                table.heading('PM6', text='PM6', anchor=W)
                table.heading('PP1', text='PP1', anchor=W)
                table.heading('PP2', text='PP2', anchor=W)
                table.heading('PP3', text='PP3', anchor=W)
                table.heading('PP4', text='PP4', anchor=W)
                table.heading('PP5', text='PP5', anchor=W)
                table.heading('BA1', text='BA1', anchor=W)
                table.heading('BP1', text='BP1', anchor=W)
                table.heading('BP2', text='BP2', anchor=W)
                table.heading('BP3', text='BP3', anchor=W)
                table.heading('BP4', text='BP4', anchor=W)
                table.heading('BP5', text='BP5', anchor=W)
                table.heading('BP6', text='BP6', anchor=W)
                table.heading('BP7', text='BP7', anchor=W)
                table.heading('BS1', text='BS1', anchor=W)
                table.heading('BS2', text='BS2', anchor=W)
                table.heading('BS3', text='BS3', anchor=W)
                table.heading('BS4', text='BS4', anchor=W)

                for i in range(len(intervar_list)):
                    (len(intervar_list))
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(searchId[i], intervar_list[i], pvs1_list[i], ps1_list[i], ps2_list[i], ps3_list[i],
                                         ps4_list[i], pm1_list[i], pm2_list[i], pm3_list[i], pm4_list[i],
                                         pm5_list[i], pm6_list[i], pp1_list[i], pp2_list[i], pp3_list[i],
                                         pp4_list[i], pp5_list[i], ba1_list[i], bp1_list[i], bp2_list[i],
                                         bp3_list[i], bp4_list[i], bp5_list[i], bp6_list[i], bp7_list[i],
                                         bs1_list[i], bs2_list[i], bs3_list[i], bs4_list[i]))
                table.place(x=0, y=0)

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

                btn_back = Button(self.frametwo, text='Back', command=self.search_window,
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
            elif (len(intervar_list)) != (len(searchId)) and ((len(intervar_list)) and (len(searchId)))!=0:

                table1 = LabelFrame(self.frametwo, text="Retreived Data")  ################
                table1.grid(padx=50, pady=300)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4',
                                    'PM5',
                                    'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4',
                                    'BP5',
                                    'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4']
                table.column('#0', width=120, minwidth=105)
                table.column('ID', width=120, minwidth=105)
                table.column('InterVar', anchor=W, minwidth=105)
                table.column('PVS1', anchor=W, width=120)
                table.column('PS1', anchor=W, width=120)
                table.column('PS2', anchor=W, width=120)
                table.column('PS3', anchor=W, width=120)
                table.column('PS3', anchor=W, width=120)
                table.column('PS4', anchor=W, width=120)
                table.column('PM1', anchor=W, width=120)
                table.column('PM2', anchor=W, width=120)
                table.column('PM3', anchor=W, width=120)
                table.column('PM4', anchor=W, width=120)
                table.column('PM5', anchor=W, width=120)
                table.column('PM6', anchor=W, width=120)
                table.column('PP1', anchor=W, width=120)
                table.column('PP2', anchor=W, width=120)
                table.column('PP3', anchor=W, width=120)
                table.column('PP4', anchor=W, width=120)
                table.column('PP5', anchor=W, width=120)
                table.column('BA1', anchor=W, width=120)
                table.column('BP1', anchor=W, width=120)
                table.column('BP2', anchor=W, width=120)
                table.column('BP3', anchor=W, width=120)
                table.column('BP4', anchor=W, width=120)
                table.column('BP5', anchor=W, width=120)
                table.column('BP6', anchor=W, width=120)
                table.column('BP7', anchor=W, width=120)
                table.column('BS1', anchor=W, width=120)
                table.column('BS2', anchor=W, width=120)
                table.column('BS3', anchor=W, width=120)
                table.column('BS4', anchor=W, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('InterVar', text='InterVar', anchor=W)
                table.heading('PVS1', text='PVS1', anchor=W)
                table.heading('PS1', text='PS1', anchor=W)
                table.heading('PS2', text='PS2', anchor=W)
                table.heading('PS3', text='PS3', anchor=W)
                table.heading('PS4', text='PS4', anchor=W)
                table.heading('PM1', text='PM1', anchor=W)
                table.heading('PM2', text='PM2', anchor=W)
                table.heading('PM3', text='PM3', anchor=W)
                table.heading('PM4', text='PM4', anchor=W)
                table.heading('PM5', text='PM5', anchor=W)
                table.heading('PM6', text='PM6', anchor=W)
                table.heading('PP1', text='PP1', anchor=W)
                table.heading('PP2', text='PP2', anchor=W)
                table.heading('PP3', text='PP3', anchor=W)
                table.heading('PP4', text='PP4', anchor=W)
                table.heading('PP5', text='PP5', anchor=W)
                table.heading('BA1', text='BA1', anchor=W)
                table.heading('BP1', text='BP1', anchor=W)
                table.heading('BP2', text='BP2', anchor=W)
                table.heading('BP3', text='BP3', anchor=W)
                table.heading('BP4', text='BP4', anchor=W)
                table.heading('BP5', text='BP5', anchor=W)
                table.heading('BP6', text='BP6', anchor=W)
                table.heading('BP7', text='BP7', anchor=W)
                table.heading('BS1', text='BS1', anchor=W)
                table.heading('BS2', text='BS2', anchor=W)
                table.heading('BS3', text='BS3', anchor=W)
                table.heading('BS4', text='BS4', anchor=W)

                for i in range(len(intervar_list)):
                    (len(intervar_list))
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(searchId[i], intervar_list[i], pvs1_list[i], ps1_list[i], ps2_list[i], ps3_list[i],
                                         ps4_list[i], pm1_list[i], pm2_list[i], pm3_list[i], pm4_list[i],
                                         pm5_list[i], pm6_list[i], pp1_list[i], pp2_list[i], pp3_list[i],
                                         pp4_list[i], pp5_list[i], ba1_list[i], bp1_list[i], bp2_list[i],
                                         bp3_list[i], bp4_list[i], bp5_list[i], bp6_list[i], bp7_list[i],
                                         bs1_list[i], bs2_list[i], bs3_list[i], bs4_list[i]))
                table.place(x=0, y=0)

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

                btn_back = Button(self.frametwo, text='Back', command=self.search_window,
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

                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again    ', font=("Times New Roman", 12),
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
        except Exception as es:
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload Values Again    ', font=("Times New Roman", 12),
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
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()

    def get_file(self):
        reverse_file = self.file[::-1]
        # (reverse_file)
        pos = reverse_file.find('/', 0)
        # (pos)
        path = reverse_file[pos + 1:]
        path = path[::-1]
        header=['HGVS_id', 'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5', 'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4']
        data1=[]
        l1 = []

        for i in range(len(intervar_list)):
            data = []
            data.append(searchId[i])
            data.append(intervar_list[i])
            data.append(pvs1_list[i])
            data.append(ps1_list[i])
            data.append(ps2_list[i])
            data.append(ps3_list[i])
            data.append(ps4_list[i])
            data.append(pm1_list[i])
            data.append(pm2_list[i])
            data.append(pm3_list[i])
            data.append(pm4_list[i])
            data.append(pm5_list[i])
            data.append(pm6_list[i])
            data.append(pp1_list[i])
            data.append(pp2_list[i])
            data.append(pp3_list[i])
            data.append(pp4_list[i])
            data.append(pp5_list[i])
            data.append(ba1_list[i])
            data.append(bp1_list[i])
            data.append(bp2_list[i])
            data.append(bp3_list[i])
            data.append(bp4_list[i])
            data.append(bp5_list[i])
            data.append(bp6_list[i])
            data.append(bp7_list[i])
            data.append(bs1_list[i])
            data.append(bs2_list[i])
            data.append(bs3_list[i])
            data.append(bs4_list[i])
            data1.append(data)
        (f"data1{data1}")
        (f"data{data}")
        for row in data1:
            (f"row{row}")

            d1 = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4],
                  header[5]: row[5], header[6]: row[6], header[7]: row[7], header[8]: row[8], header[9]: row[9]
                , header[10]: row[10], header[11]: row[11], header[12]: row[12], header[13]: row[13],
                  header[14]: row[14]
                , header[15]: row[15], header[16]: row[16], header[17]: row[17], header[18]: row[18],
                  header[19]: row[19]
                , header[20]: row[20], header[21]: row[21], header[22]: row[22], header[23]: row[23],
                  header[24]: row[24]
                , header[25]: row[25], header[26]: row[26], header[27]: row[27],header[28]: row[28],header[29]: row[29]
                  }

            l1.append(d1)

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


