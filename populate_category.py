import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','wonderland.settings')
import django
django.setup()
from category.models import Category, Page

def populate():
    europe_pages = [{
        'name':'Stonehenge',
        'rate':'9.89',
        'intro':"Stonehenge is a prehistoric monument in Wiltshire, England, two miles (3 km) west of Amesbury. It consists of a ring of standing stones, each around 13 feet (4.0 m) high, seven feet (2.1 m) wide, and weighing around 25 tons. The stones are set within earthworks in the middle of the most dense complex of Neolithic and Bronze Age monuments in England, including several hundred tumuli (burial mounds).",
    },{
        'name':'Colosseum',
        'rate':'9.89',
        'intro':"The Colosseum or Coliseum, also known as the Flavian Amphitheatre, is an oval amphitheatre in the centre of the city of Rome, Italy. Built of travertine limestone, tuff (volcanic rock), and brick-faced concrete,[1] it was the largest amphitheatre ever built at the time and held 50,000 to 80,000 spectators. The Colosseum is situated just east of the Roman Forum. Construction began under the emperor Vespasian in AD 72[2] and was completed in AD 80 under his successor and heir, Titus.[3] Further modifications were made during the reign of Domitian (81–96).[4] These three emperors are known as the Flavian dynasty, and the amphitheatre was named in Latin for its association with their family name (Flavius). ",
    },{
        'name':'Alhambra',
        'rate':'9.89',
        'intro':"The Alhambra is a palace and fortress complex located in Granada, Andalusia, Spain. It was originally constructed as a small fortress in AD 889 on the remains of Roman fortifications, and then largely ignored until its ruins were renovated and rebuilt in the mid-13th century by the Nasrid emir Mohammed ben Al-Ahmar of the Emirate of Granada, who built its current palace and walls. It was converted into a royal palace in 1333 by Yusuf I, Sultan of Granada.[1] After the conclusion of the Christian Reconquista in 1492, the site became the Royal Court of Ferdinand and Isabella (where Christopher Columbus received royal endorsement for his expedition), and the palaces were partially altered in the Renaissance style. In 1526 Charles I & V commissioned a new Renaissance palace better befitting the Holy Roman Emperor in the revolutionary Mannerist style influenced by humanist philosophy in direct juxtaposition with the Nasrid Andalusian architecture, but it was ultimately never completed due to Morisco rebellions in Granada. Alhambra's last flowering of Islamic palaces was built for the last Muslim emirs in Spain during the decline of the Nasrid dynasty, who were increasingly subject to the Christian Kings of Castile.",
    },{
        'name':'Hagia Sophia',
        'rate':'9.89',
        'intro':"Hagia Sophia is the former Greek Orthodox Christian patriarchal cathedral, later an Ottoman imperial mosque and now a museum (Ayasofya Müzesi) in Istanbul, Turkey. Built in AD 537 in the Middle Ages, it was famous in particular for its massive dome. It was the world's largest building and an engineering marvel of its time. It is considered the epitome of Byzantine architecture[1] and is said to have 'changed the history of architecture'.",
    },{
        'name':'Mont-Saint-Michel',
        'rate':'9.89',
        'intro':"Le Mont-Saint-Michel[1] is a tidal island and mainland commune in Normandy, France. The island[2] is located about one kilometer (0.6 miles) off the country's northwestern coast, at the mouth of the Couesnon River near Avranches and is 7 hectares (17 acres) in area. The mainland part of the commune is 393 hectares (971 acres) in area so that the total surface of the commune is 400 hectares (988 acres). With two hyphens and the French article Le ahead, because it is the name of a commune, not a hill. By far, the most famous part of the commune, known as the 'Mont Saint-Michel' or the 'Mount Saint-Michel', with only one hyphen and the name 'Mont' untied, because it precisely means the hill, a geologic element, in this case an island.",
    },{
        'name':'Venetian Arsenal',
        'rate':'9.89',
        'intro':"The Venetian Arsenal is a complex of former shipyards and armories clustered together in the city of Venice in northern Italy. Owned by the state, the Arsenal was responsible for the bulk of the Venetian republic's naval power during the middle part of the second millennium AD. It was 'one of the earliest large-scale industrial enterprises in history'. Construction of the Arsenal began around 1104, during Venice's republican era.[2][3] It became the largest industrial complex in Europe before the Industrial Revolution,[4] spanning an area of about 45 hectares (110 acres), or about fifteen percent of Venice.[2] Surrounded by a 2-mile (3.2 km) rampart, laborers and shipbuilders regularly worked within the Arsenal, building ships that sailed from the city's port.[5] With high walls shielding the Arsenal from public view and guards protecting its perimeter, different areas of the Arsenal each produced a particular prefabricated ship part or other maritime implement, such as munitions, rope, and rigging.[6] These parts could then be assembled into a ship in as little as one day.",
    },{
        'name':'Zollverein Coal Mine Industrial Complex',
        'rate':'9.89',
        'intro':"The Zollverein Coal Mine Industrial Complex is a large former industrial site in the city of Essen, North Rhine-Westphalia, Germany. It has been inscribed into the UNESCO list of World Heritage Sites since December 14, 2001, and is one of the anchor points of the European Route of Industrial Heritage. The first coal mine on the premises was founded in 1847, and mining activities took place from 1851 until December 23, 1986. For decades, starting in the late 1950s, the two parts of the site, Zollverein Coal Mine and Zollverein Coking Plant (erected 1957−1961, closed on June 30, 1993), ranked among the largest of their kinds in Europe. Shaft 12, built in the New Objectivity style, was opened in 1932 and is considered an architectural and technical masterpiece, earning it a reputation as the 'most beautiful coal mine in the world'",
    },{
        'name':'Oxford University',
        'rate':'9.89',
        'intro':"The University of Oxford is a collegiate research university in Oxford, England. There is evidence of teaching as early as 1096,[1] making it the oldest university in the English-speaking world and the world's second-oldest university in continuous operation.[1][2] It grew rapidly from 1167 when Henry II banned English students from attending the University of Paris.[1] The history and influence of the University of Oxford has made it one of the most prestigious universities in the world.[3][4] The university is a 'city university' in that it does not have a main campus; instead, colleges, departments, accommodation, and other facilities are scattered throughout the city centre. Iconic university buildings include the Radcliffe Camera, the Sheldonian Theatre used for music concerts, lectures, and university ceremonies, and the Examination Schools, where examinations and some lectures take place. The University Church of St Mary the Virgin was used for university ceremonies before the construction of the Sheldonian. Christ Church Cathedral uniquely serves as both a college chapel and as a cathedral.",
    },{
        'name':'Bolshoi Theatre',
        'rate':'9.89',
        'intro':"The Bolshoi Theatre is a historic theatre in Moscow, Russia, originally designed by architect Joseph Bové, which holds ballet and opera performances.[1] The main building of the theatre, rebuilt and renovated several times during its history, is a landmark of Moscow and Russia (its iconic neoclassical façade is depicted on the Russian 100-ruble banknote). On 28 October 2011, the Bolshoi re-opened after an extensive six-year renovation.[2] The renovation included restoring acoustics to the original quality (which had been lost during the Soviet Era), as well as restoring the original Imperial decor of the Bolshoi."
    },{
        'name':'Hermitage Museum',
        'rate':'9.89',
        'intro':"The State Hermitage Museum is a museum of art and culture in Saint Petersburg, Russia. The second-largest art museum in the world,[1][2] it was founded in 1764 when Empress Catherine the Great acquired an impressive collection of paintings from the Berlin merchant Johann Ernst Gotzkowsky. The museum celebrates the anniversary of its founding each year on 7 December, Saint Catherine's Day.[3] It has been open to the public since 1852. Its collections, of which only a small part is on permanent display, comprise over three million items (the numismatic collection accounts for about one-third of them),[4] including the largest collection of paintings in the world. The collections occupy a large complex of six historic buildings along Palace Embankment, including the Winter Palace, a former residence of Russian emperors. Apart from them, the Menshikov Palace, Museum of Porcelain, Storage Facility at Staraya Derevnya, and the eastern wing of the General Staff Building are also part of the museum. "
    },{
        'name':'Big Ben',
        'rate':'9.89',
        'intro':"Big Ben is the nickname for the Great Bell of the striking clock at the north end of the Palace of Westminster in London[1] and is usually extended to refer to both the clock and the clock tower.[2][3] The official name of the tower in which Big Ben is located was originally the Clock Tower, but it was renamed Elizabeth Tower in 2012 to mark the Diamond Jubilee of Elizabeth II. The tower was designed by Augustus Pugin in a neo-Gothic style. When completed in 1859, its clock was the largest and most accurate four-faced striking and chiming clock in the world.[4] The tower stands 315 feet (96 m) tall, and the climb from ground level to the belfry is 334 steps. Its base is square, measuring 39 feet (12 m) on each side. Dials of the clock are 23 feet (7.0 m) in diameter. Big Ben is the largest of the tower‘s five bells and weighs 13.5 long tons (13.7 tonnes; 15.1 short tons).[1] It was the largest bell in the United Kingdom for 23 years. The tower is a British cultural icon recognised all over the world. It is one of the most prominent symbols of the United Kingdom and parliamentary democracy."
    }]

    asia_pages = [{
        'name':'Mahabodhi Temple',
        'rate':'9.89',
        'intro':"The Mahabodhi Temple, a UNESCO World Heritage Site, is an ancient, but much rebuilt and restored, Buddhist temple in Bodh Gaya, marking the location where the Buddha is said to have attained enlightenment.[1] Bodh Gaya (in Gaya district) is about 96 km (60 mi) from Patna, Bihar state, India. The site contains a descendant of the Bodhi Tree under which Buddha gained enlightenment, and has been a major pilgrimage destination for Hindus and Buddhists for well over two thousand years, and some elements probably date to the period of Ashoka (died c. 232 BCE).",
    },{
        'name':'Petra',
        'rate':'9.89',
        'intro':"Petra, originally known to its inhabitants as Raqmu,[1] is a historical and archaeological city in southern Jordan. Petra lies around Jabal Al-Madbah in a basin surrounded by mountains which form the eastern flank of the Arabah valley that runs from the Dead Sea to the Gulf of Aqaba.[2] The area around Petra has been inhabited as early as 7,000 BC,[3] and the Nabataeans might have settled in what would become the capital city of their kingdom, as early as the 4th century BC.",
    },{
        'name':'Terracotta Army',
        'rate':'9.89',
        'intro':"The Terracotta Army is a collection of terracotta sculptures depicting the armies of Qin Shi Huang, the first Emperor of China. It is a form of funerary art buried with the emperor in 210–209 BCE with the purpose of protecting the emperor in his afterlife. The figures, dating from approximately the late third century BCE,[1] were discovered in 1974 by local farmers in Lintong County, outside Xi'an, Shaanxi, China. The figures vary in height according to their roles, with the tallest being the generals. The figures include warriors, chariots and horses. Estimates from 2007 were that the three pits containing the Terracotta Army held more than 8,000 soldiers, 130 chariots with 520 horses, and 150 cavalry horses, the majority of which remained buried in the pits near Qin Shi Huang's mausoleum.[2] Other terracotta non-military figures were found in other pits, including officials, acrobats, strongmen, and musicians.",
    },{
        'name':'Apadana',
        'rate':'9.89',
        'intro':"The Apadana was the largest building on the Terrace at Persepolis and was excavated by the German archaeologist Ernst Herzfeld and his assistant Friedrich Krefter, and Erich Schmidt, between 1931 and 1939. Important material relevant to the excavations are today housed in the archives of the Freer Gallery of Art in Washington, DC. It was most likely the main hall of the kings. The columns reached 20m high and had complex capitals in the shape of bulls or lions. Here, the great king received the tribute from all the nations in the Achaemenid Empire, and gave presents in return. Access to the hall is given by two monumental stairways, on the north and on the east. These are decorated by reliefs, showing delegates of the 23 subject nations of the Persian Empire paying tribute to Darius I, who is represented seated centrally. The various delegates are shown in great detail, giving insight into the costume and equipment of the various peoples of Persia in the 5th century BC. There are inscriptions in Old Persian and Elamite.",
    },{
        'name':'Forbidden City',
        'rate':'9.89',
        'intro':"The Forbidden City is a palace complex in central Beijing, China. It houses the Palace Museum, and was the former Chinese imperial palace from the Ming dynasty to the end of the Qing dynasty (the years 1420 to 1912). The Forbidden City served as the home of emperors and their households and was the ceremonial and political center of Chinese government for almost 500 years. Constructed from 1406 to 1420, the complex consists of 980 buildings[1] and covers 72 hectares (over 180 acres).[2][3] The palace exemplifies traditional Chinese palatial architecture,[4] and has influenced cultural and architectural developments in East Asia and elsewhere. The Forbidden City was declared a World Heritage Site in 1987,[4] and is listed by UNESCO as the largest collection of preserved ancient wooden structures in the world.",
    },{
        'name':'Potala Palace',
        'rate':'9.89',
        'intro':"The Potala Palace is a dzong fortress in the city of Lhasa, in China's Tibet Autonomous Region. It was the winter palace of the Dalai Lamas from 1649 to 1959, has been a museum since then, and is a World Heritage Site since 1994. The palace is named after Mount Potalaka, the mythical abode of the bodhisattva Avalokiteśvara.[1]  The building measures 400 metres (1,300 ft) east-west and 350 metres (1,150 ft) north-south, with sloping stone walls averaging 3 metres (9.8 ft) thick, and 5 metres (16 ft) thick at the base, and with copper poured into the foundations to help proof it against earthquakes.[2] Thirteen storeys of buildings, containing over 1,000 rooms, 10,000 shrines and about 200,000 statues, soar 117 metres (384 ft) on top of Marpo Ri, the 'Red Hill', rising more than 300 metres (980 ft) in total above the valley floor.",
    }]

    africa_pages = [{
        'name':'Egyptian Pyramids',
        'rate':'9.89',
        'intro':"The most famous pyramids are the Egyptian — huge structures built of brick or stone, some of which are among the world's largest constructions. They are shaped as a reference to the rays of the sun. Most pyramids had a polished, highly reflective white limestone surface, to give them a shining appearance when viewed from a distance. The capstone was usually made of hard stone – granite or basalt – and could be plated with gold, silver, or electrum and would also be highly reflective.[1] After 2700 BC, the ancient Egyptians began building pyramids, until around 1700 BC. The first pyramid was erected during the Third Dynasty by the Pharaoh Djoser and his architect Imhotep. This step pyramid consisted of six stacked mastabas. The largest Egyptian pyramids are those at the Giza pyramid complex.",
    },{
        'name': 'Jebel Barkal',
        'rate': '9.89',
        'intro': "The ruins around Jebel Barkal include at least 13 temples and 3 palaces, that were for the first time described by European explorers in the 1820s. In 1862 five inscriptions from the Third Intermediate Period were recovered by an Egyptian officer and transported to the Cairo Museum, but not until 1916 were scientific archeological excavations performed by a joint expedition of Harvard University and the Museum of Fine Arts of Boston under the direction of George Reisner.[1] From the 1970s, explorations continued by a team from the University of Rome La Sapienza, under the direction of Sergio Donadoni, that was joined by another team from the Boston Museum, in the 1980s, under the direction of Timothy Kendall. The larger temples, such as the Temple of Amun, are even today considered sacred to the local population. The carved wall painted chambers of the Temple of Mut are well preserved. Temple B700 built by Atlanersa and decorated by Senkamanisken is now largely destroyed. It received the sacred bark of Amun from the nearby B500 on certain cultic occasions, and may have served during the coronation of the kings of the early Napatan period, in the mid 7th century BC.",
    },{
        'name': 'Great Zimbabwe',
        'rate': '9.89',
        'intro':"Great Zimbabwe is a ruined city in the south-eastern hills of Zimbabwe near Lake Mutirikwe and the town of Masvingo. It was the capital of the Kingdom of Zimbabwe during the country's Late Iron Age. Construction on the city began in the 11th century and continued until it was abandoned in the 15th century. The edifices were erected by the ancestral Shona.[2] The stone city spans an area of 7.22 square kilometres (1,780 acres) which, at its peak, could have housed up to 18,000 people. Great Zimbabwe is believed to have served as a royal palace for the local monarch. As such, it would have been used as the seat of political power. Among the edifice's most prominent features were its walls, some of which were over five metres high. They were constructed without mortar (dry stone). Eventually, the city was abandoned and fell into ruin.",
    }]

    north_america_pages = [{
        'name': 'Chichen Itza',
        'rate': '9.89',
        'intro':'Chichen Itza was a large pre-Columbian city built by the Maya people of the Terminal Classic period. The archaeological site is located in Tinúm Municipality, Yucatán State, Mexico. Chichen Itza was a major focal point in the Northern Maya Lowlands from the Late Classic (c. AD 600–900) through the Terminal Classic (c. AD 800–900) and into the early portion of the Postclassic period (c. AD 900–1200). The site exhibits a multitude of architectural styles, reminiscent of styles seen in central Mexico and of the Puuc and Chenes styles of the Northern Maya lowlands.  Chichen Itza was one of the largest Maya cities and it was likely to have been one of the mythical great cities, or Tollans, referred to in later Mesoamerican literature.',
    }]

    south_america_pages = [{
        'name': 'Christ the Redeemer',
        'rate': '9.89',
        'intro':"Christ the Redeemer is an Art Deco statue of Jesus Christ in Rio de Janeiro, Brazil, created by French sculptor Paul Landowski and built by Brazilian engineer Heitor da Silva Costa, in collaboration with French engineer Albert Caquot. Romanian sculptor Gheorghe Leonida fashioned the face. Constructed between 1922 and 1931, the statue is 30 metres (98 ft) high, excluding its 8-metre (26 ft) pedestal. The arms stretch 28 metres (92 ft) wide. The statue weighs 635 metric tons (625 long, 700 short tons), and is located at the peak of the 700-metre (2,300 ft) Corcovado mountain in the Tijuca Forest National Park overlooking the city of Rio de Janeiro. A symbol of Christianity across the world, the statue has also become a cultural icon of both Rio de Janeiro and Brazil, and is listed as one of the New7Wonders of the World.[3] It is made of reinforced concrete and soapstone."
    }]

    Oceania_pages = []

    Antarctica_pages = []

    cats = {
        'Europe':{'pages':europe_pages},
        'Asia':{'pages':asia_pages},
        'Africa':{'pages':africa_pages},
        'North America':{'pages':north_america_pages},
        'South America':{'pages':south_america_pages},
        'Oceania':{'pages':Oceania_pages},
        'Antarctica':{'pages':Antarctica_pages}
    }
#     add data above to database
    for cat, cat_data in cats.items():
        c = add_cat(cat)
        for p in cat_data['pages']:
            add_page(c, p['name'], p['rate'], p['intro'])
    # for c in Category.objects.all():
    #     for p in Page.objects.filter(category=c):
    #         print(f'- {c}: {p}')

def add_page(cat, name, rate, intro):
    p = Page.objects.get_or_create(category=cat, name=name)[0]
    p.rate = rate
    p.intro = intro
    p.save()
    return p
def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c
if __name__ == '__main__':
    print('Starting population script...')
    populate()