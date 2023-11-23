from flask import Flask, jsonify, request
import random
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import requests

app = Flask(__name__)

tweets_list = ["when modi promised minimum government maximum governance expected him begin the difficult job reforming the state why does take years get justice state should and not business and should exit psus and temples", "talk all the nonsense and continue all the drama will vote for modi ", "what did just say vote for modi  welcome bjp told you rahul the main campaigner for modi think modi should just relax", "asking his supporters prefix chowkidar their names modi did great service now there confusion what read what not now crustal clear what will crass filthy nonsensical see how most abuses are coming from chowkidars", "answer who among these the most powerful world leader today trump putin modi may ", "kiya tho refresh maarkefir comment karo ", "surat women perform yagna seeks divine grace for narendra modi become again", "this comes from cabinet which has scholars like modi smriti and hema time introspect", "with upcoming election india saga going important pair look current modi leads govt elected with deal brexit combination this weekly looks juicy bears imho ", "gandhi was gay does modi  ", "things like demonetisation gst goods and services tax…the upper castes would sort either view favourably say that need give this more time other castes like dalits the muslims were more against because that’ just not modi’ constituency2", "hope tuthukudi people would prefer honest well behaved nationalist courageous likly minister modi cabinet vote benifit thuthukudi ", "calm waters wheres the modi wave ", "one vote can make all the difference anil kapoor answers modis election 2019 clarion call extends support his vote kar campaign ", "one vote can make all the difference anil kapoor answers modis election 2019 clarion call extends support his campaign ", "vote such party and leadershipwho can take fast and firm action none other than narendra damodardas modi and bjp party ", "vote modi who has not created jobs", "through our vote ensure govt need and deserve anupam kher responds modis appeal for the 2019 elections ", "dont play with the words was talking about the modi swamy relation guru saying what good and chowkidar protecting the good mind you tweeted dark side terrorism there any brighter side you better know there any", "didn’ write chowkidar does mean ’ anti modi try visit the plz not all who haven’ used are anti ", "was the one who recently said that people who vote against modi are anti national that put gen hooda all congress supporters and those jawans who not support modi anti national what great things did you hear about him", "with firm belief the leadership shri narendra modi bjp entering into politics given form file nomination for the khammam parliamentary seat proceeding khammam today ", "crush jaws those who shoutmodimodi says jds mla this inciting murder", "sultanpur uttar pradesh loksabha candidate select pawan kumar pandey actually public want given vote modi but your current condidate not popular district your candidate bsp candidate sonbhadra singh", "thiugh nehru not alive but still alive heart modi for every failure nehru responsible ", 
"development has become mass movement under modi govt with economic social and political empowerment life one and all has witnessed positive paradigm shift this new india", "has already taken notice and ordered probe now time for modi take notice muslim family being harassed beaten recently extremist hindus and was suggested leave india move pakistan", "was waiting for this modi will also talk about varanasi", "according yogi imran masood kin azhar masood according this logic nirav modi lalit modi and narendra modi are brothers from the same mother", "agree but only during the tenure modiganga rejuvenation works have started working", "the three codes modi cracked give india huge foreign policy jumpstart via ", "through our vote ensure govt need and deserve anupam kher responds modis vote kar appeal for the 2019 elections ", "modi govts slashing indias education budget clear indicator that they dont care for indias future congress president shri the other hand has ensured the increase the budget gdp this the future india deserves ", "being born religion where female deities worshipped its misogynistic sadistic tradition and totally against point isits man made tradition and not written one not religious lunatic support own religion its repressive", "how such people are being made amazedn fear that frustation him may not result vote against sir waste ministerdisgrace entire modi cabinet ", "only modi ", "check out latest article premier archery league via ", "india second most optimistic globally about executive job growth shows the survey indias senior executives said that they are optimistic about the growth the number job roles this year ", "people wish your vision india and least interested about your personal enmity with modi others its your personal problem handle this personally and dont expect nation will join your dirty fight with others tell why vote ", "modi for eternal what wrong dear sirji perfectly fine with indian people", "impressive godrej tata complimenting our hoping gets second term ", "our maid saying this rahul keeps saying modi kalla yet goes and hugs him and winks magand idu bekagittu", "please vote for modi congress trying divide india", "yes good job highly insensitivearrogant incompetent ploar needs defeated any costnobody knows why made such arrogant person minister gave tickethe out touch with grounddespite 3months upsc protests nvr met ", "before 2014 hindustan has seen the worst for hindus own maj hindu rashtra who thrashed the rascal faces these anti indian politiciansantinationals urban naxals wait watch after modis win pakistan mein bhi hindu hona garv baat hogi✌", "higher voting turnout directly proportional bjp victory wonder modi has launched campaigns like dont sit home ensure everyone your friends family relatives votes its now never for ", "modi govt has done remarkable job making corruption free india ultimate success shall achieved when corrupt are jailed modi govts vision corruptionfree india ensuring that all those who looted the country are now facing the law via namo app", "use this beg for campaign ", "with welfare delivery gst ibc and feo place modi can exit psus 2nd term and use that money appoint more judges police forensic labs and fasttrack delivery justice education and healthcare citizens and invest defence india well", "this the new india modi trying build with these leaders his party why have live with these deplorable characters ", "overpromise and underdelivery – that pithy summary the economic outcome the last five years under approach the general election","not just healing touch india need surgery remove the cancer spread modi and rss", "farmers’ welfare about 474 farmers get second installment from next month the centre announced the 75000crore scheme ", "mistry man not then why drag modi the nri followers this the man wrong action should taken against him for spreading hatred please don’ have agenda condemning criminal activities sir fyi please", "think you forgot dollar india handled exceptionally well and one the diplomatic shrewdness and achievement why you always undermine modi government you are always prone criticise even without considering other aspects", "entrepreneurs are rising india after modi govt created system for them took care their tax concerns and created infra for them incubate well never happened congress you guys just want power sit and shit its simple for you", "nothing else its modi phobia", "itna fark  ", "once again modi government modi govts efforts last years governance reforms have been institutionalise honesty way that every system and institution designed inculcate well inspire honesty", "all are with you sir namo again jai hind jai modimuje puri bharat janta par vishwas hai sir aap hamre prime minister honge for our future our country future you must our prime minister again and again bjp", "anchor doing canvas against modi not fit for journalism", "slams makers biopic for deliberately using name the credit ", "will these channels say modi also scared contests from two seats even propoganda needs little decency", 
"this new india this indias century because has the yuva shakti take great heights modi govt stands firmly with them via namo app", "100 sure sir will inform all family and friends give record numbers vote modi sir and bjp thanks", "you will loose your existance election rafel corruption free and scam free all nation know the nature except narendra modi and bjp all party scammer aap nautanki baj", "‘concierge’ for super rich makes unusual sight nirav modis hearing via ", "’ confused who said that intellectuals should decide modi’ policies the question was which intellectuals sided with modi and similarly there’ those who’ disagree with his policies too where’ the question deciding anything", "asked learn from how treat minority well does want what did minor ", "for new india can vote for shri narendra modi ", "modi govts years are over just cheating people promises has impacted lot things from the economy the country brotherhood the nation ", "what your logic sircould you please throw some light the logic behind your tweet that bjpnda will lose modi fights from bengaluru south", "not modi then who from opposition opposition leaders intent clear but dont understand why they are failing their attempt why not vote for modi they are not telling people what they will when come into power", "modi great his opponents generally are selfish idiots who keep attacking his governance skill modi doing great for 3040 yrs you tell what will you give oppo know after years modi rule that can wonders this stupid world created dishonest", "can pit more pictures and videos hindu extremist crime just years but use coz ppl are taken over storm modi and rss terror", "vote kar narendra modi appeals everyone during tweetstorm ", "modi mother elected more khans would killed ", "last time you paid loan some entrepreneurs named vijay maalya and nirav modi whose number this time please check next list", "rahul doesnt make false promises like modi has always delivered whatever has been promised you may check his track record you can count him ", "kitna jalte tum modi your tweet shows your jealousy towards our great prime minister modi ", "centre state govts working together make india tbfree 2025 ", "where ever rgis going through out the length breadth the country such the reception for him masses india just love him modi all other leaders bjp are just match", "mad sandip singh have some sense javed akhtar could have called narendra modi producer sandip ssingh credit row entertainment news the indian express ", "thanks modi porn sites are banned", "did modi eat beef biryani and sleep asaduddin owaisi ", "voted for modi last time but never again economy screwed hate ideology being propagated need not rahul but any one other than modi the next few weeks will tell there way bjp will get majority the propagandas only social media", "congress fed biryani terrorists modi government fed them bullets and bombs yogi adityanath ", "open your eyes not see any critic modi cong exculding these mongers there vast indai like called bharat modis concern security praise worthy but his autocratic norm denying each and every allegation like kimjong its painful sorrowful too regards", "requesting all stop using services they are giving favor big people like vijay malya nivav modi and taking money from all like nonscene charges", "this face doesn’ haunt you condemn the abduction girls but they’ alive and wel also recorded message still our personally ordered action unlike modi who treats muslims just vote bank", "sharam karodesh ghotale bech khaega tumhara just because modi youth have taken interest political issues youth are better judge the right and wrong ", "dont forget petrol prices have risen ₹ modi government when gulf prices were going down ाेशबचा ", "thought petta was the most antibjp movie recent times  ", "election live blog met sapna choudhary yesterday want her campaigning for manoj tiwari", "superbly summarizedjai hind vande mataramagain modi sarkar ", "country prospers when the women the country are leading the forefront are supported every endeavour their lives modi govt focussed policies where women have been enabled with the power empower themselves and the nation via namo app", "sabbash mera vote for peppermit abvp", "yogi adityanath hold 100 rallies seek votes for narendra modi amit shah ", "from the very beginningmodi doing wada faramoshi you dont believe take example used say giving lakhs every indian and after years governance failed fulfill his promise ", "modi politics hate modiji loves india modiji want make new india corruption free terror free india hate not nature modiji yes modiji hates only enemies our country terrorists destroying terrorists camp hatedont defame our humane kind pure honest"]

@app.route('/tweets', methods=['POST'])
def get_tweets():
    data = request.get_json()
    querynumbr = data.get('querynumbr', 1)
    random_tweets = random.sample(tweets_list, min(querynumbr, len(tweets_list)))
    return jsonify({"tweets": random_tweets})


if __name__ == '__main__':
    app.run(host='localhost', port=5001, debug=True)
