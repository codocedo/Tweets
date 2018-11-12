import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy
import csv
from datetime import datetime
import os

access_token = "171695164-qvYd37YEbNQ97muVQWvVG79jDWa3fWdpY5vBSIh0"
access_token_secret = "gfx5j5cPCQphK1CH0FDt8wyLCAKXuHo4xvWh6q8O0C4yU"
consumer_key = "rqIrZymWbSUflLoUnE9EG4mlh"
consumer_secret = "59LkELf0ChsWx2p4TvftDEsFXEd1ofWj87i11defUfxDViPyPN"

class StdOutListener(StreamListener):

    def on_data(self, data):
        json_data = json.loads(data)
        try:
            #print(json_data["user"]["id"])
            if str(json_data["user"]["id"]) in sen_list:
                print("senador ", json_data["user"]["screen_name"], str(datetime.now()))
                senfile.write(data)
                senfile.write(",")
            elif str(json_data["user"]["id"]) in dip_list:
                print("diputado ", json_data["user"]["screen_name"], str(datetime.now()))
                dipfile.write(data)
                dipfile.write(",")
            elif str(json_data["user"]["id"]) in radio_list:
                print("radio ", json_data["user"]["screen_name"], str(datetime.now()))
                radiofile.write(data)
                radiofile.write(",")
            elif str(json_data["user"]["id"]) in diarios_list:
                print("diario ", json_data["user"]["screen_name"], str(datetime.now()))
                diariofile.write(data)
                diariofile.write(",")
            elif str(json_data["user"]["id"]) in tv_list:
                print("tv ", json_data["user"]["screen_name"], str(datetime.now()))
                tvfile.write(data)
                tvfile.write(",")
            elif str(json_data["user"]["id"]) in entity_list:
                print("entidad ", json_data["user"]["screen_name"], str(datetime.now()))
                entityfile.write(data)
                entityfile.write(",")
            elif str(json_data["user"]["id"]) in american_pres:
                print("presidente ", json_data["user"]["screen_name"], str(datetime.now()))
                presfile.write(data)
                presfile.write(",")                
                
        except KeyError as e:
            print("keyerror")
            print(data)
            pass        
        return (True)

    def on_error(self, status):
        print ('error')
        print (status)
        return (True)
    
    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 120 seconds...\n")
        time.sleep(120)
        return 
 

