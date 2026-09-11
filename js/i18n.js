/* R2-IWAA — Myanmar / English toggle.
 * Approach: text-node replacement keyed on the exact English string
 * currently in the HTML. Toggle in header sets a cookie so the choice
 * persists across pages. The <html lang> attribute is set immediately by
 * an inline script in <head> (see build.py) so Myanmar font applies before
 * paint.
 *
 * To CORRECT a Myanmar translation: find the English key in DICT below
 * and replace the Myanmar value. Nothing else needs to change.
 */
(function () {
  'use strict';

  var DICT = {
    // ---------- header / nav ----------
    'IV Therapy': 'အိုင်ဗီပြုစုကုသမှု',
    'Locations': 'တည်နေရာများ',
    'Dr. Tony Su': 'ဒေါက်တာတိုနီစူ',
    'Consultation': 'ဆွေးနွေးတိုင်ပင်ခြင်း',
    'Menu': 'မီနူး',

    // ---------- footer ----------
    'R2-IWAA': 'R2-IWAA',
    'R2 International Wellness & Anti-Aging. Physician-led regenerative and anti-aging medicine, with its medical and training centre in Taipei.':
      'R2 နိုင်ငံတကာ ကျန်းမာရေးနှင့် အသက်ဆန်ကုသရေး။ ဆရာဝန်ဦးဆောင်သော ပြန်လည်ဖြစ်ထွန်းစေသော ကုသနည်းများ၊ တိုင်ပေတွင် ဆေးဘက်ဆိုင်ရာနှင့် သင်တန်းစင်တာဖြင့်။',
    'Care': 'ကုသမှု',
    'Advanced Regenerative Care': 'အဆင့်မြင့် ပြန်လည်ဖြစ်ထွန်းစေသောကုသမှု',
    'Visit': 'လာရောက်ရန်',
    'Taipei · Yangon · Ho Chi Minh City': 'တိုင်ပေ · ရန်ကုန် · ဟိုချီမင်းစီးတီး',
    'Request a consultation': 'ဆွေးနွေးတိုင်ပင်မှုအတွက် တောင်းဆိုပါ',
    '© 2023 R2 International Wellness & Anti-Aging': '© 2023 R2 နိုင်ငံတကာ ကျန်းမာရေးနှင့် အသက်ဆန်ကုသရေး',
    'Availability of individual therapies is confirmed at consultation and differs by location.':
      'တစ်ဦးချင်း ကုသနည်းများ ရရှိနိုင်မှုသည် ဆွေးနွေးတိုင်ပင်ချိန်တွင် အတည်ပြုပြီး တည်နေရာအလိုက် ကွဲပြားနိုင်ပါသည်။',

    // ---------- invite band (shared) ----------
    'One to one': 'တစ်ဦးချင်း',
    'Every plan begins with a': 'အစီအစဉ်တိုင်း စတင်သည်မှာ',
    'conversation.': 'ဆွေးနွေးမှုဖြင့်ဖြစ်သည်။',
    'A private consultation with our medical team — your history, your goals, and an honest view of what is appropriate for you.':
      'ကျွန်ုပ်တို့၏ ဆေးဘက်ဆိုင်ရာအဖွဲ့နှင့် သီးသန့်ဆွေးနွေးမှု — သင့်ရာဇဝင်၊ သင့်ရည်မှန်းချက်များနှင့် သင့်အတွက် သင့်လျော်သည့်အရာအား ရိုးသားစွာ ကြည့်မြင်ပေးမည်။',

    // ---------- home ----------
    'R2 International Wellness & Anti-Aging': 'R2 နိုင်ငံတကာ ကျန်းမာရေးနှင့် အသက်ဆန်ကုသရေး',
    'Medicine,': 'ဆေးဝါးသည်၊',
    'calibrated': 'သင့်အတွက်',
    'to you.': 'ချိန်ညှိထားသည်။',
    'Physician-led regenerative care across Taipei, Yangon and Ho Chi Minh City.':
      'တိုင်ပေ၊ ရန်ကုန်နှင့် ဟိုချီမင်းစီးတီးအနှံ့ ဆရာဝန်ဦးဆောင်သော ပြန်လည်ဖြစ်ထွန်းစေသောကုသမှု။',

    'Our foundation. Available at every R2 location.': 'ကျွန်ုပ်တို့၏ အခြေခံ။ R2 တည်နေရာတိုင်းတွင် ရရှိနိုင်သည်။',
    'Regenerative Care': 'ပြန်လည်ဖြစ်ထွန်းစေသောကုသမှု',
    'Advanced options, offered by physician consultation.': 'အဆင့်မြင့်ရွေးချယ်စရာများ၊ ဆရာဝန်နှင့် တိုင်ပင်ပြီးမှ ကမ်းလှမ်းသည်။',
    'Physician-Led': 'ဆရာဝန်ဦးဆောင်',
    'Founded and directed by Dr. Tony Su in Taipei.': 'တိုင်ပေတွင် ဒေါက်တာတိုနီစူမှ တည်ထောင်၍ ဦးဆောင်ပါသည်။',

    'The foundation': 'အခြေခံ',
    'Intravenous therapy,': 'အိုင်ဗီပြုစုကုသမှုသည်၊',
    'built around you': 'သင့်အတွက် အထူးပြုလုပ်ထားသည်',
    '.': '။',
    'Hydration, vitamins, minerals and amino acids delivered directly — chosen from your bloodwork and how you actually live.':
      'ရေဓာတ်၊ ဗီတာမင်များ၊ သတ္တုဓာတ်များနှင့် အမီနိုအက်ဆစ်များကို တိုက်ရိုက်ပေးသည် — သင့်သွေးစစ်ရလဒ်နှင့် သင့်အသက်တာအခြေအနေမှ ရွေးချယ်သည်။',
    'See IV programmes →': 'အိုင်ဗီအစီအစဉ်များကို ကြည့်ရန် →',

    'The difference': 'ကွဲပြားချက်',
    'Why patients stay with us.': 'လူနာများ ကျွန်ုပ်တို့နှင့် ဆက်လက်နေထိုင်ရသည့် အကြောင်း။',
    'Every plan is written by a physician after examination and bloodwork — never chosen from a menu.':
      'အစီအစဉ်တိုင်းကို ဆရာဝန်က စစ်ဆေးပြီး သွေးစစ်ပြီးမှသာ ရေးသည် — မီနူးမှ ရွေးခြင်း လုံးဝမရှိပါ။',
    'One patient at a time, in a private suite, with unhurried time to ask anything.':
      'တစ်ကြိမ်လျှင် လူနာတစ်ဦးသာ၊ သီးသန့်အခန်းတွင်၊ မည်သည့်အရာမဆို မေးမြန်းရန် လုံလုံလောက်လောက် အချိန်ဖြင့်။',
    'Materials and protocols come from one source in Taipei, so quality does not change by city.':
      'ဆေးပစ္စည်းများနှင့် နည်းစနစ်များသည် တိုင်ပေမှ တစ်နေရာတည်းမှ ရရှိသည်၊ ထို့ကြောင့် အရည်အသွေးသည် မြို့အလိုက် မပြောင်းလဲပါ။',
    'Mandarin, English and Myanmar spoken directly by your physician, with no interpreter in between.':
      'သင့်ဆရာဝန်ကိုယ်တိုင် တရုတ်၊ အင်္ဂလိပ်နှင့် မြန်မာဘာသာဖြင့် တိုက်ရိုက်ပြောဆိုသည်၊ ကြားပြောသူ မလိုအပ်ပါ။',

    'Advanced regenerative care': 'အဆင့်မြင့် ပြန်လည်ဖြစ်ထွန်းစေသောကုသမှု',
    'Selected therapies,': 'ရွေးချယ်ထားသော ကုသနည်းများ၊',
    'by consultation': 'တိုင်ပင်၍သာ',
    'Where the evidence and your assessment support it, our medical team may discuss advanced regenerative options with you.':
      'သက်သေအထောက်အထားများနှင့် သင့်အား စစ်ဆေးမှုက ထောက်ခံပါက ကျွန်ုပ်တို့၏ ဆေးဘက်ဆိုင်ရာအဖွဲ့သည် အဆင့်မြင့် ပြန်လည်ဖြစ်ထွန်းစေသောရွေးချယ်စရာများကို သင်နှင့် ဆွေးနွေးနိုင်ပါသည်။',
    'Learn more →': 'ပိုမိုလေ့လာရန် →',

    'Taipei': 'တိုင်ပေ',
    'One standard,': 'တစ်ခုတည်းသောစံနှုန်း၊',
    'three cities': 'သုံးမြို့',
    'Our Taipei centre trains every clinical team and prepares the materials used in Yangon and Ho Chi Minh City — so care does not change when the city does.':
      'ကျွန်ုပ်တို့၏ တိုင်ပေစင်တာသည် ဆေးဘက်ဆိုင်ရာအဖွဲ့တိုင်းကို သင်တန်းပေးပြီး ရန်ကုန်နှင့် ဟိုချီမင်းစီးတီးတွင် အသုံးပြုသည့် ဆေးပစ္စည်းများကို ပြင်ဆင်ပေးသည် — ထို့ကြောင့် မြို့ပြောင်းသည့်အခါ ကုသမှုသည် မပြောင်းလဲပါ။',
    'Our locations →': 'ကျွန်ုပ်တို့၏တည်နေရာများ →',

    'Training': 'သင်တန်း',
    'Clinical teams are taught and re-certified in Taipei before they treat anyone.':
      'ဆေးဘက်ဆိုင်ရာအဖွဲ့များသည် လူနာကုသရန်မတိုင်မီ တိုင်ပေတွင် သင်တန်းယူ၍ ပြန်လည်လက်မှတ်ရရှိသည်။',
    'Supply': 'ဆေးပစ္စည်း',
    'Materials are prepared, checked and dispatched under cold chain to each clinic.':
      'ဆေးပစ္စည်းများကို ပြင်ဆင်၊ စစ်ဆေးပြီး အအေးခံသယ်ယူပို့ဆောင်ရေးဖြင့် ဆေးခန်းတစ်ခုစီသို့ ပို့ဆောင်သည်။',

    'Founder': 'တည်ထောင်သူ',
    'Founder and Medical Director. He leads every clinical protocol at R2-IWAA and trains the teams that deliver it.':
      'တည်ထောင်သူနှင့် ဆေးဘက်ဆိုင်ရာ ဒါရိုက်တာ။ သူသည် R2-IWAA တွင် ဆေးဘက်ဆိုင်ရာနည်းစနစ်တိုင်းကို ဦးဆောင်ပြီး ပေးဆောင်သည့်အဖွဲ့များကို သင်တန်းပေးသည်။',
    'Mandarin': 'တရုတ်',
    'English': 'အင်္ဂလိပ်',
    'Myanmar': 'မြန်မာ',
    'About Dr. Su →': 'ဒေါက်တာစူအကြောင်း →',

    'Where to find us': 'ကျွန်ုပ်တို့ကို ရှာဖွေရန်',
    'Three clinics,': 'ဆေးခန်းသုံးခု၊',
    'one network': 'ကွန်ရက်တစ်ခု',
    'Main centre': 'ပင်မစင်တာ',
    'Taipei — R2-IWAA': 'တိုင်ပေ — R2-IWAA',
    'Shilin District, Taipei. R2-IWAA main center, clinical training and materials preparation.':
      'ရှီလင်ခရိုင်၊ တိုင်ပေ။ R2-IWAA ပင်မစင်တာ၊ ဆေးဘက်ဆိုင်ရာသင်တန်းနှင့် ဆေးပစ္စည်းပြင်ဆင်ခြင်း။',
    'Yangon': 'ရန်ကုန်',
    'Beauty Bank Wellness Center': 'Beauty Bank Wellness Center',
    'Kamaryut Township, Yangon. Assessment, IV therapy and procedures.':
      'ကမာရွတ်မြို့နယ်၊ ရန်ကုန်။ စစ်ဆေးမှု၊ အိုင်ဗီပြုစုကုသမှုနှင့် လုပ်ငန်းစဉ်များ။',
    'Ho Chi Minh City': 'ဟိုချီမင်းစီးတီး',
    'Recover Health': 'Recover Health',
    'Xuân Hòa Ward, Ho Chi Minh City. Assessment, IV therapy and procedures.':
      'Xuân Hòa Ward၊ ဟိုချီမင်းစီးတီး။ စစ်ဆေးမှု၊ အိုင်ဗီပြုစုကုသမှုနှင့် လုပ်ငန်းစဉ်များ။',

    // ---------- iv therapy page ----------
    'Our foundation,': 'ကျွန်ုပ်တို့၏အခြေခံ၊',
    'everywhere': 'နေရာတိုင်း',
    'we practise.': 'တွင် ကုသသည်။',
    'The same protocols, the same materials, the same standard in Taipei, Yangon and Ho Chi Minh City.':
      'တိုင်ပေ၊ ရန်ကုန်နှင့် ဟိုချီမင်းစီးတီးတွင် တူညီသောနည်းစနစ်များ၊ တူညီသောဆေးပစ္စည်းများ၊ တူညီသောစံနှုန်း။',

    'Programmes': 'အစီအစဉ်များ',
    'Chosen for you,': 'သင့်အတွက် ရွေးချယ်ထားသည်၊',
    'not from a menu': 'မီနူးမှမဟုတ်',
    'Every programme starts from your history, examination and bloodwork. Composition and pace are set by your physician.':
      'အစီအစဉ်တိုင်းသည် သင့်ရာဇဝင်၊ စစ်ဆေးမှုနှင့် သွေးစစ်ရလဒ်မှ စတင်သည်။ ဖွဲ့စည်းမှုနှင့် အရှိန်အဟုန်ကို သင့်ဆရာဝန်က သတ်မှတ်သည်။',

    'How a visit runs': 'လာရောက်မှုတစ်ခု၏ လုပ်ငန်းစဉ်',
    'Unhurried, and never improvised.': 'အလျင်စလိုမလုပ်၊ တစ်ခါမှ လွှတ်တင်၍မဆောင်ရွက်ပါ။',
    'Consultation and review of your history and goals.': 'ဆွေးနွေးတိုင်ပင်ခြင်းနှင့် သင့်ရာဇဝင်၊ ရည်မှန်းချက်များကို သုံးသပ်ခြင်း။',
    'Bloodwork where it changes the plan.': 'အစီအစဉ်ကို ပြောင်းလဲစေမည့်နေရာတွင် သွေးစစ်ခြင်း။',
    'Your programme, written and explained.': 'သင့်အစီအစဉ်ကို ရေးသား၍ ရှင်းပြခြင်း။',
    'Treatment in a private suite, 45–90 minutes.': 'သီးသန့်အခန်းတွင် ကုသမှု၊ ၄၅ – ၉၀ မိနစ်။',

    'Beyond the foundation': 'အခြေခံထက်လွန်၍',
    'Advanced': 'အဆင့်မြင့်',
    'regenerative': 'ပြန်လည်ဖြစ်ထွန်းစေသော',
    'care.': 'ကုသမှု။',
    'Some patients are assessed for options that go further than intravenous nutrition. These are discussed individually, never sold from a list.':
      'အချို့လူနာများသည် အိုင်ဗီအာဟာရထက် ပိုမိုသည့် ရွေးချယ်စရာများအတွက် စစ်ဆေးခံရသည်။ ဤအရာများကို တစ်ဦးချင်း ဆွေးနွေးသည်၊ စာရင်းမှ ရောင်းချခြင်း လုံးဝမရှိပါ။',

    // ---------- advanced-care page ----------
    'Discussed': 'တစ်ဦးချင်း',
    'individually': 'ဆွေးနွေးသည်',
    'These therapies are not for everyone, and they are not offered from a price list. Each is considered only after full medical assessment.':
      'ဤကုသနည်းများသည် လူတိုင်းအတွက်မဟုတ်ပါ၊ ဈေးနှုန်းစာရင်းမှလည်း ကမ်းလှမ်းခြင်းမရှိပါ။ တစ်ခုစီကို ဆေးဘက်ဆိုင်ရာ အပြည့်အဝ စစ်ဆေးပြီးမှသာ ထည့်သွင်းစဉ်းစားသည်။',

    'What we may discuss': 'ကျွန်ုပ်တို့ ဆွေးနွေးနိုင်သည်များ',
    'A short,': 'တိုတောင်း၍၊',
    'honest': 'ရိုးသားသော',
    'list.': 'စာရင်း။',
    'What is appropriate for you depends on your assessment, and what is available depends on where you are treated. Your physician will tell you both, plainly, before anything begins.':
      'သင့်အတွက် သင့်လျော်သည့်အရာသည် သင့်စစ်ဆေးမှုပေါ်တွင် မူတည်၍ ရရှိနိုင်သည့်အရာသည် သင်ကုသရာ တည်နေရာပေါ်တွင် မူတည်သည်။ သင့်ဆရာဝန်သည် အရာမစခင် နှစ်ခုစလုံးကို ရိုးရိုးလင်းလင်း ပြောပြပါမည်။',

    'Apheresis': 'သွေးခွဲထုတ်ခြင်း',
    'Therapeutic Plasma Exchange': 'ကုသရေး ပလာစမာလဲလှယ်ခြင်း',
    'Blood plasma is separated and replaced with sterile albumin and saline; your blood cells are returned to circulation. Used to lower circulating inflammatory and metabolic factors.':
      'သွေးပလာစမာကို ခွဲထုတ်ပြီး သန့်ရှင်းသော albumin နှင့် ဆားရေဖြင့် အစားထိုးသည်၊ သင့်သွေးဆဲလ်များကို လည်ပတ်မှုသို့ ပြန်ပို့သည်။ လည်ပတ်နေသော ရောင်ရမ်းမှုနှင့် ဇီဝဖြစ်ပျက်မှုအချက်များကို လျှော့ချရန် အသုံးပြုသည်။',
    'Adults with chronic inflammatory burden, elevated cardiometabolic markers, or persistent post-viral fatigue — where laboratory workup supports it.':
      'နာတာရှည် ရောင်ရမ်းမှုဝန်ထုပ်၊ မြင့်တက်နေသော နှလုံးဇီဝဖြစ်ပျက်မှုအမှတ်အသားများ သို့မဟုတ် ဗိုင်းရပ်စ်ဖြစ်ပြီးနောက် ဆက်လက်ဖြစ်နေသော ပင်ပန်းနွမ်းနယ်မှုရှိသော အရွယ်ရောက်ပြီးသူများ — ဓာတ်ခွဲစစ်ဆေးမှုက ထောက်ခံပါက။',
    'Setting': 'ဆောင်ရွက်ရာနေရာ',
    'Taipei clinic only, under continuous physician supervision': 'တိုင်ပေဆေးခန်းတွင်သာ၊ ဆရာဝန်၏ ဆက်လက်ကြီးကြပ်မှုအောက်တွင်',
    'Session': 'တစ်ကြိမ်',
    'About 2 to 3 hours per procedure, cyclic apheresis system': 'တစ်ကြိမ်လျှင် ၂ မှ ၃ နာရီခန့်၊ cyclic apheresis စနစ်',
    'Course': 'သင်တန်း',
    'Typically a short assessed course, spaced weekly or monthly': 'ပုံမှန်အားဖြင့် အကဲဖြတ်ထားသော တိုတောင်းသည့်သင်တန်း၊ တစ်ပတ်လျှင် သို့မဟုတ် တစ်လလျှင် တစ်ကြိမ်',
    'Before': 'မတိုင်မီ',
    'Full blood panel, cardiac and coagulation screen required': 'သွေးအပြည့်စစ်ဆေးမှု၊ နှလုံးနှင့် သွေးခဲမှုစစ်ဆေးမှု လိုအပ်သည်',

    'Regenerative': 'ပြန်လည်ဖြစ်ထွန်းစေသော',
    'Mesenchymal Cell Therapy': 'Mesenchymal ဆဲလ်ကုသနည်း',
    'An intravenous cell therapy using mesenchymal cells prepared under laboratory conditions. Studied for immunomodulatory and tissue-support effects.':
      'ဓာတ်ခွဲခန်းအခြေအနေတွင် ပြင်ဆင်ထားသော mesenchymal ဆဲလ်များကို အသုံးပြု၍ အိုင်ဗီဆဲလ်ကုသနည်း။ ကိုယ်ခံအားညှိနှိုင်းမှုနှင့် တစ်ရှူးထောက်ပံ့မှုအတွက် လေ့လာထားသည်။',
    'Selected regenerative and inflammatory profiles, and only where local regulation permits treatment. Not a routine service in every location.':
      'ရွေးချယ်ထားသော ပြန်လည်ဖြစ်ထွန်းစေမှုနှင့် ရောင်ရမ်းမှုပရိုဖိုင်များ၊ ဒေသတွင်း စည်းမျဉ်းက ကုသမှုကို ခွင့်ပြုသည့်နေရာတွင်သာ။ တည်နေရာတိုင်းတွင် ပုံမှန်ဝန်ဆောင်မှုမဟုတ်ပါ။',
    'Delivered at partner clinics where locally permitted': 'ဒေသတွင်း ခွင့်ပြုသည့် အဖွဲ့ဝင်ဆေးခန်းများတွင် ဆောင်ရွက်သည်',
    'Slow intravenous infusion, 1 to 2 hours': 'ဖြည်းညှင်းစွာ အိုင်ဗီသွင်းခြင်း၊ ၁ မှ ၂ နာရီ',
    'Single infusion or short course, defined after assessment': 'တစ်ကြိမ်သွင်းခြင်း သို့မဟုတ် တိုတောင်းသည့်သင်တန်း၊ စစ်ဆေးပြီးမှ သတ်မှတ်သည်',
    'Cell product traceability documentation provided to the patient': 'ဆဲလ်ထုတ်ကုန်၏ ခြေရာခံနိုင်မှုစာရွက်စာတမ်းများကို လူနာအား ပေးအပ်သည်',

    'Exosome Intravenous Therapy': 'Exosome အိုင်ဗီပြုစုကုသနည်း',
    'An intravenous course of extracellular vesicles (exosomes) from mesenchymal cells. Given as a short, physician-directed series, usually layered onto an IV hydration plan.':
      'Mesenchymal ဆဲလ်များမှ ဆဲလ်ပြင်ပ vesicle များ (exosomes) ကို အိုင်ဗီသင်တန်း။ တိုတောင်း၍ ဆရာဝန်ညွှန်ကြားသည့် အစီအစဉ်အဖြစ် ပေးသည်၊ များသောအားဖြင့် အိုင်ဗီရေဓာတ်ဖြည့်အစီအစဉ်ပေါ်တွင် ထပ်၍ ဆောင်ရွက်သည်။',
    'Adults seeking regenerative support alongside a wider wellness plan. Availability depends on your assessment and on local regulation.':
      'ကျယ်ပြန့်သော ကျန်းမာရေးအစီအစဉ်နှင့်အတူ ပြန်လည်ဖြစ်ထွန်းစေမှုအထောက်အပံ့ ရှာဖွေနေသော အရွယ်ရောက်ပြီးသူများ။ ရရှိနိုင်မှုသည် သင့်စစ်ဆေးမှုနှင့် ဒေသတွင်းစည်းမျဉ်းပေါ်တွင် မူတည်သည်။',
    'Intravenous infusion, approximately 60 to 90 minutes': 'အိုင်ဗီသွင်းခြင်း၊ အနီးစပ်ဆုံး ၆၀ မှ ၉၀ မိနစ်',
    'Typically 3 to 6 sessions, planned individually': 'ပုံမှန်အားဖြင့် ၃ မှ ၆ ကြိမ်၊ တစ်ဦးချင်း စီစဉ်ထားသည်',
    'Pairs with': 'တွဲဖက်သည်',
    'Precision IV hydration and recovery protocols': 'တိကျသော အိုင်ဗီရေဓာတ်ဖြည့်နှင့် ပြန်လည်နာလန်ထူရေး နည်းစနစ်များ',

    'Orthopaedic': 'အရိုးအကြောဆိုင်ရာ',
    'Exosome Knee Programme': 'Exosome ဒူးအစီအစဉ်',
    'An in-joint (intra-articular) exosome course for knee osteoarthritis, paired with a structured rehabilitation and load-management plan.':
      'ဒူးအရိုးအဆစ်ရောင်ရမ်းရောဂါအတွက် အဆစ်တွင်း (intra-articular) exosome သင်တန်း၊ ဖွဲ့စည်းထားသော ပြန်လည်ထူထောင်ရေးနှင့် ဝန်ထုပ်စီမံခန့်ခွဲမှုအစီအစဉ်နှင့် တွဲဖက်ထားသည်။',
    'Adults with imaging-confirmed knee osteoarthritis, aiming to reduce symptoms and support function. Not a substitute for surgical care where indicated.':
      'ဓာတ်မှန်ဖြင့် အတည်ပြုထားသော ဒူးအရိုးအဆစ်ရောင်ရမ်းရောဂါရှိသော အရွယ်ရောက်ပြီးသူများ၊ ရောဂါလက္ခဏာများ လျှော့ချရန်နှင့် လုပ်ဆောင်နိုင်စွမ်း ထောက်ပံ့ရန်။ ခွဲစိတ်ကုသမှုကို အစားထိုးရန်မဟုတ်ပါ။',
    'Guided intra-articular injection under aseptic conditions': 'ပိုးမွှားကင်းစင်သည့်အခြေအနေတွင် လမ်းညွှန်ထားသော အဆစ်တွင်း ဆေးထိုးခြင်း',
    'Typically a short series over several weeks': 'ပုံမှန်အားဖြင့် သီတင်းအနည်းငယ်အတွင်း တိုတောင်းသည့်အစီအစဉ်',
    'Includes': 'ပါဝင်သည်',
    'Rehabilitation guidance and follow-up review': 'ပြန်လည်ထူထောင်ရေး လမ်းညွှန်ချက်နှင့် ဆက်လက်ကြည့်ရှုမှု',

    'Photomedicine': 'အလင်းဆေးပညာ',
    'Intravenous Laser Therapy': 'အိုင်ဗီ လေဆာကုသနည်း',
    'Low-level intravascular light at specific wavelengths, delivered through a fine intravenous line. Used as an adjunct to IV protocols — not a stand-alone treatment.':
      'သွေးကြောအတွင်း အနိမ့်စား အလင်းရောင်၊ တိကျသော လှိုင်းအရှည်များဖြင့် သေးငယ်သော အိုင်ဗီလိုင်းမှတဆင့် ပေးသည်။ အိုင်ဗီနည်းစနစ်များ၏ ဖြည့်စွက်ကုသမှုအဖြစ် အသုံးပြုသည် — သီးသန့်ကုသမှုမဟုတ်ပါ။',
    'Adults on a planned IV course seeking additional support alongside hydration or recovery protocols.':
      'ရေဓာတ်ဖြည့်ခြင်း သို့မဟုတ် ပြန်လည်နာလန်ထူရေးနည်းစနစ်များနှင့်အတူ ထပ်ဆောင်းအထောက်အပံ့ရှာဖွေနေသော အိုင်ဗီသင်တန်းစီစဉ်ထားသည့် အရွယ်ရောက်ပြီးသူများ။',
    'Available at Taipei and selected partner clinics': 'တိုင်ပေနှင့် ရွေးချယ်ထားသော အဖွဲ့ဝင်ဆေးခန်းများတွင် ရရှိနိုင်သည်',
    'Approximately 30 to 60 minutes, alongside IV therapy': 'အနီးစပ်ဆုံး ၃၀ မှ ၆၀ မိနစ်၊ အိုင်ဗီပြုစုကုသမှုနှင့်အတူ',
    'Short series, aligned with your IV plan': 'တိုတောင်းသည့်အစီအစဉ်၊ သင့်အိုင်ဗီအစီအစဉ်နှင့် ချိန်ညှိထားသည်',
    'Precision IV hydration, recovery, neuro-support protocols': 'တိကျသော အိုင်ဗီရေဓာတ်ဖြည့်၊ ပြန်လည်နာလန်ထူရေး၊ အာရုံကြောထောက်ပံ့မှုနည်းစနစ်များ',

    'Who it may suit': 'သင့်လျော်နိုင်သူ',
    'How we speak about outcomes': 'ရလဒ်များအကြောင်း ကျွန်ုပ်တို့ ပြောဆိုပုံ',
    'Considered, and': 'ဂရုတစိုက်ဆင်ခြင်၍၊',
    'told plainly': 'ရိုးရိုးလင်းလင်း ပြောပြသည်',
    'Regenerative medicine is a developing field. We will tell you what is established, what is still being studied, and what we simply do not know — including when the honest answer is that a therapy is not right for you.':
      'ပြန်လည်ဖြစ်ထွန်းစေသောဆေးပညာသည် ဖွံ့ဖြိုးဆဲနယ်ပယ်ဖြစ်သည်။ တည်ငြိမ်နေပြီးသောအရာ၊ ဆက်လက်လေ့လာနေဆဲအရာနှင့် ကျွန်ုပ်တို့ ရိုးရိုးမသိသေးသောအရာများကို သင့်အား ပြောပြပါမည် — ကုသနည်းတစ်ခုသည် သင့်အတွက် သင့်လျော်ခြင်းမရှိဟု ရိုးသားစွာဖြေဆိုရသည့်အခါလည်း အပါအဝင်ဖြစ်သည်။',

    // ---------- founder page ----------
    'Founder & Medical Director': 'တည်ထောင်သူနှင့် ဆေးဘက်ဆိုင်ရာဒါရိုက်တာ',
    'He writes the protocols, trains the teams, and sees patients himself.': 'သူသည် နည်းစနစ်များကို ရေးသား၍ အဖွဲ့များကို သင်တန်းပေးပြီး လူနာများကို ကိုယ်တိုင်ကြည့်သည်။',

    'Approach': 'ချဉ်းကပ်ပုံ',
    'Calibration over': 'ချိန်ညှိမှုက',
    'catalogue': 'စာရင်းထက်',
    'Dr. Su\u2019s position is simple: a patient receives what their biology asks for, at the pace their life allows — not the package on offer. Every protocol used across the network is written and reviewed by him, and reviewed again when the evidence moves.':
      'ဒေါက်တာစူ၏ ရပ်တည်ချက်သည် ရိုးရှင်းသည်: လူနာသည် သူတို့၏ ဇီဝဗေဒက တောင်းဆိုသည့်အရာကို သူတို့၏ဘဝက ခွင့်ပြုသည့်အရှိန်ဖြင့် ရရှိသည် — ကမ်းလှမ်းသည့်ပက်ကေ့ချ်ကို မဟုတ်ပါ။ ကွန်ရက်တစ်ခုလုံးတွင် အသုံးပြုသည့် နည်းစနစ်တိုင်းကို သူကိုယ်တိုင် ရေးသား၍ ပြန်လည်သုံးသပ်ပြီး သက်သေအထောက်အထားများ ပြောင်းလဲသည့်အခါ ထပ်မံသုံးသပ်သည်။',
    'Internal medicine': 'ပြင်ပဆေးပညာ',
    'Precision medicine': 'တိကျသောဆေးပညာ',
    'Cellular & anti-aging medicine': 'ဆဲလ်နှင့် အသက်ဆန်ကုသဆေးပညာ',

    'A regenerative plan should follow bloodwork, not a brochure. That is the standard I hold every R2-IWAA physician to.':
      'ပြန်လည်ဖြစ်ထွန်းစေမည့်အစီအစဉ်သည် သွေးစစ်ရလဒ်ကို လိုက်နာသင့်သည်၊ လက်ကမ်းစာစောင်ကို မဟုတ်ပါ။ ထိုသည်ကား R2-IWAA ဆရာဝန်တိုင်းအား ကျွန်ုပ်ကိုင်စွဲထားသည့် စံနှုန်းဖြစ်သည်။',

    'Publications & Training': 'စာတမ်းများနှင့် သင်တန်း',
    'Trained where the margin for error is': 'အမှားအခွင့်အလမ်း အနည်းဆုံးသောနေရာတွင်',
    'smallest': 'သင်တန်းယူခဲ့သည်',
    'Critical care, chest and emergency medicine in Taiwan first — then cellular medicine in Japan and precision medicine at Harvard Medical School. The order matters: acute-care judgement came before the aesthetics.':
      'ထိုင်ဝမ်တွင် အရေးပေါ်ကုသမှု၊ ရင်ဘတ်နှင့် အရေးပေါ်ဆေးပညာကို ဦးစွာ — ထို့နောက် ဂျပန်တွင် ဆဲလ်ဆေးပညာနှင့် Harvard Medical School တွင် တိကျသောဆေးပညာ။ အစီအစဉ်သည် အရေးကြီးသည်: အလှအပထက် အရေးပေါ်ကုသမှုဆိုင်ရာ ဆုံးဖြတ်ချက်က အရင်လာသည်။',

    'Board Certification': 'ဘုတ်အဖွဲ့ လက်မှတ်',
    'Internal Medicine — Taiwan': 'ပြင်ပဆေးပညာ — ထိုင်ဝမ်',
    'Taiwan': 'ထိုင်ဝမ်',
    'Precision Medicine, since 2021': 'တိကျသောဆေးပညာ၊ ၂၀၂၁ မှစ၍',
    'Cellular Therapy Fellowship': 'ဆဲလ်ကုသနည်း Fellowship',
    'Dendritic cell therapy under Prof. Hasumi': 'ပါမောက္ခ Hasumi လက်အောက်တွင် Dendritic ဆဲလ်ကုသနည်း',
    'Japan, 2018': 'ဂျပန်၊ ၂၀၁၈',
    'Osaki Method NK cell therapy under Prof. Masuyama': 'ပါမောက္ခ Masuyama လက်အောက်တွင် Osaki Method NK ဆဲလ်ကုသနည်း',
    'Japan, 2022': 'ဂျပန်၊ ၂၀၂၂',
    'Postgraduate Training': 'ဘွဲ့လွန်သင်တန်း',
    'Precision Oncology, Cancer Genomics & Immuno-Oncology': 'တိကျသောကင်ဆာဆေးပညာ၊ ကင်ဆာ Genomics နှင့် Immuno-Oncology',
    'Harvard Medical School': 'Harvard Medical School',
    'Fellowship': 'Fellowship',
    'American Academy of Anti-Aging Medicine (A4M)': 'American Academy of Anti-Aging Medicine (A4M)',
    '2022': '၂၀၂၂',
    'Professional Memberships': 'ပညာရှင်အသင်းဝင်မှုများ',
    'American College of Physicians': 'American College of Physicians',
    'Ongoing': 'ဆက်လက်ဆောင်ရွက်ဆဲ',

    'Languages': 'ဘာသာစကားများ',
    'Native. First language of practice, in Taipei.': 'မိခင်ဘာသာစကား။ တိုင်ပေတွင် ကုသရာ ပထမဘာသာစကား။',
    'Clinical fluency for international patients and referring physicians.': 'နိုင်ငံတကာလူနာများနှင့် လွှဲပြောင်းပေးသည့် ဆရာဝန်များအတွက် ဆေးဘက်ဆိုင်ရာ ကျွမ်းကျင်မှု။',
    'Consultation-level, for patients from Yangon and the diaspora.': 'ဆွေးနွေးတိုင်ပင်ရေးအဆင့်၊ ရန်ကုန်နှင့် ပြည်ပရောက်လူနာများအတွက်။',
    'Training network': 'သင်တန်းကွန်ရက်',
    'Main centre. Protocols are written and materials prepared here.': 'ပင်မစင်တာ။ နည်းစနစ်များကို ရေးသား၍ ဆေးပစ္စည်းများကို ဤနေရာတွင် ပြင်ဆင်သည်။',
    'Partner care at Beauty Bank Wellness & Cell Therapy Center.': 'Beauty Bank Wellness & Cell Therapy Center တွင် အဖွဲ့ဝင်ကုသမှု။',
    'Partner care at Recover Health.': 'Recover Health တွင် အဖွဲ့ဝင်ကုသမှု။',

    'Protocols authored by Dr. Su': 'ဒေါက်တာစူ ရေးသားထားသော နည်းစနစ်များ',
    'Every formula,': 'ဖော်မြူလာတိုင်း၊',
    'one physician\u2019s hand': 'ဆရာဝန်တစ်ဦး၏လက်ရာ',
    'The IV programme across every R2-IWAA location is authored by Dr. Su and reviewed each time the evidence moves. Every plan is set to a patient\u2019s bloodwork rather than a menu.':
      'R2-IWAA တည်နေရာတိုင်းရှိ အိုင်ဗီအစီအစဉ်ကို ဒေါက်တာစူ ရေးသားပြီး သက်သေအထောက်အထား ပြောင်းလဲသည့်အခါတိုင်း ပြန်လည်သုံးသပ်သည်။ အစီအစဉ်တိုင်းကို မီနူးအစား လူနာ၏ သွေးစစ်ရလဒ်နှင့် ကိုက်ညီအောင် သတ်မှတ်သည်။',
    'See the IV therapy programme →': 'အိုင်ဗီပြုစုကုသမှုအစီအစဉ်ကို ကြည့်ရန် →',

    'VIP service': 'VIP ဝန်ဆောင်မှု',
    'One patient at a time.': 'တစ်ကြိမ်လျှင် လူနာတစ်ဦး။',
    'Consultations are private and unhurried, in Mandarin, English or Myanmar. Travelling patients are looked after from the first message to the last review.':
      'ဆွေးနွေးတိုင်ပင်ခြင်းများသည် သီးသန့်ဖြစ်၍ အလျင်စလို မလုပ်ပါ၊ တရုတ်၊ အင်္ဂလိပ် သို့မဟုတ် မြန်မာဘာသာဖြင့်။ ခရီးသွားလူနာများကို ပထမမက်ဆေ့ချ်မှ နောက်ဆုံးပြန်လည်သုံးသပ်မှုအထိ ဂရုစိုက်သည်။',
    'Request a consultation →': 'ဆွေးနွေးတိုင်ပင်မှုအတွက် တောင်းဆိုရန် →',

    // ---------- locations page ----------
    'Taipei, Yangon, Ho Chi Minh City.': 'တိုင်ပေ၊ ရန်ကုန်၊ ဟိုချီမင်းစီးတီး။',
    'One clinical standard, prepared and trained in Taipei, delivered in all three cities.': 'ဆေးဘက်ဆိုင်ရာ စံနှုန်းတစ်ခုတည်း၊ တိုင်ပေတွင် ပြင်ဆင်၍ သင်တန်းပေးသည်၊ မြို့သုံးမြို့လုံးတွင် ဆောင်ရွက်သည်။',
    'No. 516, Section 5, Zhongshan North Road, Shilin District. Our R2-IWAA main center, and the hub of the network — where clinical teams are trained and where the materials used in every clinic are prepared and released.':
      'အမှတ် ၅၁၆၊ အပိုင်း ၅၊ Zhongshan မြောက်လမ်း၊ ရှီလင်ခရိုင်။ ကျွန်ုပ်တို့၏ R2-IWAA ပင်မစင်တာနှင့် ကွန်ရက်၏ဗဟို — ဆေးဘက်ဆိုင်ရာအဖွဲ့များကို သင်တန်းပေးရာ၊ ဆေးခန်းတိုင်းတွင် အသုံးပြုသည့် ဆေးပစ္စည်းများကို ပြင်ဆင်၍ ထုတ်ပေးရာနေရာ။',

    'Partner clinics': 'အဖွဲ့ဝင်ဆေးခန်းများ',
    'Cared for': 'ဂရုစိုက်ခံရသည်',
    'close to home': 'အိမ်နှင့်နီးစပ်စွာ',
    'Beauty Bank Wellness & Cell Therapy Center': 'Beauty Bank Wellness & Cell Therapy Center',
    'Kamaryut Township, Yangon': 'ကမာရွတ်မြို့နယ်၊ ရန်ကုန်',
    'Assessment, IV therapy and procedures.': 'စစ်ဆေးမှု၊ အိုင်ဗီပြုစုကုသမှုနှင့် လုပ်ငန်းစဉ်များ။',
    'Tel': 'ဖုန်း',
    '260–262A Điện Biên Phủ, Xuân Hòa Ward, Ho Chi Minh City': '၂၆၀ – ၂၆၂A Điện Biên Phủ၊ Xuân Hòa Ward၊ ဟိုချီမင်းစီးတီး',
    'Hotline': 'အရေးပေါ်ဖုန်း',

    'The network': 'ကွန်ရက်',
    'Trained in Taipei. Delivered where you live.': 'တိုင်ပေတွင် သင်တန်းယူသည်။ သင်နေထိုင်ရာနေရာတွင် ဆောင်ရွက်သည်။',
    'Clinical training, protocols and prepared materials flow from Taipei to each clinic, so your care does not change with your city.':
      'ဆေးဘက်ဆိုင်ရာသင်တန်း၊ နည်းစနစ်များနှင့် ပြင်ဆင်ထားသော ဆေးပစ္စည်းများသည် တိုင်ပေမှ ဆေးခန်းတစ်ခုစီသို့ စီးဆင်းသည်၊ ထို့ကြောင့် သင့်ကုသမှုသည် သင့်မြို့နှင့် မပြောင်းလဲပါ။',

    // ---------- consultation page ----------
    'VIP consultation': 'VIP ဆွေးနွေးတိုင်ပင်မှု',
    'One to one,': 'တစ်ဦးချင်း၊',
    'before anything': 'အခြားအရာမတိုင်မီ',
    'else.': 'ဆွေးနွေးသည်။',
    'Tell us a little and our medical team will arrange a private consultation in Mandarin, English or Myanmar.':
      'အနည်းငယ်ပြောပြပါ၊ ကျွန်ုပ်တို့၏ ဆေးဘက်ဆိုင်ရာအဖွဲ့သည် တရုတ်၊ အင်္ဂလိပ် သို့မဟုတ် မြန်မာဘာသာဖြင့် သီးသန့်ဆွေးနွေးမှုတစ်ခုကို စီစဉ်ပေးပါမည်။',

    'Request': 'တောင်းဆိုမှု',
    'Start a': 'စတင်ရန်',
    'conversation': 'ဆွေးနွေးမှု',
    'Name': 'အမည်',
    'Email or WhatsApp': 'အီးမေးလ် သို့မဟုတ် WhatsApp',
    'Preferred location': 'နှစ်သက်သည့်တည်နေရာ',
    'Not sure yet': 'သေချာမသိသေးပါ',
    'Consultation language': 'ဆွေးနွေးမည့်ဘာသာစကား',
    'What would you like to address?': 'မည်သည့်အကြောင်းအရာကို ဆွေးနွေးလိုပါသနည်း?',
    'Send request': 'တောင်းဆိုချက် ပို့ရန်',
    'Your request opens in WhatsApp so it reaches our team directly — press send there and we reply within one working day. Please do not include detailed medical records; we collect those securely once your consultation is arranged.':
      'သင့်တောင်းဆိုမှုသည် WhatsApp တွင် ဖွင့်ပါမည်၊ ကျွန်ုပ်တို့အဖွဲ့ထံ တိုက်ရိုက်ရောက်ရှိရန် — ထိုနေရာတွင် ပို့ရန်ကို နှိပ်ပါ၊ တစ်ရက်အတွင်း ပြန်ဖြေပါမည်။ အသေးစိတ်ဆေးမှတ်တမ်းများကို မထည့်ပါနှင့်၊ သင့်ဆွေးနွေးမှုကို စီစဉ်ပြီးလျှင် ကျွန်ုပ်တို့သည် ၎င်းတို့ကို လုံခြုံစွာ စုဆောင်းပါမည်။',
    'Thank you. Your request has been prepared in WhatsApp — press send there and our team will be in touch within one working day.':
      'ကျေးဇူးတင်ပါသည်။ သင့်တောင်းဆိုမှုကို WhatsApp တွင် ပြင်ဆင်ပြီးပါပြီ — ထိုနေရာတွင် ပို့ရန်ကို နှိပ်ပါ၊ ကျွန်ုပ်တို့အဖွဲ့သည် တစ်ရက်အတွင်း ဆက်သွယ်ပါမည်။',
    'WhatsApp did not open?': 'WhatsApp မဖွင့်ဘူးလား?',
    'Send it by email instead': 'အီးမေးလ်ဖြင့် ပို့လိုက်ပါ',

    'Direct': 'တိုက်ရိုက်',
    'Or': 'သို့မဟုတ်',
    'reach us': 'ကျွန်ုပ်တို့ကိုဆက်သွယ်ရန်',
    'now.': 'ယခုပင်။',
    'WhatsApp & Viber': 'WhatsApp & Viber',
    'Email': 'အီးမေးလ်',
    'No. 516, Section 5, Zhongshan N. Rd, Shilin District, Taipei': 'အမှတ် ၅၁၆၊ အပိုင်း ၅၊ Zhongshan မြောက်လမ်း၊ ရှီလင်ခရိုင်၊ တိုင်ပေ',
    'Hours': 'အချိန်',
    'By appointment. Assessment and treatment days differ by location.': 'ချိန်းဆိုမှုအရ။ စစ်ဆေးမှုနှင့် ကုသမည့်ရက်များသည် တည်နေရာအလိုက် ကွဲပြားသည်။'
  };

  // Build a reverse map (my → en) so we can toggle back from Myanmar to English.
  var REV = {};
  Object.keys(DICT).forEach(function (en) {
    REV[DICT[en]] = en;
  });

  var LANG = document.documentElement.getAttribute('lang') || 'en';

  function setCookie(name, val) {
    try {
      document.cookie = name + '=' + val + '; path=/; max-age=' + (60 * 60 * 24 * 365);
    } catch (e) {}
  }

  // Walk the DOM once, collecting every text node whose trimmed value is
  // a key in DICT (or REV). Store both English and Myanmar for O(1) swaps later.
  var nodes = []; // { node, en, my }

  function collect() {
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        var p = n.parentNode;
        if (!p) return NodeFilter.FILTER_REJECT;
        var tag = p.nodeName;
        if (tag === 'SCRIPT' || tag === 'STYLE' || tag === 'NOSCRIPT') return NodeFilter.FILTER_REJECT;
        if (p.closest && p.closest('[data-lang-label]')) return NodeFilter.FILTER_REJECT;
        var t = n.nodeValue;
        if (!t || !t.trim()) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = walker.nextNode())) {
      var raw = n.nodeValue;
      var trimmed = raw.trim();
      var leading = raw.match(/^\s*/)[0];
      var trailing = raw.match(/\s*$/)[0];
      var en = null, my = null;
      if (DICT[trimmed]) { en = trimmed; my = DICT[trimmed]; }
      else if (REV[trimmed]) { my = trimmed; en = REV[trimmed]; }
      if (en) {
        nodes.push({ node: n, en: leading + en + trailing, my: leading + my + trailing });
      }
    }

    // Also translate placeholder/select-option/aria-label attributes
    var withPlaceholder = document.querySelectorAll('[placeholder]');
    withPlaceholder.forEach(function (el) {
      var v = el.getAttribute('placeholder').trim();
      if (DICT[v]) nodes.push({ el: el, attr: 'placeholder', en: v, my: DICT[v] });
    });
    var options = document.querySelectorAll('option');
    options.forEach(function (op) {
      var v = op.textContent.trim();
      if (DICT[v]) nodes.push({ node: op.firstChild || op, en: v, my: DICT[v] });
    });
  }

  function apply(lang) {
    nodes.forEach(function (rec) {
      if (rec.attr) {
        rec.el.setAttribute(rec.attr, lang === 'my' ? rec.my : rec.en);
      } else if (rec.node && rec.node.nodeType === 3) {
        rec.node.nodeValue = lang === 'my' ? rec.my : rec.en;
      } else if (rec.node && rec.node.textContent !== undefined) {
        rec.node.textContent = lang === 'my' ? rec.my : rec.en;
      }
    });
    document.documentElement.setAttribute('lang', lang);
    var label = document.querySelector('[data-lang-label]');
    if (label) label.textContent = lang === 'my' ? 'မြန်မာ' : 'EN';
  }

  document.addEventListener('DOMContentLoaded', function () {
    collect();
    apply(LANG);
    var btn = document.querySelector('.lang-toggle');
    if (btn) {
      btn.addEventListener('click', function () {
        LANG = LANG === 'en' ? 'my' : 'en';
        setCookie('r2lang', LANG);
        apply(LANG);
      });
    }
  });
})();
