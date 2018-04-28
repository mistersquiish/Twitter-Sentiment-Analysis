################################################################################################
# File name: sort_twitter_stream                                                               #
# Author: Henry Vuong                                                                          #
# Date Modified: 4/28/2018                                                                     #
# Description: groups the parsed twitter dataset by state and lists average sentiment polarity #
################################################################################################

import csv

statesAbr = ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'de', 'fl', 'ga',
          'hi', 'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma',
          'mi', 'mn', 'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny',
          'nc', 'nd', 'oh', 'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx',
          'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

# [polarity, count]
al_count = [0.00, 0]
ak_count = [0.00, 0]
az_count = [0.00, 0]
ar_count = [0.00, 0]
ca_count = [0.00, 0]
co_count = [0.00, 0]
ct_count = [0.00, 0]
de_count = [0.00, 0]
fl_count = [0.00, 0]
ga_count = [0.00, 0]
hi_count = [0.00, 0]
id_count = [0.00, 0]
il_count = [0.00, 0]
in_count = [0.00, 0]
ia_count = [0.00, 0]
ks_count = [0.00, 0]
ky_count = [0.00, 0]
la_count = [0.00, 0]
me_count = [0.00, 0]
md_count = [0.00, 0]
ma_count = [0.00, 0]
mi_count = [0.00, 0]
mn_count = [0.00, 0]
ms_count = [0.00, 0]
mo_count = [0.00, 0]
mt_count = [0.00, 0]
ne_count = [0.00, 0]
nv_count = [0.00, 0]
nh_count = [0.00, 0]
nj_count = [0.00, 0]
nm_count = [0.00, 0]
ny_count = [0.00, 0]
nc_count = [0.00, 0]
nd_count = [0.00, 0]
oh_count = [0.00, 0]
ok_count = [0.00, 0]
or_count = [0.00, 0]
pa_count = [0.00, 0]
ri_count = [0.00, 0]
sc_count = [0.00, 0]
sd_count = [0.00, 0]
tn_count = [0.00, 0]
tx_count = [0.00, 0]
ut_count = [0.00, 0]
vt_count = [0.00, 0]
va_count = [0.00, 0]
wa_count = [0.00, 0]
wv_count = [0.00, 0]
wi_count = [0.00, 0]
wy_count = [0.00, 0]

states_count = [al_count, ak_count, az_count, ar_count, ca_count, co_count, ct_count, de_count, fl_count, ga_count, hi_count, id_count,
                il_count, in_count, ia_count, ks_count, ky_count, la_count, me_count, md_count, ma_count, mi_count, mn_count,
                ms_count, mo_count, mt_count, ne_count, nv_count, nh_count, nj_count, nm_count, ny_count, nc_count, nd_count,
                oh_count, ok_count, or_count, pa_count, ri_count, sc_count, sd_count, tn_count, tx_count, ut_count, vt_count,
                va_count, wa_count, wv_count, wi_count, wy_count]

with open('twitter_stream_data_state_polarity.csv', 'w', newline='') as csvfile:
    field_names = ['State', 'Sentiment Polarity', 'Number of Tweets']
    writer = csv.writer(csvfile)
    writer.writerow(field_names)

    with open('datasets/twitter_stream_data_parsed.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)

        for line in csv_reader:
            for state in statesAbr:
                if state in line[1]:
                    states_count[statesAbr.index(state)][0] += float(line[2])
                    states_count[statesAbr.index(state)][1] += 1

    for state_count in states_count:
        writer.writerow([statesAbr[states_count.index(state_count)], state_count[0] / state_count[1], state_count[1]])