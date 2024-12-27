import webbrowser
import tkinter
from tkinter.filedialog import asksaveasfile
import allel
import myvariant
from tkinter import Tk, Toplevel, messagebox, ttk
from tkinter import *
import csv
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
# from pandas.tools.plotting import table
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import database_interface
from PIL import Image, ImageTk
import matplotlib.pyplot as plt

sift_pred = []
sift_score = []
sift_converted_rs = []
polyphen2_HDIV_Pred = []
polyphen2_HDIV_Score = []
polyphen2_HVAR_Pred = []
polyphen2_HVAR_Score = []
lrt_pred = []
lrt_score = []
lrt_converted_rs = []
mut_assessor_pred = []
mut_assessor_score = []
mutationassessor_rs = []
mut_taster_pred = []
mut_taster_score = []
MutationTaster_converted_rs = []
provean_pred = []
provean_score = []
provean_rs = []
dann_score = []
fathmm_pred = []
fathmm_score = []
fathmm_rs = []
fathmm_mkl_pred = []
fathmm_mkl_score = []
fathmm_mkl_rankscore = []
metasvm_pred = []
metasvm_score = []
metasvm_rankscore = []
metalr_pred = []
metalr_score = []
MetaLR_rankscore = []
integ_fitcoin_score = []
integ_fitcons_rankscore = []
integ_conf_value = []
gerp_rs = []
gerp_rs_rankscore = []
siphy_29way_logOdds = []
siphy_29way_logOdds_rs = []
revel_score_list = []
CADD_raw_list = []
CADD_phred_list = []
genoCanyon_rankscore = []
genoCanyon_score = []
eigen_rawcoding = []
eigen_pc_rawcoding = []
phylo100waylist = []
phylo100wayrankscore = []
phylo17waylist = []
phylo17rankscore = []
phylo30waylist = []
phylo30rankscore = []
phastcons100waylist = []
phastcons100wayrankscore = []
phastcons17waylist = []
phastcons17rankscore = []
phastcons30waylist = []
phastcons30rankscore = []
interpro_domain = []
GTEx_gene = []
GTEx_tissue = []
ID = []

