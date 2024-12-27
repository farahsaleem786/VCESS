import webbrowser
from tkinter.filedialog import asksaveasfile
from urllib.request import urlopen
import pathlib
import allel
import myvariant
from tkinter import Tk, Toplevel, messagebox, ttk
from tkinter import *
import csv
import database_interface
from PIL import ImageTk, Image
from urllib.request import urlopen
import ast
from cruzdb import Genome
from pyensembl import EnsemblRelease
import os
Id=[]
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
links = []
all_freq_list = []
freq_afr_list = []
freq_amr_list = []
freq_eas_list = []
freq_fin_list = []
freq_nfe_list = []
freq_oth_list = []
freq_sas_list = []

variant_id_list = []
variant_type_list = []
allele_id_list = []
cytoband_list = []
clin_interpretation_list = []
clin_condition_list = []
allelic_origin_list = []
review_status_list = []
identifier_list = []

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
rsid_list = []
mv = myvariant.MyVariantInfo()
geneIds = []
geneName = []
# f = database_interface.database_window


def main():
    main_window = Tk()
    app = info(main_window, '')
    main_window.mainloop()


class info:
    def __init__(self, root, f):
        search_id = f.get_id()
        ######################clinvar
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
        ###################dbnsfp
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
        fathmm_mkl_rankscore.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_conf_value.clear()
        integ_fitcons_rankscore.clear()
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
        #######################dbsnp
        rsid_list.clear()
        ############################exac
        all_freq_list.clear()
        freq_afr_list.clear()
        freq_amr_list.clear()
        freq_eas_list.clear()
        freq_fin_list.clear()
        freq_nfe_list.clear()
        freq_oth_list.clear()
        freq_sas_list.clear()
        ###############################intervar
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
        links.clear()
        Id.clear()
        self.error_str = ''
        self.root1 = root
        #####################PROGRESSS BAR
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)
        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')
        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 12, "bold", "italic"),
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
        progress.place(x=0, y=100)
        p = 20
        progress['value'] = p
        self.root1.update_idletasks()
        self.root1.after(100)
        p = p + 40
        link = "http://wintervar.wglab.org/api_new.php?queryType=position&chr=" + str(f.get_chr()) + "&pos=" + str(
            f.get_pos()) + "&ref=" + str(f.get_ref()) + "&alt=" + str(f.get_alt())

        try:
            self.m = mv.getvariant(search_id)
            m = self.m
            Id.append(search_id)
            page = urlopen(link)
            html_bytes = page.read()
            (html_bytes)

            html = html_bytes.decode("utf-8")

            g = Genome(db="hg19")

            nearest = g.knearest("refGene", "chr" + str(f.get_chr()), int(f.get_pos()), int(f.get_pos()))
            if len(nearest) == 0:

                self.name = '.'
            else:


                for i in nearest:
                    self.name = i.name2
                    (i.name2)
            if html == "":

                intervar = '.'
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
                    self.html = html
                    if data.get("Intervar"):
                        intervar = data['Intervar']
                    else:
                        intervar = '.'

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

                    intervar = '.'
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

            self.gene_id = ''

            # release 75 uses human reference genome GRCh37/hg19
            data = EnsemblRelease(75)
            gene_names = data.gene_names_at_locus(contig=int(f.get_chr()), position=int(f.get_pos()))
            (gene_names)
            if len(gene_names) == 0:
                self.gene_id = '.  '
            else:

                if type(data.gene_ids_of_gene_name(gene_names[0])) == list:
                    for x in data.gene_ids_of_gene_name(gene_names[0]):
                        self.gene_id += x + ', '
                else:
                    self.gene_id = data.gene_ids_of_gene_name(gene_names[0])
            self.gene_id = self.gene_id[:-2]

            if m == None :
                ########clinvar
                variant_id_list.append('.')
                variant_type_list.append('.')
                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')
                #####################dbnsfp
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
                #################dbsnp
                rsid_list.append('.')
                ###############exac
                all_freq_list.append('.')
                freq_afr_list.append('.')
                freq_amr_list.append('.')
                freq_eas_list.append('.')
                freq_fin_list.append('.')
                freq_nfe_list.append('.')
                freq_oth_list.append('.')
                freq_sas_list.append('.')


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
                                    siftpred = (max(dbnsfp['sift']['pred']))
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

                if m.get('exac'):

                    exac = m['exac']

                    ################ ALLELE COUNTTTT OF DIFFERENT COUNTRIES
                    if exac.get('ac'):
                        if exac['ac'].get('ac_adj'):
                            total_ac = exac['ac']['ac_adj']
                        else:
                            total_ac = 0
                        if exac['ac'].get('ac_afr'):

                            if type(exac['ac'].get('ac_afr')) == list:
                                ac_afr = max(exac['ac']['ac_afr'])
                            elif type(exac['ac'].get('ac_afr')) != list:
                                ac_afr = exac['ac']['ac_afr']
                        else:
                            ac_afr = 0

                        ###################
                        if exac['ac'].get('ac_amr'):
                            if type(exac['ac'].get('ac_amr')) == list:
                                ac_amr = max(exac['ac']['ac_amr'])
                            elif type(exac['ac'].get('ac_amr')) != list:
                                ac_amr = exac['ac']['ac_amr']
                        else:
                            ac_amr = 0

                        #######################
                        if exac['ac'].get('ac_eas'):
                            if type(exac['ac'].get('ac_eas')) == list:
                                ac_eas = max(exac['ac']['ac_eas'])
                            elif type(exac['ac'].get('ac_eas')) != list:
                                ac_eas = exac['ac']['ac_eas']
                        else:
                            ac_eas = 0

                        ########################
                        if exac['ac'].get('ac_fin'):
                            if type(exac['ac'].get('ac_fin')) == list:
                                ac_fin = max(exac['ac']['ac_fin'])
                            elif type(exac['ac'].get('ac_fin')) != list:
                                ac_fin = exac['ac']['ac_fin']
                        else:
                            ac_fin = 0

                        #########################
                        if exac['ac'].get('ac_nfe'):
                            if type(exac['ac'].get('ac_nfe')) == list:
                                ac_nfe = max(exac['ac']['ac_nfe'])
                            elif type(exac['ac'].get('ac_nfe')) != list:
                                ac_nfe = exac['ac']['ac_nfe']
                        else:
                            ac_nfe = 0

                        #############################
                        if exac['ac'].get('ac_oth'):
                            if type(exac['ac'].get('ac_oth')) == list:
                                ac_oth = max(exac['ac']['ac_oth'])
                            elif type(exac['ac'].get('ac_oth')) != list:
                                ac_oth = exac['ac']['ac_oth']
                        else:
                            ac_oth = 0

                        ##############################
                        if exac['ac'].get('ac_sas'):
                            if type(exac['ac'].get('ac_sas')) == list:
                                ac_sas = max(exac['ac']['ac_sas'])
                            elif type(exac['ac'].get('ac_sas')) != list:
                                ac_sas = exac['ac']['ac_sas']
                        else:
                            ac_sas = 0
                    else:
                        total_ac = 0
                        ac_afr = 0
                        ac_amr = 0
                        ac_eas = 0
                        ac_fin = 0
                        ac_nfe = 0
                        ac_oth = 0
                        ac_sas = 0

                    #####################################ALLELE NUMBER OF DIFFERENT COUNTRIES##################################

                    if exac.get('an'):
                        if exac['an'].get('an_adj'):
                            total_an = exac['an']['an_adj']
                        else:
                            total_an = 0
                        if exac['an'].get('an_afr'):
                            if type(exac['an'].get('an_afr')) == list:
                                an_afr = max(exac['an']['an_afr'])
                            elif type(exac['an'].get('an_afr')) != list:
                                an_afr = exac['an']['an_afr']
                        else:
                            an_afr = 0

                        #####################################
                        if exac['an'].get('an_amr'):
                            if type(exac['an'].get('an_amr')) == list:
                                an_amr = max(exac['an']['an_amr'])
                            elif type(exac['an'].get('an_amr')) != list:
                                an_amr = exac['an']['an_amr']
                        else:
                            an_afr = 0

                        ###########################################
                        if (exac['an'].get('an_eas')):
                            if type(exac['an'].get('an_eas')) == list:
                                an_eas = max(exac['an']['an_eas'])
                            elif type(exac['an'].get('an_eas')) != list:
                                an_eas = exac['an']['an_eas']
                        else:
                            an_eas = 0
                        ##############################################
                        if exac['an'].get('an_fin'):
                            if type(exac['an'].get('an_fin')) == list:
                                an_fin = max(exac['an']['an_fin'])
                            elif type(exac['an'].get('an_fin')) != list:
                                an_fin = exac['an']['an_fin']
                        else:
                            an_fin = 0

                        ################################
                        if (exac['an'].get('an_nfe')):
                            if type(exac['an'].get('an_nfe')) == list:
                                an_nfe = max(exac['an']['an_nfe'])
                            elif type(exac['an'].get('an_nfe')) != list:
                                an_nfe = exac['an']['an_nfe']
                        else:
                            an_nfe = 0

                        #################################
                        if (exac['an'].get('an_oth')):
                            if type(exac['an'].get('an_oth')) == list:
                                an_oth = max(exac['an']['an_oth'])
                            elif type(exac['an'].get('an_oth')) != list:
                                an_oth = exac['an']['an_oth']
                        else:
                            an_oth = 0

                        ###########################################
                        if (exac['an'].get('an_sas')):
                            if type(exac['an'].get('an_sas')) == list:
                                an_sas = max(exac['an']['an_sas'])
                            elif type(exac['an'].get('an_sas')) != list:
                                an_sas = exac['an']['an_sas']
                        else:
                            an_sas = 0
                    else:
                        total_an = 0
                        an_afr = 0
                        an_amr = 0
                        an_eas = 0
                        an_fin = 0
                        an_nfe = 0
                        an_oth = 0
                        an_sas = 0

                    if total_an == 0:
                        total_freq = 0
                    else:
                        total_freq = total_ac / total_an
                    all_freq_list.append(total_freq)
                    (f"EXAC_Freq : {total_freq}")

                    if an_afr == 0:
                        fre_afr = 0
                    else:
                        fre_afr = ac_afr / an_afr
                    freq_afr_list.append(fre_afr)
                    (f"FREQUENCY_AFR : {fre_afr}")

                    if an_amr == 0:
                        fre_amr = 0
                    else:
                        fre_amr = ac_amr / an_amr
                    freq_amr_list.append(fre_amr)
                    (f"FREQUENCY_AMR : {fre_amr}")

                    if an_eas == 0:
                        fre_eas = 0
                    else:
                        fre_eas = ac_eas / an_eas
                    freq_eas_list.append(fre_eas)
                    (f"FREQUENCY_EAS : {fre_eas}")

                    if an_fin == 0:
                        fre_fin = 0
                    else:
                        fre_fin = ac_fin / an_fin

                    freq_fin_list.append(fre_fin)
                    (f"FREQUENCY_FIN : {fre_fin}")

                    if an_nfe == 0:
                        fre_nfe = 0
                    else:
                        fre_nfe = ac_nfe / an_nfe
                    freq_nfe_list.append(fre_nfe)
                    (f"FREQUENCY_NFE : {fre_nfe}")

                    if an_oth == 0:
                        fre_oth = 0
                    else:
                        fre_oth = ac_oth / an_oth
                    freq_oth_list.append(fre_oth)
                    (f"FREQUENCY_OTH : {fre_oth}")

                    if an_sas == 0:
                        fre_sas = 0
                    else:
                        fre_sas = ac_sas / an_sas
                    freq_sas_list.append(fre_sas)
                    (f"FREQUENCY_SAS : {fre_sas}")

                else:
                    all_freq_list.append('.')
                    freq_afr_list.append('.')
                    freq_amr_list.append('.')
                    freq_eas_list.append('.')
                    freq_fin_list.append('.')
                    freq_nfe_list.append('.')
                    freq_oth_list.append('.')
                    freq_sas_list.append('.')

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
                                        clinical_condition=clinvar['rcv']['conditions'][0]['name']
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
                    variant_id_list.append('.')
                    variant_type_list.append('.')
                    allele_id_list.append('.')
                    cytoband_list.append('.')
                    clin_interpretation_list.append('.')
                    clin_condition_list.append('.')
                    allelic_origin_list.append('.')
                    review_status_list.append('.')
                    identifier_list.append('.')
            if all_freq_list[0]!='.':
                all_freq_list[0]=round(all_freq_list[0],4)
            if freq_afr_list[0]!='.':
                freq_afr_list[0]=round(freq_afr_list[0],4)
            if freq_amr_list[0]!='.':
                freq_amr_list[0]=round(freq_amr_list[0],4)
            if freq_eas_list[0]!='.':
                freq_eas_list[0]=round(freq_eas_list[0],4)
            if freq_fin_list[0]!='.':
                freq_fin_list[0]=round(freq_fin_list[0],4)
            if freq_nfe_list[0]!='.':
                freq_nfe_list[0]=round(freq_nfe_list[0],4)
            if freq_oth_list[0]!='.':
                freq_oth_list[0]=round(freq_oth_list[0],4)
            if freq_sas_list[0]!='.':
                freq_sas_list[0]=round(freq_sas_list[0],4)
        except Exception as es:
            self.error_str = es
        self.root = root
        self.root.title('VCESS-ALL')
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

        frame1 = Frame(self.root, bg='#c87894')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from All Databases",
                      font=("Times New Roman", 30, "bold", "italic"),
                      bg='#c87894',
                      fg='white')
        title.place(x=350, y=45)
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
        lblimg1 = Label(image=self.photoimage1, bg='#c87894', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')
        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 14, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 12, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=90, y=40)

        self.root.overrideredirect(False)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width()
                y1 = canvas.winfo_height()//4
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############

        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)

        text = canvas.create_text(0, -2000,
                                  text=f'ALL is retrieving data from all the Databases'
                                       f'  Clinvar , dbSNP , dbNSFP , ExAC , InterVar , RefGene , EnSemble',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=90, y=70, width=1150, height=200)
        fps = 12  # Change the fps to make the animation faster/slower
        shift()


        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        #try:

        if self.html == "" and  self.m==None and self.name == '.' and self.gene_id=='.':
            no_id = Label(self.frametwo, text='No Data available for this ID',
                          font=("Times New Roman", 15, "bold"),
                          bg='white',
                          fg='black')
            no_id.grid(padx=0, pady=0)
            no_id.place(x=60, y=65)
        table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG_19)",
                            font=('Times New Roman', 16, 'bold'),bg="white")  ################
        table1.grid(padx=0, pady=0)
        table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
        table = ttk.Treeview(table1, height="30")  #################

        table['columns'] = ['ID',
                            'rsID',
                            'Sift_Pred',
                            'Sift_Score',
                            'Sift_converted_rankScore',
                            'Polyphen2_HDIV_Pred',
                            'Polyphen2_HDIV_Score',
                            'Polyphen2_HVAR_Pred',
                            'Polyphen2_HVAR_Score',
                            'LRT_Pred',
                            'LRT_Score',
                            'LRT_converted_rankScore',
                            'Mutation_Assessor_Pred',
                            'Mutation_Assessor_Score',
                            'Mutation_Assessor_rankscore',
                            'Mutation_Taster_Pred',
                            'Mutation_Taster_Score',
                            'MutationTaster_converted_rankscore',
                            'Provean_Pred',
                            'Provean_Score',
                            'Provean_Rank_score',
                            'DANN Score',
                            'Fathmm_Pred',
                            'Fathmm_Score',
                            'fathmm_Rank_Score',
                            'Fathmm-mkl_Pred',
                            'Fathmm-mkl_Score',
                            'Fathmm-mkl_RankScore',
                            'MetaSVM_Pred',
                            'MetaSVM_Score',
                            'Meta_SVM_Rank_Score',
                            'MetaLR_Pred',
                            'MetaLR_Score',
                            'MetaLR_Rank_Score',
                            'Integrated_fitCons_score',
                            'Integrated_confidence_value',
                            'Integrated_fitcons_rankscore',
                            'GERP++_RS',
                            'GERP++_RS_Rankscore',
                            'Siphy_29way_logOdds',
                            'siphy_29way_logOdds_rankscore',
                            'Revel_Score',
                            'CADD_raw_score',
                            'CADD_Phred',
                            'genoCanyon_score',
                            'genoCanyon_rankscore',
                            "Eigen_Raw_coding",
                            "Eigen-pc_Raw_coding",
                            'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                            'phylo30rankscore',
                            'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                            'phastcons17rankscore', 'phastcons30waylist',
                            'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                            'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                            'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                            'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                            'Clinical_Condition',
                            'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                            'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5',
                            'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5',
                            'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4','RefGene.GeneName','ensGene.GeneId']

        table.column('#0', width=120, minwidth=25)
        table.column('ID', anchor=W, width=120)
        table.column('rsID', anchor=W, width=120)
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
        table.column('GTEx_tisuue', anchor=W, width=120)
        table.column('EXAC_All_Freq', anchor=W, width=120)
        table.column('EXAC_Afr_Freq', anchor=W, width=120)
        table.column('EXAC_Amr_Freq', anchor=W, width=120)
        table.column('EXAC_Eas_Freq', anchor=W, width=120)
        table.column('EXAC_Fin_Freq', anchor=W, width=120)
        table.column('EXAC_Nfe_Freq', anchor=W, width=120)
        table.column('EXAC_Oth_Freq', anchor=W, width=120)
        table.column('EXAC_Sas_Freq', anchor=W, width=120)
        table.column('Variant_ID', anchor=W, width=120)
        table.column('Clinical_Type', anchor=CENTER, width=120)
        table.column('Allelic_ID', anchor=CENTER, width=120)
        table.column('Clinical_Significance', anchor=CENTER, width=120)
        table.column('Clinical_Condition', anchor=CENTER, width=120)
        table.column('Allelic_Origin', anchor=CENTER, width=120)
        table.column('Review_Status', anchor=CENTER, width=120)
        table.column('Clinical_identifier', anchor=CENTER, width=120)
        table.column('Cytogenic_Location', anchor=CENTER, width=120)
        table.column('InterVar', width=120, minwidth=105)
        table.column('PVS1', anchor=W, width=120)
        table.column('PS1', anchor=W, width=120)
        table.column('PS2', anchor=W, width=120)
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
        table.column('RefGene.GeneName', anchor=W, width=200)
        table.column('ensGene.GeneId', anchor=W, width=200)



        table.heading('#0', text='Serial No.', anchor=W)
        table.heading('ID', text='ID', anchor=W)
        table.heading('rsID', text='rsID', anchor=W)
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
        table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
        table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
        table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
        table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
        table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
        table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
        table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
        table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
        table.heading('Variant_ID', text='Variant_ID', anchor=W)
        table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
        table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
        table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
        table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
        table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
        table.heading('Review_Status', text='Review_Status', anchor=CENTER)
        table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
        table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
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
        table.heading('RefGene.GeneName', text='RefGene.GeneName', anchor=W)
        table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)


        for i in range(len(sift_pred)):
            table.insert(parent='', index='end', iid=i, text=i + 1,
                      values=(Id[i],rsid_list[i], sift_pred[i],
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
                                 GTEx_tissue[i],
                                 all_freq_list[i],
                                 freq_afr_list[i],
                                 freq_amr_list[i],
                                 freq_eas_list[i],
                                 freq_fin_list[i],
                                 freq_nfe_list[i],
                                 freq_oth_list[i],
                                 freq_sas_list[i],
                                 variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                 clin_interpretation_list[i],
                                 clin_condition_list[i],
                                 allelic_origin_list[i],
                                 review_status_list[i],
                                 identifier_list[i],
                                 cytoband_list[i],intervar,pvs1,ps1, ps2, ps3, ps4, pm1, pm2, pm3, pm4, pm5, pm6, pp1, pp2, pp3, pp4,
                              pp5,
                              ba1,
                              bp1, bp2, bp3, bp4, bp5, bp6, bp7, bs1, bs2, bs3, bs4,self.name,self.gene_id
                                 ))
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
        """except Exception as es:
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
            btn_exit.place(x=780, y=370, width=100)"""
    def exit(self):
        self.root.destroy()
    def search_window(self):
        self.root.destroy()
        main_window = Tk()
        app = database_interface.database_window(main_window)
        main_window.mainloop()

