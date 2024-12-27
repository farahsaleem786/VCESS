import csv
import time
import webbrowser
from tkinter import *
from tkinter import messagebox, ttk
import allel
import myvariant
from PIL import ImageTk, Image
import database_interface
from tkinter.filedialog import asksaveasfile
Id = []
variant_id_list = []
variant_type_list = []
allele_id_list = []
cytoband_list = []
clin_interpretation_list = []
clin_condition_list = []
allelic_origin_list = []
review_status_list = []
identifier_list = []

mv = myvariant.MyVariantInfo()


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
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 16, "bold", "italic"),
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


            self.m = mv.getvariant(search_id)
            m = self.m
            Id.append(search_id)

            if m == None:

                variant_id_list.append('.')
                variant_type_list.append('.')

                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')

            else:

                if m.get('clinvar'):
                    # print(f"{i} : {m[i]}")
                    clinvar = m['clinvar']
                    print(clinvar)

                    if clinvar.get('variant_id'):
                        variant_id = clinvar['variant_id']
                    else:
                        variant_id = '.'
                    variant_id_list.append(variant_id)

                    print(f"Variant ID : {variant_id}")

                    if clinvar.get('type'):
                        clintype = clinvar['type']
                    else:
                        clintype = '.'
                    variant_type_list.append(clintype)
                    print(f"Type : {clintype}")

                    if clinvar.get('allele_id'):
                        allele_id = clinvar['allele_id']
                    else:
                        allele_id = '.'
                    allele_id_list.append(allele_id)
                    print(f"Allele ID : {allele_id}")

                    if clinvar.get('cytogenic'):
                        cytoband = clinvar['cytogenic']
                    else:
                        cytoband = '.'
                    cytoband_list.append(cytoband)
                    print(f"Cytogenic location : {cytoband}")

                    if clinvar.get('rcv'):

                        if type(clinvar['rcv']) == list:
                            if clinvar['rcv'][0].get('clinical_significance'):
                                clinical_significance = clinvar['rcv'][0]['clinical_significance']
                            else:
                                clinical_significance = '.'


                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv'][0]['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv'][0]['conditions']) == list:
                                    if clinvar['rcv'][0]['conditions'][0].get('name'):
                                        clinical_condition = clinvar['rcv'][0]['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'][0].get('origin'):
                                allelic_origin = clinvar['rcv'][0]['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'][0].get('review_status'):
                                review_status = clinvar['rcv'][0]['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('identifiers'):
                                        ident = clinvar['rcv'][0]['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv'][0]['conditions']) == list:

                                    if clinvar['rcv'][0]['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv'][0]['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'
                        else:
                            if clinvar['rcv'].get('clinical_significance'):
                                clinical_significance = clinvar['rcv']['clinical_significance']
                            else:
                                clinical_significance = '.'

                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv']['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv']['conditions']) == list:
                                    if clinvar['rcv']['conditions'][0].get('name'):
                                        clinical_condition =clinvar['rcv']['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'].get('origin'):
                                allelic_origin = clinvar['rcv']['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'].get('review_status'):
                                review_status = clinvar['rcv']['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('identifiers'):
                                        ident = clinvar['rcv']['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv']['conditions']) == list:

                                    if clinvar['rcv']['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv']['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'

                    clin_interpretation_list.append(clinical_significance)
                    clin_condition_list.append(clinical_condition)
                    allelic_origin_list.append(allelic_origin)
                    review_status_list.append(review_status)
                    identifier_list.append(identifier)
                    print(f"Clinvar Interpretation : {clinical_significance}")
                    print(f"Clinvar Condition : {clinical_condition}")
                    print(f"Clinvar Allelic Origin : {allelic_origin}")
                    print(f"Clinvar Review Status : {review_status}")
                    print(f"Clinvar identifier : {identifier}")

                else:
                    variant_id_list.append('.')
                    variant_type_list.append('.')
                    allele_id_list.append('.')
                    cytoband_list.append('.')
                    clin_interpretation_list.append('.')
                    clin_condition_list.append('.')
                    allelic_origin_list.append('.')
                    review_status_list.append('.')
                    identifier_list.append('.')

        except Exception as es:
            self.error_str = es




        self.root = root
        self.root.title('VCESS-ClinVar')
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
        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        frame1 = Frame(self.root, bg='#7877a5')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 40, "bold", "italic"),
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='white', borderwidth=0)
        lblimg1.place(x=80, y=15, width=250, height=130)

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

        url = 'https://www.ncbi.nlm.nih.gov/clinvar/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/clinvar/",
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
                                  text=f'ClinVar is a freely accessible, public archive of reports of the relationships'
                                       f'among human \ngenetic variations and phenotypes, with supporting evidence. '
                                       f'Essentially, this means \nit’s an archive of variants associated with a gene.'
                                       f'Variants are submitted typically by \nmajor diagnosing laboratories and '
                                       f'research centers. Variants are classified as \npathogenic (disease causing),'
                                       f'benign (not disease causing), and unknown significance (not \nenough evidence'
                                       f'to show the variant is disease causing or not).',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 375, y=50, width=750, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()

        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)

        try:
            # m = mv.getvariant(search_id)

            if self.m == None:
                no_id = Label(self.frametwo, text='No Data available for this ID',
                              font=("Times New Roman", 15, "bold"),
                              bg='white',
                              fg='black')
                no_id.grid(padx=0, pady=0)
                no_id.place(x=60, y=65)

            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
            table = ttk.Treeview(table1, height="50")  #################

            table['columns'] = ["Searched_ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                'Clinical_Condition',
                                'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
            table.column('#0', width=120, minwidth=25)
            table.column('Searched_ID', anchor=W, width=120)
            table.column('Variant_ID', anchor=W, width=120)
            table.column('Clinical_Type', anchor=CENTER, width=120)
            table.column('Allelic_ID', anchor=CENTER, width=120)
            table.column('Clinical_Significance', anchor=CENTER, width=120)
            table.column('Clinical_Condition', anchor=CENTER, width=120)
            table.column('Allelic_Origin', anchor=CENTER, width=120)
            table.column('Review_Status', anchor=CENTER, width=120)
            table.column('Clinical_identifier', anchor=CENTER, width=120)
            table.column('Clinical_Type', anchor=CENTER, width=120)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('Searched_ID', text='Searched_ID', anchor=W)
            table.heading('Variant_ID', text='Variant_ID', anchor=W)
            table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
            table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
            table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
            table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
            table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
            table.heading('Review_Status', text='Review_Status', anchor=CENTER)
            table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
            table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

            for i in range(len(variant_id_list)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                     clin_interpretation_list[i],
                                     clin_condition_list[i],
                                     allelic_origin_list[i],
                                     review_status_list[i],
                                     identifier_list[i],
                                     cytoband_list[i]))

            ##################
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
        Id.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
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
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 16, "bold", "italic"),
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
            self.m = mv.getvariant(search_id, assembly='hg38')
            m = self.m

            if m == None:
                Id.append(search_id)
                variant_id_list.append('.')
                variant_type_list.append('.')

                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')

            else:

                if m.get('clinvar'):
                    # print(f"{i} : {m[i]}")
                    clinvar = m['clinvar']

                    if clinvar.get('variant_id'):
                        variant_id = clinvar['variant_id']
                    else:
                        variant_id = '.'
                    variant_id_list.append(variant_id)

                    print(f"Variant ID : {variant_id}")

                    if clinvar.get('type'):
                        clintype = clinvar['type']
                    else:
                        clintype = '.'
                    variant_type_list.append(clintype)
                    print(f"Type : {clintype}")

                    if clinvar.get('allele_id'):
                        allele_id = clinvar['allele_id']
                    else:
                        allele_id = '.'
                    allele_id_list.append(allele_id)
                    print(f"Allele ID : {allele_id}")

                    if clinvar.get('cytogenic'):
                        cytoband = clinvar['cytogenic']
                    else:
                        cytoband = '.'
                    cytoband_list.append(cytoband)
                    print(f"Cytogenic location : {cytoband}")

                    if clinvar.get('rcv'):

                        if type(clinvar['rcv']) == list:
                            if clinvar['rcv'][0].get('clinical_significance'):
                                clinical_significance = clinvar['rcv'][0]['clinical_significance']
                            else:
                                clinical_significance = '.'


                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv'][0]['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv'][0]['conditions']) == list:
                                    if clinvar['rcv'][0]['conditions'][0].get('name'):
                                        clinical_condition =  clinvar['rcv'][0]['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'][0].get('origin'):
                                allelic_origin = clinvar['rcv'][0]['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'][0].get('review_status'):
                                review_status = clinvar['rcv'][0]['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('identifiers'):
                                        ident = clinvar['rcv'][0]['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv'][0]['conditions']) == list:

                                    if clinvar['rcv'][0]['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv'][0]['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'
                        else:
                            if clinvar['rcv'].get('clinical_significance'):
                                clinical_significance = clinvar['rcv']['clinical_significance']
                            else:
                                clinical_significance = '.'

                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv']['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv']['conditions']) == list:
                                    if clinvar['rcv']['conditions'][0].get('name'):
                                        clinical_condition = clinvar['rcv']['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'].get('origin'):
                                allelic_origin = clinvar['rcv']['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'].get('review_status'):
                                review_status = clinvar['rcv']['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('identifiers'):
                                        ident = clinvar['rcv']['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv']['conditions']) == list:

                                    if clinvar['rcv']['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv']['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'

                    clin_interpretation_list.append(clinical_significance)
                    clin_condition_list.append(clinical_condition)
                    allelic_origin_list.append(allelic_origin)
                    review_status_list.append(review_status)
                    identifier_list.append(identifier)
                    print(f"Clinvar Interpretation : {clinical_significance}")
                    print(f"Clinvar Condition : {clinical_condition}")
                    print(f"Clinvar Allelic Origin : {allelic_origin}")
                    print(f"Clinvar Review Status : {review_status}")
                    print(f"Clinvar identifier : {identifier}")

                else:
                    variant_id_list.append('.')
                    variant_type_list.append('.')
                    allele_id_list.append('.')
                    cytoband_list.append('.')
                    clin_interpretation_list.append('.')
                    clin_condition_list.append('.')
                    allelic_origin_list.append('.')
                    review_status_list.append('.')
                    identifier_list.append('.')
                    Id.append(search_id)

        except Exception as es:
            self.error_str = es

        self.root = root
        self.root.title('First window')
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
        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        frame1 = Frame(self.root, bg='#7877a5')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 40, "bold", "italic"),
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='white', borderwidth=0)
        lblimg1.place(x=80, y=15, width=250, height=130)

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

        url = 'https://www.ncbi.nlm.nih.gov/clinvar/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/clinvar/",
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
                                  text=f'ClinVar is a freely accessible, public archive of reports of the relationships'
                                       f'among human \ngenetic variations and phenotypes, with supporting evidence. '
                                       f'Essentially, this means \nit’s an archive of variants associated with a gene.'
                                       f'Variants are submitted typically by \nmajor diagnosing laboratories and '
                                       f'research centers. Variants are classified as \npathogenic (disease causing),'
                                       f'benign (not disease causing), and unknown significance (not \nenough evidence'
                                       f'to show the variant is disease causing or not).',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=int(width / 2) - 375, y=50, width=750, height=200)
        fps = 5  # Change the fps to make the animation faster/slower
        shift()

        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)

        try:
            # m = mv.getvariant(search_id)

            if self.m == None:
                '''Id.append(search_id)
                variant_id_list.append('.')
                variant_type_list.append('.')

                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')'''
                no_id = Label(self.frametwo, text='No Data available for this ID',
                              font=("Times New Roman", 15, "bold"),
                              bg='white',
                              fg='black')
                no_id.grid(padx=0, pady=0)
                no_id.place(x=60, y=65)

            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG38)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
            table = ttk.Treeview(table1, height="50")  #################

            table['columns'] = ["Searched_ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                'Clinical_Condition',
                                'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
            table.column('#0', width=120, minwidth=25)
            table.column('Searched_ID', anchor=W, width=120)
            table.column('Variant_ID', anchor=W, width=120)
            table.column('Clinical_Type', anchor=CENTER, width=120)
            table.column('Allelic_ID', anchor=CENTER, width=120)
            table.column('Clinical_Significance', anchor=CENTER, width=120)
            table.column('Clinical_Condition', anchor=CENTER, width=120)
            table.column('Allelic_Origin', anchor=CENTER, width=120)
            table.column('Review_Status', anchor=CENTER, width=120)
            table.column('Clinical_identifier', anchor=CENTER, width=120)
            table.column('Clinical_Type', anchor=CENTER, width=120)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('Searched_ID', text='Searched_ID', anchor=W)
            table.heading('Variant_ID', text='Variant_ID', anchor=W)
            table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
            table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
            table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
            table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
            table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
            table.heading('Review_Status', text='Review_Status', anchor=CENTER)
            table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
            table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

            for i in range(len(variant_id_list)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                     clin_interpretation_list[i],
                                     clin_condition_list[i],
                                     allelic_origin_list[i],
                                     review_status_list[i],
                                     identifier_list[i],
                                     cytoband_list[i]))

            ##################
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
        Id.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()


