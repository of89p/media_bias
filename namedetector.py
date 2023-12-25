import string
from string import digits
import re
import time
import lxml.html
import lxml.html.clean
from collections import Counter


from get_articles import obtain_article_info


# f = open("filt.txt", "r")
#
# words_all_text=f.read()
links_arr = []
f = open("links.txt", "r")
links=f.read()
link_arr_all = links.splitlines()
for x in link_arr_all:
    if x.startswith("https://www.straitstimes.com/singapore/politics/"):
        links_arr.append(x)

LIMIT_COUNT = 200
count = 0

total_arr = []

# arr = [["Lose the weight - and the diabetes: S'pore healthcare group's latest battle plan in war against disease", 'Salma Khalik', '5 Aug 2022, 4:02 pm SGT', 'SINGAPORE - Diabetes can be reversed, even in people who have had it for several years.A study in Britain has proven that, and now, Singapore\'s&nbsp;National Healthcare Group (NHG) hopes to show that it can also work for Asians.It is doing so through the Diabetes Reversal Programme, which is aimed at enabling at least some diabetics here to become free of a disease that can lead to severe consequences such as&nbsp;blindness, kidney failure and even death.The trigger to reversing diabetes is to significantly reduce the weight of people who are overweight or obese, the target being a 10 per cent cut or a 15kg reduction over a period of six months.Associate Professor Lim Su Chi, a senior consultant at Khoo Teck Puat Hospital (KTPH) and a principal investigator of the NHG programme, said: "Weight loss is the strongest link to remission. More than half of diabetics here are overweight or obese."The British study, called Direct, or Diabetes Remission Clinical Trial, had found that the majority who were able to achieve the target weight loss were no longer diabetic.Those who remained diabetic after losing more than 15kg had achieved better control of their sugar levels.The study, conducted between 2017 and 2018, involved putting 149 participants on a low-calorie diet. Its findings were published in The Lancet in 2018 and 2019.At the end of the first year of the study, 46 per cent were no longer diabetic. However, not all were able to maintain this, with only 36 per cent staying free of&nbsp;diabetes at the end of the second year.Associate Professor Tang Wern Ee, senior consultant at NHG Polyclinics (NHGP) and the programme\'s lead investigator, said that is still a very good outcome, as it means that more than one in three were&nbsp;free of the disease.Diabetes is a major problem in Singapore, with more than 400,000 people living with the disease. If nothing is done, the number of diabetics here is projected to surpass one million by 2050 and cost the country US$1.8 billion (S$2.5 billion).In 2016, the Ministry of Health (MOH) declared a war on diabetes to try to slow the increase in numbers.People with diabetes are unable to use up the sugar in their blood. This can damage blood vessels as well as reduce oxygen to the heart and brain. Two major contributory factors are obesity&nbsp;and insufficient exercise.Prof Tang said her team would like to see Singapore moving away from just treating the disease to getting more people reverting to a non-diabetic state.The programme will recruit 100 participants aged 21 to 60 with a body mass index (BMI) of between 27 and 45 who have had diabetes for less than six years and do not have complications caused by the disease.A&nbsp;normal BMI for Asians is 18.5 to 22.9.Half of the participants will be with the control group who will continue to be cared for by their doctor.The other half will stop their medication and be put on a very low-calorie liquid diet for three months, or less, should they achieve the target weight loss earlier."The first five days on the liquid diet can be very difficult. They will feel hungry and very tired," said Ms Pauline Xie, NHGP\'s principal dietitian who is part of the study team.By day six though, the body starts to burn the stored fat in the body, which will energise them, she added.After three months, even if they have yet to meet the weight loss target, they would move to phase two,&nbsp;where they will be reintroduced to food, starting with just one meal a day, while still maintaining a low-calorie intake.The study is funded by a $2.6 million grant from the Tanoto Foundation and $1 million from the NHG Fund.The money will be used to pay for the Optifast liquid diet, which retails at $5 per portion, wearables that will track how participants are doing, as well as manpower for the trial.Prof Tang said the study also aims to discover how to change behaviour so that it becomes something diabetics enjoy doing in the long term.The team will interact with participants throughout the programme, to find out what works for them, and what does not.Mr Hafiz Abdul Aziz, 36, is keen to be on the programme. The data engineer, who has a BMI of 32, found out he had diabetes in February this year.&nbsp;“It was quite scary,” he said. He is now eating a lot less, having&nbsp;a banana and one slice of bread for breakfast instead of the large plate of nasi rawon - rice with black beef soup - he used to eat.He is keen to join the programme because he finds it difficult to lose weight on his own. He added: “Thinking&nbsp;long term, I don’t want to have my legs cut off or have my kidneys fail.”The study will take three years in all, and recruitment is in progress. Diabetics who fit the profile and wish to volunteer can find details <a href="https://form.gov.sg/#!/62e74d11140cd300117af97d" rel=" noopener" target="_blank">at this website.</a>'], ['Apex court throws out suit by 24 death row inmates alleging right to counsel violated', 'Selina Lum', '5 Aug 2022, 1:13 am SGT', 'SINGAPORE - In an unprecedented overnight ruling, the Court of Appeal in the early hours on Friday (Aug 5) threw out a suit brought against the Attorney-General by 24 prisoners on death row alleging that their right to access to justice had been violated.One inmate, Abdul Rahim Shapiee, 45, who also brought a separate suit, failed in his last-minute bid to get a stay of his execution.The court, comprising Chief Justice Sundaresh Menon and Justices Tay Yong Kwang and Woo Bih Li, delivered its judgment at about midnight, having deliberated for some seven hours after hearing arguments on Thursday afternoon.In a statement on Friday night, the Central Narcotics Bureau said the executions of Abdul Rahim and a co-accused, Ong Seow Ping, 49, were carried out that day.The two men were jointly tried and convicted in March 2018 of different heroin trafficking charges. Ong was not involved in the current proceedings.The 24 inmates were led by Iskandar Rahmat, the former policeman <a href="https://www.straitstimes.com/singapore/courts-crime/kovan-double-murder-iskandar-found-guilty-of-murder-of-both-victims-sentenced" rel=" noopener" target="_blank">sentenced to death for the 2013 Kovan double murder.</a>On Monday (Aug 1), they filed a civil claim against the Attorney-General, alleging that provisions in the Criminal Procedure Code which empower the courts to impose costs against defence counsel were unconstitutional.The inmates claimed that such costs orders "obstructed" them from appointing lawyers to make legal challenges against their convictions and sentences.On Wednesday (Aug 3), High Court judge See Kee Oon struck out the claim for being "plainly unsustainable".The inmates then appealed.In the appeal hearing held via video conference on Thursday afternoon, Iskandar argued that lawyers were unwilling to represent them because they feared being ordered to pay costs personally.Iskandar also asked the Court of Appeal for more time to gather evidence to support their case.The apex court dismissed the appeal.In a 30-page judgment delivered by Chief Justice Menon, the court said the provisions cannot reasonably deter lawyers from acting in bona fide applications or appeals for death row inmates.Past court rulings have set out that costs orders can only imposed if the proceedings are brought or conducted with some impropriety, such as where they are frivolous, vexatious or an abuse of process."In other words, the true scope of the CPC cost provisions does not impinge on one\'s right of access to justice or right to counsel at all, simply because there is and can be no right to advance a position in court improperly," he said.As for Abdul Rahim, he had sought a stay of execution pending the resolution of an 11th hour negligence suit he filed against his former lawyer on Wednesday.He claimed that the lawyer who was assigned to defend him during his trial had failed to follow his instructions to call a certain witness.But Chief Justice Menon said this claim was without merit and an abuse of process.He noted that the lawsuit was filed five days after Abdul Rahim was notified of his execution.The Chief Justice noted that Abdul Rahim had not raised this issue during his appeal in March 2020, when he was represented by a different lawyer."He did not take any step to act on this until literally days before the sentence was to be carried out."'], ['askST Jobs: My child just entered university. What can she do to stand out in her future job hunt?', 'Calvin Yang', '22 Aug 2022, 7:02 am SGT', 'In this series, manpower correspondent Calvin Yang offers practical answers to candid questions on navigating workplace challenges and getting ahead in your career.<strong>A:</strong> The good news is, times have changed and employers today look beyond good academic qualifications and grades when hiring.Instead, they place strong emphasis on relevant work experience and expect a broad range of skills including digital competency, leadership, analytical thinking, project management and communications skills, said Dr Timothy Chan, vice-provost at SIM Global Education.As for being kiasu (Hokkien for fear of losing out), experts say that it is never too early to start planning and preparing for a career after graduation.Building up one\'s portfolio during the undergraduate years will make the future job search easier, added Ms Linda Teo, country manager at ManpowerGroup Singapore.Dr Chan also said: "It is necessary for university students to think about employability at the start of their courses, not the end. Otherwise, they would have missed the opportunities to acquire the necessary competencies to take competition head on upon their graduation."A good starting point is to have your child tap her university\'s career support office. These offices usually offer services including career profiling, which helps students learn about their personalities, strengths, as well as competency gaps that they need to work on.Your child can also consider having a career mentor to know the ins and outs of working life, said Dr Chan. For instance, if your child aspires to be a chartered accountant, join a mentoring scheme that matches her with an experienced chartered accountant.Outside of school, attending networking events with industry professionals may help job seekers get noticed, while building up contacts for future employment.Not sure what networking events are? They vary from structured ones like workshops and talks to social gatherings such as happy hour meet-ups and school reunions. These can be held by agencies, companies or alumni associations.Undergraduates can maintain these networks using LinkedIn. They can start by connecting with peers and lecturers on the platform, and subsequently add in people they have met.Ms Teo said: "Having an extensive network will help them access more job opportunities, especially in the long run as employers are always looking out for new talent as part of their succession planning."But nothing beats getting real-life working experience through internships and industry projects while in university.If you are lucky, you may even be offered a full-time role upon graduation."Start early and try to do an internship during semester breaks," said Ms Teo. "Completing internships will also add substance to the curriculum vitae and help one to stand out from the other fresh graduate job seekers."With a fast-evolving economy, the skills needed today are constantly changing. As such, the university programme that your child is enrolled in may not cover all the latest in-demand skills.Thankfully, many institutions identify gaps between skills needed in the job market and skills they are teaching, and offer bite-sized courses covering knowledge or experience in a specific subject, said Dr Chan.These short courses, typically aimed at working adults, may even be stacked up towards qualifications such as diplomas. They can be completed within several weeks.Have a question? Send it to <a href="mailto:askst@sph.com.sg">askst@sph.com.sg</a>.'], ['Morning Briefing: Top stories from The Straits Times on Aug 22', 'ERROR', '22 Aug 2022, 7:45 am SGT', 'Good morning! Here are our top stories to kick-start your Monday, Aug 22.Singapore\'s external environment has become very troubled amid worsening US-China ties and Russia\'s invasion of Ukraine.<a href="/singapore/politics/ndr-2022-better-get-real-and-be-prepared-should-things-go-wrong-in-the-region-says-pm-lee" target="_blank">READ MORE HERE</a>Key to such trust - in fact, underpinning it - is a sense of national identity and unity, says ST Political Editor Zakir Hussain.<a href="/singapore/politics/national-day-rally-2022-trust-unity-will-be-key-in-post-covid-19-world" target="_blank">READ MORE HERE</a>The move will improve the lived realities of gay men, and their families, significantly, says ST Associate Editor Chua Mui Hoong.<a href="/singapore/politics/national-day-rally-2022-s377a-repeal-a-courageous-move-with-symbolic-and-real-impact" target="_blank">READ MORE HERE</a>What will the new T5 look like? What is unique about the new town at the Paya Lebar Air Base site?<a href="/singapore/interactive-big-plans-for-changi-airport-t5-take-off" target="_blank">READ MORE HERE</a>Other highlights include building new homes in Paya Lebar and attracting top talent.<a href="/singapore/politics/8-highlights-from-ndr-2022-masks-optional-in-most-indoor-settings-section-377a-to-be-repealed" target="_blank">READ MORE HERE</a>Wife gets organ from a medically compatible donor while husband’s kidney is given to the donor’s loved one.<a href="/singapore/health/woman-37-gets-a-new-lease-of-life-after-her-husband-donates-his-kidney-in-a-transplant-swop" target="_blank">READ MORE HERE</a>Enrolment at student care centres registered with the Government jumped from 27,000 in 2016 to 40,000 today.<a href="/singapore/parenting-education/rise-in-demand-for-student-care-services-as-providers-up-the-game-with-mindfulness-enrichment-classes" target="_blank">READ MORE HERE</a>House Speaker Nancy Pelosi’s recent visit highlighted the tensions between Congress and the White House on their ties with Taipei. Greater discord looms with new legislative measures in the works and the upcoming mid-term elections in the US.<a href="/opinion/powerplay-more-dissonance-ahead-in-us-duet-on-taiwan" target="_blank">READ MORE HERE</a>It is the first concert held at the venue since the Covid-19 pandemic struck in 2020.<a href="/life/entertainment/pop-star-billie-eilish-performs-to-crowd-of-30000-at-national-stadium" target="_blank">READ MORE HERE</a>Astley released the song on July 27, 1987 when he was 21.<a href="/life/entertainment/singer-rick-astley-recreates-iconic-never-gonna-give-you-up-music-video-35-years-after-release" target="_blank">READ MORE HERE</a>']]
for link in links_arr:
    if count == LIMIT_COUNT:
        break


    # words_all_text = x[3]

    words_all_text = obtain_article_info(link)[3]
    # print(words_all_text)


    doc = lxml.html.fromstring(words_all_text)
    cleaner = lxml.html.clean.Cleaner(style=True)
    doc = cleaner.clean_html(doc)
    words_all_text = doc.text_content()

    # remove_digits = str.maketrans('', '', digits)
    # words_all_text = words_all_text.translate(remove_digits)
    # words_all_text=''.join([i for i in words_all_text if not i.isdigit()])



    words_all_text=words_all_text.replace('-', '  ')
    words_all_text=words_all_text.replace('“', '  ')
    words_all_text=words_all_text.replace('”', '  ')
    words_all_text=words_all_text.replace('’s', '  ')
    words_all_text = words_all_text.replace("'s", "")
    words_all_text=words_all_text.replace('’', '  ')
    words_all_text = words_all_text.replace('.', '  ')
    words_all_text = ''.join([i for i in words_all_text if not i.isdigit()])
    # words_all_text = words_all_text.lower()


    words = words_all_text.split()

    # print(words)


    dictionary = open("./clean_up_data/improve_dictionary/out3.txt", "r")
    # dictionary = open("new_dict.txt", "r")

    dics_arr = dictionary.read().split()

    dic_arr = []

    for x in dics_arr:
        x = x.lower()
        dic_arr.append(x)

    not_in_dic_words = []
    new_name = ''
    names = []
    repeat = False

    for ix, x in enumerate(words):
        x = x.translate(str.maketrans('', '', string.punctuation))
        x =x.lower()

        # regex = re.compile('[^a-zA-Z]')
        # # First parameter is the replacement, second parameter is your input string
        # words_all_text = regex.sub('', words_all_text)

        if x in dic_arr:
            not_in_dic_words.append([ix, x])

    # print(not_in_dic_words)

    for iy, y in enumerate(not_in_dic_words):
        if iy==len(not_in_dic_words)-1:
            break
        # print(not_in_dic_words[iy][0],not_in_dic_words[iy+1][0] )
        diff_with_prev_element =not_in_dic_words[iy+1][0] - not_in_dic_words[iy][0]

        if diff_with_prev_element == 1 and not repeat:
            new_name = not_in_dic_words[iy][1] + " " + not_in_dic_words[iy + 1][1]
            # print(new_name)
            repeat = True
        elif diff_with_prev_element == 1 and repeat:
            new_name = new_name + " " + not_in_dic_words[iy + 1][1]

        elif diff_with_prev_element > 1 and repeat:
            repeat = False
            names.append(new_name)
            new_name = ''

    final_names = []

    # Check for repeated names
    for x in names:
        if x not in final_names:
            final_names.append(x)
            total_arr.append(x)
    # print(names)
    print(final_names)


    count += 1
    print("CURRENT COUNT: "+str(count))
    time.sleep(5)


total_count = Counter(total_arr)
print(total_count)



    #removed: lee, tan, yang, ee, see, su, chi
    #added: singaporean





