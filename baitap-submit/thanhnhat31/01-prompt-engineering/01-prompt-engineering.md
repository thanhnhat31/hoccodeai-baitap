- Prompt 1
Please generate a list of multiple-choice questions from the lesson content below, 
The list should include 10 questions, each with 4 options and only 1 correct answer.
====================
Apple is fruit.
A dog is an animal.
Rose is a flower.
There are dark clouds when it is raining.
Vietnam is a tropical country.
There are seven continents in the Earth. 
====================

- Prompt 2
Write one more paragraph for below article. 
The added paragraph needs to maintain the same tone and have length of 90% to 120% length of the previous paragraph.
Write paragraphs in English.
===
Artificial intelligence is rapidly transforming our world, offering immense potential across diverse sectors. From automating mundane tasks to driving groundbreaking scientific discoveries, AI's importance is undeniable. In healthcare, it aids in early disease detection and personalized treatments. In business, it optimizes operations and enhances customer experiences. AI-powered tools are revolutionizing education, making learning more accessible and tailored. Moreover, AI's role in addressing climate change through data analysis and predictive modeling is crucial. While ethical considerations remain, the responsible development and deployment of AI promise to unlock unprecedented opportunities for human progress and societal well-being. 
===

- Prompt 3
Below is examples of reviews about an mobile application.
===========
I love this app - Positive
This app was crashed on the first run - Negative
This app is what I'm looking for - Positive
There are still bugs in the app - Negative
===========
Based on about examples, please classify below reviews into positive and negative review, aggregate and count the number of reviews.
===========
I think this app was good for me.
I don't need to find another app.
I don't want to use it anymore.
There are much things need to do with this app.
I can't stop using it.
===========

- Prompt 4
Find bugs in below code if any, add comments and explain process of this source code.
==========
def find_largest_number(array):
    if not array:
        return array
    
    largest = array[1]
    
    for number in array:
        if number >= largest:
            largest = number
            
    return largest

if __name__ == "__main__":
    test_arrays = [
        [3, 7, 2, 9, 1, 5],
        [10, 20, 5, 15, 30, 25],
        [-5, -10, -3, -1, -7],
        [42],
        []
    ]
    
    for arr in test_arrays:
        result = find_largest_number(arr)
        if result is None:
            print(f"Array {arr} is empty")
        else:
            print(f"The largest number in {arr} is {result}")
============

