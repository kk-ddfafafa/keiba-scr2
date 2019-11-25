from django.shortcuts import render
import pandas as pd
from django.template.defaulttags import register
csv_path='C:/k-ba/keiba_nouryoku.csv'

# Create your views here.
def main_func(request):
    bamei_dict={};nouryoku_dict = {};agasan_dict={};ave3_dict={};nouryoku_hensati_dict ={};agari_hensati_dict={};pre_time_dict={}
    df = pd.read_csv(csv_path)
    if request.method == 'POST':
        posted_day = request.POST['day']
        posted_month = request.POST['month']
        posted_year = request.POST['year']
        posted_course = request.POST['course']
        posted_race = request.POST['race']
        raceid=str(posted_year)+str(posted_month)+str(posted_day)+posted_course+posted_race
        raceid = int(raceid)
        if any(df['race_id'] == raceid):
            df2 = df[df['race_id'] == raceid]
        else:
            return render(request, 'main-sisuu.html')
        bamei = df2.iloc[0][2:20].values.tolist()
        nouryoku = df2.iloc[0][20:38].values.tolist()
        agasan = df2.iloc[0][38:38+18].values.tolist()
        ave3 = df2.iloc[0][56:56+18].values.tolist()
        #nouryoku_bunsanとagari_bunsanは省略
        nouryoku_hensati = df2.iloc[0][76:76+18].values.tolist()
        agari_hensati = df2.iloc[0][94:94+18].values.tolist()
        pre_time = df2.iloc[0][112:112+18].values.tolist()
        for d in range(0,18):
            if bamei[d] != bamei[d]:
                continue
            bamei_dict[d+1] = bamei[d]
            nouryoku_dict[d+1] = nouryoku[d]
            agasan_dict[d+1] = agasan[d]
            ave3_dict[d+1] = ave3[d]
            nouryoku_hensati_dict[d+1] = nouryoku_hensati[d]
            agari_hensati_dict[d+1] = agari_hensati[d]
            pre_time_dict[d+1] = pre_time[d]
        return render(request,'nouryoku.html',{'bamei':bamei_dict,
                                                   'nouryoku':nouryoku_dict,
                                                   'nouryoku_hensati':nouryoku_hensati_dict,
                                               'agari':agasan_dict,
                                               'agari_hensati':agari_hensati_dict,
                                               'yosou_time':pre_time_dict,
                                                   })


    return render(request,'main-sisuu.html')

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)