class info_hg38:
    def __init__(self, root, f):
        search_id = f.get_id()
        ######################clinvar
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
        ###################dbnsfp
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
        fathmm_mkl_rankscore.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_conf_value.clear()
        integ_fitcons_rankscore.clear()
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
        #######################dbsnp
        rsid_list.clear()
        ############################exac
        all_freq_list.clear()
        freq_afr_list.clear()
        freq_amr_list.clear()
        freq_eas_list.clear()
        freq_fin_list.clear()
        freq_nfe_list.clear()
        freq_oth_list.clear()
        freq_sas_list.clear()

        Id.clear()

        self.error_str = ''
        self.root1 = root
        #####################PROGRESSS BAR
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)
        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')
        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 12, "bold", "italic"),
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
        progress.place(x=0, y=100)
        p = 20
        progress['value'] = p
        self.root1.update_idletasks()
        self.root1.after(100)
        p = p+ 40

        try:
            self.m = mv.getvariant(search_id,assembly='hg38')
            m = self.m
            Id.append(search_id)

            g = Genome(db="hg38")

            nearest = g.knearest("refGene", "chr" + str(f.get_chr()), int(f.get_pos()), int(f.get_pos()))
            if len(nearest) == 0:

                self.name = '.'
            else:


                for i in nearest:
                    self.name = i.name2
                    (i.name2)

            self.gene_id = ''

            # release 75 uses human reference genome GRCh37/hg19
            data = EnsemblRelease(77)
            gene_names = data.gene_names_at_locus(contig=int(f.get_chr()), position=int(f.get_pos()))
            (gene_names)
            if len(gene_names) == 0:
                self.gene_id = '.  '
            else:

                if type(data.gene_ids_of_gene_name(gene_names[0])) == list:
                    for x in data.gene_ids_of_gene_name(gene_names[0]):
                        self.gene_id += x + ', '
                else:
                    self.gene_id = data.gene_ids_of_gene_name(gene_names[0])
            self.gene_id = self.gene_id[:-2]

            if m == None :
                ########clinvar
                variant_id_list.append('.')
                variant_type_list.append('.')
                allele_id_list.append('.')
                cytoband_list.append('.')
                clin_interpretation_list.append('.')
                clin_condition_list.append('.')
                allelic_origin_list.append('.')
                review_status_list.append('.')
                identifier_list.append('.')
                #####################dbnsfp
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
                #################dbsnp
                rsid_list.append('.')
                ###############exac
                all_freq_list.append('.')
                freq_afr_list.append('.')
                freq_amr_list.append('.')
                freq_eas_list.append('.')
                freq_fin_list.append('.')
                freq_nfe_list.append('.')
                freq_oth_list.append('.')
                freq_sas_list.append('.')


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
                                    siftpred = (max(dbnsfp['sift']['pred']))
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

                if m.get('exac'):

                    exac = m['exac']

                    ################ ALLELE COUNTTTT OF DIFFERENT COUNTRIES
                    if exac.get('ac'):
                        if exac['ac'].get('ac_adj'):
                            total_ac = exac['ac']['ac_adj']
                        else:
                            total_ac = 0
                        if exac['ac'].get('ac_afr'):

                            if type(exac['ac'].get('ac_afr')) == list:
                                ac_afr = max(exac['ac']['ac_afr'])
                            elif type(exac['ac'].get('ac_afr')) != list:
                                ac_afr = exac['ac']['ac_afr']
                        else:
                            ac_afr = 0

                        ###################
                        if exac['ac'].get('ac_amr'):
                            if type(exac['ac'].get('ac_amr')) == list:
                                ac_amr = max(exac['ac']['ac_amr'])
                            elif type(exac['ac'].get('ac_amr')) != list:
                                ac_amr = exac['ac']['ac_amr']
                        else:
                            ac_amr = 0

                        #######################
                        if exac['ac'].get('ac_eas'):
                            if type(exac['ac'].get('ac_eas')) == list:
                                ac_eas = max(exac['ac']['ac_eas'])
                            elif type(exac['ac'].get('ac_eas')) != list:
                                ac_eas = exac['ac']['ac_eas']
                        else:
                            ac_eas = 0

                        ########################
                        if exac['ac'].get('ac_fin'):
                            if type(exac['ac'].get('ac_fin')) == list:
                                ac_fin = max(exac['ac']['ac_fin'])
                            elif type(exac['ac'].get('ac_fin')) != list:
                                ac_fin = exac['ac']['ac_fin']
                        else:
                            ac_fin = 0

                        #########################
                        if exac['ac'].get('ac_nfe'):
                            if type(exac['ac'].get('ac_nfe')) == list:
                                ac_nfe = max(exac['ac']['ac_nfe'])
                            elif type(exac['ac'].get('ac_nfe')) != list:
                                ac_nfe = exac['ac']['ac_nfe']
                        else:
                            ac_nfe = 0

                        #############################
                        if exac['ac'].get('ac_oth'):
                            if type(exac['ac'].get('ac_oth')) == list:
                                ac_oth = max(exac['ac']['ac_oth'])
                            elif type(exac['ac'].get('ac_oth')) != list:
                                ac_oth = exac['ac']['ac_oth']
                        else:
                            ac_oth = 0

                        ##############################
                        if exac['ac'].get('ac_sas'):
                            if type(exac['ac'].get('ac_sas')) == list:
                                ac_sas = max(exac['ac']['ac_sas'])
                            elif type(exac['ac'].get('ac_sas')) != list:
                                ac_sas = exac['ac']['ac_sas']
                        else:
                            ac_sas = 0
                    else:
                        total_ac = 0
                        ac_afr = 0
                        ac_amr = 0
                        ac_eas = 0
                        ac_fin = 0
                        ac_nfe = 0
                        ac_oth = 0
                        ac_sas = 0

                    #####################################ALLELE NUMBER OF DIFFERENT COUNTRIES##################################

                    if exac.get('an'):
                        if exac['an'].get('an_adj'):
                            total_an = exac['an']['an_adj']
                        else:
                            total_an = 0
                        if exac['an'].get('an_afr'):
                            if type(exac['an'].get('an_afr')) == list:
                                an_afr = max(exac['an']['an_afr'])
                            elif type(exac['an'].get('an_afr')) != list:
                                an_afr = exac['an']['an_afr']
                        else:
                            an_afr = 0

                        #####################################
                        if exac['an'].get('an_amr'):
                            if type(exac['an'].get('an_amr')) == list:
                                an_amr = max(exac['an']['an_amr'])
                            elif type(exac['an'].get('an_amr')) != list:
                                an_amr = exac['an']['an_amr']
                        else:
                            an_afr = 0

                        ###########################################
                        if (exac['an'].get('an_eas')):
                            if type(exac['an'].get('an_eas')) == list:
                                an_eas = max(exac['an']['an_eas'])
                            elif type(exac['an'].get('an_eas')) != list:
                                an_eas = exac['an']['an_eas']
                        else:
                            an_eas = 0
                        ##############################################
                        if exac['an'].get('an_fin'):
                            if type(exac['an'].get('an_fin')) == list:
                                an_fin = max(exac['an']['an_fin'])
                            elif type(exac['an'].get('an_fin')) != list:
                                an_fin = exac['an']['an_fin']
                        else:
                            an_fin = 0

                        ################################
                        if (exac['an'].get('an_nfe')):
                            if type(exac['an'].get('an_nfe')) == list:
                                an_nfe = max(exac['an']['an_nfe'])
                            elif type(exac['an'].get('an_nfe')) != list:
                                an_nfe = exac['an']['an_nfe']
                        else:
                            an_nfe = 0

                        #################################
                        if (exac['an'].get('an_oth')):
                            if type(exac['an'].get('an_oth')) == list:
                                an_oth = max(exac['an']['an_oth'])
                            elif type(exac['an'].get('an_oth')) != list:
                                an_oth = exac['an']['an_oth']
                        else:
                            an_oth = 0

                        ###########################################
                        if (exac['an'].get('an_sas')):
                            if type(exac['an'].get('an_sas')) == list:
                                an_sas = max(exac['an']['an_sas'])
                            elif type(exac['an'].get('an_sas')) != list:
                                an_sas = exac['an']['an_sas']
                        else:
                            an_sas = 0
                    else:
                        total_an = 0
                        an_afr = 0
                        an_amr = 0
                        an_eas = 0
                        an_fin = 0
                        an_nfe = 0
                        an_oth = 0
                        an_sas = 0

                    if total_an == 0:
                        total_freq = 0
                    else:
                        total_freq = total_ac / total_an
                    all_freq_list.append(total_freq)
                    (f"EXAC_Freq : {total_freq}")

                    if an_afr == 0:
                        fre_afr = 0
                    else:
                        fre_afr = ac_afr / an_afr
                    freq_afr_list.append(fre_afr)
                    (f"FREQUENCY_AFR : {fre_afr}")

                    if an_amr == 0:
                        fre_amr = 0
                    else:
                        fre_amr = ac_amr / an_amr
                    freq_amr_list.append(fre_amr)
                    (f"FREQUENCY_AMR : {fre_amr}")

                    if an_eas == 0:
                        fre_eas = 0
                    else:
                        fre_eas = ac_eas / an_eas
                    freq_eas_list.append(fre_eas)
                    (f"FREQUENCY_EAS : {fre_eas}")

                    if an_fin == 0:
                        fre_fin = 0
                    else:
                        fre_fin = ac_fin / an_fin

                    freq_fin_list.append(fre_fin)
                    (f"FREQUENCY_FIN : {fre_fin}")

                    if an_nfe == 0:
                        fre_nfe = 0
                    else:
                        fre_nfe = ac_nfe / an_nfe
                    freq_nfe_list.append(fre_nfe)
                    (f"FREQUENCY_NFE : {fre_nfe}")

                    if an_oth == 0:
                        fre_oth = 0
                    else:
                        fre_oth = ac_oth / an_oth
                    freq_oth_list.append(fre_oth)
                    (f"FREQUENCY_OTH : {fre_oth}")

                    if an_sas == 0:
                        fre_sas = 0
                    else:
                        fre_sas = ac_sas / an_sas
                    freq_sas_list.append(fre_sas)
                    (f"FREQUENCY_SAS : {fre_sas}")

                else:
                    all_freq_list.append('.')
                    freq_afr_list.append('.')
                    freq_amr_list.append('.')
                    freq_eas_list.append('.')
                    freq_fin_list.append('.')
                    freq_nfe_list.append('.')
                    freq_oth_list.append('.')
                    freq_sas_list.append('.')

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
                    (f"Clinvar Interpretation : {clinical_significance}")
                    (f"Clinvar Condition : {clinical_condition}")
                    (f"Clinvar Allelic Origin : {allelic_origin}")
                    (f"Clinvar Review Status : {review_status}")
                    (f"Clinvar identifier : {identifier}")

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
            if all_freq_list[0]!='.':
                all_freq_list[0]=round(all_freq_list[0],4)
            if freq_afr_list[0]!='.':
                freq_afr_list[0]=round(freq_afr_list[0],4)
            if freq_amr_list[0]!='.':
                freq_amr_list[0]=round(freq_amr_list[0],4)
            if freq_eas_list[0]!='.':
                freq_eas_list[0]=round(freq_eas_list[0],4)
            if freq_fin_list[0]!='.':
                freq_fin_list[0]=round(freq_fin_list[0],4)
            if freq_nfe_list[0]!='.':
                freq_nfe_list[0]=round(freq_nfe_list[0],4)
            if freq_oth_list[0]!='.':
                freq_oth_list[0]=round(freq_oth_list[0],4)
            if freq_sas_list[0]!='.':
                freq_sas_list[0]=round(freq_sas_list[0],4)


        except Exception as es:
            self.error_str = es
        self.root = root
        self.root.title('VCESS-ALL')
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

        frame1 = Frame(self.root, bg='#c87894')
        frame1.place(x=0, y=0, width=width, height=150)
        title = Label(frame1, text="VCESS Retrieving Data from All Databases",
                      font=("Times New Roman", 30, "bold", "italic"),
                      bg='#c87894',
                      fg='white')
        title.place(x=350, y=45)
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
        lblimg1 = Label(image=self.photoimage1, bg='#c87894', borderwidth=0)
        lblimg1.place(x=80, y=10, width=250, height=130)

        self.root.configure(background='white')
        search_id = f.get_id()
        selected_id = Label(self.frametwo, text="ID: ", font=("Times New Roman", 14, 'bold'), bg='white',
                            fg='black')
        selected_id.grid(padx=0, pady=0)
        selected_id.place(x=60, y=40)
        selected_id2 = Label(self.frametwo, text=search_id, font=("Times New Roman", 12, 'italic'), bg='white',
                             fg='black')
        selected_id2.grid(padx=0, pady=0)
        selected_id2.place(x=90, y=40)

        self.root.overrideredirect(False)

        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width()
                y1 = canvas.winfo_height()//4
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1200 // fps, shift)

        ############# Main program ###############

        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)

        text = canvas.create_text(0, -2000,
                                  text=f'ALL is retrieving data from all the Databases'
                                       f'  Clinvar , dbSNP , dbNSFP , ExAC , InterVar , RefGene , EnSemble',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=90, y=70, width=1150, height=200)
        fps = 12  # Change the fps to make the animation faster/slower
        shift()


        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        try:
            if self.m==None and self.name == '.' and self.gene_id=='.':
                no_id = Label(self.frametwo, text='No Data available for this ID',
                              font=("Times New Roman", 15, "bold"),
                              bg='white',
                              fg='black')
                no_id.grid(padx=0, pady=0)
                no_id.place(x=60, y=65)
            table1 = LabelFrame(self.frametwo, text="Retrieved Data (Genomic Version HG_38)",
                                font=('Times New Roman', 16, 'bold'),bg="white")  ################
            table1.grid(padx=0, pady=0)
            table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
            table = ttk.Treeview(table1, height="30")  #################

            table['columns'] = ['ID',
                                'rsID',
                                'Sift_Pred',
                                'Sift_Score',
                                'Sift_converted_rankScore',
                                'Polyphen2_HDIV_Pred',
                                'Polyphen2_HDIV_Score',
                                'Polyphen2_HVAR_Pred',
                                'Polyphen2_HVAR_Score',
                                'LRT_Pred',
                                'LRT_Score',
                                'LRT_converted_rankScore',
                                'Mutation_Assessor_Pred',
                                'Mutation_Assessor_Score',
                                'Mutation_Assessor_rankscore',
                                'Mutation_Taster_Pred',
                                'Mutation_Taster_Score',
                                'MutationTaster_converted_rankscore',
                                'Provean_Pred',
                                'Provean_Score',
                                'Provean_Rank_score',
                                'DANN Score',
                                'Fathmm_Pred',
                                'Fathmm_Score',
                                'fathmm_Rank_Score',
                                'Fathmm-mkl_Pred',
                                'Fathmm-mkl_Score',
                                'Fathmm-mkl_RankScore',
                                'MetaSVM_Pred',
                                'MetaSVM_Score',
                                'Meta_SVM_Rank_Score',
                                'MetaLR_Pred',
                                'MetaLR_Score',
                                'MetaLR_Rank_Score',
                                'Integrated_fitCons_score',
                                'Integrated_confidence_value',
                                'Integrated_fitcons_rankscore',
                                'GERP++_RS',
                                'GERP++_RS_Rankscore',
                                'Siphy_29way_logOdds',
                                'siphy_29way_logOdds_rankscore',
                                'Revel_Score',
                                'CADD_raw_score',
                                'CADD_Phred',
                                'genoCanyon_score',
                                'genoCanyon_rankscore',
                                "Eigen_Raw_coding",
                                "Eigen-pc_Raw_coding",
                                'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                'phylo30rankscore',
                                'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                'phastcons17rankscore', 'phastcons30waylist',
                                'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                                'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                                'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                                'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                'Clinical_Condition',
                                'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                                'RefGene.GeneName','ensGene.GeneId']

            table.column('#0', width=120, minwidth=25)
            table.column('ID', anchor=W, width=120)
            table.column('rsID', anchor=W, width=120)
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
            table.column('GTEx_tisuue', anchor=W, width=120)
            table.column('EXAC_All_Freq', anchor=W, width=120)
            table.column('EXAC_Afr_Freq', anchor=W, width=120)
            table.column('EXAC_Amr_Freq', anchor=W, width=120)
            table.column('EXAC_Eas_Freq', anchor=W, width=120)
            table.column('EXAC_Fin_Freq', anchor=W, width=120)
            table.column('EXAC_Nfe_Freq', anchor=W, width=120)
            table.column('EXAC_Oth_Freq', anchor=W, width=120)
            table.column('EXAC_Sas_Freq', anchor=W, width=120)
            table.column('Variant_ID', anchor=W, width=120)
            table.column('Clinical_Type', anchor=CENTER, width=120)
            table.column('Allelic_ID', anchor=CENTER, width=120)
            table.column('Clinical_Significance', anchor=CENTER, width=120)
            table.column('Clinical_Condition', anchor=CENTER, width=120)
            table.column('Allelic_Origin', anchor=CENTER, width=120)
            table.column('Review_Status', anchor=CENTER, width=120)
            table.column('Clinical_identifier', anchor=CENTER, width=120)
            table.column('Cytogenic_Location', anchor=CENTER, width=120)
            table.column('RefGene.GeneName', anchor=W, width=200)
            table.column('ensGene.GeneId', anchor=W, width=200)



            table.heading('#0', text='Serial No.', anchor=W)
            table.heading('ID', text='ID', anchor=W)
            table.heading('rsID', text='rsID', anchor=W)
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
            table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
            table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
            table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
            table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
            table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
            table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
            table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
            table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
            table.heading('Variant_ID', text='Variant_ID', anchor=W)
            table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
            table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
            table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
            table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
            table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
            table.heading('Review_Status', text='Review_Status', anchor=CENTER)
            table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
            table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
            table.heading('RefGene.GeneName', text='RefGene.GeneName', anchor=W)
            table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)


            for i in range(len(sift_pred)):
                table.insert(parent='', index='end', iid=i, text=i + 1,
                             values=(Id[i],rsid_list[i], sift_pred[i],
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
                                     GTEx_tissue[i],
                                     all_freq_list[i],
                                     freq_afr_list[i],
                                     freq_amr_list[i],
                                     freq_eas_list[i],
                                     freq_fin_list[i],
                                     freq_nfe_list[i],
                                     freq_oth_list[i],
                                     freq_sas_list[i],
                                     variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                     clin_interpretation_list[i],
                                     clin_condition_list[i],
                                     allelic_origin_list[i],
                                     review_status_list[i],
                                     identifier_list[i],
                                     cytoband_list[i],self.name,self.gene_id
                                     ))
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
        self.error_str = ''
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
        fathmm_mkl_rankscore.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_conf_value.clear()
        integ_fitcons_rankscore.clear()
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
        rsid_list.clear()
        all_freq_list.clear()
        freq_afr_list.clear()
        freq_amr_list.clear()
        freq_eas_list.clear()
        freq_fin_list.clear()
        freq_nfe_list.clear()
        freq_oth_list.clear()
        freq_sas_list.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
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
        links.clear()
        Id.clear()
        geneName.clear()
        geneIds.clear()
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)


        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')
        self.root1.overrideredirect(True)

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 12, "bold", "italic"),
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

        progress = ttk.Progressbar(self.root1,style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        #progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        p = 20
        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)


        try:
            g = Genome(db="hg19")
            for id in vcf:
                progress['value'] = p

                self.root1.update_idletasks()
                self.root1.after(100)  # Delay in millisecs.
                p = p+ 40
                Id.append(id)
                index_id=Id.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(id)
                chr = id[0:id.index(':'):]
                chr = chr.replace('chr', '')

                pos = id[id.index('.') + 1:]
                x = [j for j in pos if ord(j) < 48 or ord(j) > 57]
                pos_index = pos.index(x[0])
                pos = pos[:pos_index]

                nearest = g.knearest("refGene", "chr" + (chr), int(pos), int(pos))
                if len(nearest) == 0:
                    geneName.append('.')
                else:
                    for n in nearest:
                        name = n.name2
                    geneName.append(name)

                chr = id[0:id.index(':'):]
                chr = chr.replace('chr', '')

                pos = id[id.index('.') + 1:]
                x = [j for j in pos if ord(j) < 48 or ord(j) > 57]
                pos_index = pos.index(x[0])
                pos = pos[:pos_index]

                self.gene_id = ''

                # release 75 uses human reference genome GRCh37/hg19
                data = EnsemblRelease(75)
                gene_names = data.gene_names_at_locus(contig=int(chr), position=int(pos))
                (gene_names)
                if len(gene_names) == 0:
                    self.gene_id = '.  '
                else:

                    if type(data.gene_ids_of_gene_name(gene_names[0])) == list:
                        for x in data.gene_ids_of_gene_name(gene_names[0]):
                            self.gene_id += x + ', '
                    else:
                        self.gene_id = data.gene_ids_of_gene_name(gene_names[0])
                self.gene_id = self.gene_id[:-2]
                geneIds.append(self.gene_id)
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

                                intervar = data['Intervar']
                            else:
                                intervar = '.'

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
                            intervar_list.append(intervar)
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


                if m == None:

                    rsid_list.append('.')

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
                    all_freq_list.append('.')
                    freq_afr_list.append('.')
                    freq_amr_list.append('.')
                    freq_eas_list.append('.')
                    freq_fin_list.append('.')
                    freq_nfe_list.append('.')
                    freq_oth_list.append('.')
                    freq_sas_list.append('.')
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
                                        siftpred = (max(dbnsfp['sift']['pred']))

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

                    if m.get('exac'):

                        exac = m['exac']

                        ################ ALLELE COUNTTTT OF DIFFERENT COUNTRIES
                        if exac.get('ac'):
                            if exac['ac'].get('ac_adj'):
                                total_ac = exac['ac']['ac_adj']
                            else:
                                total_ac = 0
                            if exac['ac'].get('ac_afr'):

                                if type(exac['ac'].get('ac_afr')) == list:
                                    ac_afr = max(exac['ac']['ac_afr'])
                                elif type(exac['ac'].get('ac_afr')) != list:
                                    ac_afr = exac['ac']['ac_afr']
                            else:
                                ac_afr = 0

                            ###################
                            if exac['ac'].get('ac_amr'):
                                if type(exac['ac'].get('ac_amr')) == list:
                                    ac_amr = max(exac['ac']['ac_amr'])
                                elif type(exac['ac'].get('ac_amr')) != list:
                                    ac_amr = exac['ac']['ac_amr']
                            else:
                                ac_amr = 0

                            #######################
                            if exac['ac'].get('ac_eas'):
                                if type(exac['ac'].get('ac_eas')) == list:
                                    ac_eas = max(exac['ac']['ac_eas'])
                                elif type(exac['ac'].get('ac_eas')) != list:
                                    ac_eas = exac['ac']['ac_eas']
                            else:
                                ac_eas = 0

                            ########################
                            if exac['ac'].get('ac_fin'):
                                if type(exac['ac'].get('ac_fin')) == list:
                                    ac_fin = max(exac['ac']['ac_fin'])
                                elif type(exac['ac'].get('ac_fin')) != list:
                                    ac_fin = exac['ac']['ac_fin']
                            else:
                                ac_fin = 0

                            #########################
                            if exac['ac'].get('ac_nfe'):
                                if type(exac['ac'].get('ac_nfe')) == list:
                                    ac_nfe = max(exac['ac']['ac_nfe'])
                                elif type(exac['ac'].get('ac_nfe')) != list:
                                    ac_nfe = exac['ac']['ac_nfe']
                            else:
                                ac_nfe = 0

                            #############################
                            if exac['ac'].get('ac_oth'):
                                if type(exac['ac'].get('ac_oth')) == list:
                                    ac_oth = max(exac['ac']['ac_oth'])
                                elif type(exac['ac'].get('ac_oth')) != list:
                                    ac_oth = exac['ac']['ac_oth']
                            else:
                                ac_oth = 0

                            ##############################
                            if exac['ac'].get('ac_sas'):
                                if type(exac['ac'].get('ac_sas')) == list:
                                    ac_sas = max(exac['ac']['ac_sas'])
                                elif type(exac['ac'].get('ac_sas')) != list:
                                    ac_sas = exac['ac']['ac_sas']
                            else:
                                ac_sas = 0
                        else:
                            total_ac = 0
                            ac_afr = 0
                            ac_amr = 0
                            ac_eas = 0
                            ac_fin = 0
                            ac_nfe = 0
                            ac_oth = 0
                            ac_sas = 0

                        #####################################ALLELE NUMBER OF DIFFERENT COUNTRIES##################################

                        if exac.get('an'):
                            if exac['an'].get('an_adj'):
                                total_an = exac['an']['an_adj']
                            else:
                                total_an = 0
                            if exac['an'].get('an_afr'):
                                if type(exac['an'].get('an_afr')) == list:
                                    an_afr = max(exac['an']['an_afr'])
                                elif type(exac['an'].get('an_afr')) != list:
                                    an_afr = exac['an']['an_afr']
                            else:
                                an_afr = 0

                            #####################################
                            if exac['an'].get('an_amr'):
                                if type(exac['an'].get('an_amr')) == list:
                                    an_amr = max(exac['an']['an_amr'])
                                elif type(exac['an'].get('an_amr')) != list:
                                    an_amr = exac['an']['an_amr']
                            else:
                                an_afr = 0

                            ###########################################
                            if (exac['an'].get('an_eas')):
                                if type(exac['an'].get('an_eas')) == list:
                                    an_eas = max(exac['an']['an_eas'])
                                elif type(exac['an'].get('an_eas')) != list:
                                    an_eas = exac['an']['an_eas']
                            else:
                                an_eas = 0
                            ##############################################
                            if exac['an'].get('an_fin'):
                                if type(exac['an'].get('an_fin')) == list:
                                    an_fin = max(exac['an']['an_fin'])
                                elif type(exac['an'].get('an_fin')) != list:
                                    an_fin = exac['an']['an_fin']
                            else:
                                an_fin = 0

                            ################################
                            if (exac['an'].get('an_nfe')):
                                if type(exac['an'].get('an_nfe')) == list:
                                    an_nfe = max(exac['an']['an_nfe'])
                                elif type(exac['an'].get('an_nfe')) != list:
                                    an_nfe = exac['an']['an_nfe']
                            else:
                                an_nfe = 0

                            #################################
                            if (exac['an'].get('an_oth')):
                                if type(exac['an'].get('an_oth')) == list:
                                    an_oth = max(exac['an']['an_oth'])
                                elif type(exac['an'].get('an_oth')) != list:
                                    an_oth = exac['an']['an_oth']
                            else:
                                an_oth = 0

                            ###########################################
                            if (exac['an'].get('an_sas')):
                                if type(exac['an'].get('an_sas')) == list:
                                    an_sas = max(exac['an']['an_sas'])
                                elif type(exac['an'].get('an_sas')) != list:
                                    an_sas = exac['an']['an_sas']
                            else:
                                an_sas = 0
                        else:
                            total_an = 0
                            an_afr = 0
                            an_amr = 0
                            an_eas = 0
                            an_fin = 0
                            an_nfe = 0
                            an_oth = 0
                            an_sas = 0

                        if total_an == 0:
                            total_freq = 0
                        else:
                            total_freq = total_ac / total_an
                        all_freq_list.append(total_freq)
                        (f"EXAC_Freq : {total_freq}")

                        if an_afr == 0:
                            fre_afr = 0
                        else:
                            fre_afr = ac_afr / an_afr
                        freq_afr_list.append(fre_afr)
                        (f"FREQUENCY_AFR : {fre_afr}")

                        if an_amr == 0:
                            fre_amr = 0
                        else:
                            fre_amr = ac_amr / an_amr
                        freq_amr_list.append(fre_amr)
                        (f"FREQUENCY_AMR : {fre_amr}")

                        if an_eas == 0:
                            fre_eas = 0
                        else:
                            fre_eas = ac_eas / an_eas
                        freq_eas_list.append(fre_eas)
                        (f"FREQUENCY_EAS : {fre_eas}")

                        if an_fin == 0:
                            fre_fin = 0
                        else:
                            fre_fin = ac_fin / an_fin

                        freq_fin_list.append(fre_fin)
                        (f"FREQUENCY_FIN : {fre_fin}")

                        if an_nfe == 0:
                            fre_nfe = 0
                        else:
                            fre_nfe = ac_nfe / an_nfe
                        freq_nfe_list.append(fre_nfe)
                        (f"FREQUENCY_NFE : {fre_nfe}")

                        if an_oth == 0:
                            fre_oth = 0
                        else:
                            fre_oth = ac_oth / an_oth
                        freq_oth_list.append(fre_oth)
                        (f"FREQUENCY_OTH : {fre_oth}")

                        if an_sas == 0:
                            fre_sas = 0
                        else:
                            fre_sas = ac_sas / an_sas
                        freq_sas_list.append(fre_sas)
                        (f"FREQUENCY_SAS : {fre_sas}")

                    else:
                        all_freq_list.append('.')
                        freq_afr_list.append('.')
                        freq_amr_list.append('.')
                        freq_eas_list.append('.')
                        freq_fin_list.append('.')
                        freq_nfe_list.append('.')
                        freq_oth_list.append('.')
                        freq_sas_list.append('.')

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
                                            clinical_condition =  clinvar['rcv']['conditions'][0]['name']
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
                        variant_id_list.append('.')
                        variant_type_list.append('.')
                        allele_id_list.append('.')
                        cytoband_list.append('.')
                        clin_interpretation_list.append('.')
                        clin_condition_list.append('.')
                        allelic_origin_list.append('.')
                        review_status_list.append('.')
                        identifier_list.append('.')
            if all_freq_list[0]!='.':
                all_freq_list[0]=round(all_freq_list[0],4)
            if freq_afr_list[0]!='.':
                freq_afr_list[0]=round(freq_afr_list[0],4)
            if freq_amr_list[0]!='.':
                freq_amr_list[0]=round(freq_amr_list[0],4)
            if freq_eas_list[0]!='.':
                freq_eas_list[0]=round(freq_eas_list[0],4)
            if freq_fin_list[0]!='.':
                freq_fin_list[0]=round(freq_fin_list[0],4)
            if freq_nfe_list[0]!='.':
                freq_nfe_list[0]=round(freq_nfe_list[0],4)
            if freq_oth_list[0]!='.':
                freq_oth_list[0]=round(freq_oth_list[0],4)
            if freq_sas_list[0]!='.':
                freq_sas_list[0]=round(freq_sas_list[0],4)
        except Exception as es:
                (es)
                self.error_str = es

        self.root = root
        self.root.title('ALL window')
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
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 30, "bold", "italic"),
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
        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width()
                y1 = canvas.winfo_height()//4
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1200 // fps, shift)

            ############# Main program ###############

        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)

        text = canvas.create_text(0, -2000,
                                  text=f'ALL is retrieving data from all the Databases'
                                       f'  Clinvar , dbSNP , dbNSFP , ExAC , InterVar , RefGene , EnSemble',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=90, y=70, width=1150, height=200)
        fps = 12  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        (f"varaimbnmhgdsljkfghhhdjgfhhjdkbndfgfdffdjfbdf{len(variant_type_list)}")
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
            self.root.protocol("WM_DELETE_WINDOW", on_closing)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(variant_type_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(variant_type_list) == len(Id) :

                table1 = LabelFrame(self.frametwo, text=
                "Retrieved Data (Genomic Version HG_19)",
                                    font=('Times New Roman', 16, 'bold'),bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
                table = ttk.Treeview(table1, height="30")  #################

                table['columns'] = ['ID',
                                    'rsID',
                                    'Sift_Pred',
                                    'Sift_Score',
                                    'Sift_converted_rankScore',
                                    'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred',
                                    'Polyphen2_HVAR_Score',
                                    'LRT_Pred',
                                    'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred',
                                    'Mutation_Assessor_Score',
                                    'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score',
                                    'MutationTaster_converted_rankscore',
                                    'Provean_Pred',
                                    'Provean_Score',
                                    'Provean_Rank_score',
                                    'DANN Score',
                                    'Fathmm_Pred',
                                    'Fathmm_Score',
                                    'fathmm_Rank_Score',
                                    'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore',
                                    'MetaSVM_Pred',
                                    'MetaSVM_Score',
                                    'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred',
                                    'MetaLR_Score',
                                    'MetaLR_Rank_Score',
                                    'Integrated_fitCons_score',
                                    'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS',
                                    'GERP++_RS_Rankscore',
                                    'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score',
                                    'CADD_Phred',
                                    'genoCanyon_score',
                                    'genoCanyon_rankscore',
                                    "Eigen_Raw_coding",
                                    "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                                    'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                                    'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                                    'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                                    'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5',
                                    'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5',
                                    'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4','ensGene.GeneId','refGene.GeneName']

                table.column('#0', width=120, minwidth=25)
                table.column('ID', anchor=W, width=120)
                table.column('rsID', anchor=W, width=120)
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
                table.column('GTEx_tisuue', anchor=W, width=120)
                table.column('EXAC_All_Freq', anchor=W, width=120)
                table.column('EXAC_Afr_Freq', anchor=W, width=120)
                table.column('EXAC_Amr_Freq', anchor=W, width=120)
                table.column('EXAC_Eas_Freq', anchor=W, width=120)
                table.column('EXAC_Fin_Freq', anchor=W, width=120)
                table.column('EXAC_Nfe_Freq', anchor=W, width=120)
                table.column('EXAC_Oth_Freq', anchor=W, width=120)
                table.column('EXAC_Sas_Freq', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Cytogenic_Location', anchor=CENTER, width=120)
                table.column('InterVar',  anchor=W, width=120)
                table.column('PVS1', anchor=W, width=120)
                table.column('PS1', anchor=W, width=120)
                table.column('PS2', anchor=W, width=120)
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
                table.column('ensGene.GeneId', anchor=W, width=200)
                table.column('refGene.GeneName', anchor=W, width=200)


                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='rsID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)
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
                table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
                table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
                table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
                table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
                table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
                table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
                table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
                table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
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
                table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)
                table.heading('refGene.GeneName', text='refGene.GeneName', anchor=W)
                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i],rsid_list[i], sift_pred[i],
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
                                         GTEx_tissue[i], all_freq_list[i],
                                         freq_afr_list[i],
                                         freq_amr_list[i],
                                         freq_eas_list[i],
                                         freq_fin_list[i],
                                         freq_nfe_list[i],
                                         freq_oth_list[i],
                                         freq_sas_list[i],
                                         variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i],
                                         intervar_list[i],
                                         pvs1_list[i],
                                         ps1_list[i],
                                         ps2_list[i],
                                         ps3_list[i],
                                         ps4_list[i], pm1_list[i], pm2_list[i], pm3_list[i], pm4_list[i],
                                         pm5_list[i], pm6_list[i], pp1_list[i], pp2_list[i], pp3_list[i],
                                         pp4_list[i], pp5_list[i], ba1_list[i], bp1_list[i], bp2_list[i],
                                         bp3_list[i], bp4_list[i], bp5_list[i], bp6_list[i], bp7_list[i],
                                         bs1_list[i], bs2_list[i], bs3_list[i], bs4_list[i],geneIds[i],geneName[i])
                                 )
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
            elif (len(variant_type_list) != len(Id)) and (len(variant_type_list))!=0 :

                table1 = LabelFrame(self.frametwo, text=
                "Retrieved Data (Genomic Version HG_19)",
                                    font=('Times New Roman', 16, 'bold'),bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
                table = ttk.Treeview(table1, height="30")  #################

                table['columns'] = ['ID',
                                    'rsID',
                                    'Sift_Pred',
                                    'Sift_Score',
                                    'Sift_converted_rankScore',
                                    'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred',
                                    'Polyphen2_HVAR_Score',
                                    'LRT_Pred',
                                    'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred',
                                    'Mutation_Assessor_Score',
                                    'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score',
                                    'MutationTaster_converted_rankscore',
                                    'Provean_Pred',
                                    'Provean_Score',
                                    'Provean_Rank_score',
                                    'DANN Score',
                                    'Fathmm_Pred',
                                    'Fathmm_Score',
                                    'fathmm_Rank_Score',
                                    'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore',
                                    'MetaSVM_Pred',
                                    'MetaSVM_Score',
                                    'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred',
                                    'MetaLR_Score',
                                    'MetaLR_Rank_Score',
                                    'Integrated_fitCons_score',
                                    'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS',
                                    'GERP++_RS_Rankscore',
                                    'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score',
                                    'CADD_Phred',
                                    'genoCanyon_score',
                                    'genoCanyon_rankscore',
                                    "Eigen_Raw_coding",
                                    "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                                    'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                                    'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                                    'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                                    'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5',
                                    'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5',
                                    'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4','ensGene.GeneId','refGene.GeneName']

                table.column('#0', width=120, minwidth=25)
                table.column('ID', anchor=W, width=120)
                table.column('rsID', anchor=W, width=120)
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
                table.column('GTEx_tisuue', anchor=W, width=120)
                table.column('EXAC_All_Freq', anchor=W, width=120)
                table.column('EXAC_Afr_Freq', anchor=W, width=120)
                table.column('EXAC_Amr_Freq', anchor=W, width=120)
                table.column('EXAC_Eas_Freq', anchor=W, width=120)
                table.column('EXAC_Fin_Freq', anchor=W, width=120)
                table.column('EXAC_Nfe_Freq', anchor=W, width=120)
                table.column('EXAC_Oth_Freq', anchor=W, width=120)
                table.column('EXAC_Sas_Freq', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Cytogenic_Location', anchor=CENTER, width=120)
                table.column('InterVar',  anchor=W, width=120)
                table.column('PVS1', anchor=W, width=120)
                table.column('PS1', anchor=W, width=120)
                table.column('PS2', anchor=W, width=120)
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
                table.column('ensGene.GeneId', anchor=W, width=200)
                table.column('refGene.GeneName', anchor=W, width=200)


                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='rsID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)
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
                table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
                table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
                table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
                table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
                table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
                table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
                table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
                table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
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
                table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)
                table.heading('refGene.GeneName', text='refGene.GeneName', anchor=W)
                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i],rsid_list[i], sift_pred[i],
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
                                         GTEx_tissue[i], all_freq_list[i],
                                         freq_afr_list[i],
                                         freq_amr_list[i],
                                         freq_eas_list[i],
                                         freq_fin_list[i],
                                         freq_nfe_list[i],
                                         freq_oth_list[i],
                                         freq_sas_list[i],
                                         variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i],
                                         intervar_list[i],
                                         pvs1_list[i],
                                         ps1_list[i],
                                         ps2_list[i],
                                         ps3_list[i],
                                         ps4_list[i], pm1_list[i], pm2_list[i], pm3_list[i], pm4_list[i],
                                         pm5_list[i], pm6_list[i], pp1_list[i], pp2_list[i], pp3_list[i],
                                         pp4_list[i], pp5_list[i], ba1_list[i], bp1_list[i], bp2_list[i],
                                         bp3_list[i], bp4_list[i], bp5_list[i], bp6_list[i], bp7_list[i],
                                         bs1_list[i], bs2_list[i], bs3_list[i], bs4_list[i],geneIds[i],geneName[i])
                                 )
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
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nEnter values again    ', font=("Times New Roman", 12),
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

    def get_file(self):
        reverse_file = self.file[::-1]
        # (reverse_file)
        pos = reverse_file.find('/', 0)
        # (pos)
        path = reverse_file[pos + 1:]
        path = path[::-1]
        input_file_csv = path + '/input.csv'


        header =['HGVS_ID', 'Sift_Pred', 'Sift_Score', 'sift_converted_rankScore', 'Polyphen2_HDIV_Pred', 'Polyphen2_HDIV_Score', 'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score', 'LRT_converted_rankScore', 'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore', 'Mutation_Taster_Pred', 'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred', 'Provean_Score', 'Provean_Rank_score', 'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred', 'Fathmm-mkl_Score', 'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score', 'MetaLR_Pred:', 'MetaLR_Score', 'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value', 'Integrated_fitcons_rankscore', 'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds', 'siphy_29way_logOdds_rankscore', 'Revel_Score', 'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore', 'Eigen_Raw_coding', 'Eigen-pc_Raw_coding', 'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way', 'phylo30rankscore', 'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist', 'phastcons17rankscore', 'phastcons30waylist', 'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue', 'rsID', 'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq', 'EXAC_Nfe_Freq', 'EXAC_Oth_Freq', 'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance', 'Clinical_Condition', 'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location', 'InterVar', 'PVS1', 'PS1', 'PS2', 'PS3', 'PS4', 'PM1', 'PM2', 'PM3', 'PM4', 'PM5', 'PM6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'BA1', 'BP1', 'BP2', 'BP3', 'BP4', 'BP5', 'BP6', 'BP7', 'BS1', 'BS2', 'BS3', 'BS4','Ensemble.ID','RefGene.GeneName']
        data1=[]

        for i in range(len(sift_pred)):
            data=[]
            data.append(Id[i])
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
            data.append(rsid_list[i])
            data.append(all_freq_list[i])
            data.append(freq_afr_list[i])
            data.append(freq_amr_list[i])
            data.append(freq_eas_list[i])
            data.append(freq_fin_list[i])
            data.append(freq_nfe_list[i])
            data.append(freq_oth_list[i])
            data.append(freq_sas_list[i])
            data.append(variant_id_list[i])
            data.append(variant_type_list[i])
            data.append(allele_id_list[i])
            data.append(clin_interpretation_list[i])
            data.append(clin_condition_list[i])
            data.append(allelic_origin_list[i])
            data.append(review_status_list[i])
            data.append(identifier_list[i])
            data.append(cytoband_list[i])
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
            data.append(geneIds[i])
            data.append(geneName[i])
            data1.append(data)


        l1 = []
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
                  header[59]: row[59],
                  header[60]: row[60], header[61]: row[61], header[62]: row[62], header[63]: row[63],
                  header[64]: row[64],
                  header[65]: row[65],
                  header[66]: row[66], header[67]: row[67], header[68]: row[68], header[69]: row[69], header[70]: row[70],
                  header[71]: row[71], header[72]: row[72], header[73]: row[73], header[74]: row[74], header[75]: row[75]
                , header[76]: row[76],
                  header[77]: row[77], header[78]: row[78], header[79]: row[79], header[80]: row[80], header[81]: row[81],header[82]: row[82],
                  header[83]: row[83], header[84]: row[84], header[85]: row[85], header[86]: row[86], header[87]: row[87]
                , header[88]: row[88], header[89]: row[89],
                  header[90]: row[90], header[91]: row[91], header[92]: row[92], header[93]: row[93], header[94]: row[94],
                  header[95]: row[95], header[96]: row[96], header[97]: row[97], header[98]: row[98], header[99]: row[99]
                , header[100]: row[100], header[101]: row[101], header[102]: row[102]
                , header[103]: row[103], header[104]: row[104], header[105]: row[105]
                , header[106]: row[106],
                  header[107]: row[107],header[108]: row[108],
                  header[109]: row[109],header[110]: row[110]
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
        self.error_str = ''
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
        fathmm_mkl_rankscore.clear()
        fathmm_rs.clear()
        fathmm_mkl_pred.clear()
        fathmm_mkl_score.clear()
        metasvm_pred.clear()
        metasvm_score.clear()
        metasvm_rankscore.clear()
        metalr_pred.clear()
        metalr_score.clear()
        MetaLR_rankscore.clear()
        integ_fitcoin_score.clear()
        integ_conf_value.clear()
        integ_fitcons_rankscore.clear()
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
        rsid_list.clear()
        all_freq_list.clear()
        freq_afr_list.clear()
        freq_amr_list.clear()
        freq_eas_list.clear()
        freq_fin_list.clear()
        freq_nfe_list.clear()
        freq_oth_list.clear()
        freq_sas_list.clear()
        variant_id_list.clear()
        variant_type_list.clear()
        allele_id_list.clear()
        cytoband_list.clear()
        clin_interpretation_list.clear()
        clin_condition_list.clear()
        allelic_origin_list.clear()
        review_status_list.clear()
        identifier_list.clear()
        Id.clear()
        geneName.clear()
        geneIds.clear()
        self.root1 = root
        self.root1.title('LOADING......')
        self.root1.geometry("380x200")
        self.root1.overrideredirect(True)


        self.root1.eval('tk::PlaceWindow . center')
        self.root1.resizable(width=False, height=False)
        self.root1.configure(background='white')
        self.root1.overrideredirect(True)

        frame1 = Frame(self.root1, bg='#7877a5')
        frame1.place(x=0, y=0, width=380, height=50)
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 12, "bold", "italic"),
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

        progress = ttk.Progressbar(self.root1,style="green.Horizontal.TProgressbar", orient=HORIZONTAL,
                                   length=380, mode='indeterminate',
                                   maximum=(48 * 40) + 20)
        #progress.configure("green.Horizontal.TProgressbar", foreground='red', background='red')
        # progress = ttk.Progressbar(self.root1,orient=HORIZONTAL,length=380)
        progress.place(x=0, y=100)
        p= 20
        self.file = f.return_filepath()

        vcf = myvariant.get_hgvs_from_vcf(self.file)
        vcf = list(vcf)


        try:
            g = Genome(db="hg38")
            for id in vcf:
                progress['value'] = p

                self.root1.update_idletasks()
                self.root1.after(100)  # Delay in millisecs.
                p= p+ 40
                Id.append(id)
                index_id=Id.index(id)
                title.configure(text="LOADING......."+str(index_id)+" /"+str(len(vcf))+" IDs",)
                mv = myvariant.MyVariantInfo()
                # m=mv.getvariant('chr1:948921T>C')
                m = mv.getvariant(id,assembly="hg38")
                chr = id[0:id.index(':'):]
                chr = chr.replace('chr', '')

                pos = id[id.index('.') + 1:]
                x = [j for j in pos if ord(j) < 48 or ord(j) > 57]
                pos_index = pos.index(x[0])
                pos = pos[:pos_index]

                nearest = g.knearest("refGene", "chr" + (chr), int(pos), int(pos))
                if len(nearest) == 0:
                    geneName.append('.')
                else:
                    for n in nearest:
                        name = n.name2
                    geneName.append(name)

                chr = id[0:id.index(':'):]
                chr = chr.replace('chr', '')

                pos = id[id.index('.') + 1:]
                x = [j for j in pos if ord(j) < 48 or ord(j) > 57]
                pos_index = pos.index(x[0])
                pos = pos[:pos_index]

                self.gene_id = ''

                # release 75 uses human reference genome GRCh37/hg19
                data = EnsemblRelease(77)
                gene_names = data.gene_names_at_locus(contig=int(chr), position=int(pos))
                (gene_names)
                if len(gene_names) == 0:
                    self.gene_id = '.  '
                else:

                    if type(data.gene_ids_of_gene_name(gene_names[0])) == list:
                        for x in data.gene_ids_of_gene_name(gene_names[0]):
                            self.gene_id += x + ', '
                    else:
                        self.gene_id = data.gene_ids_of_gene_name(gene_names[0])
                self.gene_id = self.gene_id[:-2]
                geneIds.append(self.gene_id)
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


                if m == None:

                    rsid_list.append('.')

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
                    all_freq_list.append('.')
                    freq_afr_list.append('.')
                    freq_amr_list.append('.')
                    freq_eas_list.append('.')
                    freq_fin_list.append('.')
                    freq_nfe_list.append('.')
                    freq_oth_list.append('.')
                    freq_sas_list.append('.')
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
                                        siftpred = (max(dbnsfp['sift']['pred']))

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

                    if m.get('exac'):

                        exac = m['exac']

                        ################ ALLELE COUNTTTT OF DIFFERENT COUNTRIES
                        if exac.get('ac'):
                            if exac['ac'].get('ac_adj'):
                                total_ac = exac['ac']['ac_adj']
                            else:
                                total_ac = 0
                            if exac['ac'].get('ac_afr'):

                                if type(exac['ac'].get('ac_afr')) == list:
                                    ac_afr = max(exac['ac']['ac_afr'])
                                elif type(exac['ac'].get('ac_afr')) != list:
                                    ac_afr = exac['ac']['ac_afr']
                            else:
                                ac_afr = 0

                            ###################
                            if exac['ac'].get('ac_amr'):
                                if type(exac['ac'].get('ac_amr')) == list:
                                    ac_amr = max(exac['ac']['ac_amr'])
                                elif type(exac['ac'].get('ac_amr')) != list:
                                    ac_amr = exac['ac']['ac_amr']
                            else:
                                ac_amr = 0

                            #######################
                            if exac['ac'].get('ac_eas'):
                                if type(exac['ac'].get('ac_eas')) == list:
                                    ac_eas = max(exac['ac']['ac_eas'])
                                elif type(exac['ac'].get('ac_eas')) != list:
                                    ac_eas = exac['ac']['ac_eas']
                            else:
                                ac_eas = 0

                            ########################
                            if exac['ac'].get('ac_fin'):
                                if type(exac['ac'].get('ac_fin')) == list:
                                    ac_fin = max(exac['ac']['ac_fin'])
                                elif type(exac['ac'].get('ac_fin')) != list:
                                    ac_fin = exac['ac']['ac_fin']
                            else:
                                ac_fin = 0

                            #########################
                            if exac['ac'].get('ac_nfe'):
                                if type(exac['ac'].get('ac_nfe')) == list:
                                    ac_nfe = max(exac['ac']['ac_nfe'])
                                elif type(exac['ac'].get('ac_nfe')) != list:
                                    ac_nfe = exac['ac']['ac_nfe']
                            else:
                                ac_nfe = 0

                            #############################
                            if exac['ac'].get('ac_oth'):
                                if type(exac['ac'].get('ac_oth')) == list:
                                    ac_oth = max(exac['ac']['ac_oth'])
                                elif type(exac['ac'].get('ac_oth')) != list:
                                    ac_oth = exac['ac']['ac_oth']
                            else:
                                ac_oth = 0

                            ##############################
                            if exac['ac'].get('ac_sas'):
                                if type(exac['ac'].get('ac_sas')) == list:
                                    ac_sas = max(exac['ac']['ac_sas'])
                                elif type(exac['ac'].get('ac_sas')) != list:
                                    ac_sas = exac['ac']['ac_sas']
                            else:
                                ac_sas = 0
                        else:
                            total_ac = 0
                            ac_afr = 0
                            ac_amr = 0
                            ac_eas = 0
                            ac_fin = 0
                            ac_nfe = 0
                            ac_oth = 0
                            ac_sas = 0

                        #####################################ALLELE NUMBER OF DIFFERENT COUNTRIES##################################

                        if exac.get('an'):
                            if exac['an'].get('an_adj'):
                                total_an = exac['an']['an_adj']
                            else:
                                total_an = 0
                            if exac['an'].get('an_afr'):
                                if type(exac['an'].get('an_afr')) == list:
                                    an_afr = max(exac['an']['an_afr'])
                                elif type(exac['an'].get('an_afr')) != list:
                                    an_afr = exac['an']['an_afr']
                            else:
                                an_afr = 0

                            #####################################
                            if exac['an'].get('an_amr'):
                                if type(exac['an'].get('an_amr')) == list:
                                    an_amr = max(exac['an']['an_amr'])
                                elif type(exac['an'].get('an_amr')) != list:
                                    an_amr = exac['an']['an_amr']
                            else:
                                an_afr = 0

                            ###########################################
                            if (exac['an'].get('an_eas')):
                                if type(exac['an'].get('an_eas')) == list:
                                    an_eas = max(exac['an']['an_eas'])
                                elif type(exac['an'].get('an_eas')) != list:
                                    an_eas = exac['an']['an_eas']
                            else:
                                an_eas = 0
                            ##############################################
                            if exac['an'].get('an_fin'):
                                if type(exac['an'].get('an_fin')) == list:
                                    an_fin = max(exac['an']['an_fin'])
                                elif type(exac['an'].get('an_fin')) != list:
                                    an_fin = exac['an']['an_fin']
                            else:
                                an_fin = 0

                            ################################
                            if (exac['an'].get('an_nfe')):
                                if type(exac['an'].get('an_nfe')) == list:
                                    an_nfe = max(exac['an']['an_nfe'])
                                elif type(exac['an'].get('an_nfe')) != list:
                                    an_nfe = exac['an']['an_nfe']
                            else:
                                an_nfe = 0

                            #################################
                            if (exac['an'].get('an_oth')):
                                if type(exac['an'].get('an_oth')) == list:
                                    an_oth = max(exac['an']['an_oth'])
                                elif type(exac['an'].get('an_oth')) != list:
                                    an_oth = exac['an']['an_oth']
                            else:
                                an_oth = 0

                            ###########################################
                            if (exac['an'].get('an_sas')):
                                if type(exac['an'].get('an_sas')) == list:
                                    an_sas = max(exac['an']['an_sas'])
                                elif type(exac['an'].get('an_sas')) != list:
                                    an_sas = exac['an']['an_sas']
                            else:
                                an_sas = 0
                        else:
                            total_an = 0
                            an_afr = 0
                            an_amr = 0
                            an_eas = 0
                            an_fin = 0
                            an_nfe = 0
                            an_oth = 0
                            an_sas = 0

                        if total_an == 0:
                            total_freq = 0
                        else:
                            total_freq = total_ac / total_an
                        all_freq_list.append(total_freq)
                        (f"EXAC_Freq : {total_freq}")

                        if an_afr == 0:
                            fre_afr = 0
                        else:
                            fre_afr = ac_afr / an_afr
                        freq_afr_list.append(fre_afr)
                        (f"FREQUENCY_AFR : {fre_afr}")

                        if an_amr == 0:
                            fre_amr = 0
                        else:
                            fre_amr = ac_amr / an_amr
                        freq_amr_list.append(fre_amr)
                        (f"FREQUENCY_AMR : {fre_amr}")

                        if an_eas == 0:
                            fre_eas = 0
                        else:
                            fre_eas = ac_eas / an_eas
                        freq_eas_list.append(fre_eas)
                        (f"FREQUENCY_EAS : {fre_eas}")

                        if an_fin == 0:
                            fre_fin = 0
                        else:
                            fre_fin = ac_fin / an_fin

                        freq_fin_list.append(fre_fin)
                        (f"FREQUENCY_FIN : {fre_fin}")

                        if an_nfe == 0:
                            fre_nfe = 0
                        else:
                            fre_nfe = ac_nfe / an_nfe
                        freq_nfe_list.append(fre_nfe)
                        (f"FREQUENCY_NFE : {fre_nfe}")

                        if an_oth == 0:
                            fre_oth = 0
                        else:
                            fre_oth = ac_oth / an_oth
                        freq_oth_list.append(fre_oth)
                        (f"FREQUENCY_OTH : {fre_oth}")

                        if an_sas == 0:
                            fre_sas = 0
                        else:
                            fre_sas = ac_sas / an_sas
                        freq_sas_list.append(fre_sas)
                        (f"FREQUENCY_SAS : {fre_sas}")

                    else:
                        all_freq_list.append('.')
                        freq_afr_list.append('.')
                        freq_amr_list.append('.')
                        freq_eas_list.append('.')
                        freq_fin_list.append('.')
                        freq_nfe_list.append('.')
                        freq_oth_list.append('.')
                        freq_sas_list.append('.')

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
                                            clinical_condition = clinical_condition = clinvar['rcv'][0]['conditions'][0]['name']
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
                                            clinical_condition =  clinvar['rcv']['conditions'][0]['name']
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
                        variant_id_list.append('.')
                        variant_type_list.append('.')
                        allele_id_list.append('.')
                        cytoband_list.append('.')
                        clin_interpretation_list.append('.')
                        clin_condition_list.append('.')
                        allelic_origin_list.append('.')
                        review_status_list.append('.')
                        identifier_list.append('.')
            if all_freq_list[0]!='.':
                all_freq_list[0]=round(all_freq_list[0],4)
            if freq_afr_list[0]!='.':
                freq_afr_list[0]=round(freq_afr_list[0],4)
            if freq_amr_list[0]!='.':
                freq_amr_list[0]=round(freq_amr_list[0],4)
            if freq_eas_list[0]!='.':
                freq_eas_list[0]=round(freq_eas_list[0],4)
            if freq_fin_list[0]!='.':
                freq_fin_list[0]=round(freq_fin_list[0],4)
            if freq_nfe_list[0]!='.':
                freq_nfe_list[0]=round(freq_nfe_list[0],4)
            if freq_oth_list[0]!='.':
                freq_oth_list[0]=round(freq_oth_list[0],4)
            if freq_sas_list[0]!='.':
                freq_sas_list[0]=round(freq_sas_list[0],4)

        except Exception as es:
            (es)
            self.error_str = es

        self.root = root
        self.root.title('ALL window')
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
        title = Label(frame1, text="VCESS Retrieving Data from ALL DATABASES", font=("Times New Roman", 30, "bold", "italic"),
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
        def shift():
            x1, y1, x2, y2 = canvas.bbox("marquee")
            if (x2 < 0 or y1 < 0):  # reset the coordinates
                x1 = canvas.winfo_width()
                y1 = canvas.winfo_height()//4
                canvas.coords("marquee", x1, y1)
                canvas.focus()
            else:
                canvas.move("marquee", -2, 0)
            canvas.after(1200 // fps, shift)

            ############# Main program ###############

        canvas = Canvas(self.frametwo, bg='white', highlightthickness=0)

        text = canvas.create_text(0, -2000,
                                  text=f'ALL is retrieving data from all the Databases'
                                       f'  Clinvar , dbSNP , dbNSFP , ExAC , InterVar , RefGene , EnSemble',
                                  font=('Times New Roman', 14, 'italic'), fill='black',
                                  tags=("marquee",), anchor='w')
        x1, y1, x2, y2 = canvas.bbox("marquee")
        canvas.place(x=90, y=70, width=1150, height=200)
        fps = 12  # Change the fps to make the animation faster/slower
        shift()
        rough = Label(self.frametwo,
                      bg='white')
        rough.grid(padx=1600, pady=600)
        (f"varaimbnmhgdsljkfghhhdjgfhhjdkbndfgfdffdjfbdf{len(variant_type_list)}")
        (len(Id))
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                self.root.destroy()
            self.root.protocol("WM_DELETE_WINDOW", on_closing)
        total_idz= Label(self.frametwo, text='Total IDs:', font=("Times New Roman", 14,'bold'),
                         bg='white', fg='black')
        total_idz.place(x=60, y=65)
        total_idz= Label(self.frametwo, text=" "+str(len(vcf)), font=("Times New Roman", 14),
                         bg='white', fg='black')
        total_idz.place(x=200, y=65)
        idz_p= Label(self.frametwo, text='IDs Processed:', font=("Times New Roman", 14,'bold'),
                     bg='white', fg='black')
        idz_p.place(x=60, y=85)
        idz_p= Label(self.frametwo, text=' '+str(len(variant_type_list)), font=("Times New Roman", 14),
                     bg='white', fg='black')
        idz_p.place(x=200, y=85)
        try:
            if len(variant_type_list) == len(Id) :

                table1 = LabelFrame(self.frametwo, text=
                "Retrieved Data (Genomic Version HG_38)",
                                    font=('Times New Roman', 16, 'bold'),bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
                table = ttk.Treeview(table1, height="30")  #################

                table['columns'] = ['ID',
                                    'rsID',
                                    'Sift_Pred',
                                    'Sift_Score',
                                    'Sift_converted_rankScore',
                                    'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred',
                                    'Polyphen2_HVAR_Score',
                                    'LRT_Pred',
                                    'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred',
                                    'Mutation_Assessor_Score',
                                    'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score',
                                    'MutationTaster_converted_rankscore',
                                    'Provean_Pred',
                                    'Provean_Score',
                                    'Provean_Rank_score',
                                    'DANN Score',
                                    'Fathmm_Pred',
                                    'Fathmm_Score',
                                    'fathmm_Rank_Score',
                                    'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore',
                                    'MetaSVM_Pred',
                                    'MetaSVM_Score',
                                    'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred',
                                    'MetaLR_Score',
                                    'MetaLR_Rank_Score',
                                    'Integrated_fitCons_score',
                                    'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS',
                                    'GERP++_RS_Rankscore',
                                    'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score',
                                    'CADD_Phred',
                                    'genoCanyon_score',
                                    'genoCanyon_rankscore',
                                    "Eigen_Raw_coding",
                                    "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                                    'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                                    'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                                    'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                                    'ensGene.GeneId','refGene.GeneName']

                table.column('#0', width=120, minwidth=25)
                table.column('ID', anchor=W, width=120)
                table.column('rsID', anchor=W, width=120)
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
                table.column('GTEx_tisuue', anchor=W, width=120)
                table.column('EXAC_All_Freq', anchor=W, width=120)
                table.column('EXAC_Afr_Freq', anchor=W, width=120)
                table.column('EXAC_Amr_Freq', anchor=W, width=120)
                table.column('EXAC_Eas_Freq', anchor=W, width=120)
                table.column('EXAC_Fin_Freq', anchor=W, width=120)
                table.column('EXAC_Nfe_Freq', anchor=W, width=120)
                table.column('EXAC_Oth_Freq', anchor=W, width=120)
                table.column('EXAC_Sas_Freq', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Cytogenic_Location', anchor=CENTER, width=120)
                table.column('ensGene.GeneId', anchor=W, width=200)
                table.column('refGene.GeneName', anchor=W, width=200)


                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='rsID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)
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
                table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
                table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
                table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
                table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
                table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
                table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
                table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
                table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
                table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)
                table.heading('refGene.GeneName', text='refGene.GeneName', anchor=W)
                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i],rsid_list[i], sift_pred[i],
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
                                         GTEx_tissue[i], all_freq_list[i],
                                         freq_afr_list[i],
                                         freq_amr_list[i],
                                         freq_eas_list[i],
                                         freq_fin_list[i],
                                         freq_nfe_list[i],
                                         freq_oth_list[i],
                                         freq_sas_list[i],
                                         variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i],
                                         geneIds[i],geneName[i])
                                 )
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
            elif len(variant_type_list) != len(Id) and (len(variant_type_list)!=0):

                table1 = LabelFrame(self.frametwo, text=
                "Retrieved Data (Genomic Version HG_38)",
                                    font=('Times New Roman', 16, 'bold'),bg='white')  ################
                table1.grid(padx=0, pady=0)
                table1.place(x=int(width / 2) - 550, y=180, width=1100, height=420)###################
                table = ttk.Treeview(table1, height="30")  #################

                table['columns'] = ['ID',
                                    'rsID',
                                    'Sift_Pred',
                                    'Sift_Score',
                                    'Sift_converted_rankScore',
                                    'Polyphen2_HDIV_Pred',
                                    'Polyphen2_HDIV_Score',
                                    'Polyphen2_HVAR_Pred',
                                    'Polyphen2_HVAR_Score',
                                    'LRT_Pred',
                                    'LRT_Score',
                                    'LRT_converted_rankScore',
                                    'Mutation_Assessor_Pred',
                                    'Mutation_Assessor_Score',
                                    'Mutation_Assessor_rankscore',
                                    'Mutation_Taster_Pred',
                                    'Mutation_Taster_Score',
                                    'MutationTaster_converted_rankscore',
                                    'Provean_Pred',
                                    'Provean_Score',
                                    'Provean_Rank_score',
                                    'DANN Score',
                                    'Fathmm_Pred',
                                    'Fathmm_Score',
                                    'fathmm_Rank_Score',
                                    'Fathmm-mkl_Pred',
                                    'Fathmm-mkl_Score',
                                    'Fathmm-mkl_RankScore',
                                    'MetaSVM_Pred',
                                    'MetaSVM_Score',
                                    'Meta_SVM_Rank_Score',
                                    'MetaLR_Pred',
                                    'MetaLR_Score',
                                    'MetaLR_Rank_Score',
                                    'Integrated_fitCons_score',
                                    'Integrated_confidence_value',
                                    'Integrated_fitcons_rankscore',
                                    'GERP++_RS',
                                    'GERP++_RS_Rankscore',
                                    'Siphy_29way_logOdds',
                                    'siphy_29way_logOdds_rankscore',
                                    'Revel_Score',
                                    'CADD_raw_score',
                                    'CADD_Phred',
                                    'genoCanyon_score',
                                    'genoCanyon_rankscore',
                                    "Eigen_Raw_coding",
                                    "Eigen-pc_Raw_coding",
                                    'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way',
                                    'phylo30rankscore',
                                    'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist',
                                    'phastcons17rankscore', 'phastcons30waylist',
                                    'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue',
                                    'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq',
                                    'EXAC_Nfe_Freq', 'EXAC_Oth_Freq',
                                    'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance',
                                    'Clinical_Condition',
                                    'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location',
                                    'ensGene.GeneId','refGene.GeneName']

                table.column('#0', width=120, minwidth=25)
                table.column('ID', anchor=W, width=120)
                table.column('rsID', anchor=W, width=120)
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
                table.column('GTEx_tisuue', anchor=W, width=120)
                table.column('EXAC_All_Freq', anchor=W, width=120)
                table.column('EXAC_Afr_Freq', anchor=W, width=120)
                table.column('EXAC_Amr_Freq', anchor=W, width=120)
                table.column('EXAC_Eas_Freq', anchor=W, width=120)
                table.column('EXAC_Fin_Freq', anchor=W, width=120)
                table.column('EXAC_Nfe_Freq', anchor=W, width=120)
                table.column('EXAC_Oth_Freq', anchor=W, width=120)
                table.column('EXAC_Sas_Freq', anchor=W, width=120)
                table.column('Variant_ID', anchor=W, width=120)
                table.column('Clinical_Type', anchor=CENTER, width=120)
                table.column('Allelic_ID', anchor=CENTER, width=120)
                table.column('Clinical_Significance', anchor=CENTER, width=120)
                table.column('Clinical_Condition', anchor=CENTER, width=120)
                table.column('Allelic_Origin', anchor=CENTER, width=120)
                table.column('Review_Status', anchor=CENTER, width=120)
                table.column('Clinical_identifier', anchor=CENTER, width=120)
                table.column('Cytogenic_Location', anchor=CENTER, width=120)
                table.column('InterVar',  anchor=W, width=120)
                table.column('ensGene.GeneId', anchor=W, width=200)
                table.column('refGene.GeneName', anchor=W, width=200)


                table.heading('#0', text='Serial No.', anchor=W)
                table.heading('ID', text='rsID', anchor=W)
                table.heading('rsID', text='rsID', anchor=W)
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
                table.heading('EXAC_All_Freq', text='EXAC_All_Freq', anchor=W)
                table.heading('EXAC_Afr_Freq', text='EXAC_Afr_Freq', anchor=W)
                table.heading('EXAC_Amr_Freq', text='EXAC_Amr_Freq', anchor=W)
                table.heading('EXAC_Eas_Freq', text='EXAC_Eas_Freq', anchor=W)
                table.heading('EXAC_Fin_Freq', text='EXAC_Fin_Freq', anchor=W)
                table.heading('EXAC_Nfe_Freq', text='EXAC_Nfe_Freq', anchor=W)
                table.heading('EXAC_Oth_Freq', text='EXAC_Oth_Freq', anchor=W)
                table.heading('EXAC_Sas_Freq', text='EXAC_Sas_Freq', anchor=W)
                table.heading('Variant_ID', text='Variant_ID', anchor=W)
                table.heading('Clinical_Type', text='Clinical_Type', anchor=CENTER)
                table.heading('Allelic_ID', text='Allelic_ID', anchor=CENTER)
                table.heading('Clinical_Significance', text='Clinical_Significance', anchor=CENTER)
                table.heading('Clinical_Condition', text='Clinical_Condition', anchor=CENTER)
                table.heading('Allelic_Origin', text='Allelic_Origin', anchor=CENTER)
                table.heading('Review_Status', text='Review_Status', anchor=CENTER)
                table.heading('Clinical_identifier', text='Clinical_identifier', anchor=CENTER)
                table.heading('Cytogenic_Location', text='Cytogenic_Location', anchor=CENTER)
                table.heading('InterVar', text='InterVar', anchor=W)
                table.heading('ensGene.GeneId', text='ensGene.GeneId', anchor=W)
                table.heading('refGene.GeneName', text='refGene.GeneName', anchor=W)
                for i in range(len(sift_pred)):
                    table.insert(parent='', index='end', iid=i, text=i + 1,
                                 values=(Id[i],rsid_list[i], sift_pred[i],
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
                                         GTEx_tissue[i], all_freq_list[i],
                                         freq_afr_list[i],
                                         freq_amr_list[i],
                                         freq_eas_list[i],
                                         freq_fin_list[i],
                                         freq_nfe_list[i],
                                         freq_oth_list[i],
                                         freq_sas_list[i],
                                         variant_id_list[i], variant_type_list[i], allele_id_list[i],
                                         clin_interpretation_list[i],
                                         clin_condition_list[i],
                                         allelic_origin_list[i],
                                         review_status_list[i],
                                         identifier_list[i],
                                         cytoband_list[i],
                                         geneIds[i],geneName[i])
                                 )
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
                error = Label(self.frametwo, text=f'Poor connection :(', font=("Times New Roman", 20, 'bold'),
                              bg='white',
                              fg='black')
                error.grid(padx=0, pady=0)
                error.place(x=600, y=700)

                error2 = Label(self.frametwo, text=f'Check your connection'
                                                   f'\n        Or      '
                                                   f'\nEnter values again    ', font=("Times New Roman", 12),
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

    def get_file(self):
        reverse_file = self.file[::-1]
        # (reverse_file)
        pos = reverse_file.find('/', 0)
        # (pos)
        path = reverse_file[pos + 1:]
        path = path[::-1]
        input_file_csv = path + '/input.csv'


        header =['HGVS_ID', 'Sift_Pred', 'Sift_Score', 'sift_converted_rankScore', 'Polyphen2_HDIV_Pred', 'Polyphen2_HDIV_Score', 'Polyphen2_HVAR_Pred', 'Polyphen2_HVAR_Score', 'LRT_Pred', 'LRT_Score', 'LRT_converted_rankScore', 'Mutation_Assessor_Pred', 'Mutation_Assessor_Score', 'Mutation_Assessor_rankscore', 'Mutation_Taster_Pred', 'Mutation_Taster_Score', 'MutationTaster_converted_rankscore', 'Provean_Pred', 'Provean_Score', 'Provean_Rank_score', 'DANN Score', 'Fathmm_Pred', 'Fathmm_Score', 'fathmm_Rank_Score', 'Fathmm-mkl_Pred', 'Fathmm-mkl_Score', 'Fathmm-mkl_RankScore', 'MetaSVM_Pred', 'MetaSVM_Score', 'Meta_SVM_Rank_Score', 'MetaLR_Pred:', 'MetaLR_Score', 'MetaLR_Rank_Score', 'Integrated_fitCons_score', 'Integrated_confidence_value', 'Integrated_fitcons_rankscore', 'GERP++_RS', 'GERP++_RS_Rankscore', 'Siphy_29way_logOdds', 'siphy_29way_logOdds_rankscore', 'Revel_Score', 'CADD_raw_score', 'CADD_Phred', 'genoCanyon_score', 'genoCanyon_rankscore', 'Eigen_Raw_coding', 'Eigen-pc_Raw_coding', 'phylo100way', 'phylo100wayrankscore', 'phylo17way', 'phylo17rankscore', 'phylo30way', 'phylo30rankscore', 'phastcons100waylist', 'phastcons100wayrankscore', 'phastcons17waylist', 'phastcons17rankscore', 'phastcons30waylist', 'phastcons30rankscore', 'Interpro_Domain', 'GTEx_gene', 'GTEx_tisuue', 'rsID', 'EXAC_All_Freq', 'EXAC_Afr_Freq', 'EXAC_Amr_Freq', 'EXAC_Eas_Freq', 'EXAC_Fin_Freq', 'EXAC_Nfe_Freq', 'EXAC_Oth_Freq', 'EXAC_Sas_Freq', 'Variant_ID', 'Clinical_Type', 'Allelic_ID', 'Clinical_Significance', 'Clinical_Condition', 'Allelic_Origin', 'Review_Status', 'Clinical_identifier', 'Cytogenic_Location', 'Ensemble.ID','Refgene.GeneName']
        data1=[]

        for i in range(len(sift_pred)):
            data=[]
            data.append(Id[i])
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
            data.append(rsid_list[i])
            data.append(all_freq_list[i])
            data.append(freq_afr_list[i])
            data.append(freq_amr_list[i])
            data.append(freq_eas_list[i])
            data.append(freq_fin_list[i])
            data.append(freq_nfe_list[i])
            data.append(freq_oth_list[i])
            data.append(freq_sas_list[i])
            data.append(variant_id_list[i])
            data.append(variant_type_list[i])
            data.append(allele_id_list[i])
            data.append(clin_interpretation_list[i])
            data.append(clin_condition_list[i])
            data.append(allelic_origin_list[i])
            data.append(review_status_list[i])
            data.append(identifier_list[i])
            data.append(cytoband_list[i])
            data.append(geneIds[i])
            data.append(geneName[i])
            data1.append(data)


        l1 = []
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
                  header[59]: row[59],
                  header[60]: row[60], header[61]: row[61], header[62]: row[62], header[63]: row[63],
                  header[64]: row[64],
                  header[65]: row[65],
                  header[66]: row[66], header[67]: row[67], header[68]: row[68], header[69]: row[69], header[70]: row[70],
                  header[71]: row[71], header[72]: row[72], header[73]: row[73], header[74]: row[74], header[75]: row[75]
                , header[76]: row[76],
                  header[77]: row[77], header[78]: row[78], header[79]: row[79],header[80]: row[80], header[81]: row[81]
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