class info2:
    def __init__(self, root, f):
        # start = timer()
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
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)

        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=50, y=60)
        progress = ttk.Progressbar(self.root1, orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        i = 20

        # progress['value'] = i+20

        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        ##### LIST OF IDs
        print(vcf)
        vcf = list(vcf)


        for id in vcf:
            #####
            Id.append(id)
            index_id=Id.index(id)
            title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
            progress['value'] = i
            self.root1.update_idletasks()
            # time.sleep(0.1)
            self.root1.after(100)  # Delay in millisecs.
            i = i + 40
            mv = myvariant.MyVariantInfo()
            # m=mv.getvariant('chr1:948921T>C')
            m = mv.getvariant(id)

            if m == None:
                # Id.append(id)
                variant_id_list.append('.')
                variant_type_list.append('.')

                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')

            else:

                if m.get('clinvar'):
                    # (f"{i} : {m[i]}")
                    clinvar = m['clinvar']
                    (clinvar)
                    if clinvar.get('variant_id'):
                        variant_id = clinvar['variant_id']
                    else:
                        variant_id = '.'
                    variant_id_list.append(variant_id)

                    (f"Variant ID : {variant_id}")

                    if clinvar.get('type'):
                        clintype = clinvar['type']
                    else:
                        clintype = '.'
                    variant_type_list.append(clintype)
                    (f"Type : {clintype}")

                    if clinvar.get('allele_id'):
                        allele_id = clinvar['allele_id']
                    else:
                        allele_id = '.'
                    allele_id_list.append(allele_id)
                    (f"Allele ID : {allele_id}")

                    if clinvar.get('cytogenic'):
                        cytoband = clinvar['cytogenic']
                    else:
                        cytoband = '.'
                    cytoband_list.append(cytoband)
                    (f"Cytogenic location : {cytoband}")
                    if clinvar.get('rcv'):

                        if type(clinvar['rcv']) == list:
                            if clinvar['rcv'][0].get('clinical_significance'):
                                clinical_significance = clinvar['rcv'][0]['clinical_significance']
                            else:
                                clinical_significance = '.'


                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv'][0]['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv'][0]['conditions']) == list:
                                    if clinvar['rcv'][0]['conditions'][0].get('name'):
                                        clinical_condition =  clinvar['rcv'][0]['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'][0].get('origin'):
                                allelic_origin = clinvar['rcv'][0]['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'][0].get('review_status'):
                                review_status = clinvar['rcv'][0]['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'][0].get('conditions'):
                                if type(clinvar['rcv'][0]['conditions']) == dict:
                                    if clinvar['rcv'][0]['conditions'].get('identifiers'):
                                        ident = clinvar['rcv'][0]['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv'][0]['conditions']) == list:

                                    if clinvar['rcv'][0]['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv'][0]['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'
                        else:
                            if clinvar['rcv'].get('clinical_significance'):
                                clinical_significance = clinvar['rcv']['clinical_significance']
                            else:
                                clinical_significance = '.'

                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('name'):
                                        clinical_condition = clinvar['rcv']['conditions']['name']
                                    else:
                                        clinical_condition = '.'
                                elif type(clinvar['rcv']['conditions']) == list:
                                    if clinvar['rcv']['conditions'][0].get('name'):
                                        clinical_condition = clinvar['rcv']['conditions'][0]['name']
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'
                            else:
                                clinical_condition = '.'

                            if clinvar['rcv'].get('origin'):
                                allelic_origin = clinvar['rcv']['origin']
                            else:
                                allelic_origin = '.'

                            if clinvar['rcv'].get('review_status'):
                                review_status = clinvar['rcv']['review_status']
                            else:
                                review_status = '.'
                            if clinvar['rcv'].get('conditions'):
                                if type(clinvar['rcv']['conditions']) == dict:
                                    if clinvar['rcv']['conditions'].get('identifiers'):
                                        ident = clinvar['rcv']['conditions']['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value
                                    else:
                                        identifier='.'



                                elif type(clinvar['rcv']['conditions']) == list:

                                    if clinvar['rcv']['conditions'][0].get('identifiers'):

                                        ident = clinvar['rcv']['conditions'][0]['identifiers']
                                        for key, value in ident.items():
                                            identifier = key + ':' + value

                                    else:

                                        identifier = '.'

                                else:

                                    identifier = '.'
                            else:
                                identifier = '.'

                    clin_interpretation_list.append(clinical_significance)
                    clin_condition_list.append(clinical_condition)
                    allelic_origin_list.append(allelic_origin)
                    review_status_list.append(review_status)
                    identifier_list.append(identifier)
                    (f"Clinvar Interpretation : {clinical_significance}")
                    (f"Clinvar Condition : {clinical_condition}")
                    (f"Clinvar Allelic Origin : {allelic_origin}")
                    (f"Clinvar Review Status : {review_status}")
                    (f"Clinvar identifier : {identifier}")

                else:
                    # Id.append(id)
                    variant_id_list.append('.')
                    variant_type_list.append('.')
                    allele_id_list.append('.')
                    cytoband_list.append('.')
                    clin_interpretation_list.append('.')
                    clin_condition_list.append('.')
                    allelic_origin_list.append('.')
                    review_status_list.append('.')
                    identifier_list.append('.')

        (variant_id_list)
        (variant_type_list)
        (allele_id_list)
        (cytoband_list)
        (clin_interpretation_list)
        (clin_condition_list)
        (allelic_origin_list)
        (review_status_list)
        (identifier_list)





        self.root = root
        self.root.title('Clinvar window')
        self.root.overrideredirect(False)

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        # NEW: Added a label and the progress bar ######

        # setting window to the center
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        img = PhotoImage(file=r'images/baricon.png')
        root.wm_iconphoto(True, img)

        frame1 = Frame(self.root, bg='#7877a5')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 40, "bold", "italic"),
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#7877a5', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='light grey')

        url = 'https://www.ncbi.nlm.nih.gov/clinvar/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/clinvar/",
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
                                  text=f'ClinVar is a freely accessible, public archive of reports of the relationships'
                                       f'among human \ngenetic variations and phenotypes, with supporting evidence. '
                                       f'Essentially, this means \nit’s an archive of variants associated with a gene.'
                                       f'Variants are submitted typically by \nmajor diagnosing laboratories and '
                                       f'research centers. Variants are classified as \npathogenic (disease causing),'
                                       f'benign (not disease causing), and unknown significance (not \nenough evidence'
                                       f'to show the variant is disease causing or not).',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.grid(padx=0, pady=0)
        canvas.place(x=int(width / 2) - 375, y=50, width=850, height=200)
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
        idz_p= Label(self.frametwo, text=' '+str(len(variant_id_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)


        try:

            if len(variant_type_list) == len(Id):

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic version HG38)",
                                    font=('Times New Roman', 16, 'bold'), bg='white')  ################
                table1.grid(padx=0, pady=0)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
                table.column('#0', width=120, minwidth=25)

                table.column('ID', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

                for i in range(len(Id)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i]))

                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=BOTTOM)

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
            elif (len(variant_type_list) != len(Id)) and (len(variant_type_list) and len(Id))!=0:


                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic version HG38)",
                                    font=('Times New Roman', 16, 'bold'), bg='white')  ################
                table1.grid(padx=0, pady=0)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
                table.column('#0', width=120, minwidth=25)

                table.column('ID', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

                for i in range(len(variant_id_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i]))

                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=BOTTOM)
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
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=680)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again    ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=600, y=720)

            else:
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=550, y=250)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File  Again     ', font=("Times New Roman", 12),
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
            (es)
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload File  Again    ', font=("Times New Roman", 12),
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
        Id.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
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
        header=['HGVS_id','Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance', 'Clinical_Condition', 'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
        data1 = []  # to copy input columns to output file

        l1 = []

        for i in range(len(variant_id_list)):
            data=[]
            data.append(Id[i])
            data.append(variant_id_list[i])
            data.append(variant_type_list[i])
            data.append(allele_id_list[i])
            data.append(clin_interpretation_list[i])
            data.append(clin_condition_list[i])
            data.append(allelic_origin_list[i])
            data.append(review_status_list[i])
            data.append(identifier_list[i])
            data.append(cytoband_list[i])
            data1.append(data)


        for row in data1:


            d1 = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4],
                  header[5]: row[5], header[6]: row[6], header[7]: row[7], header[8]: row[8], header[9]: row[9]
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


