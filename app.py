from flask import Flask, render_template,  session, redirect, request, jsonify
from flask_cors import CORS,cross_origin
from scraper import scrap_flipkart, scrap_amazon
import json

# Initialize the Flask application. This is where we attach the routes.
app = Flask(__name__)

# Create the index route. Add CORS. It loads the index.html page.
@app.route('/', methods=['GET'])
@cross_origin()
def homePage():
	return render_template("index.html")

# Create the scrap route. It triggers the Flipkart and Amazon scrapper. It renders the result.html template.
@app.route('/scrap', methods=['GET'])
@cross_origin()
def scrap():
	# The search text the user entered in the index page.
	search_text = request.args.get("query")
	
	# Trigger the Flipkart and Amazon scraper. The results are merged into a single list.
	flipkart_reviews = scrap_flipkart(search_text)
	amazon_reviews = scrap_amazon(search_text)
	reviews = flipkart_reviews + amazon_reviews
	
	#print(json.dumps(reviews, indent=4))
	
	# Comment the following return statement when you are working on the UI.
	# return render_template("result.html", reviews=reviews)

	# Render the template using dummy data. This is used for debugging purposes. We use early exit when the scrappers are live.
	return render_template("result.html", reviews=[
    {
        "review_title": "Amazing Experience",
        "review_content": "I am impressed by the polycarbonate build of the iPhone 5c, which is excellent to hold and very sturdy. No squeaky noises that comes from many plastic shelled smartphones as such. I recently bought this from a local store as the particular seller cannot deliver the item to my pin code. I was using an iPhone 4 for a long time but it started to die on me, so had to make a choice between Nexus 5 and iPhone 5c. Nexus was pure android and I wanted to shift this time but the battery reviews made me think for the 5c. So finally made my choice and went for the 8GB. The moment I held it for the first time i was blown away by the compactness for the phone. It's pretty fast not like nexus or note or xperia z1, but it works just more than fine. Smooth UI helps in usability not much hassles or complications. But make sure to get a case for this like spigen or skech, because it's a glossy back (not very shiny) it attracts scratches easily if you put the phone and keys in the same pocket.Regarding the screen part, iPhone screens are known for their natural colors not like over saturated screens of many smartphones. Viewing angles are excellent, brightness levels are great. Also the speaker is of good quality as the sound it imparts is well pitched. Earpiece is very good, call quality is incredible no drops. Last but no the least lightning connector charger the phone faster than average and the ear pods which comes out of the box are just awesome. Very good bass.PS - This is an average consumer review I am no tech guy.",
        "customer_name": "Sandeep Sarkar",
        "ratings": "5",
        "date": "Sandeep Sarkar"
    },
    {
        "review_title": "Classic !!!!",
        "review_content": "1.You never gonna feel the quality of this mobile untill you hold it in your hand.2.please dont compare any android mobile phone with this product because its entirely     different3.If you prefer the quality and reliabilty in operation then it is what ya lookin for4.As per the storage space it is only for decent usage5.Never lags no matter how many tasks are runnin at a time, flows like fluid.6.As per the display at this price range it is perfect by comparing with other ips lcd display because 326ppi is what enough for human eye you cant find any pixel no matter how closer you look and the colors looks pretty natural not over saturated like sony xperia and samsung7.About primary isight 8mp shooter is great for this price range8.About facetime hd cam perfect for selfies and to make video calls9.At last siri only works when wifi or mobile data is engaged otherwise voice control only works.I hope that this review will help you to what you wanna buy for your usagePEACE :)......",
        "customer_name": "Sridhar Susindhran",
        "ratings": "5",
        "date": "Sep, 2014"
    },
    {
        "review_title": "Best Online Deal Ever",
        "review_content": "Just Bought This From Flipkart. First Of All Thanks To The Team To Make Everything Best.The Packing, The Delivery. Got Only After Third Day Of Order. IPhone Itself, A Great Wish To Be Fulfilled. I Already Using 5s. I Bought It For My Sister In Law. The Best Thing Called Iphone In Mobiles. Thanks You (Flipkart) People To Make It Best Possible. Regular Buyer. Fully Satisfied. Sealed, Well Packed Very Fresh Manufacturing Date, Go For It If You Are Looking. No Doubt.",
        "customer_name": "Rajesh Gupta",
        "ratings": "5",
        "date": "Sridhar Susindhran"
    },
    {
        "review_title": "If u don't have an iPhone , U don't have an iPhone...!!! Value for money at this price....",
        "review_content": "I purchased this phone from Flipkart on 19 Sep 2014After about 15-20 days of use , I can give following reviews about the iphone.....Awesome budget iphone by apple. If u don't care much about the metal body of apple and have a limited budget, this phone is perfect for you. People asked me to compare 5C with nexus 5 , HTC desire 816 , xperia T2 ultra, MOTO X But believe me an iPhone is an iphone u cannot its features with same features in other phone.Although being a smartphone, it has a great battery life and superfast charging by USB lightning cable. The Apple's app store too has now become wide and vivid.One thing I can say is you will not regret purchasing this phone at this price.One thing more being an 8 GB model , you need to use and choose your apps wisely as u don't get much memory.So memory can be a constraint for you.I am loving my phone and ya good packaging and delivery by flipkart as well.",
        "customer_name": "Akhilesh Tripathi",
        "ratings": "4",
        "date": "Oct, 2014"
    },
    {
        "review_title": "I love My I Phone 5C!!!",
        "review_content": "Now i know what drives people crazy about I phones...........My husband is a hard core Apple Fan but i was never one.Always felt its a professional phone with restrictions.But the moment i saw the Launch video of the 5C!! I went GAGA on the colors and the minute details which the Apple team has paid attention to in building this beauty.Me playing the video multiple times made me feel obvious that i want to buy it.So I am a proud owner of a Green Apple 5C which i got in a week time it was launched in India.Thanks to flipkart..As green being the most bought color and being sold out in every outlet..FLIPKART was the only place where i could find the color with a good deal.After confirming on the color availability with the customer care who was extremely sweet and helpful ,I place the order on Thursday night 11.43pm and  the product reached me on Saturday 10.30am.Which was super fast and super satisfied a customer who was superbly excited to have her 5C.Its a fantastic phone with fantastic feataures and gives a awesome feel to operate and to hold.Apple is definitely going to attract a larger younger crowd with  the vibrant colors.Great going!!",
        "customer_name": "Moovika",
        "ratings": "5",
        "date": "Rajesh Gupta"
    },
    {
        "review_title": "iPhone 5C",
        "review_content": "The phone feels good to hold and use. The screen resolution and the speed of the phone is nice.The memory for 8GB is an issue, but I never use the phone for playing games or use large apps, so its good for me. I ordered the blue one and the color is soothing as well.Happy with the buy.",
        "customer_name": "Tamali Bhattacharya",
        "ratings": "4",
        "date": "Aug, 2014"
    },
    {
        "review_title": "TRUE FACTS:",
        "review_content": "Just adding on your wonderful review Sunoor, IPHONE 5C DOES NOT HAVE A BETTER CAMERA THAN IPHONE 5. ALL THE FEATURES OF THIS PHONE AND 5 ARE SIMILAR. There is nothing better in this phone that 5 except a variety of colours. It is true that the phone is more vulnerable than iPhone 5 and the plasticky body is more prone to scratches if you like to use the phone without a cover. Regarding the price, as you should already know, each year when apple introduces a new phone, like this year's 5s the price of the older phone JUST IN CASE 5 (I KNOW MANUFACTURING NEW iPhone 5's HAS BEEN DISCONTINUED) drops nearly by 9,000 rupees according to the storage. Therefore, if 5 was still there, the price of 5 would still be the same as today's 5c. And also, apple, for some stupid reason has increased the price of 5s in India. No other iPhone (concern storage), was as expensive as today's 5s in the history of iPhone launch in India, whereas in other countries (Not all), the price of this 5s is the same, i.e. the price of 5 when 5s wasn't launched is now the price of 5s in other countries which should have been the same in India.PLEASE PLEASE PLEASE DO NOT BUY THIS PHONE INSTEAD BY 5S, AT LEAST YOU GET NEW FEATURES!!! Makes Sense?",
        "customer_name": "Shivansh Singhal",
        "ratings": "5",
        "date": "Akhilesh Tripathi"
    },
    {
        "review_title": "better alternative avilable in this range in android !",
        "review_content": "Apple Iphone series is no more usable. After jobs's passed away this Iphone no longer gone in right direction.in 40 Range you can got Father of phone in Android. it's cost same and is one of the best phone for the feature.If you want to get it for become cool then 40 range Lumia do much better job. He have better things.Featurewise android phone/ Lumia series are better then this phone.",
        "customer_name": "anirugu",
        "ratings": "5",
        "date": "Sep, 2014"
    },
    {
        "review_title": "Nice",
        "review_content": "The Iphone 5C was my first Iphone and frankly with the larger screen its really worthwhile now. Lack of bluetooth file transfer and inability to make 3G Video calls pinches a lot. Video calling over facetime thru internet is provided over wifi. It also says thru mobile network but yet to try. However, its interface is as as smooth as hot knife in a butter brick.Maps, Whatsapp, FB etc are really very smooth. Transferring your own song library to the devise thru itunes takes a lot of technical DIY-ness. Simpler in Android to just copy paste them in the drive/card/folder. Even in Windows Phone its very cumbersome to trasnfer music. Further your playlists should be made on PC. You can't add songs to playlist in WP (Laughable).Why this nano SIM business, I fail to understand, How much weight / space can you really reduce. ITs really cumbersome to prepare the SIM to fit and then its of no use in another phone, should you need to switch for any reason.The phone was a present to my wife and she's quite happy with her limited usage of social media which is excellent. The color & rounded long slender shape went well with her. However, I will not buy an Iphone for myself till it allows Bluetooth file transfers, 3G Video Calling & easy music & file transfer from PC to Phone as lot of data travels in phone (what's the big deal?). IT appears Apple is purposefully giving lesser services then contemporay phones and adding bit by bit in every new addition.Flipkart's offer of cashback with HDFC Card was excellent and with the receipt of cashback in my account, the price really came down to a sane level of 36500. Delivery was also quite fast. Excellent big bubble packing too.",
        "customer_name": "ND MATHUR",
        "ratings": "4",
        "date": "ND MATHUR"
    },
    {
        "review_title": "Why Nothing Else Is an Iphone",
        "review_content": "It is the only product in the market where performance , battery life, build quality, and camera quality meet right.Sorry Samsung your s3 and s4 does not do that -both have cheap design both are full of unnecessary bloatware that nobody uses and touch ui is downright ugly and slow.Even the dialer does not open fast in a latest quad core like S4.And the whole android story is like that.Just imagine the multitasking-even the closed apps keep running on process manager-then what really happened when i closed the app was just a gimmick.Android is full of unnecessary settings and options that after some days of thrill just annoy.Only good android it seems to me is  htc one.but thats priced even higher and quite justifiably so considering the market.The nexuses could be good but in some area  they are always left wanting (like cam in nexus4 and battery in nexus5)Yeah Windows phone is definitely better than android ..but  for the apps.Android is one lucrative game that the industry will be bullying the buyers with ...and it seems it will attain near monopoly status.Well the iphone is priced too high but just look at the market - if nobody can give them a good competition then they will keep it priced high always.",
        "customer_name": "Sandipan Choudhury",
        "ratings": "5",
        "date": "Apr, 2014"
    },
    {
        "review_title": "Apples the best",
        "review_content": "The only apple device that i own is an ipod touch. Iam planning to buy an iphone 5c for my dad.I came to the flipkart review section in order to see the views of you guys and iam highly surprised and equally dissapointed that you guys are comparing apple with companies like samsung and even for heavens sake micromax!!!...I wont say micromax is bad..they r excellent for their price...But how can someone compare them with the god of mobile phones??..Many say tht even with the plastic body 5c is realy expensive...yes it is expensive but check the prices in other countries like uae and usa and u will c the difference..the high price is just because of the excise duty imposed by our government..apple does not produce iphones in india while other companies produce it in india..which is the reason it is expensive..if u r so conerned for the price then either go for   some other phone or buy an iphone from uae where u get it the cheapest(but no warranty)..Iphone 5c has the same specs as that of iphone5 but u get it for 100$ less than iphone 5(6300 rs cheaper!!)...Then whats the complaint???...Iphone 5 was never a failure..only the map was a failure but with google maps tht problem is solvd too...i c no other reason why not to buy an iphone...Iam not reviewing the 5c since i have not used it but i would like to advice some of u here not to write negetive reviews just because u cant afford an iphone..iphone is royalty and u shud be worthy enough to afford it...",
        "customer_name": "Ravindranath Vasudevan",
        "ratings": "5",
        "date": "Sandipan Choudhury"
    },
    {
        "review_title": "The Perfect Phone !!",
        "review_content": "First of all Flipkart should not allow every one/any one ( who doesn't know about technology )  to write a review . They should give access to that person who bought this product , can only write review here NOT ALL..I don't agree at all who gave negative response  here to I-phone 5c. This is Apple n have IOS software which is far better than android ( which u can't update expect Nexus device ) & Windows... This phone is simply awesome ... Full stylish.... Blue color looks perfect !!  If you budget 30-32 K better go apple. Don't ever go for Samsung ....If you dont want to be out dated with in few months after spending 30-35 K ... Apple is best choice. Cheers to Filpkart... n Apple as well...",
        "customer_name": "Rajdeep Parmar",
        "ratings": "5",
        "date": "Nov, 2013"
    },
    {
        "review_title": "A wonderful product from a wonderful website !",
        "review_content": "This was the first time I ordered from flipkart and I must say that the product delivery and packaging were wonderful with cent percent satisfaction. JJ Mehta was the seller which delivered the product before the official delivery date. Rest about the product , it's Apple we're talking about , unaplogetically plastic with Apple's elite signature makes it a joy to use. Highly recommended product+website+seller ! Thumbs up !",
        "customer_name": "Raja Arora",
        "ratings": "5",
        "date": "Ravindranath Vasudevan"
    },
    {
        "review_title": "Apple iPhone 5C it is not really worth the money",
        "review_content": "Apple is fleecing Indians by charging high premium for a product which is really not worth the price at which it is being sold. We Indians have a fancy for things expensive, and think high price means high quality. Consider Google Nexus series which are really worth the price and the features. The processor speed, Screen resolution, Android platform, features, Google support for Android platform is any day much superior than Apple. Apple if it does not reduce it's price it is going to decline it's market share exponentially in the coming future.Further Apple 5C is identical and a downgraded version of  Apple 5(earlier phone). The sturdy metal case has been replaced by cheap plastics and that too in fancy colors, which only downgrades the image of Apple company further.",
        "customer_name": "KRISHNA MURTHY AB",
        "ratings": "4",
        "date": "Nov, 2013"
    },
    {
        "review_title": "Definitely not so bad as projected",
        "review_content": "I did not buy this from flipkart. I got this on exchange for a 2-yr old iphone 4 from an apple authorized retailer.Pros- 1) Seems faster and quite natural with iOS 7. (Had used a iphone 4 earlier)2) Slim and Sleek and the steel-reinforced casing definitely converges with the overall design. Doesn't feel/look like even a bit of lumia. Once you hold it, you will know what I mean.3) Back casing (some steel reinforced mix) is quite strong contrary to my expectations and it's scratch resistant to a some extent. So I do not miss the corning glass-back casing of iphone 4 so much. You need to have a feel of the casing once.4) Apple iWork package including iLife (pages, numbers, keynote, imovie, iphoto) comes as a free download with 5C(&5S) else you will have to shell out around Rs. 500-600 per app. It seems to be a move to match microsoft office offering on lumia phones.5) Battery life has most certainly improved. Lost only 7% in 1.5 days.Cons:1) With this screen size even it's difficult to work with these productivity apps, unless you need to do a minor correction. Screen should be wider and nokia has perhaps nailed it.2) You know you are missing something like M7 processor on apple if you are playing a lot of games. I usually play infinity blade, real racing, so they are graphically superior on a newer phone.3) I got in exchange with 13K off for a old iphone 4, else I would have straight gone for the 5S. There is no exchange offer on 5S as expected.PS-Unfortunately call it, apple's planned obsolescence, my 2 year old iphone 4's home button finally gave up. It was working nicely even with the beta versions of iOS 7. The problems had started after iOS 7 general release upgrade. And apple is giving minimum 13K off in exchange offers for old iphone 4 if you take the 5C (it would not have sold in the used mobile-market for more than 8k), seems they intend to shift all their iphone 4S & earlier users to the mid-range iphone 5C (for clearing inventory of unsold iphone 5 cores/whatever). And they are quite successful, be it their software tweaks or absence of feature specific software upgrades.",
        "customer_name": "Sonik Mishra",
        "ratings": "5",
        "date": "Rajdeep Parmar"
    },
    {
        "review_title": "Go get a life iphone haters",
        "review_content": "personally i too never liked iphone earlier. But the colors of the iphone 5c attracted me...i used many colorful phones like nokia n8, lumia, canvas, even samsung phones... but when i first took the iphone 5c in my hand, i just fell in love with it... it feels damn premium. unlike other lumia phones or any other phone.. The CAMERA quality is also better than the previous iphone 5(rarely people know it) ..... the screen quality, the gaming experience just forced me to love iphone.. now m quite sure, i can never get out of this iphone family.. LOVE MY 5c (blue)... m also sure the people who hates iphone has never used one.",
        "customer_name": "shreyan sarkar",
        "ratings": "5",
        "date": "Jan, 2014"
    },
    {
        "review_title": "OLD Champion NEW look!!!!",
        "review_content": "iPhone 5C is amazingly an ever-changing smartphone.A6 dual core processor with 3Core Graphics.8MP camera with 1080p recording.4-inch Retina Display - Best Display ever into a mobile.Dont get fooled by 441ppi-1080p displays......Apple display still remains on the top.5 Colorful-but-shy colors.With high quality Plastic casing that beats all other plastic phones.Plastic in high quality means 3* more durability!JUST BUY THE PHONE IF YOU DO NOT HAVE THE IPHONE 5.JUST IGNORE THE PHONE IF YOU HAVE IPHONE 5 AND HAVE A GOOD BUDGET.GO FOR IPHONE 5S.YOU WILL BE MORE SATISFIED BECAUSE THIS PHONE IS THE SAME AS IPHONE 5.",
        "customer_name": "Kirat Alreja",
        "ratings": "5",
        "date": "Raja Arora"
    }
])

if __name__ == '__main__':
	app.run()