- Prompt 5
Read the below JSON and introducing sightseeing spots, activities, famous dishes, and best times to visit.
The result should consider below points:
- Prioritize places having activities related to sea.
- Don't recommend anything related to alcohol, cigarettes.
- Suggest places that have souvenir that can bring home.
- Arrange time to visit on ascending order.
====================
[
  {
    "Sightseeing Location Name": "Ha Long Bay",
    "Location Description": "One of the world's natural wonders, Ha Long Bay is famous for its thousands of limestone islands rising from the emerald waters.",
    "Activities and Entertainment": ["Cruising the bay", "Exploring caves", "Kayaking", "Swimming"],
    "Famous Dishes and Specialties": ["Fresh seafood", "Ha Long grilled chopped squid", "Horseshoe crab"],
    "Best Time to Visit": "Spring (March - April) and Autumn (September - November)"
  },
  {
    "Sightseeing Location Name": "Hoi An Ancient Town",
    "Location Description": "A UNESCO World Heritage Site, Hoi An Ancient Town is famous for its ancient houses, shimmering lantern-lit streets, and peaceful, romantic atmosphere.",
    "Activities and Entertainment": ["Evening strolls through the ancient town", "Visiting ancient houses", "Boat trips on the Hoai River", "Enjoying local cuisine", "Shopping"],
    "Famous Dishes and Specialties": ["Cao Lau", "Quang Noodles", "White Rose Dumplings", "Hoi An Chicken Rice"],
    "Best Time to Visit": "Dry season (February - August)"
  },
  {
    "Sightseeing Location Name": "Sa Pa",
    "Location Description": "Sa Pa is a highland town famous for its majestic mountain scenery, picturesque terraced fields, and unique ethnic minority cultures.",
    "Activities and Entertainment": ["Climbing Fansipan", "Trekking through ethnic villages", "Visiting local markets", "Snow watching in winter"],
    "Famous Dishes and Specialties": ["Thang Co", "Five-color sticky rice", "Buffalo jerky", "Apple wine"],
    "Best Time to Visit": "Spring (March - May) and Autumn (September - November)"
  },
  {
    "Sightseeing Location Name": "Da Lat",
    "Location Description": "Known as the 'City of a Thousand Flowers,' Da Lat is famous for its cool climate, poetic natural scenery, and classic French architecture.",
    "Activities and Entertainment": ["Visiting flower gardens", "Strolling around Xuan Huong Lake", "Visiting waterfalls", "Enjoying local cuisine"],
    "Famous Dishes and Specialties": ["Grilled rice paper", "Chicken hotpot with basil leaves", "Da Lat strawberries", "Da Lat coffee"],
    "Best Time to Visit": "Year-round"
  },
  {
    "Sightseeing Location Name": "Phu Quoc",
    "Location Description": "Phu Quoc is Vietnam's largest island, famous for its pristine beaches, crystal-clear waters, and diverse marine ecosystem.",
    "Activities and Entertainment": ["Swimming", "Snorkeling", "Visiting fishing villages", "Night squid fishing", "Visiting fish sauce factories"],
    "Famous Dishes and Specialties": ["Fresh seafood", "Herring salad", "Sea urchin with green onion oil", "Phu Quoc fish sauce"],
    "Best Time to Visit": "Dry season (November - April)"
  }
]

- Prompt 6
Please summarize the following article and list up characters appear in it.
Your summary should be concise yet informative, capturing the essence of the content. As you summarize, try to maintain a positive tone and inject a bit of humor where appropriate, without detracting from the core message. Write the summary in Vietnamese.

When generating the summary, consider the following:
- Identify and include the main ideas, central themes, and crucial plot points
- Omit unnecessary details or tangential information that doesn't contribute to the overall understanding
- Use clear and concise language to convey the summary effectively
- Maintain a positive spin on the content, highlighting uplifting or amusing aspects where possible
- If suitable, incorporate a touch of wit or humor to make the summary more engaging