class info2_hg38:
    def __init__(self, root, f):
        # start = timer()
        self.error_str = ''
        Id.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()

        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)
        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 16, "bold", "italic"),
                      bg='#7877a5',
                      fg='white')
        title.place(x=20, y=15)
        frame2 = Frame(self.root1, bg='orange')
        frame2.place(x=0, y=45, width=380, height=5)

        title = Label(self.root1, text="LOADING.......",
                      font=("Times New Roman", 12, "italic"),
                      bg='WHITE',
                      fg='BLUE')
        title.place(x=50, y=60)
        progress = ttk.Progressbar(self.root1, orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        i = 20

        # progress['value'] = i+20

        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)

        try:
            for id in vcf:
                Id.append(id)
                index_id=Id.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs")
                progress['value'] = i
                self.root1.update_idletasks()
                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                i = i + 40
                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(id)

                if m == None:
                    # Id.append(id)
                    variant_id_list.append('.')
                    variant_type_list.append('.')

                    allele_id_list.append('.')
                    cytoband_list.append('.')
                    clin_interpretation_list.append('.')
                    clin_condition_list.append('.')
                    allelic_origin_list.append('.')
                    review_status_list.append('.')
                    identifier_list.append('.')
                else:
                    if m.get('clinvar'):
                        # (f"{i} : {m[i]}")
                        clinvar = m['clinvar']
                        (clinvar)
                        if clinvar.get('variant_id'):
                            variant_id = clinvar['variant_id']
                        else:
                            variant_id = '.'
                        variant_id_list.append(variant_id)

                        (f"Variant ID : {variant_id}")

                        if clinvar.get('type'):
                            clintype = clinvar['type']
                        else:
                            clintype = '.'
                        variant_type_list.append(clintype)
                        (f"Type : {clintype}")

                        if clinvar.get('allele_id'):
                            allele_id = clinvar['allele_id']
                        else:
                            allele_id = '.'
                        allele_id_list.append(allele_id)
                        (f"Allele ID : {allele_id}")

                        if clinvar.get('cytogenic'):
                            cytoband = clinvar['cytogenic']
                        else:
                            cytoband = '.'
                        cytoband_list.append(cytoband)
                        (f"Cytogenic location : {cytoband}")

                        if clinvar.get('rcv'):

                            if type(clinvar['rcv']) == list:
                                if clinvar['rcv'][0].get('clinical_significance'):
                                    clinical_significance = clinvar['rcv'][0]['clinical_significance']
                                else:
                                    clinical_significance = '.'

                                if clinvar['rcv'][0].get('conditions'):
                                    if type(clinvar['rcv'][0]['conditions']) == dict:
                                        if clinvar['rcv'][0]['conditions'].get('name'):
                                            clinical_condition = clinvar['rcv'][0]['conditions']['name']
                                        else:
                                            clinical_condition = '.'
                                    elif type(clinvar['rcv'][0]['conditions']) == list:
                                        if clinvar['rcv'][0]['conditions'][0].get('name'):
                                            clinical_condition = clinvar['rcv'][0]['conditions'][0]['name']
                                        else:
                                            clinical_condition = '.'
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'

                                if clinvar['rcv'][0].get('origin'):
                                    allelic_origin = clinvar['rcv'][0]['origin']
                                else:
                                    allelic_origin = '.'

                                if clinvar['rcv'][0].get('review_status'):
                                    review_status = clinvar['rcv'][0]['review_status']
                                else:
                                    review_status = '.'
                                if clinvar['rcv'][0].get('conditions'):
                                    if type(clinvar['rcv'][0]['conditions']) == dict:
                                        if clinvar['rcv'][0]['conditions'].get('identifiers'):
                                            ident = clinvar['rcv'][0]['conditions']['identifiers']
                                            for key, value in ident.items():
                                                identifier = key + ':' + value
                                        else:
                                            identifier = '.'



                                    elif type(clinvar['rcv'][0]['conditions']) == list:

                                        if clinvar['rcv'][0]['conditions'][0].get('identifiers'):

                                            ident = clinvar['rcv'][0]['conditions'][0]['identifiers']
                                            for key, value in ident.items():
                                                identifier = key + ':' + value

                                        else:

                                            identifier = '.'

                                    else:

                                        identifier = '.'
                                else:
                                    identifier = '.'
                            else:
                                if clinvar['rcv'].get('clinical_significance'):
                                    clinical_significance = clinvar['rcv']['clinical_significance']
                                else:
                                    clinical_significance = '.'

                                if clinvar['rcv'].get('conditions'):
                                    if type(clinvar['rcv']['conditions']) == dict:
                                        if clinvar['rcv']['conditions'].get('name'):
                                            clinical_condition = clinvar['rcv']['conditions']['name']
                                        else:
                                            clinical_condition = '.'
                                    elif type(clinvar['rcv']['conditions']) == list:
                                        if clinvar['rcv']['conditions'][0].get('name'):
                                            clinical_condition = clinvar['rcv']['conditions'][0]['name']
                                        else:
                                            clinical_condition = '.'
                                    else:
                                        clinical_condition = '.'
                                else:
                                    clinical_condition = '.'

                                if clinvar['rcv'].get('origin'):
                                    allelic_origin = clinvar['rcv']['origin']
                                else:
                                    allelic_origin = '.'

                                if clinvar['rcv'].get('review_status'):
                                    review_status = clinvar['rcv']['review_status']
                                else:
                                    review_status = '.'
                                if clinvar['rcv'].get('conditions'):
                                    if type(clinvar['rcv']['conditions']) == dict:
                                        if clinvar['rcv']['conditions'].get('identifiers'):
                                            ident = clinvar['rcv']['conditions']['identifiers']
                                            for key, value in ident.items():
                                                identifier = key + ':' + value
                                        else:
                                            identifier = '.'



                                    elif type(clinvar['rcv']['conditions']) == list:

                                        if clinvar['rcv']['conditions'][0].get('identifiers'):

                                            ident = clinvar['rcv']['conditions'][0]['identifiers']
                                            for key, value in ident.items():
                                                identifier = key + ':' + value

                                        else:

                                            identifier = '.'

                                    else:

                                        identifier = '.'
                                else:
                                    identifier = '.'

                        clin_interpretation_list.append(clinical_significance)
                        clin_condition_list.append(clinical_condition)
                        allelic_origin_list.append(allelic_origin)
                        review_status_list.append(review_status)
                        identifier_list.append(identifier)
                        (f"Clinvar Interpretation : {clinical_significance}")
                        (f"Clinvar Condition : {clinical_condition}")
                        (f"Clinvar Allelic Origin : {allelic_origin}")
                        (f"Clinvar Review Status : {review_status}")
                        (f"Clinvar identifier : {identifier}")

                    else:
                        # Id.append(id)
                        variant_id_list.append('.')
                        variant_type_list.append('.')
                        allele_id_list.append('.')
                        cytoband_list.append('.')
                        clin_interpretation_list.append('.')
                        clin_condition_list.append('.')
                        allelic_origin_list.append('.')
                        review_status_list.append('.')
                        identifier_list.append('.')




        except Exception as es:
            self.error_str = es

        self.root = root
        self.root.title('Clinvar window')
        self.root.overrideredirect(False)
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

        # NEW: Added a label and the progress bar ######

        # setting window to the center
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        frame1 = Frame(self.root, bg='#7877a5')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from ClinVar", font=("Times New Roman", 40, "bold", "italic"),
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#7877a5', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='light grey')

        url = 'https://www.ncbi.nlm.nih.gov/clinvar/'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="https://www.ncbi.nlm.nih.gov/clinvar/",
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
                                  text=f'ClinVar is a freely accessible, public archive of reports of the relationships'
                                       f'among human \ngenetic variations and phenotypes, with supporting evidence. '
                                       f'Essentially, this means \nit’s an archive of variants associated with a gene.'
                                       f'Variants are submitted typically by \nmajor diagnosing laboratories and '
                                       f'research centers. Variants are classified as \npathogenic (disease causing),'
                                       f'benign (not disease causing), and unknown significance (not \nenough evidence'
                                       f'to show the variant is disease causing or not).',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.grid(padx=0, pady=0)
        canvas.place(x=int(width / 2) - 375, y=50, width=850, height=200)
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
        idz_p= Label(self.frametwo, text=' '+str(len(variant_id_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(variant_type_list) == len(Id):
                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic version HG38)",
                                    font=('Times New Roman', 16, 'bold'), bg='white')  ################
                table1.grid(padx=0, pady=0)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
                table.column('#0', width=120, minwidth=25)

                table.column('ID', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

                for i in range(len(Id)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i]))

                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=BOTTOM)

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
            elif (len(variant_type_list) != len(Id)) and (len(variant_type_list) and len(Id))!=0:

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic version HG38)",
                                    font=('Times New Roman', 16, 'bold'), bg='white')  ################
                table1.grid(padx=0, pady=0)  ###################
                table1.place(x=40, y=230, width=1280, height=380)
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ["ID", 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
                table.column('#0', width=120, minwidth=25)

                table.column('ID', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)

                for i in range(len(variant_id_list)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i], variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i]))

                table.place(x=0, y=0)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################

                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################

                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=BOTTOM)
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
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=720)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again   ', font=("Times New Roman", 12),
                               bg='white',
                               fg='black')
                error2.grid(padx=0, pady=0)
                error2.place(x=600, y=760)
            else:
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=550, y=250)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File  Again     ', font=("Times New Roman", 12),
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
            (es)
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload File  Again    ', font=("Times New Roman", 12),
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
        Id.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
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
        header=['HGVS_id','Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance', 'Clinical_Condition', 'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location']
        data1 = []  # to copy input columns to output file

        l1 = []


        for i in range(len(variant_id_list)):
            data=[]
            data.append(Id[i])
            data.append(variant_id_list[i])
            data.append(variant_type_list[i])
            data.append(allele_id_list[i])
            data.append(clin_interpretation_list[i])
            data.append(clin_condition_list[i])
            data.append(allelic_origin_list[i])
            data.append(review_status_list[i])
            data.append(identifier_list[i])
            data.append(cytoband_list[i])
            data1.append(data)


        for row in data1:


            d1 = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4],
                  header[5]: row[5], header[6]: row[6], header[7]: row[7], header[8]: row[8], header[9]: row[9]
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