dip_list = ['45260729', '59804915', '752239376499929088', '166744340', '138329350', '183711223', '970857122878672896', '113110615', '155978526', '190718502', '359680242', '73381588', '18110979', '2409119084', '8434092', '155368113', '2793618401', '73981088', '308757976', '108684531', '104020962', '35000699', '1546866276', '525351120', '889304496253411328', '1512131472', '121253418', '56496839', '614452720', '102282367', '485720647', '57454967', '114838214', '329052979', '45214422', '66854685', '857761375929720832', '155678724', '306855847', '123902747', '154162544', '995143896', '846044575', '171933591', '148565399', '157853001', '259877309', '2537874007', '934521405311520770', '134346453', '107135941', '60835171', '169979854', '1267420831', '612883967', '351810153', '16428200', '77518799', '3246575662', '66291168', '59215690', '785401112', '1381789998', '1043637876', '188696357', '32864397', '1265818322', '229885349', '908519111864586240', '501456046', '616320997', '36505058', '131572617', '157480943', '3011590957', '66467370', '68051319', '367555950', '2361621830', '146588209', '959168148971892736', '571922938', '183768090', '14989742', '294908394', '153585302', '66426560', '84084223', '909960007151702016', '364441111', '1678554043', '1708387596', '982311836061085696', '1121791488', '75895791', '986418323511537664', '2810502513', '118455518', '1946865918', '264957110', '187235091', '108323686', '974651202', '4870088037', '231456469', '317515432', '157831773', '1700707573', '17317080', '2424001080', '904935222818607104', '209312944', '762969810', '359670144', '83852863', '44655788', '41903524', '2385854972', '34359402', '38028428', '307483484', '1127999166', '906040111', '774654348', '109569196', '58835918', '71949243', '61943296', '145692764', '155226692', '703598448398958592', '147701898', '812001264699666432', '259360713', '49512526', '282313940', '404633650', '103871286', '1356808836', '970698154516647936', '225445834', '39157375', '1928056476', '308053862', '317843834', '101236994', '31346901', '103259570', '61524459', '2749212142']
sen_list = ['67038807', '58946189', '324641657', '153468046', '2497164414', '300968556', '41381528', '55371269', '64728588', '2691975879', '221784312', '107993838', '808760162521673729', '1002439081', '62339596', '16970297', '14050989', '1248064796', '19294551', '375248010', '760574472340504576', '16193496', '53594117', '847488627303038976', '47611358', '364461517', '67064132', '392816498', '38550531', '118507160', '185748219', '1048417952', '277470477', '807332644178509824', '2730306924', '903281780836503552', '76683098', '1224922255', '27516672', '166398735', '846461748450353162', '193969186', '49624549']
tv_list = ['2398056092', '93670805', '280504296', '231487327', '3305693667', '2702196288', '177322353', '887909418', '354067724', '887909418', '293014181', '68613067', '203169382', '887642491', '566647189', '1194815954', '87713880', '14639357', '899813334', '1881282924', '78707252', '103929561', '135527838', '3023222109', '2952276075', '3300578855', '348072620', '119998638', '104372454', '138476413', '31143885', '267243319', '172150872', '306992050', '118536654', '31220949', '2761000237', '371919782', '121492943', '13444362', '137360042', '106502630', '34918118', '58048133', '124266832', '159262912', '216436927', '24952459', '573851583', '18248645', '141290643', '418660662', '90227660', '103074420', '148815636', '2416739635', '16727770', '103856339', '85879198']
radio_list = ['2885710342', '70801596', '2677493467', '3008474877', '470292536', '2415939662', '148962339', '68052486', '23628399', '93319559', '197974623', '1457979985', '2521371896', '141657174', '119467253', '35443964', '2521389162', '2521351513', '555538558', '237437716', '100507173', '272491331', '108928107', '1559703397', '304495656', '1269890402', '179382952', '119749137', '256720636', '154795790', '96170873', '71758708', '2538319788', '302869801', '165172683', '191259078', '911202956', '3313602933', '4895685226', '208194154', '2317096874', '2410034275', '2282690827', '2975482133', '77031473', '525611257', '617723021', '394250019', '2284113907', '2184717145', '547253373', '190362687', '205233965', '264284870', '2364515366', '1241464651', '85391199', '222918559', '497890453', '414279180', '599728125', '186473534', '4054911947', '86175173', '88124686', '42961651', '31622299', '2341042274', '70402722', '2870734037', '52987236', '2291115103', '142051473', '32159476', '2149905151', '561153386', '31119751', '66444776', '2785363596', '4830741411', '1020608389', '197284090', '260267935', '104897125', '98656985', '328087469', '1901416477', '329226517', '49504744', '2279152147', '561172728', '84662879', '1655707094', '87436248', '4352727743', '2350741602', '2516988265', '265077582', '4740104061', '118028300', '329062635', '66858213', '151591171', '2600369461', '293686835', '78615081', '275302961', '35797284', '1284824022', '61502960', '1360829396', '407885646', '330350945', '1732804626', '2298733375', '31414330', '64920071', '1383952194', '614359915', '162168596', '389658450', '329062635', '69398919', '1420686781', '90066526', '105805184', '389403715', '377613495', '712461361272528897', '412277736', '108162173', '96557366', '262886585', '194474304', '334025276', '3419061015', '500834329', '2383314098', '1250447508', '726818973589880832', '87266031', '3138830723', '473365342', '1367360672', '151591171', '3396536837', '2319417618', '100312735', '2840772201', '76954333', '82235027', '135257234', '1305304615', '3366136475', '205262805', '240283871', '67033747', '221553347', '263197210', '123950722', '338664385', '62881300', '243269745', '609640782', '262140415', '1360085820', '359636047', '264407627', '753971863', '4850578846', '934655342', '97344291', '146822489', '224019390', '193501118', '122040313', '3889843887', '86224931', '105902504', '742892941', '106106673', '778862550', '794498749', '99987369', '1938757908', '300523227', '2157496285', '110407997', '162850350', '2386626860', '43537552', '134319701', '137825516', '109692058', '444707072', '51588728', '124881337', '66858213', '258764308', '555270956', '736220331350884353', '249330628', '1449874250', '163262830', '203752612', '145688708', '447147073', '145270013', '52654349', '1925487204', '176627249', '132172524', '2482949222', '61058216', '324447694', '1129174369', '133534960', '478722762', '186473534', '1129064684', '237299699', '41165047', '17492582', '201493641', '403657900', '241118260', '1215906541', '36409216', '7668952', '140123901', '237299699', '14638581', '3129768538', '14227292', '506423891', '89200813', '119535717']
entity_list = ['60912608', '418660662', '3352054948', '2377129326', '1092040621', '335436884', '140583083', '518787221', '320895582', '238162336']
diarios_list = ['239523012', '63245463', '298182062', '43269244', '752031402', '102720264', '18047052', '61812299', '303504845', '71684838', '93650544', '76781811', '58825137', '279112647', '3613151117', '98952456', '64751347', '51454933', '31285449', '1855220132', '90426711', '40603936', '34302005', '268961765', '627504083', '77308998', '404487799', '133005292', '77268837', '1327230120', '323247028', '284533961', '204871085', '2443267969', '239534277', '2935534450', '2699217710', '104389738', '844183753', '420592061', '63805938', '146087611', '167132271', '3223771', '10283902', '87769317', '3222731', '2788203272', '54115409']
american_pres = ['24900072', '720786569792253952', '48040416', '2670726740', '131574396', '39591928', '149827409', '4119914644', '13623532', '248760009', '1301761278', '61097151', '64839766', '26883683', '18804414', '524571803', '1669631264', '35485571', '209780362', '913131817', '148776931', '111124731', '282736335', '90978338', '1691434632', '96461487', '277096408', '58244743', '166669818', '144376833', '2897441', '340599928', '199112323', '250265046', '216457140', '361445173', '465983898', '151190865', '46485425', '4825296327', '475988505', '1330457336', '813286', '25073877', '822215679726100480', '1252764865']