===
Tôi sống độc lập từ thủa bé. Ấy là tục lệ lâu đời trong họ nhà dế chúng tôi. Vả lại, mẹ thường bảo chúng tôi rằng: "Phải như thế, để các con biết kiếm ăn một mình cho quen đi. Con cái mà cứ nhong nhong ăn bám vào bố mẹ thì chỉ sinh ra tính ỷ lại, xấu lắm, rồi ra đời không làm nên trò trống gì đâu". Bởi thế, lứa sinh nào cũng vậy, đẻ xong là bố mẹ thu xếp cho con cái ra ở riêng. Lứa sinh ấy, chúng tôi có cả thảy ba anh em. Ba anh em chúng tôi chỉ ở với mẹ ba hôm. Tới hôm thứ ba, mẹ đi trước, ba đứa tôi tấp tểnh, khấp khởi, nửa lo nửa vui theo sau. Mẹ dẫn chúng tôi đi và mẹ đem đặt mỗi đứa vào một cái hang đất ở bờ ruộng phía bên kia, chỗ trông ra đầm nước mà không biết mẹ đã chịu khó đào bới, be đắp tinh tươm thành hang, thành nhà cho chúng tôi từ bao giờ. Tôi là em út, bé nhất nên được mẹ tôi sau khi dắt vào hang, lại bỏ theo một ít ngọn cỏ non trước cửa, để tôi nếu có bỡ ngỡ, thì đã có ít thức ăn sẵn trong vài ngày.
Rồi mẹ tôi trở về.
Tôi cũng không buồn. Trái lại, còn thấy làm khoan khoái vì được ở một mình nơi thoáng đãng, mát mẻ. Tôi vừa thầm cảm ơn mẹ, vừa sạo sục thăm tất cả các hang mẹ đưa đến ở. Khi đã xem xét cẩn thận rồi, tôi ra đứng ở ngoài cửa và ngửng mặt lên trời. Qua những ngọn cỏ ấu nhọn và sắc, tôi thấy màu trời trong xanh. Tôi dọn giọng, vỗ đôi cánh nhỏ tới nách, rồi cao hứng gáy lên mấy tiếng rõ to.
Từ đây, tôi bắt đầu vào cuộc đời của tôi. Cho dù tôi sẽ sung sướng hay khổ sở, cái đó tùy ở tính tình tôi khôn ngoan hay đần độn. Song tôi chưa cần biết đến thế, tính đến thế. Mà hãy lấy sự được ung dung độc lập một mình là điều thích lắm rồi....
Ngày nào cũng vậy, suốt buổi, tôi chui vào trong cùng hang, hì hục đào đất để khoét một cái ổ lớn, làm thành cái giường ngủ sang trọng. Rồi cũng biết lo xa như các cụ già trong họ dế, tôi đào hang sâu sang hai ngả làm những con đường tắt, những cửa sau, những ngách thượng, phòng khi gặp nguy hiểm, có thể thoát thân ra lối khác được. Chập tối, tôi tạm nghỉ tay và ra đứng ngoài cửa, họp cùng anh chị em hàng xóm quanh bờ ruộng, vừa gảy đàn vừa hát một bài hát hoàng hôn chào tạm biệt ông mặt trời. Khi đêm đã xuống hẳn, cả xóm chúng tôi, các bô lão dế lụ khụ già cốc đế cũng bỗng nhiên vui tính, ai nấy ra khỏi hang, đến tụ hội thật đông tận giữa bãi trong đêm tối mát lạnh, cùng uống sương đọng, ăn cỏ ướt và những gã tài hoa thì gảy đàn thổi sáo, cùng nhau ca hát, nhảy múa linh đình đến tận sáng bạch, lúc ông mặt trời quen thuộc lại nghiêm trang ló lên đằng đông mới tan cuộc ai về nhà nấy.
Ngày nào, đêm nào, sớm và chiều nào cũng ngần ấy thứ việc, thứ chơi. Kể đời mà được như thế cũng khá an nhàn, nhưng mới đầu còn thấy hay hay, về sau cũng nhàm dần.
Bởi tôi ăn uống điều độ và làm việc có chừng mực nên tôi chóng lớn lắm. Chẳng bao lâu tôi đã trở thành một chàng dế thanh niên cường tráng. Ðôi càng tôi mẫm bóng. Những cái vuốt ở chân, ở khoeo cứ cứng dần và nhọn hoắt. Thỉnh thoảng, muốn thử sự lợi hại của những chiếc vuốt, tôi co cẳng lên, đạp phanh phách vào các ngọn cỏ. Những ngọn cỏ gãy rạp, y như có nhát dao vừa lia qua. Ðôi cánh tôi, trước kia ngắn hủn hoẳn bây giờ thành cái áo dài kín xuống tận chấm đuôi. Mỗi khi tôi vũ lên, đã nghe tiếng phành phạch giòn giã. Lúc tôi đi bách bộ thì cả người tôi rung rinh một màu nâu bóng mỡ soi gương được và rất ưa nhìn. Hai cái răng đen nhánh lúc nào cũng nhai ngoàm ngoạp như hai lưỡi liềm máy làm việc. Sợi râu tôi dài và uốn cong một vẻ rất đỗi hùng dũng. Tôi lấy làm hãnh diện với bà con vì cặp râu ấy lắm. Cứ chốc chốc tôi lại trịnh trọng và khoan thai đưa cả hai chân lên vuốt râu.
Tôi đi đứng oai vệ. Mỗi bước đi, tôi làm điệu dún dẩy cá khoeo chân, rung lên rung xuống hai chiếc râu. Cho ra kiểu cách con nhà võ. Tôi tợn lắm. Dám cà khịa với tất cả mọi bà con trong xóm. Khi tôi to tiếng thì ai cũng nhịn, không ai đáp lại. Bởi vì quanh quẩn ai cũng quen mình cả. Không nói, có lẽ họ nể hơn là sợ. Nhưng tôi lại tưởng thế là không ai dám ho he. Ấy vậy, tôi cho tôi giỏi. Những gã xốc nổi thường làm cử chỉ ngông cuồng là tài cao. Tôi quát mấy chị Cào Cào ngụ ngoài đầu bờ khiến mỗi lần thấy tôi đi qua, các chị phải núp khuôn mặt trái xoan dưới nhánh cỏ, chỉ dám đưa mắt lên nhìn trộm. Thỉnh thoảng, tôi ngứa chân đá một cái, ghẹo anh Gọng Vó lấm láp vừa ngơ ngác dưới đầm lên. Tôi càng tưởng tôi là tay ghê gớm, có thể sắp đứng đầu thiên hạ rồi.
Chao ôi, có biết đâu rằng: hung hăng hống hách láo chỉ tôi đem thân mà trả nợ những cử chỉ ngu dại của mình thôi. Tôi đã phải trải cảnh như thế. Thoát nạn rồi mà còn ân hận quá, ân hận mãi. Thế mới biết, nếu đã trót không suy tính, lỡ xảy ra những việc dại dột, dù về sau có hối cũng không thể làm lại được.
Câu chuyện ân hận đầu tiên mà tôi ghi nhớ suốt đời.
Bên hàng xóm tôi có cái hang của Dế Choắt. Dế Choắt là tên tôi đặt cho nó một cách chế giễu và trịch thượng thế. Choắt nọ cũng chắc trạc tuổi tôi. Nhưng vì Choắt bẩm sinh yếu đuối nên tôi coi thường và gã cũng sợ tôi lắm. Cái chàng Dế Choắt, người gày gò và dài lêu nghêu như một gã nghiện thuốc phiện. Ðã thanh niên rồi mà cánh chỉ ngắn ngủn đến giữa lưng, hở cả hai mạng sườn như người cởi trần mặc áo gi-lê. Ðôi càng bè bè, nặng nề trông đến xấu. Râu ria gì mà cụt có một mẩu, mà mặt mũi lúc nào cũng ngẩn ngẩn ngơ ngơ. Ðã vậy tính nết lại ăn sổi, ở thì (thật chỉ vì ốm đau luôn luôn không làm được) một cái hang ở cũng chỉ bới nông sát mặt đất, không biết đào sâu rồi khoét ra nhiều ngách như hang tôi.
Một hôm tôi sang chơi, thấy trong nhà luộm thuộm, bề bộn, tôi bảo:
- Sao chú mày sinh sống cẩu thả quá như thế! Nhà cửa đâu mà tuềnh toàng. Ngộ có kẻ nào đến phá thì thật chú chết ngay đuôi! Này thử xem: khi chú chui vào tổ lưng chú phải lồm cồm đụng sát lên tận mặt đất, làm cho ai trên về cỏ nhìn sang cũng biết chú đương đi đứng chỗ nào trong tổ. Phỏng thử có thằng chim Cắt nó nhòm thấy, nó tưởng mồi, nó mổ một phát, nhất định trúng giữa lưng chú, thì chú có mà đi đời! Ôi thôi, chú mày ơi! Chú mày có lớn mà chẳng có khôn.
Ngẫm ra thì tôi chỉ nói lấy sướng miệng thôi. Còn Dế Choắt than thở thế nào, tôi cũng không để tai. Hồi ấy tôi có tính tự đắc, cứ miệng mình nói tai mình nghe chứ không biết nghe ai, thậm chí cũng chẳng để ý có ai nghe mình không.
Dế Choắt trả lời tôi bằng một giọng rất buồn rầu:
- Thưa anh, em cũng muốn khôn, nhưng không khôn được, đụng đến việc là em thở rồi, không còn hơi sức đâu mà đào bới nữa. Lắm khi em cũng nghĩ nỗi nhà cửa thế này là nguy hiểm, nhưng em nghèo sức quá, em đã lo ròng rã hàng mấy tháng nay cũng không biết làm thế nào. Hay bây giờ em định thế này... Song anh có cho phép nói em mới dám nói...
Rồi dế choắt loanh quanh, băn khoăn. Tôi phải bảo:
- Ðược, chú mình cứ nói thẳng thừng ra nào:
Dế choắt nhìn tôi mà rằng:
- Anh đã nghĩ thương em như thế thì hay là anh đào giúp cho em một cái ngách sang bên nhà anh phòng khi tắt lửa tối đèn có đứa nào đến bắt nạt thì em chạy sang...
Chưa nghe hết câu tôi đã hếch răng, xì một hơi rõ dài rồi, với điệu bộ khinh khỉnh, tôi mắng:
- Hức! Thông ngách sang nhà ta? Dễ nghe nhỉ! Chú mày hôi như cú mèo thế này, ta làm sao chịu được. Thôi im cái điệu hát mưa dầm sụt sùi ấy đi. Ðào tổ nông thì cho chết!
Tôi về không một chút bận tâm.
Một buổi chiều, tôi ra đứng cửa hang như mọi khi, xem hoàng hôn xuống.
Mấy hôm nọ, trời mưa lớn, trên những hồ ao quanh bãi trước mặt, nước dâng trắng mênh mông. Nước đầy và nước mới thì cua cá cũng tấp nập xuôi ngược, thế là bao nhiêu cò, sếu, vạc, cốc, le le, sâm cầm, vịt trời, bồ nông, mòng, két ở các bãi sông xơ xác tận đâu cũng bay cả về vùng nước mới để kiếm mồi. Suốt ngày họ cãi cọ om bốn góc đầm, có khi chỉ vì tranh một mồi tép, có những anh Cò vêu vao ngày ngày bì bõm lội bùn tím cả chân mà vẫn hếch mỏ, chẳng được miếng nào. Khổ quá, những kẻ yếu đuối, vật lộn cật lực thế mà cũng không sống nổi. Tôi đứng trong bóng nắng chiều tỏa xuống ánh nước cửa hang mà suy nghĩ việc đời như thế.
Bỗng thấy chị Cốc từ mặt nước bay lên, đến đậu gần hang tôi, cách có mấy bước. Chừng rớ được món nào, vừa chén xong, chị tìm đến đứng chỗ mát rỉa lông, rỉa cánh và chùi mép.
Tính tôi hay nghịch ranh. Chẳng bận đến tôi, tôi cũng nghĩ mưu trêu chị Cốc. Tôi cất tiếng gọi Dế Choắt. Nghe tiếng thưa, tôi hỏi:
- Chú mình có muốn cùng tớ đùa vui không?
- Ðùa trò gì? Em đương lên cơn hen đây. Hừ hừ...
- Ðùa chơi một tí.
- Hừ hừ... cái gì thế?
- Con mụ Cốc kia kìa.
Dế Choắt ra cửa, hé mắt nhìn chị Cốc. Rồi hỏi tôi:
- Chị Cốc béo xù đứng trước cửa nhà ta ấy hả?
- Ừ.
- Thôi thôi... hừ hừ... Em xin vái cả sáu tay. Anh đừng trêu vào... Anh phải sợ...
Tôi quắc mắt:
- Sợ gì? Mày bảo tao sợ cái gì? Mày bảo tao còn biết sợ ai hơn tao nữa?
- Thưa anh, thế thì... hừ hừ...em xin sợ. Mời anh cứ đùa một mình thôi.
Tôi lại mắng Dế Choắt và bảo:
- Giương mắt ra xem tao trêu con mụ Cốc đây này.
Tôi rình đến lúc chị Cốc rỉa cánh quay đầu lại phía cửa tổ tôi, tôi cất giọng véo von:
Cái Cò, cái Vạc, cái Nông
Ba cái cùng béo, vặt lông cái nào?
Vặt lông cái Cốc cho tao
Tao nấu, tao nướng, tao xào, tao ăn.
Chị Cốc nghe tiếng hát từ trong đất văng vẳng lên, không hiểu như thế ào, giật nẩy hai đầu cánh, muốn bay. Ðến khi định thần lại, chị mới trợn tròn mắt, giương cánh lên như sắp sửa đánh nhau. Chị lò dò về phía cửa hang tôi hỏi:
- Ðứa nào cạnh khoé gì tao thế? Ðứa nào cạnh khoé gì tao thế?
Tôi chui tọt ngay vào hang, lên giường nằm khểnh, bắt chân chữ ngũ. Bụng nghĩ thú vị: "Mày tức thì mày cứ tức, mày ghè vỡ đầu mày ra cho nhỏ đi, nhỏ đến đâu mày cũng không chui nổi vào tổ tao đâu!"
Một tai hoạ đến mà đứa ích kỷ thì không thể biết trước được. Ðó là, không trông thấy tôi, nhưng chị Cốc đã trông thấy Dế Choắt đang loay hoay trong cửa hang, chị Cốc liền quát lớn:
- Mày nói gì?
- Lạy chị, em nói gì đâu?
Rồi Dế Choắt lủi vào.
- Chối hả? Chối này! Chối này.
Mỗi câu "chối này" chị Cốc lại giáng một mỏ xuống. Mỏ Cốc như cái dùi sắt, chọc xuyên cả đất. Rúc trong hang mà bị trúng hai mỏ, Choắt quẹo xương sống lăn ra kêu váng. Núp tận đáy đất mà tôi cũng khiếp, nằm im thít. Nhưng đã hả cơn tức, chị Cốc đứng rỉa lông cánh một lát nữa rồi lại bay là xuống đầm nước, không chút để ý đến cảnh khổ đau vừa gây ra.
Biết chị Cốc đi rồi, tôi mới mon men bò lên. Trông thấy tôi, Dế Choắt khóc thảm thiết.
Tôi hỏi một câu ngớ ngẩn:
- Sao? Sao?
Choắt không dậy được nữa, nằm thoi thóp. Thấy thế tôi hốt hoảng quỳ xuống, nâng đầu Choắt lên mà than rằng:
- Nào tôi đâu biết cơ sự lại ra nông nỗi này! Tôi hối lắm. Tôi hối hận lắm! Anh mà chết là chỉ tại cái tội ngông cuồng dại dột của tôi. Tôi biết làm thế nào bây giờ?
Tôi không ngờ Dế Choắt nói với tôi một câu thế này:
- Thôi, tôi ốm yếu quá rồi, chết cũng được. Nhưng trước khi nhắm mắt, tôi khuyên anh: ở đời mà có thói hung hăng bậy bạ, có óc mà không biết nghĩ, sớm muộn rồi cũng mang vạ vào mình đấy.
Thế rồi Dế Choắt tắt thở. Tôi thương lắm. Vừa thương vừa ăn năn tội mình. Giá tôi không trêu chị Cốc thì đâu đến nỗi Choắt việc gì. Cả tôi nữa, nếu không nhanh chân chạy vào hang thì tôi cũng chết toi rồi.
Tôi đem xác Dế Choắt đến chôn vào một vùng cỏ bùm tum. Tôi đắp thành nấm mộ to. Tôi đứng lặng giờ lâu, nghĩ về bài học đường đời đầu tiên.
===