siftsc = '.'
sift_pos = '.'
siftpred = '.'
sift_converted_rankscore = '.'
hdivsc = '.'
hdiv_pos = '.'
hdivpr = '.'
hdivrank = '.'
hvarpos = '.'
hvarsc = '.'
hvarpr = '.'
hvarrank = '.'
lrtsc = '.'
lrt_pos = '.'
lrtpr = '.'
lrt_converted_rankscore = '.'
asssc = '.'
ass_pos = '.'
asspr = '.'
mutationassessor_rankscore = '.'
tassc = '.'
taspr = '.'
MutationTaster_converted_rankscore = '.'
genoscore = '.'
geno_rs = '.'
provsc = '.'
prov_pos = '.'
provpr = '.'
prov_rs = '.'
provsc = '.'
dann = '.'
faths = '.'
fath_pos = '.'
fathp = '.'
fathrs = '.'
fathsc = '.'
fathm_pos = '.'
fathpr = '.'
fathcoding_rs = '.'
svmsc = '.'
svm_pos = '.'
svmpr = '.'
svm_rs = '.'
lrsc = '.'
lr_pos = '.'
lrpr = '.'
lr_rs = '.'
fitsc = '.'
fitcv = '.'
fitrs = '.'
rs = '.'
rs_rank = '.'
siphy = '.'
siphyrs = '.'
revsc = '.'
eigen_rc = '.'
phylo100way = '.'
phylo100wayrs = '.'
phylo17 = '.'
phylo17rs = '.'
phylo30 = '.'
phylo30rs = '.'
phastcons100way = '.'
phastcons100wayrs = '.'
phastcons17 = '.'
phastcons17rs = '.'
phastcons30 = '.'
phastcons30rs = '.'
eigenpc_rc = '.'
interpro = '.'
gene = '.'
tissue = '.'
CADDraw = '.'
CADDp = '.'

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
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 16, "bold", "italic"),
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
        p= 20

        progress['value'] = p

        self.root1.update_idletasks()

        # time.sleep(0.1)
        self.root1.after(100)  # Delay in millisecs.
        p = p + 40

        try:
            self.m = mv.getvariant(search_id)
            m = self.m

            if m == None:
                sift_pred.append('.')
                sift_score.append('.')
                sift_converted_rs.append('.')
                polyphen2_HDIV_Pred.append('.')
                polyphen2_HDIV_Score.append('.')
                polyphen2_HVAR_Pred.append('.')
                polyphen2_HVAR_Score.append('.')
                lrt_pred.append('.')
                lrt_score.append('.')
                lrt_converted_rs.append('.')
                mut_assessor_pred.append('.')
                mut_assessor_score.append('.')
                mutationassessor_rs.append('.')
                mut_taster_pred.append('.')
                mut_taster_score.append('.')
                MutationTaster_converted_rs.append('.')
                provean_pred.append('.')
                provean_score.append('.')
                provean_rs.append('.')
                dann_score.append('.')
                fathmm_pred.append('.')
                fathmm_score.append('.')
                fathmm_mkl_rankscore.append('.')
                fathmm_rs.append('.')
                fathmm_mkl_pred.append('.')
                fathmm_mkl_score.append('.')
                metasvm_pred.append('.')
                metasvm_score.append('.')
                metasvm_rankscore.append('.')
                metalr_pred.append('.')
                metalr_score.append('.')
                MetaLR_rankscore.append('.')
                integ_fitcoin_score.append('.')
                integ_conf_value.append('.')
                integ_fitcons_rankscore.append('.')
                gerp_rs.append('.')
                gerp_rs_rankscore.append('.')
                siphy_29way_logOdds.append('.')
                siphy_29way_logOdds_rs.append('.')
                revel_score_list.append('.')
                CADD_raw_list.append('.')
                CADD_phred_list.append('.')
                genoCanyon_rankscore.append('.')
                genoCanyon_score.append('.')
                eigen_rawcoding.append('.')
                eigen_pc_rawcoding.append('.')
                phylo100waylist.append('.')
                phylo100wayrankscore.append('.')
                phylo17waylist.append('.')
                phylo17rankscore.append('.')
                phylo30waylist.append('.')
                phylo30rankscore.append('.')
                phastcons100waylist.append('.')
                phastcons100wayrankscore.append('.')
                phastcons17waylist.append('.')
                phastcons17rankscore.append('.')
                phastcons30waylist.append('.')
                phastcons30rankscore.append('.')
                interpro_domain.append('.')
                GTEx_gene.append('.')
                GTEx_tissue.append('.')


            else:
                if m.get('dbnsfp'):

                    dbnsfp = m['dbnsfp']

                    for key, item in dbnsfp.items():
                        (f"{key} : {item}")
                    if dbnsfp.get('sift'):

                        if dbnsfp['sift'].get('score') and dbnsfp['sift'].get('pred'):
                            if type(dbnsfp['sift']['score']) == list:
                                siftsc = max(dbnsfp['sift']['score'])
                                sift_pos = (dbnsfp['sift']['score']).index(max(dbnsfp['sift']['score']))

                            else:
                                siftsc = (dbnsfp['sift']['score'])

                            if type(dbnsfp['sift']['pred']) == list:
                                siftpred = (dbnsfp['sift']['pred'])[sift_pos]
                                if siftpred == '.':
                                    siftpred=(max(dbnsfp['sift']['pred']))
                            else:
                                siftpred = dbnsfp['sift']['pred']
                        else:
                            siftsc = '.'
                            siftpred = '.'
                        if dbnsfp['sift'].get('converted_rankscore'):
                            if type(dbnsfp['sift'].get('converted_rankscore')) == list:
                                sift_converted_rankscore = max(dbnsfp['sift']['converted_rankscore'])
                            else:
                                sift_converted_rankscore = dbnsfp['sift']['converted_rankscore']
                        else:
                            sift_converted_rankscore = '.'
                        if siftsc == '.' and siftpred == '.' and sift_converted_rankscore != '.':
                            if dbnsfp['sift'].get('score'):

                                siftsc = (dbnsfp['sift']['score'])
                            else:
                                siftsc = '.'
                            if dbnsfp['sift'].get('pred'):
                                siftpred = dbnsfp['sift']['pred']
                            else:
                                siftpred = '.'

                    else:
                        siftsc = '.'
                        siftpred = '.'
                        sift_converted_rankscore = '.'

                    if (siftpred != '.') and siftsc == '.':
                        siftsc = 0
                    sift_pred.append(siftpred)
                    sift_score.append(siftsc)
                    sift_converted_rs.append(sift_converted_rankscore)

                    (f"SIFT Pred : {siftpred}")
                    (f'SIFT Score : {siftsc}')
                    (f'Sift_converted_rankscore : {sift_converted_rankscore}')

                    if dbnsfp.get('polyphen2'):
                        if dbnsfp['polyphen2'].get('hdiv'):

                            if dbnsfp['polyphen2']['hdiv'].get('score') and dbnsfp['polyphen2']['hdiv'].get('pred'):

                                if type(dbnsfp['polyphen2']['hdiv']['score']) == list:
                                    hdivsc = max(dbnsfp['polyphen2']['hdiv']['score'])
                                    hdiv_pos = (dbnsfp['polyphen2']['hdiv']['score']).index(
                                        max(dbnsfp['polyphen2']['hdiv']['score']))


                                else:
                                    hdivsc = dbnsfp['polyphen2']['hdiv']['score']

                                if dbnsfp['polyphen2']['hdiv'].get('pred'):
                                    if type(dbnsfp['polyphen2']['hdiv'].get('pred')) == list:
                                        hdivpr = (dbnsfp['polyphen2']['hdiv']['pred'])[hdiv_pos]
                                        if hdivpr == '.':
                                            hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])


                                    else:
                                        hdivpr = dbnsfp['polyphen2']['hdiv']['pred']
                            else:
                                hdivpr = '.'
                                hdivsc = '.'

                            if dbnsfp['polyphen2']['hdiv'].get('rankscore'):
                                hdivrank = dbnsfp['polyphen2']['hdiv']['rankscore']
                            else:
                                hdivrank = '.'

                            if hdivpr == '.' and hdivsc == '.' and hdivrank != '.':
                                if dbnsfp['polyphen2']['hdiv'].get('score'):
                                    hdivsc = dbnsfp['polyphen2']['hdiv']['score']
                                else:
                                    hdivsc = '.'
                                if dbnsfp['polyphen2']['hdiv'].get('pred'):

                                    hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])
                                else:
                                    hdivpr = '.'

                                if hdivsc == '.' and hdivpr != '.':
                                    hdivsc = 0

                        else:
                            hdivsc = '.'
                            hdivpr = '.'

                        if dbnsfp['polyphen2'].get('hvar'):
                            (dbnsfp['polyphen2'])
                            if dbnsfp['polyphen2']['hvar'].get('pred') and dbnsfp['polyphen2']['hvar'].get('score'):

                                if type(dbnsfp['polyphen2']['hvar']['score']) == list:
                                    hvarsc = max(dbnsfp['polyphen2']['hvar']['score'])
                                    hvarpos = (dbnsfp['polyphen2']['hvar']['score']).index(
                                        max(dbnsfp['polyphen2']['hvar']['score']))

                                else:
                                    hvarsc = dbnsfp['polyphen2']['hvar']['score']

                                if type(dbnsfp['polyphen2']['hvar'].get('pred')) == list:
                                    hvarpr = (dbnsfp['polyphen2']['hvar']['pred'])[hvarpos]
                                    if hvarpr == '.':
                                        hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])

                                elif type(dbnsfp['polyphen2']['hvar'].get('pred')) != list:
                                    hvarpr = dbnsfp['polyphen2']['hvar']['pred']
                            else:
                                hvarsc = '.'
                                hvarpr = '.'

                            if dbnsfp['polyphen2']['hvar'].get('rankscore'):
                                hvarrank = dbnsfp['polyphen2']['hvar']['rankscore']
                            else:
                                hvarrank = '.'

                            if hvarpr == '.' and hvarsc == '.' and hvarrank != '.':
                                if dbnsfp['polyphen2']['hvar'].get('score'):
                                    hvarsc = dbnsfp['polyphen2']['hvar']['score']
                                else:
                                    hvarsc = '.'
                                if dbnsfp['polyphen2']['hvar'].get('pred'):

                                    hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])
                                else:
                                    hvarpr = '.'

                                if hvarsc == '.' and hvarpr != '.':
                                    hvarsc = 0



                        else:

                            hvarsc = '.'
                            hvarpr = '.'

                    else:
                        hdivsc = '.'
                        hdivpr = '.'
                        hvarpr = '.'
                        hvarsc = '.'
                    if hdivpr != '.' and hdivsc == '.':
                        hdivsc = 0
                    if hvarpr != '.' and hvarsc == '.':
                        hvarsc = 0
                    polyphen2_HDIV_Pred.append(hdivpr)
                    polyphen2_HDIV_Score.append(hdivsc)
                    polyphen2_HVAR_Score.append(hvarsc)
                    polyphen2_HVAR_Pred.append(hvarpr)
                    (f'Polyphen2 HDIV Pred : {hdivpr}')
                    (f'Polyphen2 HDIV Score : {hdivsc}')
                    (f'Polyphen2 HVAR Pred : {hvarpr}')
                    (f'Polyphen2 HVAR Score : {hvarsc}')

                    if dbnsfp.get('lrt'):

                        if dbnsfp['lrt'].get('score') and dbnsfp['lrt'].get('pred'):

                            if type(dbnsfp['lrt'].get('score')) == list:
                                lrtsc = max(dbnsfp['lrt']['score'])
                                lrt_pos = (dbnsfp['lrt']['score']).index(max(dbnsfp['lrt']['score']))

                            else:
                                lrtsc = dbnsfp['lrt']['score']
                                (f'score : {lrtsc}')

                            if type(dbnsfp['lrt'].get('pred')) == list:

                                lrtpr = (dbnsfp['lrt']['pred'])[lrt_pos]
                                if lrtpr == '.':
                                    lrtpr = max(dbnsfp['lrt']['pred'])
                            else:
                                lrtpr = dbnsfp['lrt']['pred']

                        else:
                            lrtsc = '.'
                            lrtpr = '.'

                        if dbnsfp['lrt'].get('converted_rankscore'):

                            if type(dbnsfp['lrt'].get('converted_rankscore')) == list:
                                lrt_converted_rankscore = max(dbnsfp['lrt']['converted_rankscore'])

                            elif type(dbnsfp['lrt'].get('converted_rankscore')) != list:
                                lrt_converted_rankscore = dbnsfp['lrt']['converted_rankscore']

                        else:
                            lrt_converted_rankscore = '.'

                        if lrtpr == '.' and lrtsc == '.' and lrt_converted_rankscore != '.':
                            if dbnsfp['lrt'].get('score'):

                                lrtsc = dbnsfp['lrt']['score']
                                (f'score : {lrtsc}')
                            else:
                                lrtsc = '.'

                            if dbnsfp['lrt'].get('pred'):
                                lrtpr = dbnsfp['lrt']['pred']
                            else:
                                lrtpr = '.'




                    else:
                        lrtsc = '.'
                        lrtpr = '.'
                        lrt_converted_rankscore = '.'
                    if (lrtpr != '.') and lrtsc == '.':
                        lrtsc = 0

                    lrt_pred.append(lrtpr)
                    lrt_score.append(lrtsc)
                    lrt_converted_rs.append(lrt_converted_rankscore)
                    (f"LRT Pred : {lrtpr}")
                    (f'LRT Score : {lrtsc}')
                    (f'lrt_converted_rankscore : {lrt_converted_rankscore}')

                    if dbnsfp.get('mutationassessor'):
                        if dbnsfp['mutationassessor'].get('score') and dbnsfp['mutationassessor'].get('pred'):
                            if type(dbnsfp['mutationassessor']['score']) == list:
                                asssc = max(dbnsfp['mutationassessor']['score'])
                                ass_pos = (dbnsfp['mutationassessor']['score']).index(
                                    max(dbnsfp['mutationassessor']['score']))
                            else:
                                asssc = dbnsfp['mutationassessor']['score']

                            if type(dbnsfp['mutationassessor'].get('pred')) == list:

                                asspr = (dbnsfp['mutationassessor']['pred'])[ass_pos]
                                if asspr == '.':
                                    asspr = max(dbnsfp['mutationassessor']['pred'])

                            else:
                                asspr = dbnsfp['mutationassessor']['pred']

                        else:
                            asspr = '.'
                            asssc = '.'

                        if dbnsfp['mutationassessor'].get('rankscore'):
                            if type(dbnsfp['mutationassessor']['rankscore']) == list:
                                mutationassessor_rankscore = max(dbnsfp['mutationassessor']['rankscore'])
                            else:
                                mutationassessor_rankscore = dbnsfp['mutationassessor']['rankscore']
                        else:
                            mutationassessor_rankscore = '.'

                        if asspr == '.' and asssc == '.' and mutationassessor_rankscore != '.':
                            if dbnsfp['mutationassessor'].get('score'):
                                asssc = dbnsfp['mutationassessor']['score']
                            else:
                                asssc = '.'

                            if dbnsfp['mutationassessor'].get('pred'):
                                asspr = dbnsfp['mutationassessor']['pred']
                            else:
                                asspr = '.'

                    else:
                        asspr = '.'
                        asssc = '.'
                        mutationassessor_rankscore = '.'

                    if asssc == '.' and asspr != '.':
                        asssc = 0

                    mut_assessor_pred.append(asspr)
                    mut_assessor_score.append(asssc)
                    mutationassessor_rs.append(mutationassessor_rankscore)
                    (f'Mutation Assessor Pred : {asspr}')
                    (f'Mutation Assessor Score : {asssc}')
                    (f'Mutation Assessor RankScore : {mutationassessor_rankscore}')

                    if dbnsfp.get('mutationtaster'):

                        if dbnsfp['mutationtaster'].get('score') and dbnsfp['mutationtaster'].get('pred'):
                            if type(dbnsfp['mutationtaster']['score']) == list:
                                tassc = max(dbnsfp['mutationtaster']['score'])
                                position = (dbnsfp['mutationtaster']['score']).index(
                                    max(dbnsfp['mutationtaster']['score']))
                                # (index)
                                # (type(dbnsfp['mutationtaster']['score']))

                            else:
                                tassc = dbnsfp['mutationtaster']['score']

                            if type(dbnsfp['mutationtaster'].get('pred')) == list:
                                # taspr = max(dbnsfp['mutationtaster']['pred'])

                                taspr = (dbnsfp['mutationtaster']['pred'])[position]
                                if taspr == '.':
                                    taspr = max(dbnsfp['mutationtaster']['pred'])

                            else:
                                taspr = dbnsfp['mutationtaster']['pred']


                        else:
                            taspr = '.'
                            tassc = '.'

                        if dbnsfp['mutationtaster'].get('converted_rankscore'):
                            if type(dbnsfp['mutationtaster'].get('converted_rankscore')) == list:
                                # taspr = max(dbnsfp['mutationtaster']['pred'])
                                MutationTaster_converted_rankscore = (dbnsfp['mutationtaster']['converted_rankscore'])[
                                    position]
                            elif type(dbnsfp['mutationtaster'].get('converted_rankscore')) != list:
                                MutationTaster_converted_rankscore = dbnsfp['mutationtaster']['converted_rankscore']

                        else:
                            MutationTaster_converted_rankscore = '.'

                        if taspr == '.' and tassc == '.' and MutationTaster_converted_rankscore != '.':
                            if dbnsfp['mutationtaster'].get('score'):

                                tassc = dbnsfp['mutationtaster']['score']
                            else:
                                tassc = '.'

                            if dbnsfp['mutationtaster'].get('pred'):

                                taspr = dbnsfp['mutationtaster']['pred']
                            else:
                                taspr = '.'
                    else:

                        taspr = '.'
                        tassc = '.'
                        MutationTaster_converted_rankscore = '.'
                    if tassc == '.' and taspr != '.':
                        tassc = 0
                    (f'Mutation Taster Pred : {taspr}')
                    (f'Mutation Taster Score : {tassc}')
                    (f'Mutation Taster Converted rankscore : {MutationTaster_converted_rankscore}')
                    mut_taster_pred.append(taspr)
                    mut_taster_score.append(tassc)
                    MutationTaster_converted_rs.append(MutationTaster_converted_rankscore)

                    if dbnsfp.get('genocanyon'):
                        if dbnsfp['genocanyon'].get('score'):
                            if type(dbnsfp['genocanyon'].get('score')) == list:
                                genoscore = max(dbnsfp['genocanyon']['score'])
                            elif type(dbnsfp['genocanyon'].get('score')) != list:
                                genoscore = dbnsfp['genocanyon']['score']
                        else:
                            genoscore = '.'

                        if dbnsfp['genocanyon'].get('rankscore'):
                            if type(dbnsfp['genocanyon']['rankscore']) == list:
                                geno_rs = max(dbnsfp['genocanyon']['rankscore'])
                            else:
                                geno_rs = dbnsfp['genocanyon']['rankscore']


                        else:
                            geno_rs = '.'
                    else:
                        genoscore = '.'
                        geno_rs = '.'
                    genoCanyon_score.append(genoscore)
                    genoCanyon_rankscore.append(geno_rs)
                    (f'Genocanyon Score : {genoscore}')
                    (f'genocanyon Rank Score: {geno_rs}')

                    if dbnsfp.get('provean'):

                        if dbnsfp['provean'].get('score') and dbnsfp['provean'].get('pred'):
                            if type(dbnsfp['provean']['score']) == list:
                                provsc = max(dbnsfp['provean']['score'])
                                prov_pos = (dbnsfp['provean']['score']).index(max(dbnsfp['provean']['score']))

                            else:
                                provsc = dbnsfp['provean']['score']

                            if type(dbnsfp['provean'].get('pred')) == list:
                                provpr = (dbnsfp['provean']['pred'])[prov_pos]
                                if provpr == '.':
                                    provpr = max(dbnsfp['provean']['pred'])
                            else:
                                provpr = dbnsfp['provean']['pred']
                        else:
                            provpr = '.'
                            provsc = '.'

                        if dbnsfp['provean'].get('rankscore'):
                            if type(dbnsfp['provean']['rankscore']) == list:
                                prov_rs = max(dbnsfp['provean']['rankscore'])

                            else:
                                prov_rs = dbnsfp['provean']['rankscore']

                        else:
                            prov_rs = '.'
                        if provpr == '.' and provsc == '.' and prov_rs != '.':
                            if dbnsfp['provean'].get('score'):
                                provsc = dbnsfp['provean']['score']
                            else:
                                provsc = '.'
                            if dbnsfp['provean'].get('pred'):
                                provpr = dbnsfp['provean']['pred']
                            else:
                                provpr = '.'

                    else:
                        provpr = '.'
                        provsc = '.'
                        prov_rs = '.'
                    if (provpr != '.') and provsc == '.':
                        provsc = 0

                    provean_pred.append(provpr)
                    provean_score.append(provsc)
                    provean_rs.append(prov_rs)
                    (f'Provean Pred : {provpr}')
                    (f'Provean Score : {provsc}')
                    (f'Provean Rank Score : {prov_rs}')

                    if dbnsfp.get('dann'):
                        if dbnsfp['dann'].get('score'):
                            if type(dbnsfp['dann']['score']) == list:
                                dann = max(dbnsfp['dann']['score'])

                            else:
                                dann = dbnsfp['dann']['score']

                        else:
                            dann = '.'

                    else:
                        dann = '.'
                    dann_score.append(dann)
                    (f'DANN Score : {dann}')

                    if dbnsfp.get('fathmm'):
                        if dbnsfp['fathmm'].get('pred') and dbnsfp['fathmm'].get('score'):
                            if type(dbnsfp['fathmm']['score']) == list:
                                faths = max(dbnsfp['fathmm']['score'])
                                fath_pos = (dbnsfp['fathmm']['score']).index(max(dbnsfp['fathmm']['score']))

                            else:
                                faths = dbnsfp['fathmm']['score']

                            if type(dbnsfp['fathmm']['pred']) == list:
                                fathp = (dbnsfp['fathmm']['pred'])[fath_pos]
                                if fathp == '.':
                                    fathp = max(dbnsfp['fathmm']['pred'])
                            else:
                                fathp = dbnsfp['fathmm']['pred']
                        else:
                            fathp = '.'
                            faths = '.'

                        if dbnsfp['fathmm'].get('rankscore'):
                            if type(dbnsfp['fathmm']['rankscore']) == list:
                                fathrs = max(dbnsfp['fathmm']['rankscore'])
                            else:
                                fathrs = dbnsfp['fathmm']['rankscore']

                        else:
                            fathrs = '.'
                        if faths == '.' and fathp == '.' and fathrs != '.':
                            if dbnsfp['fathmm'].get('score'):
                                faths = dbnsfp['fathmm']['score']
                            else:
                                faths = '.'
                            if dbnsfp['fathmm'].get('pred'):
                                fathp = dbnsfp['fathmm']['pred']
                            else:
                                fathp = '.'
                    else:
                        fathp = '.'
                        faths = '.'
                        fathrs = '.'

                    if faths == '.' and fathp != '.':
                        faths = 0
                    fathmm_pred.append(fathp)
                    fathmm_score.append(faths)
                    fathmm_rs.append(fathrs)
                    (f'Fathmm Pred : {fathp}')
                    (f'Fathmm Score : {faths}')
                    (f'Fathmm Rank Score : {fathrs}')

                    if dbnsfp.get('fathmm-mkl'):
                        if dbnsfp['fathmm-mkl'].get('coding_pred') and dbnsfp['fathmm-mkl'].get('coding_score'):
                            if type(dbnsfp['fathmm-mkl']['coding_score']) == list:
                                fathsc = max(dbnsfp['fathmm-mkl']['coding_score'])
                                fathm_pos = (dbnsfp['fathmm-mkl']['coding_score']).index(
                                    max(dbnsfp['fathmm-mkl']['coding_score']))
                            else:
                                fathsc = dbnsfp['fathmm-mkl']['coding_score']

                            if type(dbnsfp['fathmm-mkl'].get('coding_pred')) == list:
                                fathpr = (dbnsfp['fathmm-mkl']['coding_pred'])[fathm_pos]
                                if fathpr == '.':
                                    fathpr = max(dbnsfp['fathmm-mkl']['coding_pred'])
                            else:
                                fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                        else:
                            fathpr = '.'
                            fathsc = '.'

                        if dbnsfp['fathmm-mkl'].get('coding_rankscore'):
                            if type(dbnsfp['fathmm-mkl']['coding_rankscore']) == list:
                                fathcoding_rs = max(dbnsfp['fathmm-mkl']['coding_rankscore'])
                            else:
                                fathcoding_rs = dbnsfp['fathmm-mkl']['coding_rankscore']
                        else:
                            fathcoding_rs = '.'
                        if fathsc == '.' and fathpr == '.' and fathcoding_rs != '.':
                            if dbnsfp['fathmm-mkl'].get('coding_score'):
                                fathsc = dbnsfp['fathmm-mkl']['coding_score']
                            else:
                                fathsc = '.'
                            if dbnsfp['fathmm-mkl'].get('coding_pred'):
                                fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                            else:
                                fathpr = '.'

                    else:
                        fathpr = '.'
                        fathsc = '.'
                        fathcoding_rs = '.'
                    if fathsc == '.' and fathpr != '.':
                        fathsc = 0
                    fathmm_mkl_pred.append(fathpr)
                    fathmm_mkl_score.append(fathsc)
                    fathmm_mkl_rankscore.append(fathcoding_rs)
                    (f'Fathmm-mkl Pred : {fathpr}')
                    (f'Fathmm-mkl Score : {fathsc}')
                    (f'Fathmm-mkl RankScore : {fathcoding_rs}')

                    if dbnsfp.get('metasvm'):
                        if dbnsfp['metasvm'].get('pred') and dbnsfp['metasvm'].get('score'):
                            if type(dbnsfp['metasvm']['score']) == list:
                                svmsc = max(dbnsfp['metasvm']['score'])
                                svm_pos = (dbnsfp['metasvm']['score']).index(max(dbnsfp['metasvm']['score']))
                            else:
                                svmsc = dbnsfp['metasvm']['score']
                            if type(dbnsfp['metasvm'].get('pred')) == list:
                                svmpr = (dbnsfp['metasvm']['pred'])[svm_pos]
                                if svmpr == '.':
                                    svmpr = max(dbnsfp['metasvm']['pred'])
                            else:
                                svmpr = dbnsfp['metasvm']['pred']
                        else:
                            svmpr = '.'
                            svmsc = '.'
                        if dbnsfp['metasvm'].get('rankscore'):
                            if type(dbnsfp['metasvm']['rankscore']) == list:
                                svm_rs = max(dbnsfp['metasvm']['rankscore'])

                            else:
                                svm_rs = dbnsfp['metasvm']['rankscore']

                        else:
                            svm_rs = '.'

                        if svmpr == '.' and svmsc == '.' and svm_rs != '.':
                            if dbnsfp['metasvm'].get('score'):
                                svmsc = dbnsfp['metasvm']['score']
                            else:
                                svmsc = '.'
                            if dbnsfp['metasvm'].get('pred'):
                                svmpr = dbnsfp['metasvm']['pred']
                            else:
                                svmpr = '.'

                    else:
                        svmpr = '.'
                        svmsc = '.'
                        svm_rs = '.'
                    if svmpr != '.' and svmsc == '.':
                        svmsc = 0
                    metasvm_pred.append(svmpr)
                    metasvm_score.append(svmsc)
                    metasvm_rankscore.append(svm_rs)
                    (f'MetaSVM Pred : {svmpr}')
                    (f'MetaSVM Score : {svmsc}')
                    (f'MetaSVM Rank Score : {svm_rs}')

                    if dbnsfp.get('metalr'):
                        if dbnsfp['metalr'].get('pred') and dbnsfp['metalr'].get('score'):
                            if type(dbnsfp['metalr']['score']) == list:
                                lrsc = max(dbnsfp['metalr']['score'])
                                lr_pos = (dbnsfp['metalr']['score']).index(max(dbnsfp['metalr']['score']))

                            else:
                                lrsc = dbnsfp['metalr']['score']
                            if type(dbnsfp['metalr'].get('pred')) == list:
                                lrpr = (dbnsfp['metalr']['pred'])[lrt_pos]
                                if lrpr == '.':
                                    lrpr = max(dbnsfp['metalr']['pred'])
                            elif type(dbnsfp['metalr'].get('pred')) != list:
                                lrpr = dbnsfp['metalr']['pred']
                        else:
                            lrpr = '.'
                            lrsc = '.'

                        if dbnsfp['metalr'].get('rankscore'):
                            if type(dbnsfp['metalr']['rankscore']) == list:
                                lr_rs = max(dbnsfp['metalr']['rankscore'])

                            else:
                                lr_rs = dbnsfp['metalr']['rankscore']
                        else:
                            lr_rs = '.'
                        if lrpr == '.' and lrsc == '.' and lr_rs != '.':
                            if dbnsfp['metalr'].get('score'):
                                lrsc = dbnsfp['metalr']['score']
                            else:
                                lrsc = '.'
                            if dbnsfp['metalr'].get('pred'):
                                lrpr = dbnsfp['metalr']['pred']
                            else:
                                lrpr = '.'
                    else:
                        lrpr = '.'
                        lrsc = '.'
                        lr_rs = '.'
                    if lrpr != '.' and lrsc == '.':
                        lrsc = 0
                    metalr_pred.append(lrpr)
                    metalr_score.append(lrsc)
                    MetaLR_rankscore.append(lr_rs)
                    (f"MetaLR_Pred: {lrpr}")
                    (f'MetaLR_Score : {lrsc}')
                    (f'MetaLR_Rank_Score : {lr_rs}')

                    if dbnsfp.get('integrated'):
                        if dbnsfp['integrated'].get('fitcons_score'):

                            if type(dbnsfp['integrated']['fitcons_score']) == list:
                                fitsc = max(dbnsfp['integrated']['fitcons_score'])

                            else:
                                fitsc = dbnsfp['integrated']['fitcons_score']

                        else:
                            fitsc = '.'

                        if dbnsfp['integrated'].get('confidence_value'):
                            if type(dbnsfp['integrated']['confidence_value']) == list:
                                fitcv = max(dbnsfp['integrated']['confidence_value'])

                            else:
                                fitcv = dbnsfp['integrated']['confidence_value']

                        else:
                            fitcv = 0

                        if dbnsfp['integrated'].get('fitcons_rankscore'):
                            if type(dbnsfp['integrated']['fitcons_rankscore']) == list:
                                fitrs = max(dbnsfp['integrated']['fitcons_rankscore'])

                            else:
                                fitrs = dbnsfp['integrated']['fitcons_rankscore']

                        else:
                            fitrs = 0

                    else:
                        fitsc = '.'
                        fitcv = '.'
                        fitrs = '.'
                    (f"Integrated_fitCons_score : {fitsc}")
                    (f"Integrated_confidence_value : {fitcv}")
                    (f"Integrated_fitcons_rankscore: {fitrs}")
                    integ_fitcoin_score.append(fitsc)
                    integ_conf_value.append(fitcv)
                    integ_fitcons_rankscore.append(fitrs)

                    if dbnsfp.get('gerp++'):
                        if dbnsfp['gerp++'].get('rs'):
                            if type(dbnsfp['gerp++']['rs']) == list:
                                rs = max(dbnsfp['gerp++']['rs'])

                            else:
                                rs = dbnsfp['gerp++']['rs']

                        else:
                            rs = '.'
                        if dbnsfp['gerp++'].get('rs_rankscore'):
                            if type(dbnsfp['gerp++']['rs_rankscore']) == list:
                                rs_rank = max(dbnsfp['gerp++']['rs_rankscore'])
                            else:
                                rs_rank = dbnsfp['gerp++']['rs_rankscore']
                        else:
                            rs_rank = '.'


                    else:
                        rs = '.'
                        rs_rank = '.'
                    gerp_rs.append(rs)
                    gerp_rs_rankscore.append(rs_rank)
                    (f"GERP++_RS : {rs}")
                    (f"GERP++_RS : {rs_rank}")

                    if dbnsfp.get('siphy_29way'):
                        if dbnsfp['siphy_29way'].get('logodds'):
                            if type(dbnsfp['siphy_29way']['logodds']) == list:
                                siphy = max(dbnsfp['siphy_29way']['logodds'])

                            else:
                                siphy = dbnsfp['siphy_29way']['logodds']

                        else:
                            siphy = '.'

                        if dbnsfp['siphy_29way'].get('logodds_rankscore'):
                            if type(dbnsfp['siphy_29way']['logodds_rankscore']) == list:
                                siphyrs = max(dbnsfp['siphy_29way']['logodds_rankscore'])

                            else:
                                siphyrs = dbnsfp['siphy_29way']['logodds_rankscore']

                        else:
                            siphyrs = '.'

                    else:
                        siphy = '.'
                        siphyrs = '.'

                    siphy_29way_logOdds.append(siphy)
                    siphy_29way_logOdds_rs.append(siphyrs)
                    (f'Siphy_29way_logOdds : {siphy}')
                    (f'Siphy_29way_logOdds_rankscore : {siphyrs}')

                    if dbnsfp.get('revel'):
                        if dbnsfp['revel'].get('score'):
                            if type(dbnsfp['revel']['score']) == list:
                                revsc = max(dbnsfp['revel']['score'])
                            else:
                                revsc = dbnsfp['revel']['score']
                        else:
                            revsc = '.'
                    else:
                        revsc = '.'
                    revel_score_list.append(revsc)
                    (f'Revel_Score : {revsc}')

                    if dbnsfp.get('eigen'):
                        if dbnsfp['eigen'].get('raw_coding'):
                            if type(dbnsfp['eigen']['raw_coding']) == list:
                                eigen_rc = max(dbnsfp['eigen']['raw_coding'])
                            else:
                                eigen_rc = dbnsfp['eigen']['raw_coding']
                        else:
                            eigen_rc = '.'
                    else:
                        eigen_rc = '.'
                    eigen_rawcoding.append(eigen_rc)
                    (f'Eigen Raw Coding : {eigen_rc}')

                    if dbnsfp.get('phylo'):
                        if dbnsfp['phylo'].get('p100way'):
                            if dbnsfp['phylo']['p100way'].get('vertebrate'):

                                if type(dbnsfp['phylo']['p100way']['vertebrate']) == list:
                                    phylo100way = max(dbnsfp['phylo']['p100way']['vertebrate'])
                                else:
                                    phylo100way = dbnsfp['phylo']['p100way']['vertebrate']
                            else:
                                phylo100way = '.'

                            if dbnsfp['phylo']['p100way'].get('vertebrate_rankscore'):

                                if type(dbnsfp['phylo']['p100way']['vertebrate_rankscore']) == list:
                                    phylo100wayrs = max(dbnsfp['phylo']['p100way']['vertebrate_rankscore'])
                                else:
                                    phylo100wayrs = dbnsfp['phylo']['p100way']['vertebrate_rankscore']
                            else:
                                phylo100wayrs = '.'
                        else:
                            phylo100way = '.'
                            phylo100wayrs = '.'
                        if dbnsfp['phylo'].get('p17way'):
                            if dbnsfp['phylo']['p17way'].get('primate'):
                                if type(dbnsfp['phylo']['p17way']['primate']) == list:
                                    phylo17 = max(dbnsfp['phylo']['p17way']['primate'])
                                else:
                                    phylo17 = dbnsfp['phylo']['p17way']['primate']
                            else:

                                phylo17 = '.'
                            if dbnsfp['phylo']['p17way'].get('primate_rankscore'):
                                if type(dbnsfp['phylo']['p17way']['primate_rankscore']) == list:
                                    phylo17rs = max(dbnsfp['phylo']['p17way']['primate_rankscore'])
                                else:
                                    phylo17rs = dbnsfp['phylo']['p17way']['primate_rankscore']
                            else:

                                phylo17rs = '.'
                        else:
                            phylo17 = '.'
                            phylo17rs = '.'
                        if dbnsfp['phylo'].get('p30way'):
                            if dbnsfp['phylo']['p30way'].get('mammalian'):
                                if type(dbnsfp['phylo']['p30way']['mammalian']) == list:
                                    phylo30 = max(dbnsfp['phylo']['p30way']['mammalian'])
                                else:
                                    phylo30 = dbnsfp['phylo']['p30way']['mammalian']
                            else:

                                phylo30 = '.'
                            if dbnsfp['phylo']['p30way'].get('mammalian_rankscore'):
                                if type(dbnsfp['phylo']['p30way']['mammalian_rankscore']) == list:
                                    phylo30rs = max(dbnsfp['phylo']['p30way']['mammalian_rankscore'])
                                else:
                                    phylo30rs = dbnsfp['phylo']['p30way']['mammalian_rankscore']
                            else:

                                phylo30rs = '.'
                        else:
                            phylo30 = '.'
                            phylo30rs = '.'


                    else:
                        phylo100way = '.'
                        phylo100wayrs = '.'
                        phylo17 = '.'
                        phylo17rs = '.'
                        phylo30 = '.'
                        phylo30rs = '.'
                    phylo100waylist.append(phylo100way)
                    phylo100wayrankscore.append(phylo100wayrs)
                    phylo17waylist.append(phylo17)
                    phylo17rankscore.append(phylo17rs)
                    phylo30waylist.append(phylo30)
                    phylo30rankscore.append(phylo30rs)
                    (f'phylo100way_vertebrate  : {phylo100way}')
                    (f'phylo100way_vertebrateRankscore  : {phylo100wayrs}')
                    (f'phylo17way_primate  : {phylo17}')
                    (f'phylo17way_primate_rankscore  : {phylo17rs}')
                    (f'phylo30way_mammalian  : {phylo30}')
                    (f'phylo30way_mammalian_rankscore  : {phylo30rs}')

                    if dbnsfp.get('phastcons'):
                        if dbnsfp['phastcons'].get('100way'):
                            if dbnsfp['phastcons']['100way'].get('vertebrate'):

                                if type(dbnsfp['phastcons']['100way']['vertebrate']) == list:
                                    phastcons100way = max(dbnsfp['phastcons']['100way']['vertebrate'])
                                else:
                                    phastcons100way = dbnsfp['phastcons']['100way']['vertebrate']
                            else:
                                phastcons100way = '.'

                            if dbnsfp['phastcons']['100way'].get('vertebrate_rankscore'):

                                if type(dbnsfp['phastcons']['100way']['vertebrate_rankscore']) == list:
                                    phastcons100wayrs = max(dbnsfp['phastcons']['100way']['vertebrate_rankscore'])
                                else:
                                    phastcons100wayrs = dbnsfp['phastcons']['100way']['vertebrate_rankscore']
                            else:
                                phastcons100wayrs = '.'
                        else:
                            phastcons100way = '.'
                            phastcons100wayrs = '.'
                        if phastcons100wayrs != '.' and phastcons100way == '.':
                            phastcons100way = 0
                        if dbnsfp['phastcons'].get('p17way'):
                            if dbnsfp['phastcons']['p17way'].get('primate'):
                                if type(dbnsfp['phastcons']['p17way']['primate']) == list:
                                    phastcons17 = max(dbnsfp['phastcons']['p17way']['primate'])
                                else:
                                    phastcons17 = dbnsfp['phastcons']['p17way']['primate']
                            else:

                                phastcons17 = '.'
                            if dbnsfp['phastcons']['p17way'].get('primate_rankscore'):
                                if type(dbnsfp['phastcons']['p17way']['primate_rankscore']) == list:
                                    phastcons17rs = max(dbnsfp['phastcons']['p17way']['primate_rankscore'])
                                else:
                                    phastcons17rs = dbnsfp['phastcons']['p17way']['primate_rankscore']
                            else:

                                phastcons17rs = '.'
                        else:
                            phastcons17 = '.'
                            phastcons17rs = '.'
                        if phastcons17rs != '.' and phastcons17 == '.':
                            phastcons17 = 0
                        if dbnsfp['phastcons'].get('30way'):
                            if dbnsfp['phastcons']['30way'].get('mammalian'):
                                if type(dbnsfp['phastcons']['30way']['mammalian']) == list:
                                    phastcons30 = max(dbnsfp['phastcons']['30way']['mammalian'])
                                else:
                                    phastcons30 = dbnsfp['phastcons']['30way']['mammalian']
                            else:

                                phastcons30 = '.'
                            if dbnsfp['phastcons']['30way'].get('mammalian_rankscore'):
                                if type(dbnsfp['phastcons']['30way']['mammalian_rankscore']) == list:
                                    phastcons30rs = max(dbnsfp['phastcons']['30way']['mammalian_rankscore'])
                                else:
                                    phastcons30rs = dbnsfp['phastcons']['30way']['mammalian_rankscore']
                            else:

                                phastcons30rs = '.'
                        else:
                            phastcons30 = '.'
                            phastcons30rs = '.'
                        if phastcons30rs != '.' and phastcons30 == '.':
                            phastcons30 = 0


                    else:
                        phastcons100way = '.'
                        phastcons100wayrs = '.'
                        phastcons17 = '.'
                        phastcons17rs = '.'
                        phastcons30 = '.'
                        phastcons30rs = '.'
                    phastcons100waylist.append(phastcons100way)
                    phastcons100wayrankscore.append(phastcons100wayrs)
                    phastcons17waylist.append(phastcons17)
                    phastcons17rankscore.append(phastcons17rs)
                    phastcons30waylist.append(phastcons30)
                    phastcons30rankscore.append(phastcons30rs)
                    (f'phastcons100way_vertebrate  : {phastcons100way}')
                    (f'phastcons100way_vertebrateRankscore  : {phastcons100wayrs}')
                    (f'phastcons17way_primate  : {phastcons17}')
                    (f'phastcons17way_primate_rankscore  : {phastcons17rs}')
                    (f'phastcons30way_mammalian  : {phastcons30}')
                    (f'phastcons30way_mammalian_rankscore  : {phastcons30rs}')

                    if dbnsfp.get('eigen-pc'):
                        if dbnsfp['eigen-pc'].get('raw_coding'):
                            if type(dbnsfp['eigen-pc']['raw_coding']) == list:
                                eigenpc_rc = max(dbnsfp['eigen-pc']['raw_coding'])
                            else:
                                eigenpc_rc = dbnsfp['eigen-pc']['raw_coding']
                        else:
                            eigenpc_rc = '.'
                    else:
                        eigenpc_rc = '.'
                    eigen_pc_rawcoding.append(eigenpc_rc)
                    (f'Eigen-pc Raw Coding : {eigenpc_rc}')

                    if dbnsfp.get('interpro_domain'):
                        if type(dbnsfp['interpro_domain']) == list:
                            interpro = max(dbnsfp['interpro_domain'])
                        else:
                            interpro = dbnsfp['interpro_domain']
                    else:
                        interpro = '.'
                    interpro_domain.append(interpro)
                    (f'Interpro_DOmain : {interpro}')
                    gene = ''
                    tissue = ''
                    if dbnsfp.get('gtex'):

                        if type(dbnsfp['gtex']) == list:

                            for i in dbnsfp['gtex']:
                                gene += i['gene'] + ' | '
                                tissue += i['tissue'] + ' | '

                        elif type(dbnsfp['gtex']) == dict:
                            gene += dbnsfp['gtex']['gene'] + "  "
                            tissue += dbnsfp['gtex']['tissue'] + '  '
                        else:
                            gene += '.  '
                            tissue += '.  '
                    else:
                        gene += '.  '
                        tissue += '.  '

                    GTEx_gene.append(gene[:-2])
                    GTEx_tissue.append(tissue[:-2])
                    (f'GTEx_gene {gene[:-2]}')
                    (f'GTEx_tissue{tissue[:-2]}')






                else:
                    sift_pred.append('.')
                    sift_score.append('.')
                    sift_converted_rs.append('.')
                    polyphen2_HDIV_Pred.append('.')
                    polyphen2_HDIV_Score.append('.')
                    polyphen2_HVAR_Pred.append('.')
                    polyphen2_HVAR_Score.append('.')
                    lrt_pred.append('.')
                    lrt_score.append('.')
                    lrt_converted_rs.append('.')
                    mut_assessor_pred.append('.')
                    mut_assessor_score.append('.')
                    mutationassessor_rs.append('.')
                    mut_taster_pred.append('.')
                    mut_taster_score.append('.')
                    MutationTaster_converted_rs.append('.')
                    provean_pred.append('.')
                    provean_score.append('.')
                    provean_rs.append('.')
                    dann_score.append('.')
                    fathmm_pred.append('.')
                    fathmm_score.append('.')
                    fathmm_rs.append('.')
                    fathmm_mkl_pred.append('.')
                    fathmm_mkl_score.append('.')
                    fathmm_mkl_rankscore.append('.')
                    metasvm_pred.append('.')
                    metasvm_score.append('.')
                    metasvm_rankscore.append('.')
                    metalr_pred.append('.')
                    metalr_score.append('.')
                    MetaLR_rankscore.append('.')
                    integ_fitcoin_score.append('.')
                    integ_conf_value.append('.')
                    integ_fitcons_rankscore.append('.')
                    gerp_rs.append('.')
                    gerp_rs_rankscore.append('.')
                    siphy_29way_logOdds.append('.')
                    siphy_29way_logOdds_rs.append('.')
                    revel_score_list.append('.')
                    genoCanyon_score.append('.')
                    genoCanyon_rankscore.append('.')
                    eigen_rawcoding.append('.')
                    eigen_pc_rawcoding.append('.')
                    phylo100waylist.append('.')
                    phylo100wayrankscore.append('.')
                    phylo17waylist.append('.')
                    phylo17rankscore.append('.')
                    phylo30waylist.append('.')
                    phylo30rankscore.append('.')
                    phastcons100waylist.append('.')
                    phastcons100wayrankscore.append('.')
                    phastcons17waylist.append('.')
                    phastcons17rankscore.append('.')
                    phastcons30waylist.append('.')
                    phastcons30rankscore.append('.')
                    interpro_domain.append('.')
                    GTEx_gene.append('.')
                    GTEx_tissue.append('.')
                    siftsc = '.'
                    sift_pos = '.'
                    siftpred = '.'
                    sift_converted_rankscore = '.'
                    hdivsc = '.'
                    hdiv_pos = '.'
                    hdivpr = '.'
                    hdivrank = '.'
                    hvarpos = '.'
                    hvarsc = '.'
                    hvarpr = '.'
                    hvarrank = '.'
                    lrtsc = '.'
                    lrt_pos = '.'
                    lrtpr = '.'
                    lrt_converted_rankscore = '.'
                    asssc = '.'
                    ass_pos = '.'
                    asspr = '.'
                    mutationassessor_rankscore = '.'
                    tassc = '.'
                    taspr = '.'
                    MutationTaster_converted_rankscore = '.'
                    genoscore = '.'
                    geno_rs = '.'
                    provsc = '.'
                    prov_pos = '.'
                    provpr = '.'
                    prov_rs = '.'
                    provsc = '.'
                    dann = '.'
                    faths = '.'
                    fath_pos = '.'
                    fathp = '.'
                    fathrs = '.'
                    fathsc = '.'
                    fathm_pos = '.'
                    fathpr = '.'
                    fathcoding_rs = '.'
                    svmsc = '.'
                    svm_pos = '.'
                    svmpr = '.'
                    svm_rs = '.'
                    lrsc = '.'
                    lr_pos = '.'
                    lrpr = '.'
                    lr_rs = '.'
                    fitsc = '.'
                    fitcv = '.'
                    fitrs = '.'
                    rs = '.'
                    rs_rank = '.'
                    siphy = '.'
                    siphyrs = '.'
                    revsc = '.'
                    eigen_rc = '.'
                    phylo100way = '.'
                    phylo100wayrs = '.'
                    phylo17 = '.'
                    phylo17rs = '.'
                    phylo30 = '.'
                    phylo30rs = '.'
                    phastcons100way = '.'
                    phastcons100wayrs = '.'
                    phastcons17 = '.'
                    phastcons17rs = '.'
                    phastcons30 = '.'
                    phastcons30rs = '.'
                    eigenpc_rc = '.'
                    interpro = '.'
                    gene = '.'
                    tissue = '.'

                if m.get('cadd'):
                    # (f"{i} : {m[i]}")
                    CADD = m['cadd']
                    if CADD.get('rawscore'):
                        if type(CADD['rawscore']) == list:
                            CADDraw = max(CADD['rawscore'])
                        else:
                            CADDraw = CADD['rawscore']
                    else:
                        CADDraw = '.'
                    CADD_raw_list.append(CADDraw)
                    (f"CADD RAW Score : {CADDraw}")

                    if CADD.get('phred'):
                        if type(CADD['phred']) == list:
                            CADDp = max(CADD['phred'])
                        else:
                            CADDp = CADD['phred']
                    else:
                        CADDp = '.'
                    CADD_phred_list.append(CADDp)
                    (f"CADD Phred : {CADDp}")

                else:
                    CADD_raw_list.append('.')
                    CADD_phred_list.append('.')
                    CADDraw = '.'
                    CADDp = '.'

        except Exception as es:
            self.error_str = es

        self.root = root
        self.root.title('VCESS-dbNSFP')
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

        frame1 = Frame(self.root, bg='#90ce2b')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#90ce2b',
                      fg='white')
        title.place(x=380, y=45)

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#90ce2b', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')
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

        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 14, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=95, y=42)
        url = 'http://database.liulab.science/dbNSFP'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="http://database.liulab.science/dbNSFP",
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
                                  text=f"dbNSFP is a database developed for functional\n"
                                       f"prediction and annotation of all potential non-\n"
                                       f"synonymous single-nucleotide variants (nsSNVs) \n"
                                       f"in the human genome. Its current version is based\n"
                                       f"on the Gencode release 29 / Ensembl version 94 and\n"
                                       f"includes a total of 84,013,490 nsSNVs and ssSNVs \n"
                                       f"(splicing-site SNVs). It compiles prediction scores\n"
                                       f" from 37 prediction algorithms",
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

            ###########################
            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
            # table = ttk.Treeview(table1, height="8")  #################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420) ###################
            table = ttk.Treeview(table1, height="50")

            table['columns'] = ['Searched_ID', 'Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore',
                                'Polyphen2_HDIV_Pred',
                                'Polyphen2_HDIV_Score',
                                'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                'LRT_converted_rankScore',
                                'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                'Mutation_Taster_Pred',
                                'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                'Provean_Score', 'Provean_Rank_score',
                                'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                'Fathmm-mkl_Score',
                                'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                'MetaLR_Pred', 'MetaLR_Score',
                                'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                'Integrated_fitcons_rankscore',
                                'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                'siphy_29way_logOdds_rankscore',
                                'Revel_Score',
                                'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                'phylo30rankscore',
                                'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                'phastcons17rankscore', 'phastcons30waylist',
                                'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

            table.column('#0', width=120, minwidth=120)
            table.column('Searched_ID', anchor=CENTER, width=150)
            table.column('Sift_Pred', anchor=CENTER, width=120)
            table.column('Sift_Score', anchor=CENTER, width=120)
            table.column('Sift_converted_rankScore', anchor=CENTER, width=120)
            table.column('Polyphen2_HDIV_Pred', anchor=CENTER, width=120)
            table.column('Polyphen2_HDIV_Score', anchor=CENTER, width=120)
            table.column('Polyphen2_HVAR_Pred', anchor=CENTER, width=120)
            table.column('Polyphen2_HVAR_Score', anchor=CENTER, width=120)
            table.column('LRT_Pred', anchor=CENTER, width=120)
            table.column('LRT_Score', anchor=CENTER, width=120)
            table.column('LRT_converted_rankScore', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_Pred', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_Score', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_rankscore', anchor=CENTER, width=120)
            table.column('Mutation_Taster_Pred', anchor=CENTER, width=120)
            table.column('Mutation_Taster_Score', anchor=CENTER, width=120)
            table.column('MutationTaster_converted_rankscore', anchor=CENTER, width=120)
            table.column('Provean_Pred', anchor=CENTER, width=120)
            table.column('Provean_Score', anchor=CENTER, width=120)
            table.column('Provean_Rank_score', anchor=CENTER, width=120)
            table.column('DANN Score', anchor=CENTER, width=120)
            table.column('Fathmm_Pred', anchor=CENTER, width=120)
            table.column('Fathmm_Score', anchor=CENTER, width=120)
            table.column('fathmm_Rank_Score', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_Pred', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_Score', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_RankScore', anchor=CENTER, width=120)
            table.column('MetaSVM_Pred', anchor=CENTER, width=120)
            table.column('MetaSVM_Score', anchor=CENTER, width=120)
            table.column('Meta_SVM_Rank_Score', anchor=CENTER, width=120)
            table.column('MetaLR_Pred', anchor=CENTER, width=120)
            table.column('MetaLR_Score', anchor=CENTER, width=120)
            table.column('MetaLR_Rank_Score', anchor=CENTER, width=120)
            table.column('Integrated_fitCons_score', anchor=CENTER, width=120)
            table.column('Integrated_confidence_value', anchor=CENTER, width=120)
            table.column('Integrated_fitcons_rankscore', anchor=CENTER, width=120)
            table.column('GERP++_RS', anchor=CENTER, width=120)
            table.column('GERP++_RS_Rankscore', anchor=CENTER, width=120)
            table.column('Siphy_29way_logOdds', anchor=CENTER, width=120)
            table.column('siphy_29way_logOdds_rankscore', anchor=CENTER, width=120)
            table.column('Revel_Score', anchor=CENTER, width=120)
            table.column('CADD_raw_score', anchor=CENTER, width=120)
            table.column('CADD_Phred', anchor=CENTER, width=120)
            table.column('genoCanyon_score', anchor=CENTER, width=120)
            table.column('genoCanyon_rankscore', anchor=CENTER, width=120)
            table.column("Eigen_Raw_coding", anchor=CENTER, width=120)
            table.column("Eigen-pc_Raw_coding", anchor=CENTER, width=120)
            table.column('phylo100way', anchor=CENTER, width=120)
            table.column('phylo100wayrankscore', anchor=CENTER, width=120)
            table.column('phylo17way', anchor=CENTER, width=120)
            table.column('phylo17rankscore', anchor=CENTER, width=120)
            table.column('phylo30way', anchor=CENTER, width=120)
            table.column('phylo30rankscore', anchor=CENTER, width=120)
            table.column('phastcons100waylist', anchor=CENTER, width=120)
            table.column('phastcons100wayrankscore', anchor=CENTER, width=120)
            table.column('phastcons17waylist', anchor=CENTER, width=120)
            table.column('phastcons17rankscore', anchor=CENTER, width=120)
            table.column('phastcons30waylist', anchor=CENTER, width=120)
            table.column('phastcons30rankscore', anchor=CENTER, width=120)
            table.column('Interpro_Domain', anchor=CENTER, width=120)
            table.column('GTEx_gene', anchor=CENTER, width=120)
            table.column('GTEx_tisuue', anchor=CENTER, width=200)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('Searched_ID', text='Searched_ID', anchor=W)
            table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
            table.heading('Sift_Score', text='Sift_Score', anchor=W)
            table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
            table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
            table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
            table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
            table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
            table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
            table.heading('LRT_Score', text='LRT_Score', anchor=W)
            table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
            table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
            table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
            table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
            table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
            table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
            table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
            table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
            table.heading('Provean_Score', text='Provean_Score', anchor=W)
            table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
            table.heading('DANN Score', text='DANN Score', anchor=W)
            table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
            table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
            table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
            table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
            table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
            table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
            table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
            table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
            table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
            table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
            table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
            table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
            table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
            table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
            table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
            table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
            table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
            table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
            table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
            table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
            table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
            table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
            table.heading('Revel_Score', text='Revel_Score', anchor=W)
            table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
            table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
            table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
            table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
            table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
            table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
            table.heading('phylo100way', text='phylo100way', anchor=W)
            table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
            table.heading('phylo17way', text='phylo17way', anchor=W)
            table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
            table.heading('phylo30way', text='phylo30way', anchor=W)
            table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
            table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
            table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
            table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
            table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
            table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
            table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
            table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
            table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
            table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

            for i in range(len(sift_pred)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(search_id, sift_pred[i],
                                     sift_score[i],
                                     sift_converted_rs[i],
                                     polyphen2_HDIV_Pred[i],
                                     polyphen2_HDIV_Score[i],
                                     polyphen2_HVAR_Pred[i],
                                     polyphen2_HVAR_Score[i],
                                     lrt_pred[i],
                                     lrt_score[i],
                                     lrt_converted_rs[i],
                                     mut_assessor_pred[i],
                                     mut_assessor_score[i],
                                     mutationassessor_rs[i],
                                     mut_taster_pred[i],
                                     mut_taster_score[i],
                                     MutationTaster_converted_rs[i],
                                     provean_pred[i],
                                     provean_score[i],
                                     provean_rs[i],
                                     dann_score[i],
                                     fathmm_pred[i],
                                     fathmm_score[i],
                                     fathmm_rs[i],
                                     fathmm_mkl_pred[i],
                                     fathmm_mkl_score[i],
                                     fathmm_mkl_rankscore[i],
                                     metasvm_pred[i],
                                     metasvm_score[i],
                                     metasvm_rankscore[i],
                                     metalr_pred[i],
                                     metalr_score[i],
                                     MetaLR_rankscore[i],
                                     integ_fitcoin_score[i],integ_conf_value[i],
                                     integ_fitcons_rankscore[i],

                                     gerp_rs[i],
                                     gerp_rs_rankscore[i],
                                     siphy_29way_logOdds[i],
                                     siphy_29way_logOdds_rs[i],
                                     revel_score_list[i],
                                     CADD_raw_list[i],
                                     CADD_phred_list[i],
                                     genoCanyon_rankscore[i],
                                     genoCanyon_score[i],
                                     eigen_rawcoding[i],
                                     eigen_pc_rawcoding[i],
                                     phylo100waylist[i],
                                     phylo100wayrankscore[i],
                                     phylo17waylist[i],
                                     phylo17rankscore[i],
                                     phylo30waylist[i],
                                     phylo30rankscore[i],
                                     phastcons100waylist[i],
                                     phastcons100wayrankscore[i],
                                     phastcons17waylist[i],
                                     phastcons17rankscore[i],
                                     phastcons30waylist[i],
                                     phastcons30rankscore[i],
                                     interpro_domain[i],
                                     GTEx_gene[i],
                                     GTEx_tissue[i]

                                     ))

            # table.place(x=0, y=0)  ##########################
            # VERTICAL SCROLLBAR
            yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
            yscrollbar.pack(side=RIGHT, fill='y')  ##################

            # HORIZONTAL SCROLLBAR
            xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
            xscrollbar.pack(side=BOTTOM, fill='x')  #######################

            table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
            table.pack(side=LEFT)  ##################
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
        sift_pred.clear()
        sift_score.clear()
        sift_converted_rs.clear()
        polyphen2_HDIV_Pred.clear()
        polyphen2_HDIV_Score.clear()
        polyphen2_HVAR_Pred.clear()
        polyphen2_HVAR_Score.clear()
        lrt_pred.clear()
        lrt_score.clear()
        lrt_converted_rs.clear()
        mut_assessor_pred.clear()
        mut_assessor_score.clear()
        mutationassessor_rs.clear()
        mut_taster_pred.clear()
        mut_taster_score.clear()
        MutationTaster_converted_rs.clear()
        provean_pred.clear()
        provean_score.clear()
        provean_rs.clear()
        dann_score.clear()
        fathmm_pred.clear()
        fathmm_score.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        fathmm_mkl_rankscore.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_fitcons_rankscore.clear()
        integ_conf_value.clear()
        gerp_rs.clear()
        gerp_rs_rankscore.clear()
        siphy_29way_logOdds.clear()
        siphy_29way_logOdds_rs.clear()
        revel_score_list.clear()
        CADD_raw_list.clear()
        CADD_phred_list.clear()
        genoCanyon_rankscore.clear()
        genoCanyon_score.clear()
        eigen_rawcoding.clear()
        eigen_pc_rawcoding.clear()
        phylo100waylist.clear()
        phylo100wayrankscore.clear()
        phylo17waylist.clear()
        phylo17rankscore.clear()
        phylo30waylist.clear()
        phylo30rankscore.clear()
        phastcons100waylist.clear()
        phastcons100wayrankscore.clear()
        phastcons17waylist.clear()
        phastcons17rankscore.clear()
        phastcons30waylist.clear()
        phastcons30rankscore.clear()
        interpro_domain.clear()
        GTEx_gene.clear()
        GTEx_tissue.clear()
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
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 16, "bold", "italic"),
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
        p = 20

        progress['value'] = p

        self.root1.update_idletasks()

        # time.sleep(0.1)
        self.root1.after(100)  # Delay in millisecs.
        p = p + 40

        try:
            self.m = mv.getvariant(search_id, assembly='hg38')
            m = self.m

            if m == None:
                sift_pred.append('.')
                sift_score.append('.')
                sift_converted_rs.append('.')
                polyphen2_HDIV_Pred.append('.')
                polyphen2_HDIV_Score.append('.')
                polyphen2_HVAR_Pred.append('.')
                polyphen2_HVAR_Score.append('.')
                lrt_pred.append('.')
                lrt_score.append('.')
                lrt_converted_rs.append('.')
                mut_assessor_pred.append('.')
                mut_assessor_score.append('.')
                mutationassessor_rs.append('.')
                mut_taster_pred.append('.')
                mut_taster_score.append('.')
                MutationTaster_converted_rs.append('.')
                provean_pred.append('.')
                provean_score.append('.')
                provean_rs.append('.')
                dann_score.append('.')
                fathmm_pred.append('.')
                fathmm_score.append('.')
                fathmm_mkl_rankscore.append('.')
                fathmm_rs.append('.')
                fathmm_mkl_pred.append('.')
                fathmm_mkl_score.append('.')
                metasvm_pred.append('.')
                metasvm_score.append('.')
                metasvm_rankscore.append('.')
                metalr_pred.append('.')
                metalr_score.append('.')
                MetaLR_rankscore.append('.')
                integ_fitcoin_score.append('.')
                integ_conf_value.append('.')
                integ_fitcons_rankscore.append('.')
                gerp_rs.append('.')
                gerp_rs_rankscore.append('.')
                siphy_29way_logOdds.append('.')
                siphy_29way_logOdds_rs.append('.')
                revel_score_list.append('.')
                CADD_raw_list.append('.')
                CADD_phred_list.append('.')
                genoCanyon_rankscore.append('.')
                genoCanyon_score.append('.')
                eigen_rawcoding.append('.')
                eigen_pc_rawcoding.append('.')
                phylo100waylist.append('.')
                phylo100wayrankscore.append('.')
                phylo17waylist.append('.')
                phylo17rankscore.append('.')
                phylo30waylist.append('.')
                phylo30rankscore.append('.')
                phastcons100waylist.append('.')
                phastcons100wayrankscore.append('.')
                phastcons17waylist.append('.')
                phastcons17rankscore.append('.')
                phastcons30waylist.append('.')
                phastcons30rankscore.append('.')
                interpro_domain.append('.')
                GTEx_gene.append('.')
                GTEx_tissue.append('.')


            else:
                if m.get('dbnsfp'):

                    dbnsfp = m['dbnsfp']

                    for key, item in dbnsfp.items():
                        (f"{key} : {item}")
                    if dbnsfp.get('sift'):

                        if dbnsfp['sift'].get('score') and dbnsfp['sift'].get('pred'):
                            if type(dbnsfp['sift']['score']) == list:
                                siftsc = max(dbnsfp['sift']['score'])
                                sift_pos = (dbnsfp['sift']['score']).index(max(dbnsfp['sift']['score']))

                            else:
                                siftsc = (dbnsfp['sift']['score'])

                            if type(dbnsfp['sift']['pred']) == list:
                                siftpred = (dbnsfp['sift']['pred'])[sift_pos]
                                if siftpred == '.':
                                  siftpred=  (max(dbnsfp['sift']['pred']))
                            else:
                                siftpred = dbnsfp['sift']['pred']
                        else:
                            siftsc = '.'
                            siftpred = '.'
                        if dbnsfp['sift'].get('converted_rankscore'):
                            if type(dbnsfp['sift'].get('converted_rankscore')) == list:
                                sift_converted_rankscore = max(dbnsfp['sift']['converted_rankscore'])
                            else:
                                sift_converted_rankscore = dbnsfp['sift']['converted_rankscore']
                        else:
                            sift_converted_rankscore = '.'
                        if siftsc == '.' and siftpred == '.' and sift_converted_rankscore != '.':
                            if dbnsfp['sift'].get('score'):

                                siftsc = (dbnsfp['sift']['score'])
                            else:
                                siftsc = '.'
                            if dbnsfp['sift'].get('pred'):
                                siftpred = dbnsfp['sift']['pred']
                            else:
                                siftpred = '.'

                    else:
                        siftsc = '.'
                        siftpred = '.'
                        sift_converted_rankscore = '.'

                    if (siftpred != '.') and siftsc == '.':
                        siftsc = 0
                    sift_pred.append(siftpred)
                    sift_score.append(siftsc)
                    sift_converted_rs.append(sift_converted_rankscore)

                    (f"SIFT Pred : {siftpred}")
                    (f'SIFT Score : {siftsc}')
                    (f'Sift_converted_rankscore : {sift_converted_rankscore}')

                    if dbnsfp.get('polyphen2'):
                        if dbnsfp['polyphen2'].get('hdiv'):

                            if dbnsfp['polyphen2']['hdiv'].get('score') and dbnsfp['polyphen2']['hdiv'].get('pred'):

                                if type(dbnsfp['polyphen2']['hdiv']['score']) == list:
                                    hdivsc = max(dbnsfp['polyphen2']['hdiv']['score'])
                                    hdiv_pos = (dbnsfp['polyphen2']['hdiv']['score']).index(
                                        max(dbnsfp['polyphen2']['hdiv']['score']))


                                else:
                                    hdivsc = dbnsfp['polyphen2']['hdiv']['score']

                                if dbnsfp['polyphen2']['hdiv'].get('pred'):
                                    if type(dbnsfp['polyphen2']['hdiv'].get('pred')) == list:
                                        hdivpr = (dbnsfp['polyphen2']['hdiv']['pred'])[hdiv_pos]
                                        if hdivpr == '.':
                                            hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])


                                    else:
                                        hdivpr = dbnsfp['polyphen2']['hdiv']['pred']
                            else:
                                hdivpr = '.'
                                hdivsc = '.'

                            if dbnsfp['polyphen2']['hdiv'].get('rankscore'):
                                hdivrank = dbnsfp['polyphen2']['hdiv']['rankscore']
                            else:
                                hdivrank = '.'

                            if hdivpr == '.' and hdivsc == '.' and hdivrank != '.':
                                if dbnsfp['polyphen2']['hdiv'].get('score'):
                                    hdivsc = dbnsfp['polyphen2']['hdiv']['score']
                                else:
                                    hdivsc = '.'
                                if dbnsfp['polyphen2']['hdiv'].get('pred'):

                                    hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])
                                else:
                                    hdivpr = '.'

                                if hdivsc == '.' and hdivpr != '.':
                                    hdivsc = 0

                        else:
                            hdivsc = '.'
                            hdivpr = '.'

                        if dbnsfp['polyphen2'].get('hvar'):
                            (dbnsfp['polyphen2'])
                            if dbnsfp['polyphen2']['hvar'].get('pred') and dbnsfp['polyphen2']['hvar'].get('score'):

                                if type(dbnsfp['polyphen2']['hvar']['score']) == list:
                                    hvarsc = max(dbnsfp['polyphen2']['hvar']['score'])
                                    hvarpos = (dbnsfp['polyphen2']['hvar']['score']).index(
                                        max(dbnsfp['polyphen2']['hvar']['score']))

                                else:
                                    hvarsc = dbnsfp['polyphen2']['hvar']['score']

                                if type(dbnsfp['polyphen2']['hvar'].get('pred')) == list:
                                    hvarpr = (dbnsfp['polyphen2']['hvar']['pred'])[hvarpos]
                                    if hvarpr == '.':
                                        hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])

                                elif type(dbnsfp['polyphen2']['hvar'].get('pred')) != list:
                                    hvarpr = dbnsfp['polyphen2']['hvar']['pred']
                            else:
                                hvarsc = '.'
                                hvarpr = '.'

                            if dbnsfp['polyphen2']['hvar'].get('rankscore'):
                                hvarrank = dbnsfp['polyphen2']['hvar']['rankscore']
                            else:
                                hvarrank = '.'

                            if hvarpr == '.' and hvarsc == '.' and hvarrank != '.':
                                if dbnsfp['polyphen2']['hvar'].get('score'):
                                    hvarsc = dbnsfp['polyphen2']['hvar']['score']
                                else:
                                    hvarsc = '.'
                                if dbnsfp['polyphen2']['hvar'].get('pred'):

                                    hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])
                                else:
                                    hvarpr = '.'

                                if hvarsc == '.' and hvarpr != '.':
                                    hvarsc = 0



                        else:

                            hvarsc = '.'
                            hvarpr = '.'

                    else:
                        hdivsc = '.'
                        hdivpr = '.'
                        hvarpr = '.'
                        hvarsc = '.'
                    if hdivpr != '.' and hdivsc == '.':
                        hdivsc = 0
                    if hvarpr != '.' and hvarsc == '.':
                        hvarsc = 0
                    polyphen2_HDIV_Pred.append(hdivpr)
                    polyphen2_HDIV_Score.append(hdivsc)
                    polyphen2_HVAR_Score.append(hvarsc)
                    polyphen2_HVAR_Pred.append(hvarpr)
                    (f'Polyphen2 HDIV Pred : {hdivpr}')
                    (f'Polyphen2 HDIV Score : {hdivsc}')
                    (f'Polyphen2 HVAR Pred : {hvarpr}')
                    (f'Polyphen2 HVAR Score : {hvarsc}')

                    if dbnsfp.get('lrt'):

                        if dbnsfp['lrt'].get('score') and dbnsfp['lrt'].get('pred'):

                            if type(dbnsfp['lrt'].get('score')) == list:
                                lrtsc = max(dbnsfp['lrt']['score'])
                                lrt_pos = (dbnsfp['lrt']['score']).index(max(dbnsfp['lrt']['score']))

                            else:
                                lrtsc = dbnsfp['lrt']['score']
                                (f'score : {lrtsc}')

                            if type(dbnsfp['lrt'].get('pred')) == list:

                                lrtpr = (dbnsfp['lrt']['pred'])[lrt_pos]
                                if lrtpr == '.':
                                    lrtpr = max(dbnsfp['lrt']['pred'])
                            else:
                                lrtpr = dbnsfp['lrt']['pred']

                        else:
                            lrtsc = '.'
                            lrtpr = '.'

                        if dbnsfp['lrt'].get('converted_rankscore'):

                            if type(dbnsfp['lrt'].get('converted_rankscore')) == list:
                                lrt_converted_rankscore = max(dbnsfp['lrt']['converted_rankscore'])

                            elif type(dbnsfp['lrt'].get('converted_rankscore')) != list:
                                lrt_converted_rankscore = dbnsfp['lrt']['converted_rankscore']

                        else:
                            lrt_converted_rankscore = '.'

                        if lrtpr == '.' and lrtsc == '.' and lrt_converted_rankscore != '.':
                            if dbnsfp['lrt'].get('score'):

                                lrtsc = dbnsfp['lrt']['score']
                                (f'score : {lrtsc}')
                            else:
                                lrtsc = '.'

                            if dbnsfp['lrt'].get('pred'):
                                lrtpr = dbnsfp['lrt']['pred']
                            else:
                                lrtpr = '.'




                    else:
                        lrtsc = '.'
                        lrtpr = '.'
                        lrt_converted_rankscore = '.'
                    if (lrtpr != '.') and lrtsc == '.':
                        lrtsc = 0

                    lrt_pred.append(lrtpr)
                    lrt_score.append(lrtsc)
                    lrt_converted_rs.append(lrt_converted_rankscore)
                    (f"LRT Pred : {lrtpr}")
                    (f'LRT Score : {lrtsc}')
                    (f'lrt_converted_rankscore : {lrt_converted_rankscore}')

                    if dbnsfp.get('mutationassessor'):
                        if dbnsfp['mutationassessor'].get('score') and dbnsfp['mutationassessor'].get('pred'):
                            if type(dbnsfp['mutationassessor']['score']) == list:
                                asssc = max(dbnsfp['mutationassessor']['score'])
                                ass_pos = (dbnsfp['mutationassessor']['score']).index(
                                    max(dbnsfp['mutationassessor']['score']))
                            else:
                                asssc = dbnsfp['mutationassessor']['score']

                            if type(dbnsfp['mutationassessor'].get('pred')) == list:

                                asspr = (dbnsfp['mutationassessor']['pred'])[ass_pos]
                                if asspr == '.':
                                    asspr = max(dbnsfp['mutationassessor']['pred'])

                            else:
                                asspr = dbnsfp['mutationassessor']['pred']

                        else:
                            asspr = '.'
                            asssc = '.'

                        if dbnsfp['mutationassessor'].get('rankscore'):
                            if type(dbnsfp['mutationassessor']['rankscore']) == list:
                                mutationassessor_rankscore = max(dbnsfp['mutationassessor']['rankscore'])
                            else:
                                mutationassessor_rankscore = dbnsfp['mutationassessor']['rankscore']
                        else:
                            mutationassessor_rankscore = '.'

                        if asspr == '.' and asssc == '.' and mutationassessor_rankscore != '.':
                            if dbnsfp['mutationassessor'].get('score'):
                                asssc = dbnsfp['mutationassessor']['score']
                            else:
                                asssc = '.'

                            if dbnsfp['mutationassessor'].get('pred'):
                                asspr = dbnsfp['mutationassessor']['pred']
                            else:
                                asspr = '.'

                    else:
                        asspr = '.'
                        asssc = '.'
                        mutationassessor_rankscore = '.'

                    if asssc == '.' and asspr != '.':
                        asssc = 0

                    mut_assessor_pred.append(asspr)
                    mut_assessor_score.append(asssc)
                    mutationassessor_rs.append(mutationassessor_rankscore)
                    (f'Mutation Assessor Pred : {asspr}')
                    (f'Mutation Assessor Score : {asssc}')
                    (f'Mutation Assessor RankScore : {mutationassessor_rankscore}')

                    if dbnsfp.get('mutationtaster'):

                        if dbnsfp['mutationtaster'].get('score') and dbnsfp['mutationtaster'].get('pred'):
                            if type(dbnsfp['mutationtaster']['score']) == list:
                                tassc = max(dbnsfp['mutationtaster']['score'])
                                position = (dbnsfp['mutationtaster']['score']).index(
                                    max(dbnsfp['mutationtaster']['score']))
                                # (index)
                                # (type(dbnsfp['mutationtaster']['score']))

                            else:
                                tassc = dbnsfp['mutationtaster']['score']

                            if type(dbnsfp['mutationtaster'].get('pred')) == list:
                                # taspr = max(dbnsfp['mutationtaster']['pred'])

                                taspr = (dbnsfp['mutationtaster']['pred'])[position]
                                if taspr == '.':
                                    taspr = max(dbnsfp['mutationtaster']['pred'])

                            else:
                                taspr = dbnsfp['mutationtaster']['pred']


                        else:
                            taspr = '.'
                            tassc = '.'

                        if dbnsfp['mutationtaster'].get('converted_rankscore'):
                            if type(dbnsfp['mutationtaster'].get('converted_rankscore')) == list:
                                # taspr = max(dbnsfp['mutationtaster']['pred'])
                                MutationTaster_converted_rankscore = (dbnsfp['mutationtaster']['converted_rankscore'])[
                                    position]
                            elif type(dbnsfp['mutationtaster'].get('converted_rankscore')) != list:
                                MutationTaster_converted_rankscore = dbnsfp['mutationtaster']['converted_rankscore']

                        else:
                            MutationTaster_converted_rankscore = '.'

                        if taspr == '.' and tassc == '.' and MutationTaster_converted_rankscore != '.':
                            if dbnsfp['mutationtaster'].get('score'):

                                tassc = dbnsfp['mutationtaster']['score']
                            else:
                                tassc = '.'

                            if dbnsfp['mutationtaster'].get('pred'):

                                taspr = dbnsfp['mutationtaster']['pred']
                            else:
                                taspr = '.'
                    else:

                        taspr = '.'
                        tassc = '.'
                        MutationTaster_converted_rankscore = '.'
                    if tassc == '.' and taspr != '.':
                        tassc = 0
                    (f'Mutation Taster Pred : {taspr}')
                    (f'Mutation Taster Score : {tassc}')
                    (f'Mutation Taster Converted rankscore : {MutationTaster_converted_rankscore}')
                    mut_taster_pred.append(taspr)
                    mut_taster_score.append(tassc)
                    MutationTaster_converted_rs.append(MutationTaster_converted_rankscore)

                    if dbnsfp.get('genocanyon'):
                        if dbnsfp['genocanyon'].get('score'):
                            if type(dbnsfp['genocanyon'].get('score')) == list:
                                genoscore = max(dbnsfp['genocanyon']['score'])
                            elif type(dbnsfp['genocanyon'].get('score')) != list:
                                genoscore = dbnsfp['genocanyon']['score']
                        else:
                            genoscore = '.'

                        if dbnsfp['genocanyon'].get('rankscore'):
                            if type(dbnsfp['genocanyon']['rankscore']) == list:
                                geno_rs = max(dbnsfp['genocanyon']['rankscore'])
                            else:
                                geno_rs = dbnsfp['genocanyon']['rankscore']


                        else:
                            geno_rs = '.'
                    else:
                        genoscore = '.'
                        geno_rs = '.'
                    genoCanyon_score.append(genoscore)
                    genoCanyon_rankscore.append(geno_rs)
                    (f'Genocanyon Score : {genoscore}')
                    (f'genocanyon Rank Score: {geno_rs}')

                    if dbnsfp.get('provean'):

                        if dbnsfp['provean'].get('score') and dbnsfp['provean'].get('pred'):
                            if type(dbnsfp['provean']['score']) == list:
                                provsc = max(dbnsfp['provean']['score'])
                                prov_pos = (dbnsfp['provean']['score']).index(max(dbnsfp['provean']['score']))

                            else:
                                provsc = dbnsfp['provean']['score']

                            if type(dbnsfp['provean'].get('pred')) == list:
                                provpr = (dbnsfp['provean']['pred'])[prov_pos]
                                if provpr == '.':
                                    provpr = max(dbnsfp['provean']['pred'])
                            else:
                                provpr = dbnsfp['provean']['pred']
                        else:
                            provpr = '.'
                            provsc = '.'

                        if dbnsfp['provean'].get('rankscore'):
                            if type(dbnsfp['provean']['rankscore']) == list:
                                prov_rs = max(dbnsfp['provean']['rankscore'])

                            else:
                                prov_rs = dbnsfp['provean']['rankscore']

                        else:
                            prov_rs = '.'
                        if provpr == '.' and provsc == '.' and prov_rs != '.':
                            if dbnsfp['provean'].get('score'):
                                provsc = dbnsfp['provean']['score']
                            else:
                                provsc = '.'
                            if dbnsfp['provean'].get('pred'):
                                provpr = dbnsfp['provean']['pred']
                            else:
                                provpr = '.'

                    else:
                        provpr = '.'
                        provsc = '.'
                        prov_rs = '.'
                    if (provpr != '.') and provsc == '.':
                        provsc = 0

                    provean_pred.append(provpr)
                    provean_score.append(provsc)
                    provean_rs.append(prov_rs)
                    (f'Provean Pred : {provpr}')
                    (f'Provean Score : {provsc}')
                    (f'Provean Rank Score : {prov_rs}')

                    if dbnsfp.get('dann'):
                        if dbnsfp['dann'].get('score'):
                            if type(dbnsfp['dann']['score']) == list:
                                dann = max(dbnsfp['dann']['score'])

                            else:
                                dann = dbnsfp['dann']['score']

                        else:
                            dann = '.'

                    else:
                        dann = '.'
                    dann_score.append(dann)
                    (f'DANN Score : {dann}')

                    if dbnsfp.get('fathmm'):
                        if dbnsfp['fathmm'].get('pred') and dbnsfp['fathmm'].get('score'):
                            if type(dbnsfp['fathmm']['score']) == list:
                                faths = max(dbnsfp['fathmm']['score'])
                                fath_pos = (dbnsfp['fathmm']['score']).index(max(dbnsfp['fathmm']['score']))

                            else:
                                faths = dbnsfp['fathmm']['score']

                            if type(dbnsfp['fathmm']['pred']) == list:
                                fathp = (dbnsfp['fathmm']['pred'])[fath_pos]
                                if fathp == '.':
                                    fathp = max(dbnsfp['fathmm']['pred'])
                            else:
                                fathp = dbnsfp['fathmm']['pred']
                        else:
                            fathp = '.'
                            faths = '.'

                        if dbnsfp['fathmm'].get('rankscore'):
                            if type(dbnsfp['fathmm']['rankscore']) == list:
                                fathrs = max(dbnsfp['fathmm']['rankscore'])
                            else:
                                fathrs = dbnsfp['fathmm']['rankscore']

                        else:
                            fathrs = '.'
                        if faths == '.' and fathp == '.' and fathrs != '.':
                            if dbnsfp['fathmm'].get('score'):
                                faths = dbnsfp['fathmm']['score']
                            else:
                                faths = '.'
                            if dbnsfp['fathmm'].get('pred'):
                                fathp = dbnsfp['fathmm']['pred']
                            else:
                                fathp = '.'
                    else:
                        fathp = '.'
                        faths = '.'
                        fathrs = '.'

                    if faths == '.' and fathp != '.':
                        faths = 0
                    fathmm_pred.append(fathp)
                    fathmm_score.append(faths)
                    fathmm_rs.append(fathrs)
                    (f'Fathmm Pred : {fathp}')
                    (f'Fathmm Score : {faths}')
                    (f'Fathmm Rank Score : {fathrs}')

                    if dbnsfp.get('fathmm-mkl'):
                        if dbnsfp['fathmm-mkl'].get('coding_pred') and dbnsfp['fathmm-mkl'].get('coding_score'):
                            if type(dbnsfp['fathmm-mkl']['coding_score']) == list:
                                fathsc = max(dbnsfp['fathmm-mkl']['coding_score'])
                                fathm_pos = (dbnsfp['fathmm-mkl']['coding_score']).index(
                                    max(dbnsfp['fathmm-mkl']['coding_score']))
                            else:
                                fathsc = dbnsfp['fathmm-mkl']['coding_score']

                            if type(dbnsfp['fathmm-mkl'].get('coding_pred')) == list:
                                fathpr = (dbnsfp['fathmm-mkl']['coding_pred'])[fathm_pos]
                                if fathpr == '.':
                                    fathpr = max(dbnsfp['fathmm-mkl']['coding_pred'])
                            else:
                                fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                        else:
                            fathpr = '.'
                            fathsc = '.'

                        if dbnsfp['fathmm-mkl'].get('coding_rankscore'):
                            if type(dbnsfp['fathmm-mkl']['coding_rankscore']) == list:
                                fathcoding_rs = max(dbnsfp['fathmm-mkl']['coding_rankscore'])
                            else:
                                fathcoding_rs = dbnsfp['fathmm-mkl']['coding_rankscore']
                        else:
                            fathcoding_rs = '.'
                        if fathsc == '.' and fathpr == '.' and fathcoding_rs != '.':
                            if dbnsfp['fathmm-mkl'].get('coding_score'):
                                fathsc = dbnsfp['fathmm-mkl']['coding_score']
                            else:
                                fathsc = '.'
                            if dbnsfp['fathmm-mkl'].get('coding_pred'):
                                fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                            else:
                                fathpr = '.'

                    else:
                        fathpr = '.'
                        fathsc = '.'
                        fathcoding_rs = '.'
                    if fathsc == '.' and fathpr != '.':
                        fathsc = 0
                    fathmm_mkl_pred.append(fathpr)
                    fathmm_mkl_score.append(fathsc)
                    fathmm_mkl_rankscore.append(fathcoding_rs)
                    (f'Fathmm-mkl Pred : {fathpr}')
                    (f'Fathmm-mkl Score : {fathsc}')
                    (f'Fathmm-mkl RankScore : {fathcoding_rs}')

                    if dbnsfp.get('metasvm'):
                        if dbnsfp['metasvm'].get('pred') and dbnsfp['metasvm'].get('score'):
                            if type(dbnsfp['metasvm']['score']) == list:
                                svmsc = max(dbnsfp['metasvm']['score'])
                                svm_pos = (dbnsfp['metasvm']['score']).index(max(dbnsfp['metasvm']['score']))
                            else:
                                svmsc = dbnsfp['metasvm']['score']
                            if type(dbnsfp['metasvm'].get('pred')) == list:
                                svmpr = (dbnsfp['metasvm']['pred'])[svm_pos]
                                if svmpr == '.':
                                    svmpr = max(dbnsfp['metasvm']['pred'])
                            else:
                                svmpr = dbnsfp['metasvm']['pred']
                        else:
                            svmpr = '.'
                            svmsc = '.'
                        if dbnsfp['metasvm'].get('rankscore'):
                            if type(dbnsfp['metasvm']['rankscore']) == list:
                                svm_rs = max(dbnsfp['metasvm']['rankscore'])

                            else:
                                svm_rs = dbnsfp['metasvm']['rankscore']

                        else:
                            svm_rs = '.'

                        if svmpr == '.' and svmsc == '.' and svm_rs != '.':
                            if dbnsfp['metasvm'].get('score'):
                                svmsc = dbnsfp['metasvm']['score']
                            else:
                                svmsc = '.'
                            if dbnsfp['metasvm'].get('pred'):
                                svmpr = dbnsfp['metasvm']['pred']
                            else:
                                svmpr = '.'

                    else:
                        svmpr = '.'
                        svmsc = '.'
                        svm_rs = '.'
                    if svmpr != '.' and svmsc == '.':
                        svmsc = 0
                    metasvm_pred.append(svmpr)
                    metasvm_score.append(svmsc)
                    metasvm_rankscore.append(svm_rs)
                    (f'MetaSVM Pred : {svmpr}')
                    (f'MetaSVM Score : {svmsc}')
                    (f'MetaSVM Rank Score : {svm_rs}')

                    if dbnsfp.get('metalr'):
                        if dbnsfp['metalr'].get('pred') and dbnsfp['metalr'].get('score'):
                            if type(dbnsfp['metalr']['score']) == list:
                                lrsc = max(dbnsfp['metalr']['score'])
                                lr_pos = (dbnsfp['metalr']['score']).index(max(dbnsfp['metalr']['score']))

                            else:
                                lrsc = dbnsfp['metalr']['score']
                            if type(dbnsfp['metalr'].get('pred')) == list:
                                lrpr = (dbnsfp['metalr']['pred'])[lrt_pos]
                                if lrpr == '.':
                                    lrpr = max(dbnsfp['metalr']['pred'])
                            elif type(dbnsfp['metalr'].get('pred')) != list:
                                lrpr = dbnsfp['metalr']['pred']
                        else:
                            lrpr = '.'
                            lrsc = '.'

                        if dbnsfp['metalr'].get('rankscore'):
                            if type(dbnsfp['metalr']['rankscore']) == list:
                                lr_rs = max(dbnsfp['metalr']['rankscore'])

                            else:
                                lr_rs = dbnsfp['metalr']['rankscore']
                        else:
                            lr_rs = '.'
                        if lrpr == '.' and lrsc == '.' and lr_rs != '.':
                            if dbnsfp['metalr'].get('score'):
                                lrsc = dbnsfp['metalr']['score']
                            else:
                                lrsc = '.'
                            if dbnsfp['metalr'].get('pred'):
                                lrpr = dbnsfp['metalr']['pred']
                            else:
                                lrpr = '.'
                    else:
                        lrpr = '.'
                        lrsc = '.'
                        lr_rs = '.'
                    if lrpr != '.' and lrsc == '.':
                        lrsc = 0
                    metalr_pred.append(lrpr)
                    metalr_score.append(lrsc)
                    MetaLR_rankscore.append(lr_rs)
                    (f"MetaLR_Pred: {lrpr}")
                    (f'MetaLR_Score : {lrsc}')
                    (f'MetaLR_Rank_Score : {lr_rs}')

                    if dbnsfp.get('integrated'):
                        if dbnsfp['integrated'].get('fitcons_score'):

                            if type(dbnsfp['integrated']['fitcons_score']) == list:
                                fitsc = max(dbnsfp['integrated']['fitcons_score'])

                            else:
                                fitsc = dbnsfp['integrated']['fitcons_score']

                        else:
                            fitsc = '.'

                        if dbnsfp['integrated'].get('confidence_value'):
                            if type(dbnsfp['integrated']['confidence_value']) == list:
                                fitcv = max(dbnsfp['integrated']['confidence_value'])

                            else:
                                fitcv = dbnsfp['integrated']['confidence_value']

                        else:
                            fitcv = 0

                        if dbnsfp['integrated'].get('fitcons_rankscore'):
                            if type(dbnsfp['integrated']['fitcons_rankscore']) == list:
                                fitrs = max(dbnsfp['integrated']['fitcons_rankscore'])

                            else:
                                fitrs = dbnsfp['integrated']['fitcons_rankscore']

                        else:
                            fitrs = 0

                    else:
                        fitsc = '.'
                        fitcv = '.'
                        fitrs = '.'
                    (f"Integrated_fitCons_score : {fitsc}")
                    (f"Integrated_confidence_value : {fitcv}")
                    (f"Integrated_fitcons_rankscore: {fitrs}")
                    integ_fitcoin_score.append(fitsc)
                    integ_conf_value.append(fitcv)
                    integ_fitcons_rankscore.append(fitrs)

                    if dbnsfp.get('gerp++'):
                        if dbnsfp['gerp++'].get('rs'):
                            if type(dbnsfp['gerp++']['rs']) == list:
                                rs = max(dbnsfp['gerp++']['rs'])

                            else:
                                rs = dbnsfp['gerp++']['rs']

                        else:
                            rs = '.'
                        if dbnsfp['gerp++'].get('rs_rankscore'):
                            if type(dbnsfp['gerp++']['rs_rankscore']) == list:
                                rs_rank = max(dbnsfp['gerp++']['rs_rankscore'])
                            else:
                                rs_rank = dbnsfp['gerp++']['rs_rankscore']
                        else:
                            rs_rank = '.'


                    else:
                        rs = '.'
                        rs_rank = '.'
                    gerp_rs.append(rs)
                    gerp_rs_rankscore.append(rs_rank)
                    (f"GERP++_RS : {rs}")
                    (f"GERP++_RS : {rs_rank}")

                    if dbnsfp.get('siphy_29way'):
                        if dbnsfp['siphy_29way'].get('logodds'):
                            if type(dbnsfp['siphy_29way']['logodds']) == list:
                                siphy = max(dbnsfp['siphy_29way']['logodds'])

                            else:
                                siphy = dbnsfp['siphy_29way']['logodds']

                        else:
                            siphy = '.'

                        if dbnsfp['siphy_29way'].get('logodds_rankscore'):
                            if type(dbnsfp['siphy_29way']['logodds_rankscore']) == list:
                                siphyrs = max(dbnsfp['siphy_29way']['logodds_rankscore'])

                            else:
                                siphyrs = dbnsfp['siphy_29way']['logodds_rankscore']

                        else:
                            siphyrs = '.'

                    else:
                        siphy = '.'
                        siphyrs = '.'

                    siphy_29way_logOdds.append(siphy)
                    siphy_29way_logOdds_rs.append(siphyrs)
                    (f'Siphy_29way_logOdds : {siphy}')
                    (f'Siphy_29way_logOdds_rankscore : {siphyrs}')

                    if dbnsfp.get('revel'):
                        if dbnsfp['revel'].get('score'):
                            if type(dbnsfp['revel']['score']) == list:
                                revsc = max(dbnsfp['revel']['score'])
                            else:
                                revsc = dbnsfp['revel']['score']
                        else:
                            revsc = '.'
                    else:
                        revsc = '.'
                    revel_score_list.append(revsc)
                    (f'Revel_Score : {revsc}')

                    if dbnsfp.get('eigen'):
                        if dbnsfp['eigen'].get('raw_coding'):
                            if type(dbnsfp['eigen']['raw_coding']) == list:
                                eigen_rc = max(dbnsfp['eigen']['raw_coding'])
                            else:
                                eigen_rc = dbnsfp['eigen']['raw_coding']
                        else:
                            eigen_rc = '.'
                    else:
                        eigen_rc = '.'
                    eigen_rawcoding.append(eigen_rc)
                    (f'Eigen Raw Coding : {eigen_rc}')

                    if dbnsfp.get('phylo'):
                        if dbnsfp['phylo'].get('p100way'):
                            if dbnsfp['phylo']['p100way'].get('vertebrate'):

                                if type(dbnsfp['phylo']['p100way']['vertebrate']) == list:
                                    phylo100way = max(dbnsfp['phylo']['p100way']['vertebrate'])
                                else:
                                    phylo100way = dbnsfp['phylo']['p100way']['vertebrate']
                            else:
                                phylo100way = '.'

                            if dbnsfp['phylo']['p100way'].get('vertebrate_rankscore'):

                                if type(dbnsfp['phylo']['p100way']['vertebrate_rankscore']) == list:
                                    phylo100wayrs = max(dbnsfp['phylo']['p100way']['vertebrate_rankscore'])
                                else:
                                    phylo100wayrs = dbnsfp['phylo']['p100way']['vertebrate_rankscore']
                            else:
                                phylo100wayrs = '.'
                        else:
                            phylo100way = '.'
                            phylo100wayrs = '.'
                        if dbnsfp['phylo'].get('p17way'):
                            if dbnsfp['phylo']['p17way'].get('primate'):
                                if type(dbnsfp['phylo']['p17way']['primate']) == list:
                                    phylo17 = max(dbnsfp['phylo']['p17way']['primate'])
                                else:
                                    phylo17 = dbnsfp['phylo']['p17way']['primate']
                            else:

                                phylo17 = '.'
                            if dbnsfp['phylo']['p17way'].get('primate_rankscore'):
                                if type(dbnsfp['phylo']['p17way']['primate_rankscore']) == list:
                                    phylo17rs = max(dbnsfp['phylo']['p17way']['primate_rankscore'])
                                else:
                                    phylo17rs = dbnsfp['phylo']['p17way']['primate_rankscore']
                            else:

                                phylo17rs = '.'
                        else:
                            phylo17 = '.'
                            phylo17rs = '.'
                        if dbnsfp['phylo'].get('p30way'):
                            if dbnsfp['phylo']['p30way'].get('mammalian'):
                                if type(dbnsfp['phylo']['p30way']['mammalian']) == list:
                                    phylo30 = max(dbnsfp['phylo']['p30way']['mammalian'])
                                else:
                                    phylo30 = dbnsfp['phylo']['p30way']['mammalian']
                            else:

                                phylo30 = '.'
                            if dbnsfp['phylo']['p30way'].get('mammalian_rankscore'):
                                if type(dbnsfp['phylo']['p30way']['mammalian_rankscore']) == list:
                                    phylo30rs = max(dbnsfp['phylo']['p30way']['mammalian_rankscore'])
                                else:
                                    phylo30rs = dbnsfp['phylo']['p30way']['mammalian_rankscore']
                            else:

                                phylo30rs = '.'
                        else:
                            phylo30 = '.'
                            phylo30rs = '.'


                    else:
                        phylo100way = '.'
                        phylo100wayrs = '.'
                        phylo17 = '.'
                        phylo17rs = '.'
                        phylo30 = '.'
                        phylo30rs = '.'
                    phylo100waylist.append(phylo100way)
                    phylo100wayrankscore.append(phylo100wayrs)
                    phylo17waylist.append(phylo17)
                    phylo17rankscore.append(phylo17rs)
                    phylo30waylist.append(phylo30)
                    phylo30rankscore.append(phylo30rs)
                    (f'phylo100way_vertebrate  : {phylo100way}')
                    (f'phylo100way_vertebrateRankscore  : {phylo100wayrs}')
                    (f'phylo17way_primate  : {phylo17}')
                    (f'phylo17way_primate_rankscore  : {phylo17rs}')
                    (f'phylo30way_mammalian  : {phylo30}')
                    (f'phylo30way_mammalian_rankscore  : {phylo30rs}')

                    if dbnsfp.get('phastcons'):
                        if dbnsfp['phastcons'].get('100way'):
                            if dbnsfp['phastcons']['100way'].get('vertebrate'):

                                if type(dbnsfp['phastcons']['100way']['vertebrate']) == list:
                                    phastcons100way = max(dbnsfp['phastcons']['100way']['vertebrate'])
                                else:
                                    phastcons100way = dbnsfp['phastcons']['100way']['vertebrate']
                            else:
                                phastcons100way = '.'

                            if dbnsfp['phastcons']['100way'].get('vertebrate_rankscore'):

                                if type(dbnsfp['phastcons']['100way']['vertebrate_rankscore']) == list:
                                    phastcons100wayrs = max(dbnsfp['phastcons']['100way']['vertebrate_rankscore'])
                                else:
                                    phastcons100wayrs = dbnsfp['phastcons']['100way']['vertebrate_rankscore']
                            else:
                                phastcons100wayrs = '.'
                        else:
                            phastcons100way = '.'
                            phastcons100wayrs = '.'
                        if phastcons100wayrs != '.' and phastcons100way == '.':
                            phastcons100way = 0
                        if dbnsfp['phastcons'].get('p17way'):
                            if dbnsfp['phastcons']['p17way'].get('primate'):
                                if type(dbnsfp['phastcons']['p17way']['primate']) == list:
                                    phastcons17 = max(dbnsfp['phastcons']['p17way']['primate'])
                                else:
                                    phastcons17 = dbnsfp['phastcons']['p17way']['primate']
                            else:

                                phastcons17 = '.'
                            if dbnsfp['phastcons']['p17way'].get('primate_rankscore'):
                                if type(dbnsfp['phastcons']['p17way']['primate_rankscore']) == list:
                                    phastcons17rs = max(dbnsfp['phastcons']['p17way']['primate_rankscore'])
                                else:
                                    phastcons17rs = dbnsfp['phastcons']['p17way']['primate_rankscore']
                            else:

                                phastcons17rs = '.'
                        else:
                            phastcons17 = '.'
                            phastcons17rs = '.'
                        if phastcons17rs != '.' and phastcons17 == '.':
                            phastcons17 = 0
                        if dbnsfp['phastcons'].get('30way'):
                            if dbnsfp['phastcons']['30way'].get('mammalian'):
                                if type(dbnsfp['phastcons']['30way']['mammalian']) == list:
                                    phastcons30 = max(dbnsfp['phastcons']['30way']['mammalian'])
                                else:
                                    phastcons30 = dbnsfp['phastcons']['30way']['mammalian']
                            else:

                                phastcons30 = '.'
                            if dbnsfp['phastcons']['30way'].get('mammalian_rankscore'):
                                if type(dbnsfp['phastcons']['30way']['mammalian_rankscore']) == list:
                                    phastcons30rs = max(dbnsfp['phastcons']['30way']['mammalian_rankscore'])
                                else:
                                    phastcons30rs = dbnsfp['phastcons']['30way']['mammalian_rankscore']
                            else:

                                phastcons30rs = '.'
                        else:
                            phastcons30 = '.'
                            phastcons30rs = '.'
                        if phastcons30rs != '.' and phastcons30 == '.':
                            phastcons30 = 0


                    else:
                        phastcons100way = '.'
                        phastcons100wayrs = '.'
                        phastcons17 = '.'
                        phastcons17rs = '.'
                        phastcons30 = '.'
                        phastcons30rs = '.'
                    phastcons100waylist.append(phastcons100way)
                    phastcons100wayrankscore.append(phastcons100wayrs)
                    phastcons17waylist.append(phastcons17)
                    phastcons17rankscore.append(phastcons17rs)
                    phastcons30waylist.append(phastcons30)
                    phastcons30rankscore.append(phastcons30rs)
                    (f'phastcons100way_vertebrate  : {phastcons100way}')
                    (f'phastcons100way_vertebrateRankscore  : {phastcons100wayrs}')
                    (f'phastcons17way_primate  : {phastcons17}')
                    (f'phastcons17way_primate_rankscore  : {phastcons17rs}')
                    (f'phastcons30way_mammalian  : {phastcons30}')
                    (f'phastcons30way_mammalian_rankscore  : {phastcons30rs}')

                    if dbnsfp.get('eigen-pc'):
                        if dbnsfp['eigen-pc'].get('raw_coding'):
                            if type(dbnsfp['eigen-pc']['raw_coding']) == list:
                                eigenpc_rc = max(dbnsfp['eigen-pc']['raw_coding'])
                            else:
                                eigenpc_rc = dbnsfp['eigen-pc']['raw_coding']
                        else:
                            eigenpc_rc = '.'
                    else:
                        eigenpc_rc = '.'
                    eigen_pc_rawcoding.append(eigenpc_rc)
                    (f'Eigen-pc Raw Coding : {eigenpc_rc}')

                    if dbnsfp.get('interpro_domain'):
                        if type(dbnsfp['interpro_domain']) == list:
                            interpro = max(dbnsfp['interpro_domain'])
                        else:
                            interpro = dbnsfp['interpro_domain']
                    else:
                        interpro = '.'
                    interpro_domain.append(interpro)
                    (f'Interpro_DOmain : {interpro}')
                    gene = ''
                    tissue = ''
                    if dbnsfp.get('gtex'):

                        if type(dbnsfp['gtex']) == list:

                            for i in dbnsfp['gtex']:
                                gene += i['gene'] + ' | '
                                tissue += i['tissue'] + ' | '

                        elif type(dbnsfp['gtex']) == dict:
                            gene += dbnsfp['gtex']['gene'] + "  "
                            tissue += dbnsfp['gtex']['tissue'] + '  '
                        else:
                            gene += '.  '
                            tissue += '.  '
                    else:
                        gene += '.  '
                        tissue += '.  '

                    GTEx_gene.append(gene[:-2])
                    GTEx_tissue.append(tissue[:-2])
                    (f'GTEx_gene {gene[:-2]}')
                    (f'GTEx_tissue{tissue[:-2]}')






                else:
                    sift_pred.append('.')
                    sift_score.append('.')
                    sift_converted_rs.append('.')
                    polyphen2_HDIV_Pred.append('.')
                    polyphen2_HDIV_Score.append('.')
                    polyphen2_HVAR_Pred.append('.')
                    polyphen2_HVAR_Score.append('.')
                    lrt_pred.append('.')
                    lrt_score.append('.')
                    lrt_converted_rs.append('.')
                    mut_assessor_pred.append('.')
                    mut_assessor_score.append('.')
                    mutationassessor_rs.append('.')
                    mut_taster_pred.append('.')
                    mut_taster_score.append('.')
                    MutationTaster_converted_rs.append('.')
                    provean_pred.append('.')
                    provean_score.append('.')
                    provean_rs.append('.')
                    dann_score.append('.')
                    fathmm_pred.append('.')
                    fathmm_score.append('.')
                    fathmm_rs.append('.')
                    fathmm_mkl_pred.append('.')
                    fathmm_mkl_score.append('.')
                    fathmm_mkl_rankscore.append('.')
                    metasvm_pred.append('.')
                    metasvm_score.append('.')
                    metasvm_rankscore.append('.')
                    metalr_pred.append('.')
                    metalr_score.append('.')
                    MetaLR_rankscore.append('.')
                    integ_fitcoin_score.append('.')
                    integ_conf_value.append('.')
                    integ_fitcons_rankscore.append('.')
                    gerp_rs.append('.')
                    gerp_rs_rankscore.append('.')
                    siphy_29way_logOdds.append('.')
                    siphy_29way_logOdds_rs.append('.')
                    revel_score_list.append('.')
                    genoCanyon_score.append('.')
                    genoCanyon_rankscore.append('.')
                    eigen_rawcoding.append('.')
                    eigen_pc_rawcoding.append('.')
                    phylo100waylist.append('.')
                    phylo100wayrankscore.append('.')
                    phylo17waylist.append('.')
                    phylo17rankscore.append('.')
                    phylo30waylist.append('.')
                    phylo30rankscore.append('.')
                    phastcons100waylist.append('.')
                    phastcons100wayrankscore.append('.')
                    phastcons17waylist.append('.')
                    phastcons17rankscore.append('.')
                    phastcons30waylist.append('.')
                    phastcons30rankscore.append('.')
                    interpro_domain.append('.')
                    GTEx_gene.append('.')
                    GTEx_tissue.append('.')
                    siftsc = '.'
                    sift_pos = '.'
                    siftpred = '.'
                    sift_converted_rankscore = '.'
                    hdivsc = '.'
                    hdiv_pos = '.'
                    hdivpr = '.'
                    hdivrank = '.'
                    hvarpos = '.'
                    hvarsc = '.'
                    hvarpr = '.'
                    hvarrank = '.'
                    lrtsc = '.'
                    lrt_pos = '.'
                    lrtpr = '.'
                    lrt_converted_rankscore = '.'
                    asssc = '.'
                    ass_pos = '.'
                    asspr = '.'
                    mutationassessor_rankscore = '.'
                    tassc = '.'
                    taspr = '.'
                    MutationTaster_converted_rankscore = '.'
                    genoscore = '.'
                    geno_rs = '.'
                    provsc = '.'
                    prov_pos = '.'
                    provpr = '.'
                    prov_rs = '.'
                    provsc = '.'
                    dann = '.'
                    faths = '.'
                    fath_pos = '.'
                    fathp = '.'
                    fathrs = '.'
                    fathsc = '.'
                    fathm_pos = '.'
                    fathpr = '.'
                    fathcoding_rs = '.'
                    svmsc = '.'
                    svm_pos = '.'
                    svmpr = '.'
                    svm_rs = '.'
                    lrsc = '.'
                    lr_pos = '.'
                    lrpr = '.'
                    lr_rs = '.'
                    fitsc = '.'
                    fitcv = '.'
                    fitrs = '.'
                    rs = '.'
                    rs_rank = '.'
                    siphy = '.'
                    siphyrs = '.'
                    revsc = '.'
                    eigen_rc = '.'
                    phylo100way = '.'
                    phylo100wayrs = '.'
                    phylo17 = '.'
                    phylo17rs = '.'
                    phylo30 = '.'
                    phylo30rs = '.'
                    phastcons100way = '.'
                    phastcons100wayrs = '.'
                    phastcons17 = '.'
                    phastcons17rs = '.'
                    phastcons30 = '.'
                    phastcons30rs = '.'
                    eigenpc_rc = '.'
                    interpro = '.'
                    gene = '.'
                    tissue = '.'

                if m.get('cadd'):
                    # (f"{i} : {m[i]}")
                    CADD = m['cadd']
                    if CADD.get('rawscore'):
                        if type(CADD['rawscore']) == list:
                            CADDraw = max(CADD['rawscore'])
                        else:
                            CADDraw = CADD['rawscore']
                    else:
                        CADDraw = '.'
                    CADD_raw_list.append(CADDraw)
                    (f"CADD RAW Score : {CADDraw}")

                    if CADD.get('phred'):
                        if type(CADD['phred']) == list:
                            CADDp = max(CADD['phred'])
                        else:
                            CADDp = CADD['phred']
                    else:
                        CADDp = '.'
                    CADD_phred_list.append(CADDp)
                    (f"CADD Phred : {CADDp}")

                else:
                    CADD_raw_list.append('.')
                    CADD_phred_list.append('.')
                    CADDraw = '.'
                    CADDp = '.'

        except Exception as es:
            self.error_str = es

        self.root = root
        self.root.title('VCESS-dbNSFP')
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

        frame1 = Frame(self.root, bg='#90ce2b')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 40, "bold", "italic"),
                      bg='#90ce2b',
                      fg='white')
        title.place(x=380, y=45)

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#90ce2b', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')
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

        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 14, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=95, y=42)
        url = 'http://database.liulab.science/dbNSFP'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="http://database.liulab.science/dbNSFP",
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
                                  text=f"dbNSFP is a database developed for functional\n"
                                       f"prediction and annotation of all potential non-\n"
                                       f"synonymous single-nucleotide variants (nsSNVs) \n"
                                       f"in the human genome. Its current version is based\n"
                                       f"on the Gencode release 29 / Ensembl version 94 and\n"
                                       f"includes a total of 84,013,490 nsSNVs and ssSNVs \n"
                                       f"(splicing-site SNVs). It compiles prediction scores\n"
                                       f" from 37 prediction algorithms",
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

            ###########################
            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG38)",
                                font=('Times New Roman', 16, 'bold'),
                                bg='white')  ################
            # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
            # table = ttk.Treeview(table1, height="8")  #################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420) ###################
            table = ttk.Treeview(table1, height="50")

            table['columns'] = ['Searched_ID', 'Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore',
                                'Polyphen2_HDIV_Pred',
                                'Polyphen2_HDIV_Score',
                                'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                'LRT_converted_rankScore',
                                'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                'Mutation_Taster_Pred',
                                'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                'Provean_Score', 'Provean_Rank_score',
                                'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                'Fathmm-mkl_Score',
                                'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                'MetaLR_Pred', 'MetaLR_Score',
                                'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                'Integrated_fitcons_rankscore',
                                'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                'siphy_29way_logOdds_rankscore',
                                'Revel_Score',
                                'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                'phylo30rankscore',
                                'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                'phastcons17rankscore', 'phastcons30waylist',
                                'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

            table.column('#0', width=120, minwidth=120)
            table.column('Searched_ID', anchor=CENTER, width=150)
            table.column('Sift_Pred', anchor=CENTER, width=120)
            table.column('Sift_Score', anchor=CENTER, width=120)
            table.column('Sift_converted_rankScore', anchor=CENTER, width=120)
            table.column('Polyphen2_HDIV_Pred', anchor=CENTER, width=120)
            table.column('Polyphen2_HDIV_Score', anchor=CENTER, width=120)
            table.column('Polyphen2_HVAR_Pred', anchor=CENTER, width=120)
            table.column('Polyphen2_HVAR_Score', anchor=CENTER, width=120)
            table.column('LRT_Pred', anchor=CENTER, width=120)
            table.column('LRT_Score', anchor=CENTER, width=120)
            table.column('LRT_converted_rankScore', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_Pred', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_Score', anchor=CENTER, width=120)
            table.column('Mutation_Assessor_rankscore', anchor=CENTER, width=120)
            table.column('Mutation_Taster_Pred', anchor=CENTER, width=120)
            table.column('Mutation_Taster_Score', anchor=CENTER, width=120)
            table.column('MutationTaster_converted_rankscore', anchor=CENTER, width=120)
            table.column('Provean_Pred', anchor=CENTER, width=120)
            table.column('Provean_Score', anchor=CENTER, width=120)
            table.column('Provean_Rank_score', anchor=CENTER, width=120)
            table.column('DANN Score', anchor=CENTER, width=120)
            table.column('Fathmm_Pred', anchor=CENTER, width=120)
            table.column('Fathmm_Score', anchor=CENTER, width=120)
            table.column('fathmm_Rank_Score', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_Pred', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_Score', anchor=CENTER, width=120)
            table.column('Fathmm-mkl_RankScore', anchor=CENTER, width=120)
            table.column('MetaSVM_Pred', anchor=CENTER, width=120)
            table.column('MetaSVM_Score', anchor=CENTER, width=120)
            table.column('Meta_SVM_Rank_Score', anchor=CENTER, width=120)
            table.column('MetaLR_Pred', anchor=CENTER, width=120)
            table.column('MetaLR_Score', anchor=CENTER, width=120)
            table.column('MetaLR_Rank_Score', anchor=CENTER, width=120)
            table.column('Integrated_fitCons_score', anchor=CENTER, width=120)
            table.column('Integrated_confidence_value', anchor=CENTER, width=120)
            table.column('Integrated_fitcons_rankscore', anchor=CENTER, width=120)
            table.column('GERP++_RS', anchor=CENTER, width=120)
            table.column('GERP++_RS_Rankscore', anchor=CENTER, width=120)
            table.column('Siphy_29way_logOdds', anchor=CENTER, width=120)
            table.column('siphy_29way_logOdds_rankscore', anchor=CENTER, width=120)
            table.column('Revel_Score', anchor=CENTER, width=120)
            table.column('CADD_raw_score', anchor=CENTER, width=120)
            table.column('CADD_Phred', anchor=CENTER, width=120)
            table.column('genoCanyon_score', anchor=CENTER, width=120)
            table.column('genoCanyon_rankscore', anchor=CENTER, width=120)
            table.column("Eigen_Raw_coding", anchor=CENTER, width=120)
            table.column("Eigen-pc_Raw_coding", anchor=CENTER, width=120)
            table.column('phylo100way', anchor=CENTER, width=120)
            table.column('phylo100wayrankscore', anchor=CENTER, width=120)
            table.column('phylo17way', anchor=CENTER, width=120)
            table.column('phylo17rankscore', anchor=CENTER, width=120)
            table.column('phylo30way', anchor=CENTER, width=120)
            table.column('phylo30rankscore', anchor=CENTER, width=120)
            table.column('phastcons100waylist', anchor=CENTER, width=120)
            table.column('phastcons100wayrankscore', anchor=CENTER, width=120)
            table.column('phastcons17waylist', anchor=CENTER, width=120)
            table.column('phastcons17rankscore', anchor=CENTER, width=120)
            table.column('phastcons30waylist', anchor=CENTER, width=120)
            table.column('phastcons30rankscore', anchor=CENTER, width=120)
            table.column('Interpro_Domain', anchor=CENTER, width=120)
            table.column('GTEx_gene', anchor=CENTER, width=120)
            table.column('GTEx_tisuue', anchor=CENTER, width=200)

            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('Searched_ID', text='Searched_ID', anchor=W)
            table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
            table.heading('Sift_Score', text='Sift_Score', anchor=W)
            table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
            table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
            table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
            table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
            table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
            table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
            table.heading('LRT_Score', text='LRT_Score', anchor=W)
            table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
            table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
            table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
            table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
            table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
            table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
            table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
            table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
            table.heading('Provean_Score', text='Provean_Score', anchor=W)
            table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
            table.heading('DANN Score', text='DANN Score', anchor=W)
            table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
            table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
            table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
            table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
            table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
            table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
            table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
            table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
            table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
            table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
            table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
            table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
            table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
            table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
            table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
            table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
            table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
            table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
            table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
            table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
            table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
            table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
            table.heading('Revel_Score', text='Revel_Score', anchor=W)
            table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
            table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
            table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
            table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
            table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
            table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
            table.heading('phylo100way', text='phylo100way', anchor=W)
            table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
            table.heading('phylo17way', text='phylo17way', anchor=W)
            table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
            table.heading('phylo30way', text='phylo30way', anchor=W)
            table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
            table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
            table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
            table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
            table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
            table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
            table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
            table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
            table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
            table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

            for i in range(len(sift_pred)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(search_id, sift_pred[i],
                                     sift_score[i],
                                     sift_converted_rs[i],
                                     polyphen2_HDIV_Pred[i],
                                     polyphen2_HDIV_Score[i],
                                     polyphen2_HVAR_Pred[i],
                                     polyphen2_HVAR_Score[i],
                                     lrt_pred[i],
                                     lrt_score[i],
                                     lrt_converted_rs[i],
                                     mut_assessor_pred[i],
                                     mut_assessor_score[i],
                                     mutationassessor_rs[i],
                                     mut_taster_pred[i],
                                     mut_taster_score[i],
                                     MutationTaster_converted_rs[i],
                                     provean_pred[i],
                                     provean_score[i],
                                     provean_rs[i],
                                     dann_score[i],
                                     fathmm_pred[i],
                                     fathmm_score[i],
                                     fathmm_rs[i],
                                     fathmm_mkl_pred[i],
                                     fathmm_mkl_score[i],
                                     fathmm_mkl_rankscore[i],
                                     metasvm_pred[i],
                                     metasvm_score[i],
                                     metasvm_rankscore[i],
                                     metalr_pred[i],
                                     metalr_score[i],
                                     MetaLR_rankscore[i],
                                     integ_fitcoin_score[i],integ_conf_value[i],
                                     integ_fitcons_rankscore[i],

                                     gerp_rs[i],
                                     gerp_rs_rankscore[i],
                                     siphy_29way_logOdds[i],
                                     siphy_29way_logOdds_rs[i],
                                     revel_score_list[i],
                                     CADD_raw_list[i],
                                     CADD_phred_list[i],
                                     genoCanyon_rankscore[i],
                                     genoCanyon_score[i],
                                     eigen_rawcoding[i],
                                     eigen_pc_rawcoding[i],
                                     phylo100waylist[i],
                                     phylo100wayrankscore[i],
                                     phylo17waylist[i],
                                     phylo17rankscore[i],
                                     phylo30waylist[i],
                                     phylo30rankscore[i],
                                     phastcons100waylist[i],
                                     phastcons100wayrankscore[i],
                                     phastcons17waylist[i],
                                     phastcons17rankscore[i],
                                     phastcons30waylist[i],
                                     phastcons30rankscore[i],
                                     interpro_domain[i],
                                     GTEx_gene[i],
                                     GTEx_tissue[i]

                                     ))

            # table.place(x=0, y=0)  ##########################
            # VERTICAL SCROLLBAR
            yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
            yscrollbar.pack(side=RIGHT, fill='y')  ##################

            # HORIZONTAL SCROLLBAR
            xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
            xscrollbar.pack(side=BOTTOM, fill='x')  #######################

            table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
            table.pack(side=LEFT)  ##################
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
        sift_pred.clear()
        sift_score.clear()
        sift_converted_rs.clear()
        polyphen2_HDIV_Pred.clear()
        polyphen2_HDIV_Score.clear()
        polyphen2_HVAR_Pred.clear()
        polyphen2_HVAR_Score.clear()
        lrt_pred.clear()
        lrt_score.clear()
        lrt_converted_rs.clear()
        mut_assessor_pred.clear()
        mut_assessor_score.clear()
        mutationassessor_rs.clear()
        mut_taster_pred.clear()
        mut_taster_score.clear()
        MutationTaster_converted_rs.clear()
        provean_pred.clear()
        provean_score.clear()
        provean_rs.clear()
        dann_score.clear()
        fathmm_pred.clear()
        fathmm_score.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        fathmm_mkl_rankscore.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_fitcons_rankscore.clear()
        integ_conf_value.clear()
        gerp_rs.clear()
        gerp_rs_rankscore.clear()
        siphy_29way_logOdds.clear()
        siphy_29way_logOdds_rs.clear()
        revel_score_list.clear()
        CADD_raw_list.clear()
        CADD_phred_list.clear()
        genoCanyon_rankscore.clear()
        genoCanyon_score.clear()
        eigen_rawcoding.clear()
        eigen_pc_rawcoding.clear()
        phylo100waylist.clear()
        phylo100wayrankscore.clear()
        phylo17waylist.clear()
        phylo17rankscore.clear()
        phylo30waylist.clear()
        phylo30rankscore.clear()
        phastcons100waylist.clear()
        phastcons100wayrankscore.clear()
        phastcons17waylist.clear()
        phastcons17rankscore.clear()
        phastcons30waylist.clear()
        phastcons30rankscore.clear()
        interpro_domain.clear()
        GTEx_gene.clear()
        GTEx_tissue.clear()
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()


class info2:
    def __init__(self, root, f):
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 16, "bold", "italic"),
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
        p = 20

        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)

        try:
            for id in vcf:
                ID.append(id)
                index_id=ID.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                self.root1.update_idletasks()

                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                p = p + 40



                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(id)
                progress['value'] = p



                if m == None:

                    sift_pred.append('.')
                    sift_score.append('.')
                    sift_converted_rs.append('.')
                    polyphen2_HDIV_Pred.append('.')
                    polyphen2_HDIV_Score.append('.')
                    polyphen2_HVAR_Pred.append('.')
                    polyphen2_HVAR_Score.append('.')
                    lrt_pred.append('.')
                    lrt_score.append('.')
                    lrt_converted_rs.append('.')
                    mut_assessor_pred.append('.')
                    mut_assessor_score.append('.')
                    mutationassessor_rs.append('.')
                    mut_taster_pred.append('.')
                    mut_taster_score.append('.')
                    MutationTaster_converted_rs.append('.')
                    provean_pred.append('.')
                    provean_score.append('.')
                    provean_rs.append('.')
                    dann_score.append('.')
                    fathmm_pred.append('.')
                    fathmm_score.append('.')
                    fathmm_mkl_rankscore.append('.')
                    fathmm_rs.append('.')
                    fathmm_mkl_pred.append('.')
                    fathmm_mkl_score.append('.')
                    metasvm_pred.append('.')
                    metasvm_score.append('.')
                    metasvm_rankscore.append('.')
                    metalr_pred.append('.')
                    metalr_score.append('.')
                    MetaLR_rankscore.append('.')
                    integ_fitcoin_score.append('.')
                    integ_conf_value.append('.')
                    integ_fitcons_rankscore.append('.')
                    gerp_rs.append('.')
                    gerp_rs_rankscore.append('.')
                    siphy_29way_logOdds.append('.')
                    siphy_29way_logOdds_rs.append('.')
                    revel_score_list.append('.')
                    CADD_raw_list.append('.')
                    CADD_phred_list.append('.')
                    genoCanyon_rankscore.append('.')
                    genoCanyon_score.append('.')
                    eigen_rawcoding.append('.')
                    eigen_pc_rawcoding.append('.')
                    phylo100waylist.append('.')
                    phylo100wayrankscore.append('.')
                    phylo17waylist.append('.')
                    phylo17rankscore.append('.')
                    phylo30waylist.append('.')
                    phylo30rankscore.append('.')
                    phastcons100waylist.append('.')
                    phastcons100wayrankscore.append('.')
                    phastcons17waylist.append('.')
                    phastcons17rankscore.append('.')
                    phastcons30waylist.append('.')
                    phastcons30rankscore.append('.')
                    interpro_domain.append('.')
                    GTEx_gene.append('.')
                    GTEx_tissue.append('.')
                else:

                    if m.get('dbnsfp'):

                        dbnsfp = m['dbnsfp']

                        for key, item in dbnsfp.items():
                            (f"{key} : {item}")
                        if dbnsfp.get('sift'):

                            if dbnsfp['sift'].get('score') and dbnsfp['sift'].get('pred'):
                                if type(dbnsfp['sift']['score']) == list:
                                    siftsc = max(dbnsfp['sift']['score'])
                                    sift_pos = (dbnsfp['sift']['score']).index(max(dbnsfp['sift']['score']))

                                else:
                                    siftsc = (dbnsfp['sift']['score'])

                                if type(dbnsfp['sift']['pred']) == list:
                                    siftpred = (dbnsfp['sift']['pred'])[sift_pos]
                                    if siftpred == '.':
                                       siftpred= (max(dbnsfp['sift']['pred']))

                                else:
                                    siftpred = dbnsfp['sift']['pred']


                            else:

                                siftsc = '.'
                                siftpred = '.'
                            if dbnsfp['sift'].get('converted_rankscore'):
                                if type(dbnsfp['sift'].get('converted_rankscore')) == list:
                                    sift_converted_rankscore = max(dbnsfp['sift']['converted_rankscore'])

                                else:
                                    sift_converted_rankscore = dbnsfp['sift']['converted_rankscore']
                            else:
                                sift_converted_rankscore = '.'

                            if siftsc == '.' and siftpred == '.' and sift_converted_rankscore != '.':
                                if dbnsfp['sift'].get('score'):

                                    siftsc = (dbnsfp['sift']['score'])
                                else:
                                    siftsc = '.'
                                if dbnsfp['sift'].get('pred'):
                                    siftpred = dbnsfp['sift']['pred']
                                else:
                                    siftpred = '.'

                        else:
                            siftsc = '.'
                            siftpred = '.'
                            sift_converted_rankscore = '.'

                        if (siftpred != '.') and siftsc == '.':
                            siftsc = 0
                        sift_pred.append(siftpred)
                        sift_score.append(siftsc)
                        sift_converted_rs.append(sift_converted_rankscore)

                        (f"SIFT Pred : {siftpred}")
                        (f'SIFT Score : {siftsc}')
                        (f'Sift_converted_rankscore : {sift_converted_rankscore}')

                        if dbnsfp.get('polyphen2'):
                            if dbnsfp['polyphen2'].get('hdiv'):

                                if dbnsfp['polyphen2']['hdiv'].get('score') and dbnsfp['polyphen2']['hdiv'].get('pred'):

                                    if type(dbnsfp['polyphen2']['hdiv']['score']) == list:
                                        hdivsc = max(dbnsfp['polyphen2']['hdiv']['score'])
                                        hdiv_pos = (dbnsfp['polyphen2']['hdiv']['score']).index(
                                            max(dbnsfp['polyphen2']['hdiv']['score']))


                                    else:
                                        hdivsc = dbnsfp['polyphen2']['hdiv']['score']

                                    if dbnsfp['polyphen2']['hdiv'].get('pred'):
                                        if type(dbnsfp['polyphen2']['hdiv'].get('pred')) == list:
                                            hdivpr = (dbnsfp['polyphen2']['hdiv']['pred'])[hdiv_pos]
                                            if hdivpr == '.':
                                                hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])


                                        else:
                                            hdivpr = dbnsfp['polyphen2']['hdiv']['pred']
                                else:
                                    hdivpr = '.'
                                    hdivsc = '.'

                                if dbnsfp['polyphen2']['hdiv'].get('rankscore'):
                                    hdivrank = dbnsfp['polyphen2']['hdiv']['rankscore']
                                else:
                                    hdivrank = '.'

                                if hdivpr == '.' and hdivsc == '.' and hdivrank != '.':
                                    if dbnsfp['polyphen2']['hdiv'].get('score'):
                                        hdivsc = dbnsfp['polyphen2']['hdiv']['score']
                                    else:
                                        hdivsc = '.'
                                    if dbnsfp['polyphen2']['hdiv'].get('pred'):

                                        hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])
                                    else:
                                        hdivpr = '.'

                                    if hdivsc == '.' and hdivpr != '.':
                                        hdivsc = 0

                            else:
                                hdivsc = '.'
                                hdivpr = '.'

                            if dbnsfp['polyphen2'].get('hvar'):
                                (dbnsfp['polyphen2'])
                                if dbnsfp['polyphen2']['hvar'].get('pred') and dbnsfp['polyphen2']['hvar'].get('score'):

                                    if type(dbnsfp['polyphen2']['hvar']['score']) == list:
                                        hvarsc = max(dbnsfp['polyphen2']['hvar']['score'])
                                        hvarpos = (dbnsfp['polyphen2']['hvar']['score']).index(
                                            max(dbnsfp['polyphen2']['hvar']['score']))

                                    else:
                                        hvarsc = dbnsfp['polyphen2']['hvar']['score']

                                    if type(dbnsfp['polyphen2']['hvar'].get('pred')) == list:
                                        hvarpr = (dbnsfp['polyphen2']['hvar']['pred'])[hvarpos]
                                        if hvarpr == '.':
                                            hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])

                                    elif type(dbnsfp['polyphen2']['hvar'].get('pred')) != list:
                                        hvarpr = dbnsfp['polyphen2']['hvar']['pred']
                                else:
                                    hvarsc = '.'
                                    hvarpr = '.'

                                if dbnsfp['polyphen2']['hvar'].get('rankscore'):
                                    hvarrank = dbnsfp['polyphen2']['hvar']['rankscore']
                                else:
                                    hvarrank = '.'

                                if hvarpr == '.' and hvarsc == '.' and hvarrank != '.':
                                    if dbnsfp['polyphen2']['hvar'].get('score'):
                                        hvarsc = dbnsfp['polyphen2']['hvar']['score']
                                    else:
                                        hvarsc = '.'
                                    if dbnsfp['polyphen2']['hvar'].get('pred'):

                                        hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])
                                    else:
                                        hvarpr = '.'

                                    if hvarsc == '.' and hvarpr != '.':
                                        hvarsc = 0



                            else:

                                hvarsc = '.'
                                hvarpr = '.'

                        else:
                            hdivsc = '.'
                            hdivpr = '.'
                            hvarpr = '.'
                            hvarsc = '.'
                        if hdivpr != '.' and hdivsc == '.':
                            hdivsc = 0
                        if hvarpr != '.' and hvarsc == '.':
                            hvarsc = 0
                        polyphen2_HDIV_Pred.append(hdivpr)
                        polyphen2_HDIV_Score.append(hdivsc)
                        polyphen2_HVAR_Score.append(hvarsc)
                        polyphen2_HVAR_Pred.append(hvarpr)
                        (f'Polyphen2 HDIV Pred : {hdivpr}')
                        (f'Polyphen2 HDIV Score : {hdivsc}')
                        (f'Polyphen2 HVAR Pred : {hvarpr}')
                        (f'Polyphen2 HVAR Score : {hvarsc}')

                        if dbnsfp.get('lrt'):

                            if dbnsfp['lrt'].get('score') and dbnsfp['lrt'].get('pred'):

                                if type(dbnsfp['lrt'].get('score')) == list:
                                    lrtsc = max(dbnsfp['lrt']['score'])
                                    lrt_pos = (dbnsfp['lrt']['score']).index(max(dbnsfp['lrt']['score']))

                                else:
                                    lrtsc = dbnsfp['lrt']['score']
                                    (f'score : {lrtsc}')

                                if type(dbnsfp['lrt'].get('pred')) == list:

                                    lrtpr = (dbnsfp['lrt']['pred'])[lrt_pos]
                                    if lrtpr == '.':
                                        lrtpr = max(dbnsfp['lrt']['pred'])
                                else:
                                    lrtpr = dbnsfp['lrt']['pred']

                            else:
                                lrtsc = '.'
                                lrtpr = '.'

                            if dbnsfp['lrt'].get('converted_rankscore'):

                                if type(dbnsfp['lrt'].get('converted_rankscore')) == list:
                                    lrt_converted_rankscore = max(dbnsfp['lrt']['converted_rankscore'])

                                elif type(dbnsfp['lrt'].get('converted_rankscore')) != list:
                                    lrt_converted_rankscore = dbnsfp['lrt']['converted_rankscore']

                            else:
                                lrt_converted_rankscore = '.'

                            if lrtpr == '.' and lrtsc == '.' and lrt_converted_rankscore != '.':
                                if dbnsfp['lrt'].get('score'):

                                    lrtsc = dbnsfp['lrt']['score']
                                    (f'score : {lrtsc}')
                                else:
                                    lrtsc = '.'

                                if dbnsfp['lrt'].get('pred'):
                                    lrtpr = dbnsfp['lrt']['pred']
                                else:
                                    lrtpr = '.'




                        else:
                            lrtsc = '.'
                            lrtpr = '.'
                            lrt_converted_rankscore = '.'
                        if (lrtpr != '.') and lrtsc == '.':
                            lrtsc = 0

                        lrt_pred.append(lrtpr)
                        lrt_score.append(lrtsc)
                        lrt_converted_rs.append(lrt_converted_rankscore)
                        (f"LRT Pred : {lrtpr}")
                        (f'LRT Score : {lrtsc}')
                        (f'lrt_converted_rankscore : {lrt_converted_rankscore}')

                        if dbnsfp.get('mutationassessor'):
                            if dbnsfp['mutationassessor'].get('score') and dbnsfp['mutationassessor'].get('pred'):
                                if type(dbnsfp['mutationassessor']['score']) == list:
                                    asssc = max(dbnsfp['mutationassessor']['score'])
                                    ass_pos = (dbnsfp['mutationassessor']['score']).index(
                                        max(dbnsfp['mutationassessor']['score']))
                                else:
                                    asssc = dbnsfp['mutationassessor']['score']

                                if type(dbnsfp['mutationassessor'].get('pred')) == list:

                                    asspr = (dbnsfp['mutationassessor']['pred'])[ass_pos]
                                    if asspr == '.':
                                        asspr = max(dbnsfp['mutationassessor']['pred'])

                                else:
                                    asspr = dbnsfp['mutationassessor']['pred']

                            else:
                                asspr = '.'
                                asssc = '.'

                            if dbnsfp['mutationassessor'].get('rankscore'):
                                if type(dbnsfp['mutationassessor']['rankscore']) == list:
                                    mutationassessor_rankscore = max(dbnsfp['mutationassessor']['rankscore'])
                                else:
                                    mutationassessor_rankscore = dbnsfp['mutationassessor']['rankscore']
                            else:
                                mutationassessor_rankscore = '.'

                            if asspr == '.' and asssc == '.' and mutationassessor_rankscore != '.':
                                if dbnsfp['mutationassessor'].get('score'):
                                    asssc = dbnsfp['mutationassessor']['score']
                                else:
                                    asssc = '.'

                                if dbnsfp['mutationassessor'].get('pred'):
                                    asspr = dbnsfp['mutationassessor']['pred']
                                else:
                                    asspr = '.'

                        else:
                            asspr = '.'
                            asssc = '.'
                            mutationassessor_rankscore = '.'

                        if asssc == '.' and asspr != '.':
                            asssc = 0

                        mut_assessor_pred.append(asspr)
                        mut_assessor_score.append(asssc)
                        mutationassessor_rs.append(mutationassessor_rankscore)
                        (f'Mutation Assessor Pred : {asspr}')
                        (f'Mutation Assessor Score : {asssc}')
                        (f'Mutation Assessor RankScore : {mutationassessor_rankscore}')

                        if dbnsfp.get('mutationtaster'):

                            if dbnsfp['mutationtaster'].get('score') and dbnsfp['mutationtaster'].get('pred'):
                                if type(dbnsfp['mutationtaster']['score']) == list:
                                    tassc = max(dbnsfp['mutationtaster']['score'])
                                    position = (dbnsfp['mutationtaster']['score']).index(
                                        max(dbnsfp['mutationtaster']['score']))
                                    # (index)
                                    # (type(dbnsfp['mutationtaster']['score']))

                                else:
                                    tassc = dbnsfp['mutationtaster']['score']

                                if type(dbnsfp['mutationtaster'].get('pred')) == list:
                                    # taspr = max(dbnsfp['mutationtaster']['pred'])

                                    taspr = (dbnsfp['mutationtaster']['pred'])[position]
                                    if taspr == '.':
                                        taspr = max(dbnsfp['mutationtaster']['pred'])

                                else:
                                    taspr = dbnsfp['mutationtaster']['pred']


                            else:
                                taspr = '.'
                                tassc = '.'

                            if dbnsfp['mutationtaster'].get('converted_rankscore'):
                                if type(dbnsfp['mutationtaster'].get('converted_rankscore')) == list:
                                    # taspr = max(dbnsfp['mutationtaster']['pred'])
                                    MutationTaster_converted_rankscore = \
                                    (dbnsfp['mutationtaster']['converted_rankscore'])[
                                        position]
                                elif type(dbnsfp['mutationtaster'].get('converted_rankscore')) != list:
                                    MutationTaster_converted_rankscore = dbnsfp['mutationtaster']['converted_rankscore']

                            else:
                                MutationTaster_converted_rankscore = '.'

                            if taspr == '.' and tassc == '.' and MutationTaster_converted_rankscore != '.':
                                if dbnsfp['mutationtaster'].get('score'):

                                    tassc = dbnsfp['mutationtaster']['score']
                                else:
                                    tassc = '.'

                                if dbnsfp['mutationtaster'].get('pred'):

                                    taspr = dbnsfp['mutationtaster']['pred']
                                else:
                                    taspr = '.'
                        else:

                            taspr = '.'
                            tassc = '.'
                            MutationTaster_converted_rankscore = '.'
                        if tassc == '.' and taspr != '.':
                            tassc = 0
                        (f'Mutation Taster Pred : {taspr}')
                        (f'Mutation Taster Score : {tassc}')
                        (f'Mutation Taster Converted rankscore : {MutationTaster_converted_rankscore}')
                        mut_taster_pred.append(taspr)
                        mut_taster_score.append(tassc)
                        MutationTaster_converted_rs.append(MutationTaster_converted_rankscore)

                        if dbnsfp.get('genocanyon'):
                            if dbnsfp['genocanyon'].get('score'):
                                if type(dbnsfp['genocanyon'].get('score')) == list:
                                    genoscore = max(dbnsfp['genocanyon']['score'])
                                elif type(dbnsfp['genocanyon'].get('score')) != list:
                                    genoscore = dbnsfp['genocanyon']['score']
                            else:
                                genoscore = '.'

                            if dbnsfp['genocanyon'].get('rankscore'):
                                if type(dbnsfp['genocanyon']['rankscore']) == list:
                                    geno_rs = max(dbnsfp['genocanyon']['rankscore'])
                                else:
                                    geno_rs = dbnsfp['genocanyon']['rankscore']


                            else:
                                geno_rs = '.'
                        else:
                            genoscore = '.'
                            geno_rs = '.'
                        genoCanyon_score.append(genoscore)
                        genoCanyon_rankscore.append(geno_rs)
                        (f'Genocanyon Score : {genoscore}')
                        (f'genocanyon Rank Score: {geno_rs}')

                        if dbnsfp.get('provean'):

                            if dbnsfp['provean'].get('score') and dbnsfp['provean'].get('pred'):
                                if type(dbnsfp['provean']['score']) == list:
                                    provsc = max(dbnsfp['provean']['score'])
                                    prov_pos = (dbnsfp['provean']['score']).index(max(dbnsfp['provean']['score']))

                                else:
                                    provsc = dbnsfp['provean']['score']

                                if type(dbnsfp['provean'].get('pred')) == list:
                                    provpr = (dbnsfp['provean']['pred'])[prov_pos]
                                    if provpr == '.':
                                        provpr = max(dbnsfp['provean']['pred'])
                                else:
                                    provpr = dbnsfp['provean']['pred']
                            else:
                                provpr = '.'
                                provsc = '.'

                            if dbnsfp['provean'].get('rankscore'):
                                if type(dbnsfp['provean']['rankscore']) == list:
                                    prov_rs = max(dbnsfp['provean']['rankscore'])

                                else:
                                    prov_rs = dbnsfp['provean']['rankscore']

                            else:
                                prov_rs = '.'
                            if provpr == '.' and provsc == '.' and prov_rs != '.':
                                if dbnsfp['provean'].get('score'):
                                    provsc = dbnsfp['provean']['score']
                                else:
                                    provsc = '.'
                                if dbnsfp['provean'].get('pred'):
                                    provpr = dbnsfp['provean']['pred']
                                else:
                                    provpr = '.'

                        else:
                            provpr = '.'
                            provsc = '.'
                            prov_rs = '.'
                        if (provpr != '.') and provsc == '.':
                            provsc = 0

                        provean_pred.append(provpr)
                        provean_score.append(provsc)
                        provean_rs.append(prov_rs)
                        (f'Provean Pred : {provpr}')
                        (f'Provean Score : {provsc}')
                        (f'Provean Rank Score : {prov_rs}')

                        if dbnsfp.get('dann'):
                            if dbnsfp['dann'].get('score'):
                                if type(dbnsfp['dann']['score']) == list:
                                    dann = max(dbnsfp['dann']['score'])

                                else:
                                    dann = dbnsfp['dann']['score']

                            else:
                                dann = '.'

                        else:
                            dann = '.'
                        dann_score.append(dann)
                        (f'DANN Score : {dann}')

                        if dbnsfp.get('fathmm'):
                            if dbnsfp['fathmm'].get('pred') and dbnsfp['fathmm'].get('score'):
                                if type(dbnsfp['fathmm']['score']) == list:
                                    faths = max(dbnsfp['fathmm']['score'])
                                    fath_pos = (dbnsfp['fathmm']['score']).index(max(dbnsfp['fathmm']['score']))

                                else:
                                    faths = dbnsfp['fathmm']['score']

                                if type(dbnsfp['fathmm']['pred']) == list:
                                    fathp = (dbnsfp['fathmm']['pred'])[fath_pos]
                                    if fathp == '.':
                                        fathp = max(dbnsfp['fathmm']['pred'])
                                else:
                                    fathp = dbnsfp['fathmm']['pred']
                            else:
                                fathp = '.'
                                faths = '.'

                            if dbnsfp['fathmm'].get('rankscore'):
                                if type(dbnsfp['fathmm']['rankscore']) == list:
                                    fathrs = max(dbnsfp['fathmm']['rankscore'])
                                else:
                                    fathrs = dbnsfp['fathmm']['rankscore']

                            else:
                                fathrs = '.'
                            if faths == '.' and fathp == '.' and fathrs != '.':
                                if dbnsfp['fathmm'].get('score'):
                                    faths = dbnsfp['fathmm']['score']
                                else:
                                    faths = '.'
                                if dbnsfp['fathmm'].get('pred'):
                                    fathp = dbnsfp['fathmm']['pred']
                                else:
                                    fathp = '.'
                        else:
                            fathp = '.'
                            faths = '.'
                            fathrs = '.'

                        if faths == '.' and fathp != '.':
                            faths = 0
                        fathmm_pred.append(fathp)
                        fathmm_score.append(faths)
                        fathmm_rs.append(fathrs)
                        (f'Fathmm Pred : {fathp}')
                        (f'Fathmm Score : {faths}')
                        (f'Fathmm Rank Score : {fathrs}')

                        if dbnsfp.get('fathmm-mkl'):
                            if dbnsfp['fathmm-mkl'].get('coding_pred') and dbnsfp['fathmm-mkl'].get('coding_score'):
                                if type(dbnsfp['fathmm-mkl']['coding_score']) == list:
                                    fathsc = max(dbnsfp['fathmm-mkl']['coding_score'])
                                    fathm_pos = (dbnsfp['fathmm-mkl']['coding_score']).index(
                                        max(dbnsfp['fathmm-mkl']['coding_score']))
                                else:
                                    fathsc = dbnsfp['fathmm-mkl']['coding_score']

                                if type(dbnsfp['fathmm-mkl'].get('coding_pred')) == list:
                                    fathpr = (dbnsfp['fathmm-mkl']['coding_pred'])[fathm_pos]
                                    if fathpr == '.':
                                        fathpr = max(dbnsfp['fathmm-mkl']['coding_pred'])
                                else:
                                    fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                            else:
                                fathpr = '.'
                                fathsc = '.'

                            if dbnsfp['fathmm-mkl'].get('coding_rankscore'):
                                if type(dbnsfp['fathmm-mkl']['coding_rankscore']) == list:
                                    fathcoding_rs = max(dbnsfp['fathmm-mkl']['coding_rankscore'])
                                else:
                                    fathcoding_rs = dbnsfp['fathmm-mkl']['coding_rankscore']
                            else:
                                fathcoding_rs = '.'
                            if fathsc == '.' and fathpr == '.' and fathcoding_rs != '.':
                                if dbnsfp['fathmm-mkl'].get('coding_score'):
                                    fathsc = dbnsfp['fathmm-mkl']['coding_score']
                                else:
                                    fathsc = '.'
                                if dbnsfp['fathmm-mkl'].get('coding_pred'):
                                    fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                                else:
                                    fathpr = '.'

                        else:
                            fathpr = '.'
                            fathsc = '.'
                            fathcoding_rs = '.'
                        if fathsc == '.' and fathpr != '.':
                            fathsc = 0
                        fathmm_mkl_pred.append(fathpr)
                        fathmm_mkl_score.append(fathsc)
                        fathmm_mkl_rankscore.append(fathcoding_rs)
                        (f'Fathmm-mkl Pred : {fathpr}')
                        (f'Fathmm-mkl Score : {fathsc}')
                        (f'Fathmm-mkl RankScore : {fathcoding_rs}')

                        if dbnsfp.get('metasvm'):
                            if dbnsfp['metasvm'].get('pred') and dbnsfp['metasvm'].get('score'):
                                if type(dbnsfp['metasvm']['score']) == list:
                                    svmsc = max(dbnsfp['metasvm']['score'])
                                    svm_pos = (dbnsfp['metasvm']['score']).index(max(dbnsfp['metasvm']['score']))
                                else:
                                    svmsc = dbnsfp['metasvm']['score']
                                if type(dbnsfp['metasvm'].get('pred')) == list:
                                    svmpr = (dbnsfp['metasvm']['pred'])[svm_pos]
                                    if svmpr == '.':
                                        svmpr = max(dbnsfp['metasvm']['pred'])
                                else:
                                    svmpr = dbnsfp['metasvm']['pred']
                            else:
                                svmpr = '.'
                                svmsc = '.'
                            if dbnsfp['metasvm'].get('rankscore'):
                                if type(dbnsfp['metasvm']['rankscore']) == list:
                                    svm_rs = max(dbnsfp['metasvm']['rankscore'])

                                else:
                                    svm_rs = dbnsfp['metasvm']['rankscore']

                            else:
                                svm_rs = '.'

                            if svmpr == '.' and svmsc == '.' and svm_rs != '.':
                                if dbnsfp['metasvm'].get('score'):
                                    svmsc = dbnsfp['metasvm']['score']
                                else:
                                    svmsc = '.'
                                if dbnsfp['metasvm'].get('pred'):
                                    svmpr = dbnsfp['metasvm']['pred']
                                else:
                                    svmpr = '.'

                        else:
                            svmpr = '.'
                            svmsc = '.'
                            svm_rs = '.'
                        if svmpr != '.' and svmsc == '.':
                            svmsc = 0
                        metasvm_pred.append(svmpr)
                        metasvm_score.append(svmsc)
                        metasvm_rankscore.append(svm_rs)
                        (f'MetaSVM Pred : {svmpr}')
                        (f'MetaSVM Score : {svmsc}')
                        (f'MetaSVM Rank Score : {svm_rs}')

                        if dbnsfp.get('metalr'):
                            if dbnsfp['metalr'].get('pred') and dbnsfp['metalr'].get('score'):
                                if type(dbnsfp['metalr']['score']) == list:
                                    lrsc = max(dbnsfp['metalr']['score'])
                                    lr_pos = (dbnsfp['metalr']['score']).index(max(dbnsfp['metalr']['score']))

                                else:
                                    lrsc = dbnsfp['metalr']['score']
                                if type(dbnsfp['metalr'].get('pred')) == list:
                                    lrpr = (dbnsfp['metalr']['pred'])[lrt_pos]
                                    if lrpr == '.':
                                        lrpr = max(dbnsfp['metalr']['pred'])
                                elif type(dbnsfp['metalr'].get('pred')) != list:
                                    lrpr = dbnsfp['metalr']['pred']
                            else:
                                lrpr = '.'
                                lrsc = '.'

                            if dbnsfp['metalr'].get('rankscore'):
                                if type(dbnsfp['metalr']['rankscore']) == list:
                                    lr_rs = max(dbnsfp['metalr']['rankscore'])

                                else:
                                    lr_rs = dbnsfp['metalr']['rankscore']
                            else:
                                lr_rs = '.'
                            if lrpr == '.' and lrsc == '.' and lr_rs != '.':
                                if dbnsfp['metalr'].get('score'):
                                    lrsc = dbnsfp['metalr']['score']
                                else:
                                    lrsc = '.'
                                if dbnsfp['metalr'].get('pred'):
                                    lrpr = dbnsfp['metalr']['pred']
                                else:
                                    lrpr = '.'
                        else:
                            lrpr = '.'
                            lrsc = '.'
                            lr_rs = '.'
                        if lrpr != '.' and lrsc == '.':
                            lrsc = 0
                        metalr_pred.append(lrpr)
                        metalr_score.append(lrsc)
                        MetaLR_rankscore.append(lr_rs)
                        (f"MetaLR_Pred: {lrpr}")
                        (f'MetaLR_Score : {lrsc}')
                        (f'MetaLR_Rank_Score : {lr_rs}')

                        if dbnsfp.get('integrated'):
                            if dbnsfp['integrated'].get('fitcons_score'):

                                if type(dbnsfp['integrated']['fitcons_score']) == list:
                                    fitsc = max(dbnsfp['integrated']['fitcons_score'])

                                else:
                                    fitsc = dbnsfp['integrated']['fitcons_score']

                            else:
                                fitsc = '.'

                            if dbnsfp['integrated'].get('confidence_value'):
                                if type(dbnsfp['integrated']['confidence_value']) == list:
                                    fitcv = max(dbnsfp['integrated']['confidence_value'])

                                else:
                                    fitcv = dbnsfp['integrated']['confidence_value']

                            else:
                                fitcv = 0

                            if dbnsfp['integrated'].get('fitcons_rankscore'):
                                if type(dbnsfp['integrated']['fitcons_rankscore']) == list:
                                    fitrs = max(dbnsfp['integrated']['fitcons_rankscore'])

                                else:
                                    fitrs = dbnsfp['integrated']['fitcons_rankscore']

                            else:
                                fitrs = 0

                        else:
                            fitsc = '.'
                            fitcv = '.'
                            fitrs = '.'
                        (f"Integrated_fitCons_score : {fitsc}")
                        (f"Integrated_confidence_value : {fitcv}")
                        (f"Integrated_fitcons_rankscore: {fitrs}")
                        integ_fitcoin_score.append(fitsc)
                        integ_conf_value.append(fitcv)
                        integ_fitcons_rankscore.append(fitrs)

                        if dbnsfp.get('gerp++'):
                            if dbnsfp['gerp++'].get('rs'):
                                if type(dbnsfp['gerp++']['rs']) == list:
                                    rs = max(dbnsfp['gerp++']['rs'])

                                else:
                                    rs = dbnsfp['gerp++']['rs']

                            else:
                                rs = '.'
                            if dbnsfp['gerp++'].get('rs_rankscore'):
                                if type(dbnsfp['gerp++']['rs_rankscore']) == list:
                                    rs_rank = max(dbnsfp['gerp++']['rs_rankscore'])
                                else:
                                    rs_rank = dbnsfp['gerp++']['rs_rankscore']
                            else:
                                rs_rank = '.'


                        else:
                            rs = '.'
                            rs_rank = '.'
                        gerp_rs.append(rs)
                        gerp_rs_rankscore.append(rs_rank)
                        (f"GERP++_RS : {rs}")
                        (f"GERP++_RS : {rs_rank}")

                        if dbnsfp.get('siphy_29way'):
                            if dbnsfp['siphy_29way'].get('logodds'):
                                if type(dbnsfp['siphy_29way']['logodds']) == list:
                                    siphy = max(dbnsfp['siphy_29way']['logodds'])

                                else:
                                    siphy = dbnsfp['siphy_29way']['logodds']

                            else:
                                siphy = '.'

                            if dbnsfp['siphy_29way'].get('logodds_rankscore'):
                                if type(dbnsfp['siphy_29way']['logodds_rankscore']) == list:
                                    siphyrs = max(dbnsfp['siphy_29way']['logodds_rankscore'])

                                else:
                                    siphyrs = dbnsfp['siphy_29way']['logodds_rankscore']

                            else:
                                siphyrs = '.'

                        else:
                            siphy = '.'
                            siphyrs = '.'

                        siphy_29way_logOdds.append(siphy)
                        siphy_29way_logOdds_rs.append(siphyrs)
                        (f'Siphy_29way_logOdds : {siphy}')
                        (f'Siphy_29way_logOdds_rankscore : {siphyrs}')

                        if dbnsfp.get('revel'):
                            if dbnsfp['revel'].get('score'):
                                if type(dbnsfp['revel']['score']) == list:
                                    revsc = max(dbnsfp['revel']['score'])
                                else:
                                    revsc = dbnsfp['revel']['score']
                            else:
                                revsc = '.'
                        else:
                            revsc = '.'
                        revel_score_list.append(revsc)
                        (f'Revel_Score : {revsc}')

                        if dbnsfp.get('eigen'):
                            if dbnsfp['eigen'].get('raw_coding'):
                                if type(dbnsfp['eigen']['raw_coding']) == list:
                                    eigen_rc = max(dbnsfp['eigen']['raw_coding'])
                                else:
                                    eigen_rc = dbnsfp['eigen']['raw_coding']
                            else:
                                eigen_rc = '.'
                        else:
                            eigen_rc = '.'
                        eigen_rawcoding.append(eigen_rc)
                        (f'Eigen Raw Coding : {eigen_rc}')

                        if dbnsfp.get('phylo'):
                            if dbnsfp['phylo'].get('p100way'):
                                if dbnsfp['phylo']['p100way'].get('vertebrate'):

                                    if type(dbnsfp['phylo']['p100way']['vertebrate']) == list:
                                        phylo100way = max(dbnsfp['phylo']['p100way']['vertebrate'])
                                    else:
                                        phylo100way = dbnsfp['phylo']['p100way']['vertebrate']
                                else:
                                    phylo100way = '.'

                                if dbnsfp['phylo']['p100way'].get('vertebrate_rankscore'):

                                    if type(dbnsfp['phylo']['p100way']['vertebrate_rankscore']) == list:
                                        phylo100wayrs = max(dbnsfp['phylo']['p100way']['vertebrate_rankscore'])
                                    else:
                                        phylo100wayrs = dbnsfp['phylo']['p100way']['vertebrate_rankscore']
                                else:
                                    phylo100wayrs = '.'
                            else:
                                phylo100way = '.'
                                phylo100wayrs = '.'
                            if dbnsfp['phylo'].get('p17way'):
                                if dbnsfp['phylo']['p17way'].get('primate'):
                                    if type(dbnsfp['phylo']['p17way']['primate']) == list:
                                        phylo17 = max(dbnsfp['phylo']['p17way']['primate'])
                                    else:
                                        phylo17 = dbnsfp['phylo']['p17way']['primate']
                                else:

                                    phylo17 = '.'
                                if dbnsfp['phylo']['p17way'].get('primate_rankscore'):
                                    if type(dbnsfp['phylo']['p17way']['primate_rankscore']) == list:
                                        phylo17rs = max(dbnsfp['phylo']['p17way']['primate_rankscore'])
                                    else:
                                        phylo17rs = dbnsfp['phylo']['p17way']['primate_rankscore']
                                else:

                                    phylo17rs = '.'
                            else:
                                phylo17 = '.'
                                phylo17rs = '.'
                            if dbnsfp['phylo'].get('p30way'):
                                if dbnsfp['phylo']['p30way'].get('mammalian'):
                                    if type(dbnsfp['phylo']['p30way']['mammalian']) == list:
                                        phylo30 = max(dbnsfp['phylo']['p30way']['mammalian'])
                                    else:
                                        phylo30 = dbnsfp['phylo']['p30way']['mammalian']
                                else:

                                    phylo30 = '.'
                                if dbnsfp['phylo']['p30way'].get('mammalian_rankscore'):
                                    if type(dbnsfp['phylo']['p30way']['mammalian_rankscore']) == list:
                                        phylo30rs = max(dbnsfp['phylo']['p30way']['mammalian_rankscore'])
                                    else:
                                        phylo30rs = dbnsfp['phylo']['p30way']['mammalian_rankscore']
                                else:

                                    phylo30rs = '.'
                            else:
                                phylo30 = '.'
                                phylo30rs = '.'


                        else:
                            phylo100way = '.'
                            phylo100wayrs = '.'
                            phylo17 = '.'
                            phylo17rs = '.'
                            phylo30 = '.'
                            phylo30rs = '.'
                        phylo100waylist.append(phylo100way)
                        phylo100wayrankscore.append(phylo100wayrs)
                        phylo17waylist.append(phylo17)
                        phylo17rankscore.append(phylo17rs)
                        phylo30waylist.append(phylo30)
                        phylo30rankscore.append(phylo30rs)
                        (f'phylo100way_vertebrate  : {phylo100way}')
                        (f'phylo100way_vertebrateRankscore  : {phylo100wayrs}')
                        (f'phylo17way_primate  : {phylo17}')
                        (f'phylo17way_primate_rankscore  : {phylo17rs}')
                        (f'phylo30way_mammalian  : {phylo30}')
                        (f'phylo30way_mammalian_rankscore  : {phylo30rs}')

                        if dbnsfp.get('phastcons'):
                            if dbnsfp['phastcons'].get('100way'):
                                if dbnsfp['phastcons']['100way'].get('vertebrate'):

                                    if type(dbnsfp['phastcons']['100way']['vertebrate']) == list:
                                        phastcons100way = max(dbnsfp['phastcons']['100way']['vertebrate'])
                                    else:
                                        phastcons100way = dbnsfp['phastcons']['100way']['vertebrate']
                                else:
                                    phastcons100way = '.'

                                if dbnsfp['phastcons']['100way'].get('vertebrate_rankscore'):

                                    if type(dbnsfp['phastcons']['100way']['vertebrate_rankscore']) == list:
                                        phastcons100wayrs = max(dbnsfp['phastcons']['100way']['vertebrate_rankscore'])
                                    else:
                                        phastcons100wayrs = dbnsfp['phastcons']['100way']['vertebrate_rankscore']
                                else:
                                    phastcons100wayrs = '.'
                            else:
                                phastcons100way = '.'
                                phastcons100wayrs = '.'
                            if phastcons100wayrs != '.' and phastcons100way == '.':
                                phastcons100way = 0
                            if dbnsfp['phastcons'].get('p17way'):
                                if dbnsfp['phastcons']['p17way'].get('primate'):
                                    if type(dbnsfp['phastcons']['p17way']['primate']) == list:
                                        phastcons17 = max(dbnsfp['phastcons']['p17way']['primate'])
                                    else:
                                        phastcons17 = dbnsfp['phastcons']['p17way']['primate']
                                else:

                                    phastcons17 = '.'
                                if dbnsfp['phastcons']['p17way'].get('primate_rankscore'):
                                    if type(dbnsfp['phastcons']['p17way']['primate_rankscore']) == list:
                                        phastcons17rs = max(dbnsfp['phastcons']['p17way']['primate_rankscore'])
                                    else:
                                        phastcons17rs = dbnsfp['phastcons']['p17way']['primate_rankscore']
                                else:

                                    phastcons17rs = '.'
                            else:
                                phastcons17 = '.'
                                phastcons17rs = '.'
                            if phastcons17rs != '.' and phastcons17 == '.':
                                phastcons17 = 0
                            if dbnsfp['phastcons'].get('30way'):
                                if dbnsfp['phastcons']['30way'].get('mammalian'):
                                    if type(dbnsfp['phastcons']['30way']['mammalian']) == list:
                                        phastcons30 = max(dbnsfp['phastcons']['30way']['mammalian'])
                                    else:
                                        phastcons30 = dbnsfp['phastcons']['30way']['mammalian']
                                else:

                                    phastcons30 = '.'
                                if dbnsfp['phastcons']['30way'].get('mammalian_rankscore'):
                                    if type(dbnsfp['phastcons']['30way']['mammalian_rankscore']) == list:
                                        phastcons30rs = max(dbnsfp['phastcons']['30way']['mammalian_rankscore'])
                                    else:
                                        phastcons30rs = dbnsfp['phastcons']['30way']['mammalian_rankscore']
                                else:

                                    phastcons30rs = '.'
                            else:
                                phastcons30 = '.'
                                phastcons30rs = '.'
                            if phastcons30rs != '.' and phastcons30 == '.':
                                phastcons30 = 0


                        else:
                            phastcons100way = '.'
                            phastcons100wayrs = '.'
                            phastcons17 = '.'
                            phastcons17rs = '.'
                            phastcons30 = '.'
                            phastcons30rs = '.'
                        phastcons100waylist.append(phastcons100way)
                        phastcons100wayrankscore.append(phastcons100wayrs)
                        phastcons17waylist.append(phastcons17)
                        phastcons17rankscore.append(phastcons17rs)
                        phastcons30waylist.append(phastcons30)
                        phastcons30rankscore.append(phastcons30rs)
                        (f'phastcons100way_vertebrate  : {phastcons100way}')
                        (f'phastcons100way_vertebrateRankscore  : {phastcons100wayrs}')
                        (f'phastcons17way_primate  : {phastcons17}')
                        (f'phastcons17way_primate_rankscore  : {phastcons17rs}')
                        (f'phastcons30way_mammalian  : {phastcons30}')
                        (f'phastcons30way_mammalian_rankscore  : {phastcons30rs}')

                        if dbnsfp.get('eigen-pc'):
                            if dbnsfp['eigen-pc'].get('raw_coding'):
                                if type(dbnsfp['eigen-pc']['raw_coding']) == list:
                                    eigenpc_rc = max(dbnsfp['eigen-pc']['raw_coding'])
                                else:
                                    eigenpc_rc = dbnsfp['eigen-pc']['raw_coding']
                            else:
                                eigenpc_rc = '.'
                        else:
                            eigenpc_rc = '.'
                        eigen_pc_rawcoding.append(eigenpc_rc)
                        (f'Eigen-pc Raw Coding : {eigenpc_rc}')

                        if dbnsfp.get('interpro_domain'):
                            if type(dbnsfp['interpro_domain']) == list:
                                interpro = max(dbnsfp['interpro_domain'])
                            else:
                                interpro = dbnsfp['interpro_domain']
                        else:
                            interpro = '.'
                        interpro_domain.append(interpro)
                        (f'Interpro_DOmain : {interpro}')
                        gene = ''
                        tissue = ''
                        if dbnsfp.get('gtex'):
                            if type(dbnsfp['gtex']) == list:

                                for i in dbnsfp['gtex']:
                                    gene += i['gene'] + ' | '
                                    tissue += i['tissue'] + ' | '

                            elif type(dbnsfp['gtex']) == dict:
                                gene += dbnsfp['gtex']['gene'] + "  "
                                tissue += dbnsfp['gtex']['tissue'] + '  '
                            else:
                                gene += '.  '
                                tissue += '.  '
                        else:
                            gene += '.  '
                            tissue += '.  '

                        GTEx_gene.append(gene[:-2])
                        GTEx_tissue.append(tissue[:-2])
                        (f'GTEx_gene {gene[:-2]}')
                        (f'GTEx_tissue{tissue[:-2]}')






                    else:
                        sift_pred.append('.')
                        sift_score.append('.')
                        sift_converted_rs.append('.')
                        polyphen2_HDIV_Pred.append('.')
                        polyphen2_HDIV_Score.append('.')
                        polyphen2_HVAR_Pred.append('.')
                        polyphen2_HVAR_Score.append('.')
                        lrt_pred.append('.')
                        lrt_score.append('.')
                        lrt_converted_rs.append('.')
                        mut_assessor_pred.append('.')
                        mut_assessor_score.append('.')
                        mutationassessor_rs.append('.')
                        mut_taster_pred.append('.')
                        mut_taster_score.append('.')
                        MutationTaster_converted_rs.append('.')
                        provean_pred.append('.')
                        provean_score.append('.')
                        provean_rs.append('.')
                        dann_score.append('.')
                        fathmm_pred.append('.')
                        fathmm_score.append('.')
                        fathmm_rs.append('.')
                        fathmm_mkl_pred.append('.')
                        fathmm_mkl_score.append('.')
                        fathmm_mkl_rankscore.append('.')
                        metasvm_pred.append('.')
                        metasvm_score.append('.')
                        metasvm_rankscore.append('.')
                        metalr_pred.append('.')
                        metalr_score.append('.')
                        MetaLR_rankscore.append('.')
                        integ_fitcoin_score.append('.')
                        integ_conf_value.append('.')
                        integ_fitcons_rankscore.append('.')
                        gerp_rs.append('.')
                        gerp_rs_rankscore.append('.')
                        siphy_29way_logOdds.append('.')
                        siphy_29way_logOdds_rs.append('.')
                        revel_score_list.append('.')
                        genoCanyon_score.append('.')
                        genoCanyon_rankscore.append('.')
                        eigen_rawcoding.append('.')
                        eigen_pc_rawcoding.append('.')
                        phylo100waylist.append('.')
                        phylo100wayrankscore.append('.')
                        phylo17waylist.append('.')
                        phylo17rankscore.append('.')
                        phylo30waylist.append('.')
                        phylo30rankscore.append('.')
                        phastcons100waylist.append('.')
                        phastcons100wayrankscore.append('.')
                        phastcons17waylist.append('.')
                        phastcons17rankscore.append('.')
                        phastcons30waylist.append('.')
                        phastcons30rankscore.append('.')
                        interpro_domain.append('.')
                        GTEx_gene.append('.')
                        GTEx_tissue.append('.')

                    if m.get('cadd'):
                        # (f"{i} : {m[i]}")
                        CADD = m['cadd']
                        if CADD.get('rawscore'):
                            if type(CADD['rawscore']) == list:
                                CADDraw = max(CADD['rawscore'])
                            else:
                                CADDraw = CADD['rawscore']
                        else:
                            CADDraw = '.'
                        CADD_raw_list.append(CADDraw)
                        (f"CADD RAW Score : {CADDraw}")

                        if CADD.get('phred'):
                            if type(CADD['phred']) == list:
                                CADDp = max(CADD['phred'])
                            else:
                                CADDp = CADD['phred']
                        else:
                            CADDp = '.'
                        CADD_phred_list.append(CADDp)
                        (f"CADD Phred : {CADDp}")

                    else:
                        CADD_raw_list.append('.')
                        CADD_phred_list.append('.')
        except Exception as es:
            (es)
            self.error_str = es

            ###########################
        self.root = root
        self.root.title('dbNSFP window')
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
        title = Label(self.root, text="VCESS Retrieving Data from dbNSFP",
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#7877a5', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='White')
        url = 'http://database.liulab.science/dbNSFP'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="http://database.liulab.science/dbNSFP",
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
                                  text=f"dbNSFP is a database developed for functional\n"
                                       f"prediction and annotation of all potential non-\n"
                                       f"synonymous single-nucleotide variants (nsSNVs) \n"
                                       f"in the human genome. Its current version is based\n"
                                       f"on the Gencode release 29 / Ensembl version 94 and\n"
                                       f"includes a total of 84,013,490 nsSNVs and ssSNVs \n"
                                       f"(splicing-site SNVs). It compiles prediction scores\n"
                                       f" from 37 prediction algorithms",
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.grid(padx=0, pady=0)
        canvas.place(x=int(width / 2) - 225, y=50, width=450, height=200)

        fps = 5  # Change the fps to make the animation faster/slower
        shift()

        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=1600)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(sift_score)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(ID) == len(sift_score):

                self.sift_pred = sift_pred
                self.sift_score = sift_score
                self.lrt_pred = lrt_pred
                self.mut_taster_pred = mut_taster_pred

                ################################

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
                # table = ttk.Treeview(table1, height="8")  #################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID','Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore', 'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                    'Provean_Score', 'Provean_Rank_score',
                                    'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred', 'MetaLR_Score',
                                    'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                    "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

                table.column('#0', width=120, minwidth=120)
                table.column('ID', anchor=W, width=150)
                table.column('Sift_Pred', anchor=W, width=120)
                table.column('Sift_Score', anchor=W, width=120)
                table.column('Sift_converted_rankScore', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Pred', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Score', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Pred', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Score', anchor=W, width=120)
                table.column('LRT_Pred', anchor=W, width=120)
                table.column('LRT_Score', anchor=W, width=120)
                table.column('LRT_converted_rankScore', anchor=W, width=120)
                table.column('Mutation_Assessor_Pred', anchor=W, width=120)
                table.column('Mutation_Assessor_Score', anchor=W, width=120)
                table.column('Mutation_Assessor_rankscore', anchor=W, width=120)
                table.column('Mutation_Taster_Pred', anchor=W, width=120)
                table.column('Mutation_Taster_Score', anchor=W, width=120)
                table.column('MutationTaster_converted_rankscore', anchor=W, width=120)
                table.column('Provean_Pred', anchor=W, width=120)
                table.column('Provean_Score', anchor=W, width=120)
                table.column('Provean_Rank_score', anchor=W, width=120)
                table.column('DANN Score', anchor=W, width=120)
                table.column('Fathmm_Pred', anchor=W, width=120)
                table.column('Fathmm_Score', anchor=W, width=120)
                table.column('fathmm_Rank_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_Pred', anchor=W, width=120)
                table.column('Fathmm-mkl_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_RankScore', anchor=W, width=120)
                table.column('MetaSVM_Pred', anchor=W, width=120)
                table.column('MetaSVM_Score', anchor=W, width=120)
                table.column('Meta_SVM_Rank_Score', anchor=W, width=120)
                table.column('MetaLR_Pred', anchor=W, width=120)
                table.column('MetaLR_Score', anchor=W, width=120)
                table.column('MetaLR_Rank_Score', anchor=W, width=120)
                table.column('Integrated_fitCons_score', anchor=W, width=120)
                table.column('Integrated_confidence_value', anchor=W, width=120)
                table.column('Integrated_fitcons_rankscore', anchor=W, width=120)
                table.column('GERP++_RS', anchor=W, width=120)
                table.column('GERP++_RS_Rankscore', anchor=W, width=120)
                table.column('Siphy_29way_logOdds', anchor=W, width=120)
                table.column('siphy_29way_logOdds_rankscore', anchor=W, width=120)
                table.column('Revel_Score', anchor=W, width=120)
                table.column('CADD_raw_score', anchor=W, width=120)
                table.column('CADD_Phred', anchor=W, width=120)
                table.column('genoCanyon_score', anchor=W, width=120)
                table.column('genoCanyon_rankscore', anchor=W, width=120)
                table.column("Eigen_Raw_coding", anchor=W, width=120)
                table.column("Eigen-pc_Raw_coding", anchor=W, width=120)
                table.column('phylo100way', anchor=W, width=120)
                table.column('phylo100wayrankscore', anchor=W, width=120)
                table.column('phylo17way', anchor=W, width=120)
                table.column('phylo17rankscore', anchor=W, width=120)
                table.column('phylo30way', anchor=W, width=120)
                table.column('phylo30rankscore', anchor=W, width=120)
                table.column('phastcons100waylist', anchor=W, width=120)
                table.column('phastcons100wayrankscore', anchor=W, width=120)
                table.column('phastcons17waylist', anchor=W, width=120)
                table.column('phastcons17rankscore', anchor=W, width=120)
                table.column('phastcons30waylist', anchor=W, width=120)
                table.column('phastcons30rankscore', anchor=W, width=120)
                table.column('Interpro_Domain', anchor=W, width=120)
                table.column('GTEx_gene', anchor=W, width=120)
                table.column('GTEx_tisuue', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
                table.heading('Sift_Score', text='Sift_Score', anchor=W)
                table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
                table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
                table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
                table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
                table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
                table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
                table.heading('LRT_Score', text='LRT_Score', anchor=W)
                table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
                table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
                table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
                table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
                table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
                table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
                table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
                table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
                table.heading('Provean_Score', text='Provean_Score', anchor=W)
                table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
                table.heading('DANN Score', text='DANN Score', anchor=W)
                table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
                table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
                table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
                table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
                table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
                table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
                table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
                table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
                table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
                table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
                table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
                table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
                table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
                table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
                table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
                table.heading('Revel_Score', text='Revel_Score', anchor=W)
                table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
                table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
                table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
                table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
                table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
                table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
                table.heading('phylo100way', text='phylo100way', anchor=W)
                table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
                table.heading('phylo17way', text='phylo17way', anchor=W)
                table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
                table.heading('phylo30way', text='phylo30way', anchor=W)
                table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
                table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
                table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
                table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
                table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
                table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
                table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
                table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
                table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
                table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(ID[i],sift_pred[i],
                                         sift_score[i],
                                         sift_converted_rs[i],
                                         polyphen2_HDIV_Pred[i],
                                         polyphen2_HDIV_Score[i],
                                         polyphen2_HVAR_Pred[i],
                                         polyphen2_HVAR_Score[i],
                                         lrt_pred[i],
                                         lrt_score[i],
                                         lrt_converted_rs[i],
                                         mut_assessor_pred[i],
                                         mut_assessor_score[i],
                                         mutationassessor_rs[i],
                                         mut_taster_pred[i],
                                         mut_taster_score[i],
                                         MutationTaster_converted_rs[i],
                                         provean_pred[i],
                                         provean_score[i],
                                         provean_rs[i],
                                         dann_score[i],
                                         fathmm_pred[i],
                                         fathmm_score[i],
                                         fathmm_rs[i],
                                         fathmm_mkl_pred[i],
                                         fathmm_mkl_score[i],
                                         fathmm_mkl_rankscore[i],
                                         metasvm_pred[i],
                                         metasvm_score[i],
                                         metasvm_rankscore[i],
                                         metalr_pred[i],
                                         metalr_score[i],
                                         MetaLR_rankscore[i],
                                         integ_fitcoin_score[i],integ_conf_value[i],
                                         integ_fitcons_rankscore[i],
                                         gerp_rs[i],
                                         gerp_rs_rankscore[i],
                                         siphy_29way_logOdds[i],
                                         siphy_29way_logOdds_rs[i],
                                         revel_score_list[i],
                                         CADD_raw_list[i],
                                         CADD_phred_list[i],
                                         genoCanyon_rankscore[i],
                                         genoCanyon_score[i],
                                         eigen_rawcoding[i],
                                         eigen_pc_rawcoding[i],
                                         phylo100waylist[i],
                                         phylo100wayrankscore[i],
                                         phylo17waylist[i],
                                         phylo17rankscore[i],
                                         phylo30waylist[i],
                                         phylo30rankscore[i],
                                         phastcons100waylist[i],
                                         phastcons100wayrankscore[i],
                                         phastcons17waylist[i],
                                         phastcons17rankscore[i],
                                         phastcons30waylist[i],
                                         phastcons30rankscore[i],
                                         interpro_domain[i],
                                         GTEx_gene[i],
                                         GTEx_tissue[i]

                                         ))
                ##################
                table.place(x=0, y=0, width=1200, height=400)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################
                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################
                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                ##############################################################################################
                ###Creates frame widget under which all other widgets will be kept
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
                chr = Label(self.frametwo, text="GRAPHS", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
                chr.grid(padx=0, pady=0)
                chr.place(x=250, y=640)

                # Combobox creation
                self.chrstring = tkinter.StringVar(self.frametwo)
                self.chrchoosen = ttk.Combobox(self.frametwo, width=27, textvariable=self.chrstring, state='readonly')
                # chrchoosen = ttk.Combobox(self.root, width=27, textvariable=self.chrstring)

                # Adding combobox drop down list
                self.chrchoosen.bind("<<ComboboxSelected>>", self.justamethod)
                self.chrchoosen['values'] = (
                    'BAR_GRAPH', 'PIE_CHART','SCATTER_PLOT')
                # (self.chrchoosen.index(0))

                self.chrchoosen.grid(column=1, row=5, padx=0, pady=0)
                self.chrchoosen.place(x=360, y=645)
                self.chrchoosen.current(0)
                # for values in chrchoosen:
            elif len(ID) != len(sift_score)   and (len(ID) and len(sift_score))!=0:

                ################################

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
                # table = ttk.Treeview(table1, height="8")  #################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID','Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore', 'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                    'Provean_Score', 'Provean_Rank_score',
                                    'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred', 'MetaLR_Score',
                                    'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                    "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

                table.column('#0', width=120, minwidth=120)
                table.column('ID', anchor=W, width=150)
                table.column('Sift_Pred', anchor=W, width=120)
                table.column('Sift_Score', anchor=W, width=120)
                table.column('Sift_converted_rankScore', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Pred', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Score', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Pred', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Score', anchor=W, width=120)
                table.column('LRT_Pred', anchor=W, width=120)
                table.column('LRT_Score', anchor=W, width=120)
                table.column('LRT_converted_rankScore', anchor=W, width=120)
                table.column('Mutation_Assessor_Pred', anchor=W, width=120)
                table.column('Mutation_Assessor_Score', anchor=W, width=120)
                table.column('Mutation_Assessor_rankscore', anchor=W, width=120)
                table.column('Mutation_Taster_Pred', anchor=W, width=120)
                table.column('Mutation_Taster_Score', anchor=W, width=120)
                table.column('MutationTaster_converted_rankscore', anchor=W, width=120)
                table.column('Provean_Pred', anchor=W, width=120)
                table.column('Provean_Score', anchor=W, width=120)
                table.column('Provean_Rank_score', anchor=W, width=120)
                table.column('DANN Score', anchor=W, width=120)
                table.column('Fathmm_Pred', anchor=W, width=120)
                table.column('Fathmm_Score', anchor=W, width=120)
                table.column('fathmm_Rank_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_Pred', anchor=W, width=120)
                table.column('Fathmm-mkl_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_RankScore', anchor=W, width=120)
                table.column('MetaSVM_Pred', anchor=W, width=120)
                table.column('MetaSVM_Score', anchor=W, width=120)
                table.column('Meta_SVM_Rank_Score', anchor=W, width=120)
                table.column('MetaLR_Pred', anchor=W, width=120)
                table.column('MetaLR_Score', anchor=W, width=120)
                table.column('MetaLR_Rank_Score', anchor=W, width=120)
                table.column('Integrated_fitCons_score', anchor=W, width=120)
                table.column('Integrated_confidence_value', anchor=W, width=120)
                table.column('Integrated_fitcons_rankscore', anchor=W, width=120)
                table.column('GERP++_RS', anchor=W, width=120)
                table.column('GERP++_RS_Rankscore', anchor=W, width=120)
                table.column('Siphy_29way_logOdds', anchor=W, width=120)
                table.column('siphy_29way_logOdds_rankscore', anchor=W, width=120)
                table.column('Revel_Score', anchor=W, width=120)
                table.column('CADD_raw_score', anchor=W, width=120)
                table.column('CADD_Phred', anchor=W, width=120)
                table.column('genoCanyon_score', anchor=W, width=120)
                table.column('genoCanyon_rankscore', anchor=W, width=120)
                table.column("Eigen_Raw_coding", anchor=W, width=120)
                table.column("Eigen-pc_Raw_coding", anchor=W, width=120)
                table.column('phylo100way', anchor=W, width=120)
                table.column('phylo100wayrankscore', anchor=W, width=120)
                table.column('phylo17way', anchor=W, width=120)
                table.column('phylo17rankscore', anchor=W, width=120)
                table.column('phylo30way', anchor=W, width=120)
                table.column('phylo30rankscore', anchor=W, width=120)
                table.column('phastcons100waylist', anchor=W, width=120)
                table.column('phastcons100wayrankscore', anchor=W, width=120)
                table.column('phastcons17waylist', anchor=W, width=120)
                table.column('phastcons17rankscore', anchor=W, width=120)
                table.column('phastcons30waylist', anchor=W, width=120)
                table.column('phastcons30rankscore', anchor=W, width=120)
                table.column('Interpro_Domain', anchor=W, width=120)
                table.column('GTEx_gene', anchor=W, width=120)
                table.column('GTEx_tisuue', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
                table.heading('Sift_Score', text='Sift_Score', anchor=W)
                table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
                table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
                table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
                table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
                table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
                table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
                table.heading('LRT_Score', text='LRT_Score', anchor=W)
                table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
                table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
                table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
                table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
                table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
                table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
                table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
                table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
                table.heading('Provean_Score', text='Provean_Score', anchor=W)
                table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
                table.heading('DANN Score', text='DANN Score', anchor=W)
                table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
                table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
                table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
                table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
                table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
                table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
                table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
                table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
                table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
                table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
                table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
                table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
                table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
                table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
                table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
                table.heading('Revel_Score', text='Revel_Score', anchor=W)
                table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
                table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
                table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
                table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
                table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
                table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
                table.heading('phylo100way', text='phylo100way', anchor=W)
                table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
                table.heading('phylo17way', text='phylo17way', anchor=W)
                table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
                table.heading('phylo30way', text='phylo30way', anchor=W)
                table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
                table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
                table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
                table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
                table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
                table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
                table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
                table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
                table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
                table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(ID[i],sift_pred[i],
                                         sift_score[i],
                                         sift_converted_rs[i],
                                         polyphen2_HDIV_Pred[i],
                                         polyphen2_HDIV_Score[i],
                                         polyphen2_HVAR_Pred[i],
                                         polyphen2_HVAR_Score[i],
                                         lrt_pred[i],
                                         lrt_score[i],
                                         lrt_converted_rs[i],
                                         mut_assessor_pred[i],
                                         mut_assessor_score[i],
                                         mutationassessor_rs[i],
                                         mut_taster_pred[i],
                                         mut_taster_score[i],
                                         MutationTaster_converted_rs[i],
                                         provean_pred[i],
                                         provean_score[i],
                                         provean_rs[i],
                                         dann_score[i],
                                         fathmm_pred[i],
                                         fathmm_score[i],
                                         fathmm_rs[i],
                                         fathmm_mkl_pred[i],
                                         fathmm_mkl_score[i],
                                         fathmm_mkl_rankscore[i],
                                         metasvm_pred[i],
                                         metasvm_score[i],
                                         metasvm_rankscore[i],
                                         metalr_pred[i],
                                         metalr_score[i],
                                         MetaLR_rankscore[i],
                                         integ_fitcoin_score[i],integ_conf_value[i],
                                         integ_fitcons_rankscore[i],

                                         gerp_rs[i],
                                         gerp_rs_rankscore[i],
                                         siphy_29way_logOdds[i],
                                         siphy_29way_logOdds_rs[i],
                                         revel_score_list[i],
                                         CADD_raw_list[i],
                                         CADD_phred_list[i],
                                         genoCanyon_rankscore[i],
                                         genoCanyon_score[i],
                                         eigen_rawcoding[i],
                                         eigen_pc_rawcoding[i],
                                         phylo100waylist[i],
                                         phylo100wayrankscore[i],
                                         phylo17waylist[i],
                                         phylo17rankscore[i],
                                         phylo30waylist[i],
                                         phylo30rankscore[i],
                                         phastcons100waylist[i],
                                         phastcons100wayrankscore[i],
                                         phastcons17waylist[i],
                                         phastcons17rankscore[i],
                                         phastcons30waylist[i],
                                         phastcons30rankscore[i],
                                         interpro_domain[i],
                                         GTEx_gene[i],
                                         GTEx_tissue[i]

                                         ))
                ##################
                table.place(x=0, y=0, width=1200, height=400)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################
                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################
                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                ##############################################################################################
                ###Creates frame widget under which all other widgets will be kept

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
                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)


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
        except Exception as es:
            error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                          bg='white',
                          fg='black')
            error.grid(padx=0, pady=0)
            error.place(x=550, y=250)

            error2 = Label(self.frametwo, text=f'Check your connection'
                                               f'\n        Or      '
                                               f'\nUpload File again    ', font=("Times New Roman", 12),
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

        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()

        self.root.protocol("WM_DELETE_WINDOW", on_closing)

    def justamethod (self, event):
        if(self.chrchoosen.get()=='PIE_CHART'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))
            sizes.append((len(nodata)))
            sizes.append((len(D)))
            sizes.append((len(P)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = "A ","N","NoData","D","P"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(5, 2), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True,normalize=True)
            legend=['A(Disease_causing_automatic) - '+str(round(len(A)/total*100))+"%",'N(Polymorphism) - '+str(round(len(N)/total*100))+"%",'No_data - '+str(round(len(nodata)/total*100))+"%", 'D(Disease_causing) - ' +str(round((len(D)/total*100)))+"%","P(Polymorphism_automatic) - " +str(round(len(P)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)
            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3,normalize=True)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True,normalize=True)
            legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')
        elif(self.chrchoosen.get()=='BAR_GRAPH'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))

            sizes.append((len(D)))
            sizes.append((len(P)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = ["A ","N","D","P","NoData"]
            #sizes = ([totaltol, totaldele, totalother])*100

            #colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(6, 6), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)


            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green', 'black', 'cyan'])
            #legend=['A(Disease_causing_automatic)', 'N(Polymorphism)','D(Disease_causing)', 'P(Polymorphism_automatic) ','No DATA']
            red_patch = mpatches.Patch(color='red', label='A(Disease_causing_automatic)')
            blue_patch = mpatches.Patch(color='blue', label='N(Polymorphism)')
            green_patch = mpatches.Patch(color='green', label='D(Disease_causing)')
            black_patch = mpatches.Patch(color='black', label='P(Polymorphism_automatic)')
            cyan_patch = mpatches.Patch(color='cyan', label='No Data')
            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch,black_patch,cyan_patch],loc ="upper left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)
            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            #ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            #ax.legend(legend,loc ="lower left")
            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green', 'black'])
            red_patch = mpatches.Patch(color='red', label='D(eleterious)')
            blue_patch = mpatches.Patch(color='blue', label='N(eutral)')
            green_patch = mpatches.Patch(color='green', label='U(nknown) ')
            black_patch = mpatches.Patch(color='black', label='No Data')

            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch,black_patch],loc ="upper left")

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            #ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True)
            #legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green'])
            red_patch = mpatches.Patch(color='red', label='T(olerated)')
            blue_patch = mpatches.Patch(color='blue', label='D(amaging)')
            green_patch = mpatches.Patch(color='green', label='No Data ')


            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch],loc ="upper left")


            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')
        elif(self.chrchoosen.get()=='SCATTER_PLOT'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))

            sizes.append((len(D)))
            sizes.append((len(P)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = ["A ","N","D","P","NoData"]
            #sizes = ([totaltol, totaldele, totalother])*100

            #colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(6, 6), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure


            ax.scatter(labels,sizes,color=['red', 'blue', 'green', 'black', 'cyan'])
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]

            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            #ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            #ax.legend(legend,loc ="lower left")
            ax.scatter(labels,sizes,color=['red', 'blue', 'green', 'black'])

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            #ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True)
            #legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            ax.scatter(labels,sizes,color=['red', 'blue', 'green'])
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')

    def exit(self):
        self.root.destroy()

    def search_window(self):
        ID.clear()
        sift_pred.clear()
        sift_score.clear()
        sift_converted_rs.clear()
        polyphen2_HDIV_Pred.clear()
        polyphen2_HDIV_Score.clear()
        polyphen2_HVAR_Pred.clear()
        polyphen2_HVAR_Score.clear()
        lrt_pred.clear()
        lrt_score.clear()
        lrt_converted_rs.clear()
        mut_assessor_pred.clear()
        mut_assessor_score.clear()
        mutationassessor_rs.clear()
        mut_taster_pred.clear()
        mut_taster_score.clear()
        MutationTaster_converted_rs.clear()
        provean_pred.clear()
        provean_score.clear()
        provean_rs.clear()
        dann_score.clear()
        fathmm_pred.clear()
        fathmm_score.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        fathmm_mkl_rankscore.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_fitcons_rankscore.clear()
        integ_conf_value.clear()
        gerp_rs.clear()
        gerp_rs_rankscore.clear()
        siphy_29way_logOdds.clear()
        siphy_29way_logOdds_rs.clear()
        revel_score_list.clear()
        CADD_raw_list.clear()
        CADD_phred_list.clear()
        genoCanyon_rankscore.clear()
        genoCanyon_score.clear()
        eigen_rawcoding.clear()
        eigen_pc_rawcoding.clear()
        phylo100waylist.clear()
        phylo100wayrankscore.clear()
        phylo17waylist.clear()
        phylo17rankscore.clear()
        phylo30waylist.clear()
        phylo30rankscore.clear()
        phastcons100waylist.clear()
        phastcons100wayrankscore.clear()
        phastcons17waylist.clear()
        phastcons17rankscore.clear()
        phastcons30waylist.clear()
        phastcons30rankscore.clear()
        interpro_domain.clear()
        GTEx_gene.clear()
        GTEx_tissue.clear()
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
        header=['HGVS_id', 'Sift_Pred', 'Sift_Score', 'sift_converted_rankScore', 'Polyphen2_HDIV_Pred', 'Polyphen2_HDIV_Score', 'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score', 'LRT_converted_rankScore', 'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore', 'Mutation_Taster_Pred', 'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred', 'Provean_Score', 'Provean_Rank_score', 'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred', 'Fathmm-mkl_Score', 'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score', 'MetaLR_Pred:', 'MetaLR_Score', 'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value', 'Integrated_fitcons_rankscore', 'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds', 'siphy_29way_logOdds_rankscore', 'Revel_Score', 'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore', 'Eigen_Raw_coding', 'Eigen-pc_Raw_coding', 'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way', 'phylo30rankscore', 'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist', 'phastcons17rankscore', 'phastcons30waylist', 'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']
        data1=[]
        l1 = []

        for i in range(len(sift_pred)):
            data = []
            data.append(ID[i])
            data.append(sift_pred[i])
            data.append(sift_score[i])
            data.append(sift_converted_rs[i])
            data.append(polyphen2_HDIV_Pred[i])
            data.append(polyphen2_HDIV_Score[i])
            data.append(polyphen2_HVAR_Pred[i])
            data.append(polyphen2_HVAR_Score[i])
            data.append(lrt_pred[i])
            data.append(lrt_score[i])
            data.append(lrt_converted_rs[i])
            data.append(mut_assessor_pred[i])
            data.append(mut_assessor_score[i])
            data.append(mutationassessor_rs[i])
            data.append(mut_taster_pred[i])
            data.append(mut_taster_score[i])
            data.append(MutationTaster_converted_rs[i])
            data.append(provean_pred[i])
            data.append(provean_score[i])
            data.append(provean_rs[i])
            data.append(dann_score[i])
            data.append(fathmm_pred[i])
            data.append(fathmm_score[i])
            data.append(fathmm_rs[i])
            data.append(fathmm_mkl_pred[i])
            data.append(fathmm_mkl_score[i])
            data.append(fathmm_mkl_rankscore[i])
            data.append(metasvm_pred[i])
            data.append(metasvm_score[i])
            data.append(metasvm_rankscore[i])
            data.append(metalr_pred[i])
            data.append(metalr_score[i])
            data.append(MetaLR_rankscore[i])

            data.append(integ_fitcoin_score[i])
            data.append(integ_conf_value[i])
            data.append(integ_fitcons_rankscore[i])
            data.append(gerp_rs[i])
            data.append(gerp_rs_rankscore[i])
            data.append(siphy_29way_logOdds[i])
            data.append(siphy_29way_logOdds_rs[i])
            data.append(revel_score_list[i])
            data.append(CADD_raw_list[i])
            data.append(CADD_phred_list[i])
            data.append(genoCanyon_score[i])
            data.append(genoCanyon_rankscore[i])
            data.append(eigen_rawcoding[i])
            data.append(eigen_pc_rawcoding[i])
            data.append(phylo100waylist[i])
            data.append(phylo100wayrankscore[i])
            data.append(phylo17waylist[i])
            data.append(phylo17rankscore[i])
            data.append(phylo30waylist[i])
            data.append(phylo30rankscore[i])
            data.append(phastcons100waylist[i])
            data.append(phastcons100wayrankscore[i])
            data.append(phastcons17waylist[i])
            data.append(phastcons17rankscore[i])
            data.append(phastcons30waylist[i])
            data.append(phastcons30rankscore[i])
            data.append(interpro_domain[i])
            data.append(GTEx_gene[i])
            data.append(GTEx_tissue[i])
            data1.append(data)



        for row in data1:

            d1 = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4],
                  header[5]: row[5], header[6]: row[6], header[7]: row[7], header[8]: row[8], header[9]: row[9]
                , header[10]: row[10], header[11]: row[11], header[12]: row[12], header[13]: row[13],
                  header[14]: row[14]
                , header[15]: row[15], header[16]: row[16], header[17]: row[17], header[18]: row[18],
                  header[19]: row[19]
                , header[20]: row[20], header[21]: row[21], header[22]: row[22], header[23]: row[23],
                  header[24]: row[24]
                , header[25]: row[25], header[26]: row[26], header[27]: row[27], header[28]: row[28],
                  header[29]: row[29],
                  header[30]: row[30], header[31]: row[31], header[32]: row[32], header[33]: row[33],
                  header[34]: row[34],
                  header[35]: row[35], header[36]: row[36], header[37]: row[37], header[38]: row[38],
                  header[39]: row[39],
                  header[40]: row[40], header[41]: row[41], header[42]: row[42]
                , header[43]: row[43], header[44]: row[44], header[45]: row[45], header[46]: row[46]
                , header[47]: row[47], header[48]: row[48]
                , header[49]: row[49], header[50]: row[50], header[51]: row[51], header[52]: row[52]

                , header[53]: row[53], header[54]: row[54]
                , header[55]: row[55], header[56]: row[56], header[57]: row[57], header[58]: row[58],
                  header[59]: row[59],header[60]: row[60],header[61]: row[61]}

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
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)

        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from dbNSFP", font=("Times New Roman", 16, "bold", "italic"),
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
        p= 20

        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)

        try:
            for id in vcf:
                ID.append(id)
                index_id=ID.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                progress['value'] = p

                self.root1.update_idletasks()

                # time.sleep(0.1)
                self.root1.after(100)  # Delay in millisecs.
                p = p + 40

                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(id, assembly='hg38')

                if m == None:

                    sift_pred.append('.')
                    sift_score.append('.')
                    sift_converted_rs.append('.')
                    polyphen2_HDIV_Pred.append('.')
                    polyphen2_HDIV_Score.append('.')
                    polyphen2_HVAR_Pred.append('.')
                    polyphen2_HVAR_Score.append('.')
                    lrt_pred.append('.')
                    lrt_score.append('.')
                    lrt_converted_rs.append('.')
                    mut_assessor_pred.append('.')
                    mut_assessor_score.append('.')
                    mutationassessor_rs.append('.')
                    mut_taster_pred.append('.')
                    mut_taster_score.append('.')
                    MutationTaster_converted_rs.append('.')
                    provean_pred.append('.')
                    provean_score.append('.')
                    provean_rs.append('.')
                    dann_score.append('.')
                    fathmm_pred.append('.')
                    fathmm_score.append('.')
                    fathmm_mkl_rankscore.append('.')
                    fathmm_rs.append('.')
                    fathmm_mkl_pred.append('.')
                    fathmm_mkl_score.append('.')
                    metasvm_pred.append('.')
                    metasvm_score.append('.')
                    metasvm_rankscore.append('.')
                    metalr_pred.append('.')
                    metalr_score.append('.')
                    MetaLR_rankscore.append('.')
                    integ_fitcoin_score.append('.')
                    integ_conf_value.append('.')
                    integ_fitcons_rankscore.append('.')
                    gerp_rs.append('.')
                    gerp_rs_rankscore.append('.')
                    siphy_29way_logOdds.append('.')
                    siphy_29way_logOdds_rs.append('.')
                    revel_score_list.append('.')
                    CADD_raw_list.append('.')
                    CADD_phred_list.append('.')
                    genoCanyon_rankscore.append('.')
                    genoCanyon_score.append('.')
                    eigen_rawcoding.append('.')
                    eigen_pc_rawcoding.append('.')
                    phylo100waylist.append('.')
                    phylo100wayrankscore.append('.')
                    phylo17waylist.append('.')
                    phylo17rankscore.append('.')
                    phylo30waylist.append('.')
                    phylo30rankscore.append('.')
                    phastcons100waylist.append('.')
                    phastcons100wayrankscore.append('.')
                    phastcons17waylist.append('.')
                    phastcons17rankscore.append('.')
                    phastcons30waylist.append('.')
                    phastcons30rankscore.append('.')
                    interpro_domain.append('.')
                    GTEx_gene.append('.')
                    GTEx_tissue.append('.')
                else:

                    if m.get('dbnsfp'):

                        dbnsfp = m['dbnsfp']

                        for key, item in dbnsfp.items():
                            (f"{key} : {item}")
                        if dbnsfp.get('sift'):

                            if dbnsfp['sift'].get('score') and dbnsfp['sift'].get('pred'):
                                if type(dbnsfp['sift']['score']) == list:
                                    siftsc = max(dbnsfp['sift']['score'])
                                    sift_pos = (dbnsfp['sift']['score']).index(max(dbnsfp['sift']['score']))

                                else:
                                    siftsc = (dbnsfp['sift']['score'])

                                if type(dbnsfp['sift']['pred']) == list:
                                    siftpred = (dbnsfp['sift']['pred'])[sift_pos]
                                    if siftpred == '.':
                                       siftpred= (max(dbnsfp['sift']['pred']))

                                else:
                                    siftpred = dbnsfp['sift']['pred']


                            else:

                                siftsc = '.'
                                siftpred = '.'
                            if dbnsfp['sift'].get('converted_rankscore'):
                                if type(dbnsfp['sift'].get('converted_rankscore')) == list:
                                    sift_converted_rankscore = max(dbnsfp['sift']['converted_rankscore'])

                                else:
                                    sift_converted_rankscore = dbnsfp['sift']['converted_rankscore']
                            else:
                                sift_converted_rankscore = '.'

                            if siftsc == '.' and siftpred == '.' and sift_converted_rankscore != '.':
                                if dbnsfp['sift'].get('score'):

                                    siftsc = (dbnsfp['sift']['score'])
                                else:
                                    siftsc = '.'
                                if dbnsfp['sift'].get('pred'):
                                    siftpred = dbnsfp['sift']['pred']
                                else:
                                    siftpred = '.'

                        else:
                            siftsc = '.'
                            siftpred = '.'
                            sift_converted_rankscore = '.'

                        if (siftpred != '.') and siftsc == '.':
                            siftsc = 0
                        sift_pred.append(siftpred)
                        sift_score.append(siftsc)
                        sift_converted_rs.append(sift_converted_rankscore)

                        (f"SIFT Pred : {siftpred}")
                        (f'SIFT Score : {siftsc}')
                        (f'Sift_converted_rankscore : {sift_converted_rankscore}')

                        if dbnsfp.get('polyphen2'):
                            if dbnsfp['polyphen2'].get('hdiv'):

                                if dbnsfp['polyphen2']['hdiv'].get('score') and dbnsfp['polyphen2']['hdiv'].get('pred'):

                                    if type(dbnsfp['polyphen2']['hdiv']['score']) == list:
                                        hdivsc = max(dbnsfp['polyphen2']['hdiv']['score'])
                                        hdiv_pos = (dbnsfp['polyphen2']['hdiv']['score']).index(
                                            max(dbnsfp['polyphen2']['hdiv']['score']))


                                    else:
                                        hdivsc = dbnsfp['polyphen2']['hdiv']['score']

                                    if dbnsfp['polyphen2']['hdiv'].get('pred'):
                                        if type(dbnsfp['polyphen2']['hdiv'].get('pred')) == list:
                                            hdivpr = (dbnsfp['polyphen2']['hdiv']['pred'])[hdiv_pos]
                                            if hdivpr == '.':
                                                hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])


                                        else:
                                            hdivpr = dbnsfp['polyphen2']['hdiv']['pred']
                                else:
                                    hdivpr = '.'
                                    hdivsc = '.'

                                if dbnsfp['polyphen2']['hdiv'].get('rankscore'):
                                    hdivrank = dbnsfp['polyphen2']['hdiv']['rankscore']
                                else:
                                    hdivrank = '.'

                                if hdivpr == '.' and hdivsc == '.' and hdivrank != '.':
                                    if dbnsfp['polyphen2']['hdiv'].get('score'):
                                        hdivsc = dbnsfp['polyphen2']['hdiv']['score']
                                    else:
                                        hdivsc = '.'
                                    if dbnsfp['polyphen2']['hdiv'].get('pred'):

                                        hdivpr = max(dbnsfp['polyphen2']['hdiv']['pred'])
                                    else:
                                        hdivpr = '.'

                                    if hdivsc == '.' and hdivpr != '.':
                                        hdivsc = 0

                            else:
                                hdivsc = '.'
                                hdivpr = '.'

                            if dbnsfp['polyphen2'].get('hvar'):
                                (dbnsfp['polyphen2'])
                                if dbnsfp['polyphen2']['hvar'].get('pred') and dbnsfp['polyphen2']['hvar'].get('score'):

                                    if type(dbnsfp['polyphen2']['hvar']['score']) == list:
                                        hvarsc = max(dbnsfp['polyphen2']['hvar']['score'])
                                        hvarpos = (dbnsfp['polyphen2']['hvar']['score']).index(
                                            max(dbnsfp['polyphen2']['hvar']['score']))

                                    else:
                                        hvarsc = dbnsfp['polyphen2']['hvar']['score']

                                    if type(dbnsfp['polyphen2']['hvar'].get('pred')) == list:
                                        hvarpr = (dbnsfp['polyphen2']['hvar']['pred'])[hvarpos]
                                        if hvarpr == '.':
                                            hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])

                                    elif type(dbnsfp['polyphen2']['hvar'].get('pred')) != list:
                                        hvarpr = dbnsfp['polyphen2']['hvar']['pred']
                                else:
                                    hvarsc = '.'
                                    hvarpr = '.'

                                if dbnsfp['polyphen2']['hvar'].get('rankscore'):
                                    hvarrank = dbnsfp['polyphen2']['hvar']['rankscore']
                                else:
                                    hvarrank = '.'

                                if hvarpr == '.' and hvarsc == '.' and hvarrank != '.':
                                    if dbnsfp['polyphen2']['hvar'].get('score'):
                                        hvarsc = dbnsfp['polyphen2']['hvar']['score']
                                    else:
                                        hvarsc = '.'
                                    if dbnsfp['polyphen2']['hvar'].get('pred'):

                                        hvarpr = max(dbnsfp['polyphen2']['hvar']['pred'])
                                    else:
                                        hvarpr = '.'

                                    if hvarsc == '.' and hvarpr != '.':
                                        hvarsc = 0



                            else:

                                hvarsc = '.'
                                hvarpr = '.'

                        else:
                            hdivsc = '.'
                            hdivpr = '.'
                            hvarpr = '.'
                            hvarsc = '.'
                        if hdivpr != '.' and hdivsc == '.':
                            hdivsc = 0
                        if hvarpr != '.' and hvarsc == '.':
                            hvarsc = 0
                        polyphen2_HDIV_Pred.append(hdivpr)
                        polyphen2_HDIV_Score.append(hdivsc)
                        polyphen2_HVAR_Score.append(hvarsc)
                        polyphen2_HVAR_Pred.append(hvarpr)
                        (f'Polyphen2 HDIV Pred : {hdivpr}')
                        (f'Polyphen2 HDIV Score : {hdivsc}')
                        (f'Polyphen2 HVAR Pred : {hvarpr}')
                        (f'Polyphen2 HVAR Score : {hvarsc}')

                        if dbnsfp.get('lrt'):

                            if dbnsfp['lrt'].get('score') and dbnsfp['lrt'].get('pred'):

                                if type(dbnsfp['lrt'].get('score')) == list:
                                    lrtsc = max(dbnsfp['lrt']['score'])
                                    lrt_pos = (dbnsfp['lrt']['score']).index(max(dbnsfp['lrt']['score']))

                                else:
                                    lrtsc = dbnsfp['lrt']['score']
                                    (f'score : {lrtsc}')

                                if type(dbnsfp['lrt'].get('pred')) == list:

                                    lrtpr = (dbnsfp['lrt']['pred'])[lrt_pos]
                                    if lrtpr == '.':
                                        lrtpr = max(dbnsfp['lrt']['pred'])
                                else:
                                    lrtpr = dbnsfp['lrt']['pred']

                            else:
                                lrtsc = '.'
                                lrtpr = '.'

                            if dbnsfp['lrt'].get('converted_rankscore'):

                                if type(dbnsfp['lrt'].get('converted_rankscore')) == list:
                                    lrt_converted_rankscore = max(dbnsfp['lrt']['converted_rankscore'])

                                elif type(dbnsfp['lrt'].get('converted_rankscore')) != list:
                                    lrt_converted_rankscore = dbnsfp['lrt']['converted_rankscore']

                            else:
                                lrt_converted_rankscore = '.'

                            if lrtpr == '.' and lrtsc == '.' and lrt_converted_rankscore != '.':
                                if dbnsfp['lrt'].get('score'):

                                    lrtsc = dbnsfp['lrt']['score']
                                    (f'score : {lrtsc}')
                                else:
                                    lrtsc = '.'

                                if dbnsfp['lrt'].get('pred'):
                                    lrtpr = dbnsfp['lrt']['pred']
                                else:
                                    lrtpr = '.'




                        else:
                            lrtsc = '.'
                            lrtpr = '.'
                            lrt_converted_rankscore = '.'
                        if (lrtpr != '.') and lrtsc == '.':
                            lrtsc = 0

                        lrt_pred.append(lrtpr)
                        lrt_score.append(lrtsc)
                        lrt_converted_rs.append(lrt_converted_rankscore)
                        (f"LRT Pred : {lrtpr}")
                        (f'LRT Score : {lrtsc}')
                        (f'lrt_converted_rankscore : {lrt_converted_rankscore}')

                        if dbnsfp.get('mutationassessor'):
                            if dbnsfp['mutationassessor'].get('score') and dbnsfp['mutationassessor'].get('pred'):
                                if type(dbnsfp['mutationassessor']['score']) == list:
                                    asssc = max(dbnsfp['mutationassessor']['score'])
                                    ass_pos = (dbnsfp['mutationassessor']['score']).index(
                                        max(dbnsfp['mutationassessor']['score']))
                                else:
                                    asssc = dbnsfp['mutationassessor']['score']

                                if type(dbnsfp['mutationassessor'].get('pred')) == list:

                                    asspr = (dbnsfp['mutationassessor']['pred'])[ass_pos]
                                    if asspr == '.':
                                        asspr = max(dbnsfp['mutationassessor']['pred'])

                                else:
                                    asspr = dbnsfp['mutationassessor']['pred']

                            else:
                                asspr = '.'
                                asssc = '.'

                            if dbnsfp['mutationassessor'].get('rankscore'):
                                if type(dbnsfp['mutationassessor']['rankscore']) == list:
                                    mutationassessor_rankscore = max(dbnsfp['mutationassessor']['rankscore'])
                                else:
                                    mutationassessor_rankscore = dbnsfp['mutationassessor']['rankscore']
                            else:
                                mutationassessor_rankscore = '.'

                            if asspr == '.' and asssc == '.' and mutationassessor_rankscore != '.':
                                if dbnsfp['mutationassessor'].get('score'):
                                    asssc = dbnsfp['mutationassessor']['score']
                                else:
                                    asssc = '.'

                                if dbnsfp['mutationassessor'].get('pred'):
                                    asspr = dbnsfp['mutationassessor']['pred']
                                else:
                                    asspr = '.'

                        else:
                            asspr = '.'
                            asssc = '.'
                            mutationassessor_rankscore = '.'

                        if asssc == '.' and asspr != '.':
                            asssc = 0

                        mut_assessor_pred.append(asspr)
                        mut_assessor_score.append(asssc)
                        mutationassessor_rs.append(mutationassessor_rankscore)
                        (f'Mutation Assessor Pred : {asspr}')
                        (f'Mutation Assessor Score : {asssc}')
                        (f'Mutation Assessor RankScore : {mutationassessor_rankscore}')

                        if dbnsfp.get('mutationtaster'):

                            if dbnsfp['mutationtaster'].get('score') and dbnsfp['mutationtaster'].get('pred'):
                                if type(dbnsfp['mutationtaster']['score']) == list:
                                    tassc = max(dbnsfp['mutationtaster']['score'])
                                    position = (dbnsfp['mutationtaster']['score']).index(
                                        max(dbnsfp['mutationtaster']['score']))
                                    # (index)
                                    # (type(dbnsfp['mutationtaster']['score']))

                                else:
                                    tassc = dbnsfp['mutationtaster']['score']

                                if type(dbnsfp['mutationtaster'].get('pred')) == list:
                                    # taspr = max(dbnsfp['mutationtaster']['pred'])

                                    taspr = (dbnsfp['mutationtaster']['pred'])[position]
                                    if taspr == '.':
                                        taspr = max(dbnsfp['mutationtaster']['pred'])

                                else:
                                    taspr = dbnsfp['mutationtaster']['pred']


                            else:
                                taspr = '.'
                                tassc = '.'

                            if dbnsfp['mutationtaster'].get('converted_rankscore'):
                                if type(dbnsfp['mutationtaster'].get('converted_rankscore')) == list:
                                    # taspr = max(dbnsfp['mutationtaster']['pred'])
                                    MutationTaster_converted_rankscore = \
                                    (dbnsfp['mutationtaster']['converted_rankscore'])[
                                        position]
                                elif type(dbnsfp['mutationtaster'].get('converted_rankscore')) != list:
                                    MutationTaster_converted_rankscore = dbnsfp['mutationtaster']['converted_rankscore']

                            else:
                                MutationTaster_converted_rankscore = '.'

                            if taspr == '.' and tassc == '.' and MutationTaster_converted_rankscore != '.':
                                if dbnsfp['mutationtaster'].get('score'):

                                    tassc = dbnsfp['mutationtaster']['score']
                                else:
                                    tassc = '.'

                                if dbnsfp['mutationtaster'].get('pred'):

                                    taspr = dbnsfp['mutationtaster']['pred']
                                else:
                                    taspr = '.'
                        else:

                            taspr = '.'
                            tassc = '.'
                            MutationTaster_converted_rankscore = '.'
                        if tassc == '.' and taspr != '.':
                            tassc = 0
                        (f'Mutation Taster Pred : {taspr}')
                        (f'Mutation Taster Score : {tassc}')
                        (f'Mutation Taster Converted rankscore : {MutationTaster_converted_rankscore}')
                        mut_taster_pred.append(taspr)
                        mut_taster_score.append(tassc)
                        MutationTaster_converted_rs.append(MutationTaster_converted_rankscore)

                        if dbnsfp.get('genocanyon'):
                            if dbnsfp['genocanyon'].get('score'):
                                if type(dbnsfp['genocanyon'].get('score')) == list:
                                    genoscore = max(dbnsfp['genocanyon']['score'])
                                elif type(dbnsfp['genocanyon'].get('score')) != list:
                                    genoscore = dbnsfp['genocanyon']['score']
                            else:
                                genoscore = '.'

                            if dbnsfp['genocanyon'].get('rankscore'):
                                if type(dbnsfp['genocanyon']['rankscore']) == list:
                                    geno_rs = max(dbnsfp['genocanyon']['rankscore'])
                                else:
                                    geno_rs = dbnsfp['genocanyon']['rankscore']


                            else:
                                geno_rs = '.'
                        else:
                            genoscore = '.'
                            geno_rs = '.'
                        genoCanyon_score.append(genoscore)
                        genoCanyon_rankscore.append(geno_rs)
                        (f'Genocanyon Score : {genoscore}')
                        (f'genocanyon Rank Score: {geno_rs}')

                        if dbnsfp.get('provean'):

                            if dbnsfp['provean'].get('score') and dbnsfp['provean'].get('pred'):
                                if type(dbnsfp['provean']['score']) == list:
                                    provsc = max(dbnsfp['provean']['score'])
                                    prov_pos = (dbnsfp['provean']['score']).index(max(dbnsfp['provean']['score']))

                                else:
                                    provsc = dbnsfp['provean']['score']

                                if type(dbnsfp['provean'].get('pred')) == list:
                                    provpr = (dbnsfp['provean']['pred'])[prov_pos]
                                    if provpr == '.':
                                        provpr = max(dbnsfp['provean']['pred'])
                                else:
                                    provpr = dbnsfp['provean']['pred']
                            else:
                                provpr = '.'
                                provsc = '.'

                            if dbnsfp['provean'].get('rankscore'):
                                if type(dbnsfp['provean']['rankscore']) == list:
                                    prov_rs = max(dbnsfp['provean']['rankscore'])

                                else:
                                    prov_rs = dbnsfp['provean']['rankscore']

                            else:
                                prov_rs = '.'
                            if provpr == '.' and provsc == '.' and prov_rs != '.':
                                if dbnsfp['provean'].get('score'):
                                    provsc = dbnsfp['provean']['score']
                                else:
                                    provsc = '.'
                                if dbnsfp['provean'].get('pred'):
                                    provpr = dbnsfp['provean']['pred']
                                else:
                                    provpr = '.'

                        else:
                            provpr = '.'
                            provsc = '.'
                            prov_rs = '.'
                        if (provpr != '.') and provsc == '.':
                            provsc = 0

                        provean_pred.append(provpr)
                        provean_score.append(provsc)
                        provean_rs.append(prov_rs)
                        (f'Provean Pred : {provpr}')
                        (f'Provean Score : {provsc}')
                        (f'Provean Rank Score : {prov_rs}')

                        if dbnsfp.get('dann'):
                            if dbnsfp['dann'].get('score'):
                                if type(dbnsfp['dann']['score']) == list:
                                    dann = max(dbnsfp['dann']['score'])

                                else:
                                    dann = dbnsfp['dann']['score']

                            else:
                                dann = '.'

                        else:
                            dann = '.'
                        dann_score.append(dann)
                        (f'DANN Score : {dann}')

                        if dbnsfp.get('fathmm'):
                            if dbnsfp['fathmm'].get('pred') and dbnsfp['fathmm'].get('score'):
                                if type(dbnsfp['fathmm']['score']) == list:
                                    faths = max(dbnsfp['fathmm']['score'])
                                    fath_pos = (dbnsfp['fathmm']['score']).index(max(dbnsfp['fathmm']['score']))

                                else:
                                    faths = dbnsfp['fathmm']['score']

                                if type(dbnsfp['fathmm']['pred']) == list:
                                    fathp = (dbnsfp['fathmm']['pred'])[fath_pos]
                                    if fathp == '.':
                                        fathp = max(dbnsfp['fathmm']['pred'])
                                else:
                                    fathp = dbnsfp['fathmm']['pred']
                            else:
                                fathp = '.'
                                faths = '.'

                            if dbnsfp['fathmm'].get('rankscore'):
                                if type(dbnsfp['fathmm']['rankscore']) == list:
                                    fathrs = max(dbnsfp['fathmm']['rankscore'])
                                else:
                                    fathrs = dbnsfp['fathmm']['rankscore']

                            else:
                                fathrs = '.'
                            if faths == '.' and fathp == '.' and fathrs != '.':
                                if dbnsfp['fathmm'].get('score'):
                                    faths = dbnsfp['fathmm']['score']
                                else:
                                    faths = '.'
                                if dbnsfp['fathmm'].get('pred'):
                                    fathp = dbnsfp['fathmm']['pred']
                                else:
                                    fathp = '.'
                        else:
                            fathp = '.'
                            faths = '.'
                            fathrs = '.'

                        if faths == '.' and fathp != '.':
                            faths = 0
                        fathmm_pred.append(fathp)
                        fathmm_score.append(faths)
                        fathmm_rs.append(fathrs)
                        (f'Fathmm Pred : {fathp}')
                        (f'Fathmm Score : {faths}')
                        (f'Fathmm Rank Score : {fathrs}')

                        if dbnsfp.get('fathmm-mkl'):
                            if dbnsfp['fathmm-mkl'].get('coding_pred') and dbnsfp['fathmm-mkl'].get('coding_score'):
                                if type(dbnsfp['fathmm-mkl']['coding_score']) == list:
                                    fathsc = max(dbnsfp['fathmm-mkl']['coding_score'])
                                    fathm_pos = (dbnsfp['fathmm-mkl']['coding_score']).index(
                                        max(dbnsfp['fathmm-mkl']['coding_score']))
                                else:
                                    fathsc = dbnsfp['fathmm-mkl']['coding_score']

                                if type(dbnsfp['fathmm-mkl'].get('coding_pred')) == list:
                                    fathpr = (dbnsfp['fathmm-mkl']['coding_pred'])[fathm_pos]
                                    if fathpr == '.':
                                        fathpr = max(dbnsfp['fathmm-mkl']['coding_pred'])
                                else:
                                    fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                            else:
                                fathpr = '.'
                                fathsc = '.'

                            if dbnsfp['fathmm-mkl'].get('coding_rankscore'):
                                if type(dbnsfp['fathmm-mkl']['coding_rankscore']) == list:
                                    fathcoding_rs = max(dbnsfp['fathmm-mkl']['coding_rankscore'])
                                else:
                                    fathcoding_rs = dbnsfp['fathmm-mkl']['coding_rankscore']
                            else:
                                fathcoding_rs = '.'
                            if fathsc == '.' and fathpr == '.' and fathcoding_rs != '.':
                                if dbnsfp['fathmm-mkl'].get('coding_score'):
                                    fathsc = dbnsfp['fathmm-mkl']['coding_score']
                                else:
                                    fathsc = '.'
                                if dbnsfp['fathmm-mkl'].get('coding_pred'):
                                    fathpr = dbnsfp['fathmm-mkl']['coding_pred']
                                else:
                                    fathpr = '.'

                        else:
                            fathpr = '.'
                            fathsc = '.'
                            fathcoding_rs = '.'
                        if fathsc == '.' and fathpr != '.':
                            fathsc = 0
                        fathmm_mkl_pred.append(fathpr)
                        fathmm_mkl_score.append(fathsc)
                        fathmm_mkl_rankscore.append(fathcoding_rs)
                        (f'Fathmm-mkl Pred : {fathpr}')
                        (f'Fathmm-mkl Score : {fathsc}')
                        (f'Fathmm-mkl RankScore : {fathcoding_rs}')

                        if dbnsfp.get('metasvm'):
                            if dbnsfp['metasvm'].get('pred') and dbnsfp['metasvm'].get('score'):
                                if type(dbnsfp['metasvm']['score']) == list:
                                    svmsc = max(dbnsfp['metasvm']['score'])
                                    svm_pos = (dbnsfp['metasvm']['score']).index(max(dbnsfp['metasvm']['score']))
                                else:
                                    svmsc = dbnsfp['metasvm']['score']
                                if type(dbnsfp['metasvm'].get('pred')) == list:
                                    svmpr = (dbnsfp['metasvm']['pred'])[svm_pos]
                                    if svmpr == '.':
                                        svmpr = max(dbnsfp['metasvm']['pred'])
                                else:
                                    svmpr = dbnsfp['metasvm']['pred']
                            else:
                                svmpr = '.'
                                svmsc = '.'
                            if dbnsfp['metasvm'].get('rankscore'):
                                if type(dbnsfp['metasvm']['rankscore']) == list:
                                    svm_rs = max(dbnsfp['metasvm']['rankscore'])

                                else:
                                    svm_rs = dbnsfp['metasvm']['rankscore']

                            else:
                                svm_rs = '.'

                            if svmpr == '.' and svmsc == '.' and svm_rs != '.':
                                if dbnsfp['metasvm'].get('score'):
                                    svmsc = dbnsfp['metasvm']['score']
                                else:
                                    svmsc = '.'
                                if dbnsfp['metasvm'].get('pred'):
                                    svmpr = dbnsfp['metasvm']['pred']
                                else:
                                    svmpr = '.'

                        else:
                            svmpr = '.'
                            svmsc = '.'
                            svm_rs = '.'
                        if svmpr != '.' and svmsc == '.':
                            svmsc = 0
                        metasvm_pred.append(svmpr)
                        metasvm_score.append(svmsc)
                        metasvm_rankscore.append(svm_rs)
                        (f'MetaSVM Pred : {svmpr}')
                        (f'MetaSVM Score : {svmsc}')
                        (f'MetaSVM Rank Score : {svm_rs}')

                        if dbnsfp.get('metalr'):
                            if dbnsfp['metalr'].get('pred') and dbnsfp['metalr'].get('score'):
                                if type(dbnsfp['metalr']['score']) == list:
                                    lrsc = max(dbnsfp['metalr']['score'])
                                    lr_pos = (dbnsfp['metalr']['score']).index(max(dbnsfp['metalr']['score']))

                                else:
                                    lrsc = dbnsfp['metalr']['score']
                                if type(dbnsfp['metalr'].get('pred')) == list:
                                    lrpr = (dbnsfp['metalr']['pred'])[lrt_pos]
                                    if lrpr == '.':
                                        lrpr = max(dbnsfp['metalr']['pred'])
                                elif type(dbnsfp['metalr'].get('pred')) != list:
                                    lrpr = dbnsfp['metalr']['pred']
                            else:
                                lrpr = '.'
                                lrsc = '.'

                            if dbnsfp['metalr'].get('rankscore'):
                                if type(dbnsfp['metalr']['rankscore']) == list:
                                    lr_rs = max(dbnsfp['metalr']['rankscore'])

                                else:
                                    lr_rs = dbnsfp['metalr']['rankscore']
                            else:
                                lr_rs = '.'
                            if lrpr == '.' and lrsc == '.' and lr_rs != '.':
                                if dbnsfp['metalr'].get('score'):
                                    lrsc = dbnsfp['metalr']['score']
                                else:
                                    lrsc = '.'
                                if dbnsfp['metalr'].get('pred'):
                                    lrpr = dbnsfp['metalr']['pred']
                                else:
                                    lrpr = '.'
                        else:
                            lrpr = '.'
                            lrsc = '.'
                            lr_rs = '.'
                        if lrpr != '.' and lrsc == '.':
                            lrsc = 0
                        metalr_pred.append(lrpr)
                        metalr_score.append(lrsc)
                        MetaLR_rankscore.append(lr_rs)
                        (f"MetaLR_Pred: {lrpr}")
                        (f'MetaLR_Score : {lrsc}')
                        (f'MetaLR_Rank_Score : {lr_rs}')

                        if dbnsfp.get('integrated'):
                            if dbnsfp['integrated'].get('fitcons_score'):

                                if type(dbnsfp['integrated']['fitcons_score']) == list:
                                    fitsc = max(dbnsfp['integrated']['fitcons_score'])

                                else:
                                    fitsc = dbnsfp['integrated']['fitcons_score']

                            else:
                                fitsc = '.'

                            if dbnsfp['integrated'].get('confidence_value'):
                                if type(dbnsfp['integrated']['confidence_value']) == list:
                                    fitcv = max(dbnsfp['integrated']['confidence_value'])

                                else:
                                    fitcv = dbnsfp['integrated']['confidence_value']

                            else:
                                fitcv = 0

                            if dbnsfp['integrated'].get('fitcons_rankscore'):
                                if type(dbnsfp['integrated']['fitcons_rankscore']) == list:
                                    fitrs = max(dbnsfp['integrated']['fitcons_rankscore'])

                                else:
                                    fitrs = dbnsfp['integrated']['fitcons_rankscore']

                            else:
                                fitrs = 0

                        else:
                            fitsc = '.'
                            fitcv = '.'
                            fitrs = '.'
                        (f"Integrated_fitCons_score : {fitsc}")
                        (f"Integrated_confidence_value : {fitcv}")
                        (f"Integrated_fitcons_rankscore: {fitrs}")
                        integ_fitcoin_score.append(fitsc)
                        integ_conf_value.append(fitcv)
                        integ_fitcons_rankscore.append(fitrs)

                        if dbnsfp.get('gerp++'):
                            if dbnsfp['gerp++'].get('rs'):
                                if type(dbnsfp['gerp++']['rs']) == list:
                                    rs = max(dbnsfp['gerp++']['rs'])

                                else:
                                    rs = dbnsfp['gerp++']['rs']

                            else:
                                rs = '.'
                            if dbnsfp['gerp++'].get('rs_rankscore'):
                                if type(dbnsfp['gerp++']['rs_rankscore']) == list:
                                    rs_rank = max(dbnsfp['gerp++']['rs_rankscore'])
                                else:
                                    rs_rank = dbnsfp['gerp++']['rs_rankscore']
                            else:
                                rs_rank = '.'


                        else:
                            rs = '.'
                            rs_rank = '.'
                        gerp_rs.append(rs)
                        gerp_rs_rankscore.append(rs_rank)
                        (f"GERP++_RS : {rs}")
                        (f"GERP++_RS : {rs_rank}")

                        if dbnsfp.get('siphy_29way'):
                            if dbnsfp['siphy_29way'].get('logodds'):
                                if type(dbnsfp['siphy_29way']['logodds']) == list:
                                    siphy = max(dbnsfp['siphy_29way']['logodds'])

                                else:
                                    siphy = dbnsfp['siphy_29way']['logodds']

                            else:
                                siphy = '.'

                            if dbnsfp['siphy_29way'].get('logodds_rankscore'):
                                if type(dbnsfp['siphy_29way']['logodds_rankscore']) == list:
                                    siphyrs = max(dbnsfp['siphy_29way']['logodds_rankscore'])

                                else:
                                    siphyrs = dbnsfp['siphy_29way']['logodds_rankscore']

                            else:
                                siphyrs = '.'

                        else:
                            siphy = '.'
                            siphyrs = '.'

                        siphy_29way_logOdds.append(siphy)
                        siphy_29way_logOdds_rs.append(siphyrs)
                        (f'Siphy_29way_logOdds : {siphy}')
                        (f'Siphy_29way_logOdds_rankscore : {siphyrs}')

                        if dbnsfp.get('revel'):
                            if dbnsfp['revel'].get('score'):
                                if type(dbnsfp['revel']['score']) == list:
                                    revsc = max(dbnsfp['revel']['score'])
                                else:
                                    revsc = dbnsfp['revel']['score']
                            else:
                                revsc = '.'
                        else:
                            revsc = '.'
                        revel_score_list.append(revsc)
                        (f'Revel_Score : {revsc}')

                        if dbnsfp.get('eigen'):
                            if dbnsfp['eigen'].get('raw_coding'):
                                if type(dbnsfp['eigen']['raw_coding']) == list:
                                    eigen_rc = max(dbnsfp['eigen']['raw_coding'])
                                else:
                                    eigen_rc = dbnsfp['eigen']['raw_coding']
                            else:
                                eigen_rc = '.'
                        else:
                            eigen_rc = '.'
                        eigen_rawcoding.append(eigen_rc)
                        (f'Eigen Raw Coding : {eigen_rc}')

                        if dbnsfp.get('phylo'):
                            if dbnsfp['phylo'].get('p100way'):
                                if dbnsfp['phylo']['p100way'].get('vertebrate'):

                                    if type(dbnsfp['phylo']['p100way']['vertebrate']) == list:
                                        phylo100way = max(dbnsfp['phylo']['p100way']['vertebrate'])
                                    else:
                                        phylo100way = dbnsfp['phylo']['p100way']['vertebrate']
                                else:
                                    phylo100way = '.'

                                if dbnsfp['phylo']['p100way'].get('vertebrate_rankscore'):

                                    if type(dbnsfp['phylo']['p100way']['vertebrate_rankscore']) == list:
                                        phylo100wayrs = max(dbnsfp['phylo']['p100way']['vertebrate_rankscore'])
                                    else:
                                        phylo100wayrs = dbnsfp['phylo']['p100way']['vertebrate_rankscore']
                                else:
                                    phylo100wayrs = '.'
                            else:
                                phylo100way = '.'
                                phylo100wayrs = '.'
                            if dbnsfp['phylo'].get('p17way'):
                                if dbnsfp['phylo']['p17way'].get('primate'):
                                    if type(dbnsfp['phylo']['p17way']['primate']) == list:
                                        phylo17 = max(dbnsfp['phylo']['p17way']['primate'])
                                    else:
                                        phylo17 = dbnsfp['phylo']['p17way']['primate']
                                else:

                                    phylo17 = '.'
                                if dbnsfp['phylo']['p17way'].get('primate_rankscore'):
                                    if type(dbnsfp['phylo']['p17way']['primate_rankscore']) == list:
                                        phylo17rs = max(dbnsfp['phylo']['p17way']['primate_rankscore'])
                                    else:
                                        phylo17rs = dbnsfp['phylo']['p17way']['primate_rankscore']
                                else:

                                    phylo17rs = '.'
                            else:
                                phylo17 = '.'
                                phylo17rs = '.'
                            if dbnsfp['phylo'].get('p30way'):
                                if dbnsfp['phylo']['p30way'].get('mammalian'):
                                    if type(dbnsfp['phylo']['p30way']['mammalian']) == list:
                                        phylo30 = max(dbnsfp['phylo']['p30way']['mammalian'])
                                    else:
                                        phylo30 = dbnsfp['phylo']['p30way']['mammalian']
                                else:

                                    phylo30 = '.'
                                if dbnsfp['phylo']['p30way'].get('mammalian_rankscore'):
                                    if type(dbnsfp['phylo']['p30way']['mammalian_rankscore']) == list:
                                        phylo30rs = max(dbnsfp['phylo']['p30way']['mammalian_rankscore'])
                                    else:
                                        phylo30rs = dbnsfp['phylo']['p30way']['mammalian_rankscore']
                                else:

                                    phylo30rs = '.'
                            else:
                                phylo30 = '.'
                                phylo30rs = '.'


                        else:
                            phylo100way = '.'
                            phylo100wayrs = '.'
                            phylo17 = '.'
                            phylo17rs = '.'
                            phylo30 = '.'
                            phylo30rs = '.'
                        phylo100waylist.append(phylo100way)
                        phylo100wayrankscore.append(phylo100wayrs)
                        phylo17waylist.append(phylo17)
                        phylo17rankscore.append(phylo17rs)
                        phylo30waylist.append(phylo30)
                        phylo30rankscore.append(phylo30rs)
                        (f'phylo100way_vertebrate  : {phylo100way}')
                        (f'phylo100way_vertebrateRankscore  : {phylo100wayrs}')
                        (f'phylo17way_primate  : {phylo17}')
                        (f'phylo17way_primate_rankscore  : {phylo17rs}')
                        (f'phylo30way_mammalian  : {phylo30}')
                        (f'phylo30way_mammalian_rankscore  : {phylo30rs}')

                        if dbnsfp.get('phastcons'):
                            if dbnsfp['phastcons'].get('100way'):
                                if dbnsfp['phastcons']['100way'].get('vertebrate'):

                                    if type(dbnsfp['phastcons']['100way']['vertebrate']) == list:
                                        phastcons100way = max(dbnsfp['phastcons']['100way']['vertebrate'])
                                    else:
                                        phastcons100way = dbnsfp['phastcons']['100way']['vertebrate']
                                else:
                                    phastcons100way = '.'

                                if dbnsfp['phastcons']['100way'].get('vertebrate_rankscore'):

                                    if type(dbnsfp['phastcons']['100way']['vertebrate_rankscore']) == list:
                                        phastcons100wayrs = max(dbnsfp['phastcons']['100way']['vertebrate_rankscore'])
                                    else:
                                        phastcons100wayrs = dbnsfp['phastcons']['100way']['vertebrate_rankscore']
                                else:
                                    phastcons100wayrs = '.'
                            else:
                                phastcons100way = '.'
                                phastcons100wayrs = '.'
                            if phastcons100wayrs != '.' and phastcons100way == '.':
                                phastcons100way = 0
                            if dbnsfp['phastcons'].get('p17way'):
                                if dbnsfp['phastcons']['p17way'].get('primate'):
                                    if type(dbnsfp['phastcons']['p17way']['primate']) == list:
                                        phastcons17 = max(dbnsfp['phastcons']['p17way']['primate'])
                                    else:
                                        phastcons17 = dbnsfp['phastcons']['p17way']['primate']
                                else:

                                    phastcons17 = '.'
                                if dbnsfp['phastcons']['p17way'].get('primate_rankscore'):
                                    if type(dbnsfp['phastcons']['p17way']['primate_rankscore']) == list:
                                        phastcons17rs = max(dbnsfp['phastcons']['p17way']['primate_rankscore'])
                                    else:
                                        phastcons17rs = dbnsfp['phastcons']['p17way']['primate_rankscore']
                                else:

                                    phastcons17rs = '.'
                            else:
                                phastcons17 = '.'
                                phastcons17rs = '.'
                            if phastcons17rs != '.' and phastcons17 == '.':
                                phastcons17 = 0
                            if dbnsfp['phastcons'].get('30way'):
                                if dbnsfp['phastcons']['30way'].get('mammalian'):
                                    if type(dbnsfp['phastcons']['30way']['mammalian']) == list:
                                        phastcons30 = max(dbnsfp['phastcons']['30way']['mammalian'])
                                    else:
                                        phastcons30 = dbnsfp['phastcons']['30way']['mammalian']
                                else:

                                    phastcons30 = '.'
                                if dbnsfp['phastcons']['30way'].get('mammalian_rankscore'):
                                    if type(dbnsfp['phastcons']['30way']['mammalian_rankscore']) == list:
                                        phastcons30rs = max(dbnsfp['phastcons']['30way']['mammalian_rankscore'])
                                    else:
                                        phastcons30rs = dbnsfp['phastcons']['30way']['mammalian_rankscore']
                                else:

                                    phastcons30rs = '.'
                            else:
                                phastcons30 = '.'
                                phastcons30rs = '.'
                            if phastcons30rs != '.' and phastcons30 == '.':
                                phastcons30 = 0


                        else:
                            phastcons100way = '.'
                            phastcons100wayrs = '.'
                            phastcons17 = '.'
                            phastcons17rs = '.'
                            phastcons30 = '.'
                            phastcons30rs = '.'
                        phastcons100waylist.append(phastcons100way)
                        phastcons100wayrankscore.append(phastcons100wayrs)
                        phastcons17waylist.append(phastcons17)
                        phastcons17rankscore.append(phastcons17rs)
                        phastcons30waylist.append(phastcons30)
                        phastcons30rankscore.append(phastcons30rs)
                        (f'phastcons100way_vertebrate  : {phastcons100way}')
                        (f'phastcons100way_vertebrateRankscore  : {phastcons100wayrs}')
                        (f'phastcons17way_primate  : {phastcons17}')
                        (f'phastcons17way_primate_rankscore  : {phastcons17rs}')
                        (f'phastcons30way_mammalian  : {phastcons30}')
                        (f'phastcons30way_mammalian_rankscore  : {phastcons30rs}')

                        if dbnsfp.get('eigen-pc'):
                            if dbnsfp['eigen-pc'].get('raw_coding'):
                                if type(dbnsfp['eigen-pc']['raw_coding']) == list:
                                    eigenpc_rc = max(dbnsfp['eigen-pc']['raw_coding'])
                                else:
                                    eigenpc_rc = dbnsfp['eigen-pc']['raw_coding']
                            else:
                                eigenpc_rc = '.'
                        else:
                            eigenpc_rc = '.'
                        eigen_pc_rawcoding.append(eigenpc_rc)
                        (f'Eigen-pc Raw Coding : {eigenpc_rc}')

                        if dbnsfp.get('interpro_domain'):
                            if type(dbnsfp['interpro_domain']) == list:
                                interpro = max(dbnsfp['interpro_domain'])
                            else:
                                interpro = dbnsfp['interpro_domain']
                        else:
                            interpro = '.'
                        interpro_domain.append(interpro)
                        (f'Interpro_DOmain : {interpro}')
                        gene = ''
                        tissue = ''
                        if dbnsfp.get('gtex'):
                            if type(dbnsfp['gtex']) == list:

                                for i in dbnsfp['gtex']:
                                    gene += i['gene'] + ' | '
                                    tissue += i['tissue'] + ' | '

                            elif type(dbnsfp['gtex']) == dict:
                                gene += dbnsfp['gtex']['gene'] + "  "
                                tissue += dbnsfp['gtex']['tissue'] + '  '
                            else:
                                gene += '.  '
                                tissue += '.  '
                        else:
                            gene += '.  '
                            tissue += '.  '

                        GTEx_gene.append(gene[:-2])
                        GTEx_tissue.append(tissue[:-2])
                        (f'GTEx_gene {gene[:-2]}')
                        (f'GTEx_tissue{tissue[:-2]}')






                    else:
                        sift_pred.append('.')
                        sift_score.append('.')
                        sift_converted_rs.append('.')
                        polyphen2_HDIV_Pred.append('.')
                        polyphen2_HDIV_Score.append('.')
                        polyphen2_HVAR_Pred.append('.')
                        polyphen2_HVAR_Score.append('.')
                        lrt_pred.append('.')
                        lrt_score.append('.')
                        lrt_converted_rs.append('.')
                        mut_assessor_pred.append('.')
                        mut_assessor_score.append('.')
                        mutationassessor_rs.append('.')
                        mut_taster_pred.append('.')
                        mut_taster_score.append('.')
                        MutationTaster_converted_rs.append('.')
                        provean_pred.append('.')
                        provean_score.append('.')
                        provean_rs.append('.')
                        dann_score.append('.')
                        fathmm_pred.append('.')
                        fathmm_score.append('.')
                        fathmm_rs.append('.')
                        fathmm_mkl_pred.append('.')
                        fathmm_mkl_score.append('.')
                        fathmm_mkl_rankscore.append('.')
                        metasvm_pred.append('.')
                        metasvm_score.append('.')
                        metasvm_rankscore.append('.')
                        metalr_pred.append('.')
                        metalr_score.append('.')
                        MetaLR_rankscore.append('.')
                        integ_fitcoin_score.append('.')
                        integ_conf_value.append('.')
                        integ_fitcons_rankscore.append('.')
                        gerp_rs.append('.')
                        gerp_rs_rankscore.append('.')
                        siphy_29way_logOdds.append('.')
                        siphy_29way_logOdds_rs.append('.')
                        revel_score_list.append('.')
                        genoCanyon_score.append('.')
                        genoCanyon_rankscore.append('.')
                        eigen_rawcoding.append('.')
                        eigen_pc_rawcoding.append('.')
                        phylo100waylist.append('.')
                        phylo100wayrankscore.append('.')
                        phylo17waylist.append('.')
                        phylo17rankscore.append('.')
                        phylo30waylist.append('.')
                        phylo30rankscore.append('.')
                        phastcons100waylist.append('.')
                        phastcons100wayrankscore.append('.')
                        phastcons17waylist.append('.')
                        phastcons17rankscore.append('.')
                        phastcons30waylist.append('.')
                        phastcons30rankscore.append('.')
                        interpro_domain.append('.')
                        GTEx_gene.append('.')
                        GTEx_tissue.append('.')

                    if m.get('cadd'):
                        # (f"{i} : {m[i]}")
                        CADD = m['cadd']
                        if CADD.get('rawscore'):
                            if type(CADD['rawscore']) == list:
                                CADDraw = max(CADD['rawscore'])
                            else:
                                CADDraw = CADD['rawscore']
                        else:
                            CADDraw = '.'
                        CADD_raw_list.append(CADDraw)
                        (f"CADD RAW Score : {CADDraw}")

                        if CADD.get('phred'):
                            if type(CADD['phred']) == list:
                                CADDp = max(CADD['phred'])
                            else:
                                CADDp = CADD['phred']
                        else:
                            CADDp = '.'
                        CADD_phred_list.append(CADDp)
                        (f"CADD Phred : {CADDp}")

                    else:
                        CADD_raw_list.append('.')
                        CADD_phred_list.append('.')
        except Exception as es:
            self.error_str = es
            ###########################
        self.root = root
        self.root.title('dbNSFP window')
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
        title = Label(self.root, text="VCESS Retrieving Data from dbNSFP",
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

        img1 = Image.open(r'images/fin_logo-removebg.png')
        img1 = img1.resize((250, 130), Image.ANTIALIAS)  # antialias converts high into low level image
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image=self.photoimage1, bg='#7877a5', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='White')
        url = 'http://database.liulab.science/dbNSFP'
        new = 1

        def openweb():
            webbrowser.open(url, new=new)

        Btn = Button(self.frametwo, text="http://database.liulab.science/dbNSFP",
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
                                  text=f"dbNSFP is a database developed for functional\n"
                                       f"prediction and annotation of all potential non-\n"
                                       f"synonymous single-nucleotide variants (nsSNVs) \n"
                                       f"in the human genome. Its current version is based\n"
                                       f"on the Gencode release 29 / Ensembl version 94 and\n"
                                       f"includes a total of 84,013,490 nsSNVs and ssSNVs \n"
                                       f"(splicing-site SNVs). It compiles prediction scores\n"
                                       f" from 37 prediction algorithms",
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.grid(padx=0, pady=0)
        canvas.place(x=int(width / 2) - 225, y=50, width=450, height=200)

        fps = 5  # Change the fps to make the animation faster/slower
        shift()

        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=1600)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(sift_score)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(ID) == len(sift_score):



                ################################

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
                # table = ttk.Treeview(table1, height="8")  #################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID','Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore', 'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                    'Provean_Score', 'Provean_Rank_score',
                                    'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred', 'MetaLR_Score',
                                    'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                    "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

                table.column('#0', width=120, minwidth=120)
                table.column('ID', anchor=W, width=150)
                table.column('Sift_Pred', anchor=W, width=120)
                table.column('Sift_Score', anchor=W, width=120)
                table.column('Sift_converted_rankScore', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Pred', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Score', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Pred', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Score', anchor=W, width=120)
                table.column('LRT_Pred', anchor=W, width=120)
                table.column('LRT_Score', anchor=W, width=120)
                table.column('LRT_converted_rankScore', anchor=W, width=120)
                table.column('Mutation_Assessor_Pred', anchor=W, width=120)
                table.column('Mutation_Assessor_Score', anchor=W, width=120)
                table.column('Mutation_Assessor_rankscore', anchor=W, width=120)
                table.column('Mutation_Taster_Pred', anchor=W, width=120)
                table.column('Mutation_Taster_Score', anchor=W, width=120)
                table.column('MutationTaster_converted_rankscore', anchor=W, width=120)
                table.column('Provean_Pred', anchor=W, width=120)
                table.column('Provean_Score', anchor=W, width=120)
                table.column('Provean_Rank_score', anchor=W, width=120)
                table.column('DANN Score', anchor=W, width=120)
                table.column('Fathmm_Pred', anchor=W, width=120)
                table.column('Fathmm_Score', anchor=W, width=120)
                table.column('fathmm_Rank_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_Pred', anchor=W, width=120)
                table.column('Fathmm-mkl_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_RankScore', anchor=W, width=120)
                table.column('MetaSVM_Pred', anchor=W, width=120)
                table.column('MetaSVM_Score', anchor=W, width=120)
                table.column('Meta_SVM_Rank_Score', anchor=W, width=120)
                table.column('MetaLR_Pred', anchor=W, width=120)
                table.column('MetaLR_Score', anchor=W, width=120)
                table.column('MetaLR_Rank_Score', anchor=W, width=120)
                table.column('Integrated_fitCons_score', anchor=W, width=120)
                table.column('Integrated_confidence_value', anchor=W, width=120)
                table.column('Integrated_fitcons_rankscore', anchor=W, width=120)
                table.column('GERP++_RS', anchor=W, width=120)
                table.column('GERP++_RS_Rankscore', anchor=W, width=120)
                table.column('Siphy_29way_logOdds', anchor=W, width=120)
                table.column('siphy_29way_logOdds_rankscore', anchor=W, width=120)
                table.column('Revel_Score', anchor=W, width=120)
                table.column('CADD_raw_score', anchor=W, width=120)
                table.column('CADD_Phred', anchor=W, width=120)
                table.column('genoCanyon_score', anchor=W, width=120)
                table.column('genoCanyon_rankscore', anchor=W, width=120)
                table.column("Eigen_Raw_coding", anchor=W, width=120)
                table.column("Eigen-pc_Raw_coding", anchor=W, width=120)
                table.column('phylo100way', anchor=W, width=120)
                table.column('phylo100wayrankscore', anchor=W, width=120)
                table.column('phylo17way', anchor=W, width=120)
                table.column('phylo17rankscore', anchor=W, width=120)
                table.column('phylo30way', anchor=W, width=120)
                table.column('phylo30rankscore', anchor=W, width=120)
                table.column('phastcons100waylist', anchor=W, width=120)
                table.column('phastcons100wayrankscore', anchor=W, width=120)
                table.column('phastcons17waylist', anchor=W, width=120)
                table.column('phastcons17rankscore', anchor=W, width=120)
                table.column('phastcons30waylist', anchor=W, width=120)
                table.column('phastcons30rankscore', anchor=W, width=120)
                table.column('Interpro_Domain', anchor=W, width=120)
                table.column('GTEx_gene', anchor=W, width=120)
                table.column('GTEx_tisuue', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
                table.heading('Sift_Score', text='Sift_Score', anchor=W)
                table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
                table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
                table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
                table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
                table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
                table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
                table.heading('LRT_Score', text='LRT_Score', anchor=W)
                table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
                table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
                table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
                table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
                table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
                table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
                table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
                table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
                table.heading('Provean_Score', text='Provean_Score', anchor=W)
                table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
                table.heading('DANN Score', text='DANN Score', anchor=W)
                table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
                table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
                table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
                table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
                table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
                table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
                table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
                table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
                table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
                table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
                table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
                table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
                table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
                table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
                table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
                table.heading('Revel_Score', text='Revel_Score', anchor=W)
                table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
                table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
                table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
                table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
                table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
                table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
                table.heading('phylo100way', text='phylo100way', anchor=W)
                table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
                table.heading('phylo17way', text='phylo17way', anchor=W)
                table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
                table.heading('phylo30way', text='phylo30way', anchor=W)
                table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
                table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
                table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
                table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
                table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
                table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
                table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
                table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
                table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
                table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(ID[i],sift_pred[i],
                                         sift_score[i],
                                         sift_converted_rs[i],
                                         polyphen2_HDIV_Pred[i],
                                         polyphen2_HDIV_Score[i],
                                         polyphen2_HVAR_Pred[i],
                                         polyphen2_HVAR_Score[i],
                                         lrt_pred[i],
                                         lrt_score[i],
                                         lrt_converted_rs[i],
                                         mut_assessor_pred[i],
                                         mut_assessor_score[i],
                                         mutationassessor_rs[i],
                                         mut_taster_pred[i],
                                         mut_taster_score[i],
                                         MutationTaster_converted_rs[i],
                                         provean_pred[i],
                                         provean_score[i],
                                         provean_rs[i],
                                         dann_score[i],
                                         fathmm_pred[i],
                                         fathmm_score[i],
                                         fathmm_rs[i],
                                         fathmm_mkl_pred[i],
                                         fathmm_mkl_score[i],
                                         fathmm_mkl_rankscore[i],
                                         metasvm_pred[i],
                                         metasvm_score[i],
                                         metasvm_rankscore[i],
                                         metalr_pred[i],
                                         metalr_score[i],
                                         MetaLR_rankscore[i],
                                         integ_fitcoin_score[i],integ_conf_value[i],
                                         integ_fitcons_rankscore[i],
                                         gerp_rs[i],
                                         gerp_rs_rankscore[i],
                                         siphy_29way_logOdds[i],
                                         siphy_29way_logOdds_rs[i],
                                         revel_score_list[i],
                                         CADD_raw_list[i],
                                         CADD_phred_list[i],
                                         genoCanyon_rankscore[i],
                                         genoCanyon_score[i],
                                         eigen_rawcoding[i],
                                         eigen_pc_rawcoding[i],
                                         phylo100waylist[i],
                                         phylo100wayrankscore[i],
                                         phylo17waylist[i],
                                         phylo17rankscore[i],
                                         phylo30waylist[i],
                                         phylo30rankscore[i],
                                         phastcons100waylist[i],
                                         phastcons100wayrankscore[i],
                                         phastcons17waylist[i],
                                         phastcons17rankscore[i],
                                         phastcons30waylist[i],
                                         phastcons30rankscore[i],
                                         interpro_domain[i],
                                         GTEx_gene[i],
                                         GTEx_tissue[i]

                                         ))
                ##################
                table.place(x=0, y=0, width=1200, height=400)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################
                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################
                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                ##############################################################################################
                ###Creates frame widget under which all other widgets will be kept
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
                chr = Label(self.frametwo, text="GRAPHS", font=("Times New Roman", 16, 'bold'), bg='white',
                            fg='black')
                chr.grid(padx=0, pady=0)
                chr.place(x=250, y=640)
                self.sift_pred = sift_pred
                self.sift_score = sift_score
                self.lrt_pred = lrt_pred
                self.mut_taster_pred = mut_taster_pred

                # Combobox creation
                self.chrstring = tkinter.StringVar(self.frametwo)
                self.chrchoosen = ttk.Combobox(self.frametwo, width=27, textvariable=self.chrstring, state='readonly')
                # chrchoosen = ttk.Combobox(self.root, width=27, textvariable=self.chrstring)

                # Adding combobox drop down list
                self.chrchoosen.bind("<<ComboboxSelected>>", self.justamethod)
                self.chrchoosen['values'] = (
                    'BAR_GRAPH', 'PIE_CHART','SCATTER_PLOT')
                # (self.chrchoosen.index(0))

                self.chrchoosen.grid(column=1, row=5, padx=0, pady=0)
                self.chrchoosen.place(x=360, y=645)
                self.chrchoosen.current(0)
                # for values in chrchoosen:
            elif len(ID) != len(sift_score)   and (len(ID) and len(sift_score))!=0:

                ################################

                table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG19)",
                                    font=('Times New Roman', 16, 'bold'),
                                    bg='white')  ################
                # table1.pack(fill="both", expand="yes", padx=50, pady=300)  ###################
                # table = ttk.Treeview(table1, height="8")  #################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)  ###################
                table = ttk.Treeview(table1, height="50")  #################

                table['columns'] = ['ID','Sift_Pred', 'Sift_Score', 'Sift_converted_rankScore', 'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred',
                                    'Provean_Score', 'Provean_Rank_score',
                                    'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred', 'MetaLR_Score',
                                    'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore',
                                    "Eigen_Raw_coding", "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']

                table.column('#0', width=120, minwidth=120)
                table.column('ID', anchor=W, width=150)
                table.column('Sift_Pred', anchor=W, width=120)
                table.column('Sift_Score', anchor=W, width=120)
                table.column('Sift_converted_rankScore', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Pred', anchor=W, width=120)
                table.column('Polyphen2_HDIV_Score', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Pred', anchor=W, width=120)
                table.column('Polyphen2_HVAR_Score', anchor=W, width=120)
                table.column('LRT_Pred', anchor=W, width=120)
                table.column('LRT_Score', anchor=W, width=120)
                table.column('LRT_converted_rankScore', anchor=W, width=120)
                table.column('Mutation_Assessor_Pred', anchor=W, width=120)
                table.column('Mutation_Assessor_Score', anchor=W, width=120)
                table.column('Mutation_Assessor_rankscore', anchor=W, width=120)
                table.column('Mutation_Taster_Pred', anchor=W, width=120)
                table.column('Mutation_Taster_Score', anchor=W, width=120)
                table.column('MutationTaster_converted_rankscore', anchor=W, width=120)
                table.column('Provean_Pred', anchor=W, width=120)
                table.column('Provean_Score', anchor=W, width=120)
                table.column('Provean_Rank_score', anchor=W, width=120)
                table.column('DANN Score', anchor=W, width=120)
                table.column('Fathmm_Pred', anchor=W, width=120)
                table.column('Fathmm_Score', anchor=W, width=120)
                table.column('fathmm_Rank_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_Pred', anchor=W, width=120)
                table.column('Fathmm-mkl_Score', anchor=W, width=120)
                table.column('Fathmm-mkl_RankScore', anchor=W, width=120)
                table.column('MetaSVM_Pred', anchor=W, width=120)
                table.column('MetaSVM_Score', anchor=W, width=120)
                table.column('Meta_SVM_Rank_Score', anchor=W, width=120)
                table.column('MetaLR_Pred', anchor=W, width=120)
                table.column('MetaLR_Score', anchor=W, width=120)
                table.column('MetaLR_Rank_Score', anchor=W, width=120)
                table.column('Integrated_fitCons_score', anchor=W, width=120)
                table.column('Integrated_confidence_value', anchor=W, width=120)
                table.column('Integrated_fitcons_rankscore', anchor=W, width=120)
                table.column('GERP++_RS', anchor=W, width=120)
                table.column('GERP++_RS_Rankscore', anchor=W, width=120)
                table.column('Siphy_29way_logOdds', anchor=W, width=120)
                table.column('siphy_29way_logOdds_rankscore', anchor=W, width=120)
                table.column('Revel_Score', anchor=W, width=120)
                table.column('CADD_raw_score', anchor=W, width=120)
                table.column('CADD_Phred', anchor=W, width=120)
                table.column('genoCanyon_score', anchor=W, width=120)
                table.column('genoCanyon_rankscore', anchor=W, width=120)
                table.column("Eigen_Raw_coding", anchor=W, width=120)
                table.column("Eigen-pc_Raw_coding", anchor=W, width=120)
                table.column('phylo100way', anchor=W, width=120)
                table.column('phylo100wayrankscore', anchor=W, width=120)
                table.column('phylo17way', anchor=W, width=120)
                table.column('phylo17rankscore', anchor=W, width=120)
                table.column('phylo30way', anchor=W, width=120)
                table.column('phylo30rankscore', anchor=W, width=120)
                table.column('phastcons100waylist', anchor=W, width=120)
                table.column('phastcons100wayrankscore', anchor=W, width=120)
                table.column('phastcons17waylist', anchor=W, width=120)
                table.column('phastcons17rankscore', anchor=W, width=120)
                table.column('phastcons30waylist', anchor=W, width=120)
                table.column('phastcons30rankscore', anchor=W, width=120)
                table.column('Interpro_Domain', anchor=W, width=120)
                table.column('GTEx_gene', anchor=W, width=120)
                table.column('GTEx_tisuue', anchor=W, width=200)

                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='ID', anchor=W)
                table.heading('Sift_Pred', text='Sift_Pred', anchor=W)
                table.heading('Sift_Score', text='Sift_Score', anchor=W)
                table.heading('Sift_converted_rankScore', text='Sift_converted_rankScore', anchor=W)
                table.heading('Polyphen2_HDIV_Pred', text='Polyphen2_HDIV_Pred', anchor=W)
                table.heading('Polyphen2_HDIV_Score', text='Polyphen2_HDIV_Score', anchor=W)
                table.heading('Polyphen2_HVAR_Pred', text='Polyphen2_HVAR_Pred', anchor=W)
                table.heading('Polyphen2_HVAR_Score', text='Polyphen2_HVAR_Score', anchor=W)
                table.heading('LRT_Pred', text='LRT_Pred', anchor=W)
                table.heading('LRT_Score', text='LRT_Score', anchor=W)
                table.heading('LRT_converted_rankScore', text='LRT_converted_rankScore', anchor=W)
                table.heading('Mutation_Assessor_Pred', text='Mutation_Assessor_Pred', anchor=W)
                table.heading('Mutation_Assessor_Score', text='Mutation_Assessor_Score', anchor=W)
                table.heading('Mutation_Assessor_rankscore', text='Mutation_Assessor_rankscore', anchor=W)
                table.heading('Mutation_Taster_Pred', text='Mutation_Taster_Pred', anchor=W)
                table.heading('Mutation_Taster_Score', text='Mutation_Taster_Score', anchor=W)
                table.heading('MutationTaster_converted_rankscore', text='MutationTaster_converted_rankscore', anchor=W)
                table.heading('Provean_Pred', text='Provean_Pred', anchor=W)
                table.heading('Provean_Score', text='Provean_Score', anchor=W)
                table.heading('Provean_Rank_score', text='Provean_Rank_score', anchor=W)
                table.heading('DANN Score', text='DANN Score', anchor=W)
                table.heading('Fathmm_Pred', text='Fathmm_Pred', anchor=W)
                table.heading('Fathmm_Score', text='Fathmm_Score', anchor=W)
                table.heading('fathmm_Rank_Score', text='fathmm_Rank_Score', anchor=W)
                table.heading('Fathmm-mkl_Pred', text='Fathmm-mkl_Pred', anchor=W)
                table.heading('Fathmm-mkl_Score', text='Fathmm-mkl_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Fathmm-mkl_RankScore', text='Fathmm-mkl_RankScore', anchor=W)
                table.heading('MetaSVM_Pred', text='MetaSVM_Pred', anchor=W)
                table.heading('MetaSVM_Score', text='MetaSVM_Score', anchor=W)
                table.heading('Meta_SVM_Rank_Score', text='Meta_SVM_Rank_Score', anchor=W)
                table.heading('MetaLR_Pred', text='MetaLR_Pred', anchor=W)
                table.heading('MetaLR_Score', text='MetaLR_Score', anchor=W)
                table.heading('MetaLR_Rank_Score', text='MetaLR_Rank_Score', anchor=W)
                table.heading('Integrated_fitCons_score', text='Integrated_fitCons_score', anchor=W)
                table.heading('Integrated_confidence_value', text='Integrated_confidence_value', anchor=W)
                table.heading('Integrated_fitcons_rankscore', text='Integrated_fitcons_rankscore', anchor=W)
                table.heading('GERP++_RS', text='GERP++_RS', anchor=W)
                table.heading('GERP++_RS_Rankscore', text='GERP++_RS_Rankscore', anchor=W)
                table.heading('Siphy_29way_logOdds', text='Siphy_29way_logOdds', anchor=W)
                table.heading('siphy_29way_logOdds_rankscore', text='siphy_29way_logOdds_rankscore', anchor=W)
                table.heading('Revel_Score', text='Revel_Score', anchor=W)
                table.heading('CADD_raw_score', text='CADD_raw_score', anchor=W)
                table.heading('CADD_Phred', text='CADD_Phred', anchor=W)
                table.heading('genoCanyon_score', text='genoCanyon_score', anchor=W)
                table.heading('genoCanyon_rankscore', text='genoCanyon_rankscore', anchor=W)
                table.heading("Eigen_Raw_coding", text="Eigen_Raw_coding", anchor=W)
                table.heading("Eigen-pc_Raw_coding", text="Eigen-pc_Raw_coding", anchor=W)
                table.heading('phylo100way', text='phylo100way', anchor=W)
                table.heading('phylo100wayrankscore', text='phylo100wayrankscore', anchor=W)
                table.heading('phylo17way', text='phylo17way', anchor=W)
                table.heading('phylo17rankscore', text='phylo17rankscore', anchor=W)
                table.heading('phylo30way', text='phylo30way', anchor=W)
                table.heading('phylo30rankscore', text='phylo30rankscore', anchor=W)
                table.heading('phastcons100waylist', text='phastcons100waylist', anchor=W)
                table.heading('phastcons100wayrankscore', text='phastcons100wayrankscore', anchor=W)
                table.heading('phastcons17waylist', text='phastcons17waylist', anchor=W)
                table.heading('phastcons17rankscore', text='phastcons17rankscore', anchor=W)
                table.heading('phastcons30waylist', text='phastcons30waylist', anchor=W)
                table.heading('phastcons30rankscore', text='phastcons30rankscore', anchor=W)
                table.heading('Interpro_Domain', text='Interpro_Domain', anchor=W)
                table.heading('GTEx_gene', text='GTEx_gene', anchor=W)
                table.heading('GTEx_tisuue', text='GTEx_tisuue', anchor=W)

                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(ID[i],sift_pred[i],
                                         sift_score[i],
                                         sift_converted_rs[i],
                                         polyphen2_HDIV_Pred[i],
                                         polyphen2_HDIV_Score[i],
                                         polyphen2_HVAR_Pred[i],
                                         polyphen2_HVAR_Score[i],
                                         lrt_pred[i],
                                         lrt_score[i],
                                         lrt_converted_rs[i],
                                         mut_assessor_pred[i],
                                         mut_assessor_score[i],
                                         mutationassessor_rs[i],
                                         mut_taster_pred[i],
                                         mut_taster_score[i],
                                         MutationTaster_converted_rs[i],
                                         provean_pred[i],
                                         provean_score[i],
                                         provean_rs[i],
                                         dann_score[i],
                                         fathmm_pred[i],
                                         fathmm_score[i],
                                         fathmm_rs[i],
                                         fathmm_mkl_pred[i],
                                         fathmm_mkl_score[i],
                                         fathmm_mkl_rankscore[i],
                                         metasvm_pred[i],
                                         metasvm_score[i],
                                         metasvm_rankscore[i],
                                         metalr_pred[i],
                                         metalr_score[i],
                                         MetaLR_rankscore[i],
                                         integ_fitcoin_score[i],integ_conf_value[i],
                                         integ_fitcons_rankscore[i],

                                         gerp_rs[i],
                                         gerp_rs_rankscore[i],
                                         siphy_29way_logOdds[i],
                                         siphy_29way_logOdds_rs[i],
                                         revel_score_list[i],
                                         CADD_raw_list[i],
                                         CADD_phred_list[i],
                                         genoCanyon_rankscore[i],
                                         genoCanyon_score[i],
                                         eigen_rawcoding[i],
                                         eigen_pc_rawcoding[i],
                                         phylo100waylist[i],
                                         phylo100wayrankscore[i],
                                         phylo17waylist[i],
                                         phylo17rankscore[i],
                                         phylo30waylist[i],
                                         phylo30rankscore[i],
                                         phastcons100waylist[i],
                                         phastcons100wayrankscore[i],
                                         phastcons17waylist[i],
                                         phastcons17rankscore[i],
                                         phastcons30waylist[i],
                                         phastcons30rankscore[i],
                                         interpro_domain[i],
                                         GTEx_gene[i],
                                         GTEx_tissue[i]

                                         ))
                ##################
                table.place(x=0, y=0, width=1200, height=400)  ##########################
                # VERTICAL SCROLLBAR
                yscrollbar = ttk.Scrollbar(table1, orient=VERTICAL, command=table.yview)  #############
                yscrollbar.pack(side=RIGHT, fill='y')  ##################
                # HORIZONTAL SCROLLBAR
                xscrollbar = ttk.Scrollbar(table1, orient=HORIZONTAL, command=table.xview)  ###################
                xscrollbar.pack(side=BOTTOM, fill='x')  #######################
                table.configure(yscrollcommand=yscrollbar.set, xscrollcommand=xscrollbar.set)  ##############
                table.pack(side=LEFT)
                ##############################################################################################
                ###Creates frame widget under which all other widgets will be kept

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
                btn_download = Button(self.frametwo, text='Save File', command=self.get_file,
                                      font=("Times New Roman", 14, 'bold'), bd=3, relief=RIDGE,
                                      cursor='hand2', bg='#154857', fg='white', activeforeground='white',
                                      activebackground='#154857')
                btn_download.grid(padx=0, pady=0)
                btn_download.place(x=860, y=640, width=120)


                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nUpload File Again  ', font=("Times New Roman", 12),
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
                                                   f'\nUpload File Again  ', font=("Times New Roman", 12),
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
                                               f'\nUpload File again    ', font=("Times New Roman", 12),
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

    def justamethod (self, event):
        if(self.chrchoosen.get()=='PIE_CHART'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))
            sizes.append((len(nodata)))
            sizes.append((len(D)))
            sizes.append((len(P)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = "A ","N","NoData","D","P"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(5, 2), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True,normalize=True)
            legend=['A(Disease_causing_automatic) - '+str(round(len(A)/total*100))+"%",'N(Polymorphism) - '+str(round(len(N)/total*100))+"%",'No_data - '+str(round(len(nodata)/total*100))+"%", 'D(Disease_causing) - ' +str(round((len(D)/total*100)))+"%","P(Polymorphism_automatic) - " +str(round(len(P)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)
            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3,normalize=True)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True,normalize=True)
            legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')
        elif(self.chrchoosen.get()=='BAR_GRAPH'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))

            sizes.append((len(D)))
            sizes.append((len(P)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = ["A ","N","D","P","NoData"]
            #sizes = ([totaltol, totaldele, totalother])*100

            #colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(6, 6), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)


            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green', 'black', 'cyan'])
            #legend=['A(Disease_causing_automatic)', 'N(Polymorphism)','D(Disease_causing)', 'P(Polymorphism_automatic) ','No DATA']
            red_patch = mpatches.Patch(color='red', label='A(Disease_causing_automatic)')
            blue_patch = mpatches.Patch(color='blue', label='N(Polymorphism)')
            green_patch = mpatches.Patch(color='green', label='D(Disease_causing)')
            black_patch = mpatches.Patch(color='black', label='P(Polymorphism_automatic)')
            cyan_patch = mpatches.Patch(color='cyan', label='No Data')
            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch,black_patch,cyan_patch],loc ="upper left")
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]
            explode = (0.1, 0, 0,0)  # explode 1st slice
            # Plot

            explode = list()
            for k in labels:
                explode.append(0.1)
            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            #ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            #ax.legend(legend,loc ="lower left")
            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green', 'black'])
            red_patch = mpatches.Patch(color='red', label='D(eleterious)')
            blue_patch = mpatches.Patch(color='blue', label='N(eutral)')
            green_patch = mpatches.Patch(color='green', label='U(nknown) ')
            black_patch = mpatches.Patch(color='black', label='No Data')

            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch,black_patch],loc ="upper left")

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            #ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True)
            #legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            ax.legend(legend,loc ="lower left")
            ax.bar(labels,sizes,alpha=0.5,color=['red', 'blue', 'green'])
            red_patch = mpatches.Patch(color='red', label='T(olerated)')
            blue_patch = mpatches.Patch(color='blue', label='D(amaging)')
            green_patch = mpatches.Patch(color='green', label='No Data ')


            #plt.legend(handles=[red_patch, blue_patch])

            ax.legend(handles=[red_patch, blue_patch,green_patch],loc ="upper left")


            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')
        elif(self.chrchoosen.get()=='SCATTER_PLOT'):
            A=[]
            D=[]
            N=[]
            P=[]
            nodata=[]
            for i in mut_taster_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='A':
                    A.append(i)
                elif  i=='D':
                    D.append(i)
                elif  i=='N':
                    N.append(i)
                elif  i=='P':
                    P.append(i)
            totalother=0
            total=len(A)+len(D)+len(N)+len(P)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(A)))
            sizes.append((len(N)))

            sizes.append((len(D)))
            sizes.append((len(P)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            #######################################################

            #l=["No_data","A(Disease_causing_automatic) ","N(Polymorphism)","D(Disease_causing)","P(Polymorphism_automatic)",]

            labels = ["A ","N","D","P","NoData"]
            #sizes = ([totaltol, totaldele, totalother])*100

            #colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            #fig1 = plt.Figure(figsize=(6, 6), dpi=100)
            ax = fig1.add_subplot(111) # add an Axes to the figure


            ax.scatter(labels,sizes,color=['red', 'blue', 'green', 'black', 'cyan'])
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=50,y=850)
            uname = Label(self.frametwo, text = f"Graph is showing the percentage of each prediction in the data."
                                                f"\nThe values of each prediction in data are:"
                                                f'\nA(Disease_causing_automatic) ='+ str(len(A))+
                                                f'\nN(Polymorphism) ='+ str(len(N))+
                                                f'\nD(Disease_causing) ='+ str(len(D))+
                                                f'\nNo_data =' +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 80,y = 1400)
            ax.set_title('MUTATION TASTER PREDICTION')


            dele=[]
            neutral=[]
            unknown=[]
            nodata=[]
            for i in lrt_pred:
                if i=='.':
                    nodata.append(i)
                elif  i=='D':
                    dele.append(i)
                elif  i=='N':
                    neutral.append(i)
                elif  i=='U':
                    unknown.append(i)
            totalother=0

            total=len(dele)+len(neutral)+len(unknown)+len(nodata)
            sizes=[]
            (f"{total}")
            sizes.append((len(dele)))
            sizes.append((len(neutral)))
            sizes.append((len(unknown)))
            sizes.append((len(nodata)))
            (f"sizesssssssssssssss{sizes}")
            labels =   "D","N","U","NoData"
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral',"red"]

            fig = Figure() # create a figure object
            ax = fig.add_subplot(111) # add an Axes to the figure
            #ax.legend([ "D(eleterious)","N(eutral)","U(nknown)","NoData"],loc=3)
            #ax.pie(sizes, labels=labels,autopct='%0.1f%%',explode= explode, shadow=True, radius=1.3)
            legend=["D(eleterious) - "+str(round(len(dele)/total*100))+"%","N(eutral) -"+str(round(len(neutral)/total*100))+"%","U(nknown) - "+str(round(len(unknown)/total*100))+"%","NoData  - "+str(round(len(nodata)/total*100))+"%"]
            #ax.legend(legend,loc ="lower left")
            ax.scatter(labels,sizes,color=['red', 'blue', 'green', 'black'])

            chart1 = FigureCanvasTkAgg(fig,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=630,y=850)
            uname = Label(self.frametwo, text = "Graph is showing the percentage of each prediction in the data."+
                                                "\nThe values of each prediction in data are:"
                                                "\nD(eleterious) = " +str(len(dele))+"\nN(eutral) = " +str(len(neutral))+"\nU(nknown) = " +str(len(unknown))+"\nNoData = " +str(len(nodata)),font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 745,y = 1400)

            ax.set_title('LRT PREDICTION')

            dele=[]
            tol=[]
            other=[]
            (sift_pred)
            for i in sift_pred:
                if i=='.':
                    other.append(i)
                elif  i=='T':
                    tol.append(i)
                elif  i=='D':
                    dele.append(i)

            (f"tol{len(tol)}")
            (f"tdele{dele}")
            (f"other{other}")

            total=(len(tol)+len(dele)+len(other))
            (f"total{total}")
            sizes=[]
            sizes.append((len(tol)))
            sizes.append((len(dele)))
            sizes.append((len(other)))

            (f"sizesssssssssssssss{sizes}")
            labels = 'T', 'D','NoData'
            #sizes = ([totaltol, totaldele, totalother])*100

            colors = ['gold', 'yellowgreen', 'lightcoral']
            #explode = (0.1, 0, 0)  # explode 1st slice
            fig1 = Figure() # create a figure object
            ax = fig1.add_subplot(111) # add an Axes to the figure
            explode = list()
            for k in labels:
                explode.append(0.1)
            #ax.pie(sizes, radius=1.3, labels=labels,autopct='%0.2f%%', explode= explode,shadow=True)
            #legend=['T(olerated) - '+str(round(len(tol)/total*100))+"%", 'D(amaging) - '+str(round(len(dele)/total*100))+"%",'NoData - '+str(round(len(other)/total*100))+"%"]
            #ax.legend(legend,loc ="lower left")
            ax.scatter(labels,sizes,color=['red', 'blue', 'green'])
            chart1 = FigureCanvasTkAgg(fig1,self.frametwo)
            chart1.get_tk_widget().grid(padx=0,pady=0)
            chart1.get_tk_widget().place(x=70,y=1600)
            uname = Label(self.frametwo, text = f'Graph is showing the percentage of each prediction in the data.\nThe values of each prediction in data are: \nT(olerated)='+str(len(tol))+f'\nD(amaging)='+str(len(dele)) +f'\nNo_Data='+str(len(other)),
                          font=12,bg="white")
            uname.grid(padx=0,pady=0)
            uname.place(x = 70,y = 2100)
            ax.set_title('SIFT PREDICTION')

    def exit(self):
        self.root.destroy()

    def search_window(self):
        ID.clear()
        sift_pred.clear()
        sift_score.clear()
        sift_converted_rs.clear()
        polyphen2_HDIV_Pred.clear()
        polyphen2_HDIV_Score.clear()
        polyphen2_HVAR_Pred.clear()
        polyphen2_HVAR_Score.clear()
        lrt_pred.clear()
        lrt_score.clear()
        lrt_converted_rs.clear()
        mut_assessor_pred.clear()
        mut_assessor_score.clear()
        mutationassessor_rs.clear()
        mut_taster_pred.clear()
        mut_taster_score.clear()
        MutationTaster_converted_rs.clear()
        provean_pred.clear()
        provean_score.clear()
        provean_rs.clear()
        dann_score.clear()
        fathmm_pred.clear()
        fathmm_score.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        fathmm_mkl_rankscore.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_fitcons_rankscore.clear()
        integ_conf_value.clear()
        gerp_rs.clear()
        gerp_rs_rankscore.clear()
        siphy_29way_logOdds.clear()
        siphy_29way_logOdds_rs.clear()
        revel_score_list.clear()
        CADD_raw_list.clear()
        CADD_phred_list.clear()
        genoCanyon_rankscore.clear()
        genoCanyon_score.clear()
        eigen_rawcoding.clear()
        eigen_pc_rawcoding.clear()
        phylo100waylist.clear()
        phylo100wayrankscore.clear()
        phylo17waylist.clear()
        phylo17rankscore.clear()
        phylo30waylist.clear()
        phylo30rankscore.clear()
        phastcons100waylist.clear()
        phastcons100wayrankscore.clear()
        phastcons17waylist.clear()
        phastcons17rankscore.clear()
        phastcons30waylist.clear()
        phastcons30rankscore.clear()
        interpro_domain.clear()
        GTEx_gene.clear()
        GTEx_tissue.clear()
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
        header=['HGVS_id', 'Sift_Pred', 'Sift_Score', 'sift_converted_rankScore', 'Polyphen2_HDIV_Pred', 'Polyphen2_HDIV_Score', 'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score', 'LRT_converted_rankScore', 'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore', 'Mutation_Taster_Pred', 'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred', 'Provean_Score', 'Provean_Rank_score', 'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred', 'Fathmm-mkl_Score', 'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score', 'MetaLR_Pred:', 'MetaLR_Score', 'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value', 'Integrated_fitcons_rankscore', 'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds', 'siphy_29way_logOdds_rankscore', 'Revel_Score', 'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore', 'Eigen_Raw_coding', 'Eigen-pc_Raw_coding', 'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way', 'phylo30rankscore', 'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist', 'phastcons17rankscore', 'phastcons30waylist', 'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue']
        data1=[]
        l1 = []

        for i in range(len(sift_pred)):
            data = []
            data.append(ID[i])
            data.append(sift_pred[i])
            data.append(sift_score[i])
            data.append(sift_converted_rs[i])
            data.append(polyphen2_HDIV_Pred[i])
            data.append(polyphen2_HDIV_Score[i])
            data.append(polyphen2_HVAR_Pred[i])
            data.append(polyphen2_HVAR_Score[i])
            data.append(lrt_pred[i])
            data.append(lrt_score[i])
            data.append(lrt_converted_rs[i])
            data.append(mut_assessor_pred[i])
            data.append(mut_assessor_score[i])
            data.append(mutationassessor_rs[i])
            data.append(mut_taster_pred[i])
            data.append(mut_taster_score[i])
            data.append(MutationTaster_converted_rs[i])
            data.append(provean_pred[i])
            data.append(provean_score[i])
            data.append(provean_rs[i])
            data.append(dann_score[i])
            data.append(fathmm_pred[i])
            data.append(fathmm_score[i])
            data.append(fathmm_rs[i])
            data.append(fathmm_mkl_pred[i])
            data.append(fathmm_mkl_score[i])
            data.append(fathmm_mkl_rankscore[i])
            data.append(metasvm_pred[i])
            data.append(metasvm_score[i])
            data.append(metasvm_rankscore[i])
            data.append(metalr_pred[i])
            data.append(metalr_score[i])
            data.append(MetaLR_rankscore[i])
            data.append(integ_fitcoin_score[i])
            data.append(integ_conf_value[i])
            data.append(integ_fitcons_rankscore[i])
            data.append(gerp_rs[i])
            data.append(gerp_rs_rankscore[i])
            data.append(siphy_29way_logOdds[i])
            data.append(siphy_29way_logOdds_rs[i])
            data.append(revel_score_list[i])
            data.append(CADD_raw_list[i])
            data.append(CADD_phred_list[i])
            data.append(genoCanyon_score[i])
            data.append(genoCanyon_rankscore[i])
            data.append(eigen_rawcoding[i])
            data.append(eigen_pc_rawcoding[i])
            data.append(phylo100waylist[i])
            data.append(phylo100wayrankscore[i])
            data.append(phylo17waylist[i])
            data.append(phylo17rankscore[i])
            data.append(phylo30waylist[i])
            data.append(phylo30rankscore[i])
            data.append(phastcons100waylist[i])
            data.append(phastcons100wayrankscore[i])
            data.append(phastcons17waylist[i])
            data.append(phastcons17rankscore[i])
            data.append(phastcons30waylist[i])
            data.append(phastcons30rankscore[i])
            data.append(interpro_domain[i])
            data.append(GTEx_gene[i])
            data.append(GTEx_tissue[i])
            data1.append(data)



        for row in data1:

            d1 = {header[0]: row[0], header[1]: row[1], header[2]: row[2], header[3]: row[3], header[4]: row[4],
                  header[5]: row[5], header[6]: row[6], header[7]: row[7], header[8]: row[8], header[9]: row[9]
                , header[10]: row[10], header[11]: row[11], header[12]: row[12], header[13]: row[13],
                  header[14]: row[14]
                , header[15]: row[15], header[16]: row[16], header[17]: row[17], header[18]: row[18],
                  header[19]: row[19]
                , header[20]: row[20], header[21]: row[21], header[22]: row[22], header[23]: row[23],
                  header[24]: row[24]
                , header[25]: row[25], header[26]: row[26], header[27]: row[27], header[28]: row[28],
                  header[29]: row[29],
                  header[30]: row[30], header[31]: row[31], header[32]: row[32], header[33]: row[33],
                  header[34]: row[34],
                  header[35]: row[35], header[36]: row[36], header[37]: row[37], header[38]: row[38],
                  header[39]: row[39],
                  header[40]: row[40], header[41]: row[41], header[42]: row[42]
                , header[43]: row[43], header[44]: row[44], header[45]: row[45], header[46]: row[46]
                , header[47]: row[47], header[48]: row[48]
                , header[49]: row[49], header[50]: row[50], header[51]: row[51], header[52]: row[52]

                , header[53]: row[53], header[54]: row[54]
                , header[55]: row[55], header[56]: row[56], header[57]: row[57], header[58]: row[58],
                  header[59]: row[59],header[60]: row[60],header[61]: row[61]}

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