full_list = american_pres + diarios_list + entity_list + radio_list + tv_list + sen_list + dip_list

if __name__ == '__main__':
    senfile = open("tweets/senfile.txt","a")
    if os.path.getsize("tweets/senfile.txt") == 0:
        senfile.write("[")
    dipfile = open("tweets/dipfile.txt","a")
    if os.path.getsize("tweets/dipfile.txt") == 0:
        dipfile.write("[")
    radiofile = open("tweets/sradiofile.txt","a")
    if os.path.getsize("tweets/sradiofile.txt") == 0:
        radiofile.write("[")
    tvfile = open("tweets/stvfile.txt","a")
    if os.path.getsize("tweets/stvfile.txt") == 0:
        tvfile.write("[")
    diariofile = open("tweets/diariofile.txt","a")
    if os.path.getsize("tweets/diariofile.txt") == 0:
        diariofile.write("[")
    entityfile = open("tweets/entityfile.txt","a")
    if os.path.getsize("tweets/entityfile.txt") == 0:
        entityfile.write("[")
    presfile = open("tweets/presfile.txt","a")
    if os.path.getsize("tweets/presfile.txt") == 0:
        presfile.write("[")
    try:
	    while True:
	        try:
	            l = StdOutListener()
	            auth = OAuthHandler(consumer_key, consumer_secret)
	            auth.set_access_token(access_token, access_token_secret)
	            stream = Stream(auth, l)
	            stream.filter(full_list)

	        except tweepy.TweepError as e:
	            print(e)
	            pass
	        
	        except Exception as e:
	            print(e)
	            pass
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        dipfile.close()
        radiofile.close()
        tvfile.close()
        diariofile.close()
        entityfile.close()
        presfile.close()
