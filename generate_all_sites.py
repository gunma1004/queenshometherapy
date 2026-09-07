import os
import random

# 전체 지역 구 및 동 데이터 정의
full_regions_data = {
    "seoul": {
        "name": "서울",
        "districts": {
            "gangnam": {"name": "강남구", "dongs": ["역삼동", "개포동", "청담동", "삼성동", "대치동", "신사동", "논현동", "압구정동", "세곡동", "자곡동", "율현동", "일원동", "수서동", "도곡동"]},
            "seocho": {"name": "서초구", "dongs": ["서초동", "잠원동", "반포동", "방배동", "양재동", "우면동", "원지동", "내곡동", "신원동"]},
            "songpa": {"name": "송파구", "dongs": ["잠실동", "신천동", "풍납동", "송파동", "석촌동", "삼전동", "가락동", "문정동", "장지동", "방이동", "오금동", "거여동", "마천동", "위례동"]},
            "mapo": {"name": "마포구", "dongs": ["아현동", "공덕동", "도화동", "용강동", "토정동", "신수동", "구수동", "창전동", "상수동", "하중동", "신정동", "당인동", "서교동", "동교동", "합정동", "망원동", "연남동", "성산동", "상암동", "염리동", "대흥동"]},
            "jongno": {"name": "종로구", "dongs": ["청운동", "신교동", "궁정동", "효자동", "창성동", "통인동", "체부동", "통의동", "사직동", "적선동", "도렴동", "내자동", "필운동", "누상동", "누하동", "옥인동", "회현동", "명동", "종로1가", "종로2가", "종로3가", "종로4가", "종로5가", "종로6가", "인의동", "원남동", "연지동", "효제동", "동숭동", "이화동", "혜화동", "명륜1가", "명륜2가", "명륜3가", "명륜4가", "창신동", "숭인동"]},
            "jung-seoul": {"name": "중구", "dongs": ["무교동", "다동", "태평로1가", "을지로1가", "을지로2가", "남대문로1가", "남대문로2가", "삼각동", "수하동", "장교동", "수표동", "을지로3가", "주교동", "방산동", "오장동", "입정동", "산림동", "을지로4가", "을지로5가", "을지로6가", "장충동1가", "장충동2가", "광희동1가", "광희동2가", "을지로7가", "쌍림동", "소공동", "회현동1가", "회현동2가", "남산동1가", "후암동", "남창동", "필동", "신당동", "황학동", "중림동"]},
            "yongsan": {"name": "용산구", "dongs": ["후암동", "용산동", "동자동", "갈월동", "남영동", "한강로", "원효로", "신창동", "산천동", "청암동", "효창동", "도원동", "용문동", "문배동", "신계동", "이촌동", "이태원동", "한남동", "서빙고동", "보광동", "청파동"]},
            "seongdong": {"name": "성동구", "dongs": ["상왕십리동", "하왕십리동", "홍익동", "도선동", "마장동", "사근동", "행당동", "응봉동", "금호동", "옥수동", "성수동", "송정동", "용답동"]},
            "gwangjin": {"name": "광진구", "dongs": ["중곡동", "능동", "구의동", "광장동", "자양동", "화양동", "군자동"]},
            "dongdaemun": {"name": "동대문구", "dongs": ["신설동", "용두동", "제기동", "전농동", "답십리동", "장안동", "청량리동", "회기동", "휘경동", "이문동"]},
            "jungnang": {"name": "중랑구", "dongs": ["면목동", "상봉동", "중화동", "묵동", "망우동", "신내동"]},
            "seongbuk": {"name": "성북구", "dongs": ["성북동", "동소문동", "삼선동", "동선동", "돈암동", "안암동", "보문동", "정릉동", "길음동", "종암동", "하월곡동", "상월곡동", "장위동", "석관동"]},
            "gangbuk": {"name": "강북구", "dongs": ["미아동", "번동", "수유동", "우이동"]},
            "dobong": {"name": "도봉구", "dongs": ["창동", "도봉동", "방학동", "쌍문동"]},
            "nowon": {"name": "노원구", "dongs": ["월계동", "공릉동", "하계동", "중계동", "상계동"]},
            "eunpyeong": {"name": "은평구", "dongs": ["불광동", "갈현동", "구산동", "대조동", "응암동", "역촌동", "신사동", "증산동", "수색동", "진관동", "녹번동"]},
            "seodaemun": {"name": "서대문구", "dongs": ["충정로동", "천연동", "북아현동", "신촌동", "연희동", "홍제동", "홍은동", "남가좌동", "북가좌동"]},
            "yangcheon": {"name": "양천구", "dongs": ["신정동", "목동", "신월동"]},
            "gangseo": {"name": "강서구", "dongs": ["염창동", "등촌동", "화곡동", "가양동", "마곡동", "내발산동", "외발산동", "공항동", "방화동", "개화동", "발산동"]},
            "guro": {"name": "구로구", "dongs": ["신도림동", "구로동", "가리봉동", "오류동", "개봉동", "고척동", "궁동", "항동", "천왕동"]},
            "geumcheon": {"name": "금천구", "dongs": ["가산동", "독산동", "시흥동"]},
            "yeongdeungpo": {"name": "영등포구", "dongs": ["영등포동", "여의도동", "당산동", "도림동", "문래동", "양평동", "신길동", "대림동"]},
            "dongjak": {"name": "동작구", "dongs": ["노량진동", "상도동", "본동", "흑석동", "동작동", "사당동", "대방동", "신대방동"]},
            "gwanak": {"name": "관악구", "dongs": ["봉천동", "신림동", "남현동", "보라매동", "청림동", "성현동", "행운동", "낙성대동", "청룡동", "은천동", "난향동", "조원동", "대학동", "삼성동", "서원동", "신원동", "서림동", "난곡동", "신사동"]},
            "gangdong": {"name": "강동구", "dongs": ["강일동", "상일동", "명일동", "고덕동", "암사동", "천호동", "성내동", "둔촌동", "길동"]}
        }
    },
    "gyeonggi": {
        "name": "경기",
        "districts": {
            "suwon": {"name": "수원시", "dongs": ["파장동", "정자동", "율전동", "천천동", "조원동", "영화동", "송죽동", "연무동", "세류동", "평동", "서둔동", "구운동", "탑동", "금곡동", "호매실동", "오목천동", "고색동", "권선동", "곡반정동", "입북동", "당수동", "지동", "우만동", "인계동", "매교동", "매산동", "고등동", "원천동", "매탄동", "영통동", "이의동", "하동", "망포동"]},
            "seongnam": {"name": "성남시", "dongs": ["신흥동", "태평동", "수진동", "단대동", "산성동", "양지동", "복정동", "창곡동", "시흥동", "여수동", "도촌동", "하대원동", "중앙동", "성남동", "상대원동", "분당동", "수내동", "정자동", "서현동", "이매동", "야탑동", "금곡동", "구미동", "판교동", "삼평동", "백현동", "운중동"]},
            "uijeongbu": {"name": "의정부시", "dongs": ["의정부동", "호원동", "장암동", "신곡동", "용현동", "민락동", "금오동", "가능동", "녹양동"]},
            "anyang": {"name": "안양시", "dongs": ["안양동", "석수동", "박달동", "비산동", "관양동", "평촌동", "호계동"]},
            "bucheon": {"name": "부천시", "dongs": ["원미동", "역곡동", "심곡동", "춘의동", "도당동", "상동", "중동", "소사동", "범박동", "옥길동", "괴안동", "송내동", "소사본동", "오정동", "여월동", "원종동", "고강동"]},
            "gwangmyeong": {"name": "광명시", "dongs": ["광명동", "철산동", "하안동", "소하동", "일직동"]},
            "pyeongtaek": {"name": "평택시", "dongs": ["팽성읍", "안중읍", "포승읍", "청북읍", "진위면", "서탄면", "고덕면", "오성면", "현덕면", "신평동", "원평동", "통복동", "세교동", "송탄동", "지산동", "서정동", "중앙동", "비전동", "동삭동", "용이동"]},
            "dongducheon": {"name": "동두천시", "dongs": ["생연동", "보산동", "동두천동", "상패동", "송내동", "지행동", "불현동", "소요동"]},
            "ansan": {"name": "안산시", "dongs": ["사동", "일동", "이동", "본오동", "반월동", "성포동", "월피동", "부곡동", "선부동", "원곡동", "백운동", "초지동", "고잔동", "신길동"]},
            "goyang": {"name": "고양시", "dongs": ["원흥동", "성사동", "주교동", "대자동", "관산동", "효자동", "삼송동", "신원동", "화정동", "행신동", "토당동", "일산동", "탄현동", "중산동", "정발산동", "마두동", "백석동", "식사동", "풍동", "가좌동", "대화동", "주엽동", "덕이동"]},
            "gwacheon": {"name": "과천시", "dongs": ["과천동", "문원동", "별양동", "중앙동", "갈현동", "주암동"]},
            "guri": {"name": "구리시", "dongs": ["갈매동", "동구동", "인창동", "교문동", "수택동", "토평동"]},
            "namyangju": {"name": "남양주시", "dongs": ["와부읍", "진접읍", "화도읍", "수동면", "진건읍", "퇴계원읍", "오남읍", "별내동", "다산동", "금곡동", "평내동", "호평동"]},
            "osan": {"name": "오산시", "dongs": ["궐동", "원동", "청호동", "고현동", "청학동", "은계동", "양산동", "가수동", "수청동", "오산동", "세교동"]},
            "siheung": {"name": "시흥시", "dongs": ["대야동", "신천동", "은행동", "매화동", "목감동", "조남동", "거모동", "군자동", "월곶동", "장곡동", "장현동", "능곡동", "배곧동", "정왕동"]},
            "gunpo": {"name": "군포시", "dongs": ["산본동", "금정동", "당동", "부곡동", "대야미동", "광정동", "수리동", "궁내동", "오금동", "재궁동"]},
            "uiwang": {"name": "의왕시", "dongs": ["고천동", "부곡동", "오전동", "내손동", "청계동", "포일동"]},
            "hanam": {"name": "하남시", "dongs": ["천현동", "신장동", "풍산동", "창우동", "덕풍동", "감일동", "학암동", "망월동", "미사동", "위례동"]},
            "yongin": {"name": "용인시", "dongs": ["포곡읍", "모현읍", "남사읍", "원삼면", "백암면", "양지면", "유림동", "중앙동", "동부동", "역북동", "삼가동", "유방동", "고림동", "풍덕천동", "신봉동", "죽전동", "동천동", "상현동", "성복동", "구갈동", "상갈동", "보라동", "서천동", "보정동", "마북동", "청덕동", "동백동"]},
            "paju": {"name": "파주시", "dongs": ["문산읍", "조리읍", "법원읍", "파주읍", "월롱면", "탄현면", "광탄면", "교하동", "금촌동", "운정동", "동패동", "목동동", "야당동", "와동동"]},
            "icheon": {"name": "이천시", "dongs": ["장호원읍", "마장면", "부발읍", "신둔면", "백사면", "호법면", "대월면", "모가면", "설성면", "창전동", "중리동", "증포동", "관고동"]},
            "anseong": {"name": "안성시", "dongs": ["공도읍", "보개면", "금광면", "서운면", "미양면", "대덕면", "원곡면", "양성면", "고삼면", "일죽면", "죽산면", "삼죽면", "당왕동", "옥산동"]},
            "gimpo": {"name": "김포시", "dongs": ["통진읍", "고촌읍", "양촌읍", "대곶면", "월곶면", "하성면", "사우동", "풍무동", "걸포동", "운양동", "장기동", "구래동", "마산동"]},
            "hwaseong": {"name": "화성시", "dongs": ["봉담읍", "우정읍", "향남읍", "남양읍", "매송면", "비봉면", "마도면", "송산면", "서신면", "팔탄면", "장안면", "양감면", "정남면", "병점동", "반송동", "동탄동", "능동", "석우동", "오산동", "영천동", "신동", "방교동", "산척동", "목동", "장지동", "진안동"]},
            "gwangju-gy": {"name": "광주시", "dongs": ["오포읍", "초월읍", "곤지암읍", "도척면", "퇴촌면", "경안동", "송정동", "광남동", "쌍령동", "탄벌동", "태전동", "양벌동", "매산동", "신현동", "능평동"]},
            "yangju": {"name": "양주시", "dongs": ["백석읍", "은현면", "남면", "장흥면", "광적면", "고읍동", "만송동", "삼숭동", "옥정동", "율정동", "회암동", "덕계동", "덕정동"]},
            "pocheon": {"name": "포천시", "dongs": ["소흘읍", "군내면", "내촌면", "가산면", "일동면", "이동면", "화현면", "창수면", "영중면", "영북면", "신북면", "포천동", "선단동"]},
            "yeoju": {"name": "여주시", "dongs": ["가남읍", "점동면", "흥천면", "금사면", "산북면", "대신면", "북내면", "강천면", "여흥동", "중앙동", "오학동"]},
            "yeoncheon": {"name": "연천군", "dongs": ["연천읍", "전곡읍", "군남면", "청산면", "백학면", "미산면", "왕징면", "신서면"]},
            "gapyeong": {"name": "가평군", "dongs": ["가평읍", "설악면", "상면", "북면", "조종면", "청평면"]},
            "yangpyeong": {"name": "양평군", "dongs": ["양평읍", "강상면", "강하면", "양서면", "옥천면", "서종면", "단월면", "청운면", "양동면", "지평면", "용문면", "개군면"]}
        }
    },
    "incheon": {
        "name": "인천",
        "districts": {
            "jemulpo": {"name": "제물포구", "dongs": ["중앙동", "해안동", "항동", "관동", "송학동", "사동", "신흥동", "답동", "도원동", "율목동", "도화동", "주안동", "용현동", "학익동", "숭의동", "만석동", "화수동", "화평동", "송현동", "창영동", "금곡동", "송림동"]},
            "yeongjong": {"name": "영종구", "dongs": ["운서동", "중산동", "운남동", "운북동", "무의동"]},
            "michuhol": {"name": "미추홀구", "dongs": ["숭의동", "용현동", "학익동", "도화동", "주안동", "관교동", "문학동"]},
            "yeonsu": {"name": "연수구", "dongs": ["옥련동", "선학동", "연수동", "청학동", "동춘동", "송도동"]},
            "namdong": {"name": "남동구", "dongs": ["구월동", "간석동", "만수동", "장수동", "서창동", "도림동", "고잔동", "논현동"]},
            "bupyeong": {"name": "부평구", "dongs": ["부평동", "일신동", "십정동", "산곡동", "청천동", "삼산동", "갈산동", "부개동"]},
            "gyeyang": {"name": "계양구", "dongs": ["효성동", "작전동", "서운동", "임학동", "용종동", "병방동", "방축동", "동양동", "귤현동", "이화동", "계산동"]},
            "seohae": {"name": "서해구", "dongs": ["연평면", "백령면", "대청면", "덕적면", "자월면", "영흥면"]},
            "geomdan": {"name": "검단구", "dongs": ["검암동", "경서동", "원당동", "당하동", "마전동", "불로동", "금곡동", "오류동", "왕길동", "아라동", "검단동"]},
            "ganghwa": {"name": "강화군", "dongs": ["강화읍", "선원면", "불은면", "길상면", "화도면", "내가면", "양사면", "하점면", "삼산면", "서도면", "송해면", "교동면"]},
            "ongjin": {"name": "옹진군", "dongs": ["북도면", "연평면", "백령면", "대청면", "덕적면", "자월면", "영흥면"]}
        }
    }
}

title_templates = [
    "{full_name} {dong} 출장마사지 - 24시 홈타이 후불제",
    "{dong} 출장마사지 전문 퀸즈홈테라피 | {full_name} 30분 내 방문",
    "[{full_name}] {dong} 출장안마·홈타이 서비스 24시간 연중무휴",
    "{dong} 출장마사지 추천 퀸즈홈테라피 - 믿을 수 있는 100% 후불제",
    "{full_name} {dong} 홈타이 및 출장마사지 | 피로 회복 맞춤 케어",
    "{dong} 출장마사지 잘하는 곳 퀸즈홈테라피 ({full_name} 전지역)",
    "[{dong} 출장마사지] 퀸즈홈테라피 - 아로마·스웨디시·건식 24시",
    "{full_name} {dong} 출장마사지 서비스 | 프라이빗 홈케어",
    "{dong} 홈타이 출장마사지 - 퀸즈홈테라피 {full_name} 직영 관리사",
    "[{full_name} {dong}] 24시 출장마사지·홈타이 빠른 방문 서비스",
    "{dong} 출장마사지 | 지친 일상을 깨우는 퀸즈홈테라피 힐링 케어",
    "{full_name} {dong} 출장안마 및 홈타이 | 365일 연중무휴 24시",
    "{dong} 출장마사지 퀸즈홈테라피 - 건식·아로마 맞춤 프로그램",
    "[{full_name}] {dong} 홈타이 출장마사지 후불제 안심 서비스",
    "{dong} 출장마사지 전문 퀸즈홈테라피와 함께하는 편안한 휴식",
    "{full_name} {dong} 출장마사지·홈타이 | 1:1 맞춤 프리미엄 케어",
    "{dong} 출장마사지 | 퀸즈홈테라피 {full_name} 어디서나 30분 방문",
    "[{dong} 출장안마] 퀸즈홈테라피에서 제공하는 24시 홈케어",
    "{full_name} {dong} 홈타이 출장마사지 - 전문 관리사 상시 대기",
    "{dong} 출장마사지 추천 퀸즈홈테라피 ({full_name} 권역별 밀착 케어)",
    "[{full_name} {dong}] 프라이빗하게 즐기는 24시 출장마사지",
    "{dong} 출장마사지 퀸즈홈테라피 - 쌓인 피로를 풀어주는 힐링",
    "{full_name} {dong} 홈타이 및 출장마사지 | 신속한 방문 서비스",
    "{dong} 출장마사지 전문 - 퀸즈홈테라피 {full_name} 전 지역 운영",
    "[{dong} 출장마사지] 퀸즈홈테라피와 함께 편안한 공간에서 힐링",
    "{full_name} {dong} 출장안마 홈타이 24시 | 믿을 수 있는 후불제"
]

desc_templates = [
    "{full_name} {dong} 출장마사지 및 홈타이 전문 퀸즈홈테라피입니다. 30분 내 신속 방문과 100% 후불제 안심 서비스로 24시간 언제든 편안한 케어를 받아보세요.",
    "{dong} 출장마사지를 찾고 계신가요? 퀸즈홈테라피는 {full_name} {dong} 지역 어디든 24시간 빠르게 방문하여 건식, 아로마, 스웨디시 케어를 제공합니다.",
    "일상을 채우는 휴식, {full_name} {dong} 출장마사지 퀸즈홈테라피. 실력 있는 전문 관리사가 직접 찾아가 피로를 말끔히 풀어드립니다.",
    "100% 후불제로 안전한 {full_name} {dong} 출장마사지·홈타이 서비스. 건식, 아로마, 스웨디시, VIP 코스로 나만의 맞춤 힐링을 경험하세요.",
    "{dong} 지역 24시 출장마사지 전문! 퀸즈홈테라피가 {full_name} 고객님 계신 곳으로 직접 찾아가 편안하고 품격 있는 휴식을 선물합니다.",
    "지친 몸과 마음을 위한 힐링 타임, {full_name} {dong} 출장마사지 퀸즈홈테라피. 365일 연중무휴 24시간 편안한 방문 홈케어를 만나보세요.",
    "빠르고 신속한 방문, {dong} 출장마사지는 퀸즈홈테라피입니다. {full_name} 전 지역에서 24시간 편안하게 전문 관리사의 케어를 받아보실 수 있습니다.",
    "프리미엄 관리로 완성되는 {full_name} {dong} 출장마사지·홈타이. 퀸즈홈테라피만의 특별한 프로그램으로 일상의 피로를 날려버리세요.",
    "언제 어디서나 편안하게, {dong} 출장마사지 퀸즈홈테라피가 {full_name} 지역 구석구석 신속하게 방문하여 맞춤형 힐링 케어를 선사합니다.",
    "믿을 수 있는 100% 후불제 시스템! {full_name} {dong} 출장마사지 및 홈타이는 퀸즈홈테라피에서 편안하게 예약하고 이용하세요.",
    "체계적인 프로그램과 전문 관리사의 손길, {dong} 출장마사지 퀸즈홈테라피가 {full_name} 고객님을 위해 24시간 대기하고 있습니다.",
    "나만의 공간에서 즐기는 휴식, {full_name} {dong} 출장마사지·홈타이 전문 퀸즈홈테라피와 함께 완벽한 힐링을 경험해 보세요.",
    "스트레스와 피로 해소를 위한 선택, {dong} 출장마사지 퀸즈홈테라피. {full_name} 지역 24시 친절 상담 및 신속 방문을 보장합니다.",
    "품격 있는 관리를 원하신다면 {full_name} {dong} 출장마사지 퀸즈홈테라피를 찾아주세요. 건식부터 아로마까지 전문적인 케어가 찾아갑니다.",
    "기다림 없는 빠른 방문, {dong} 출장마사지 전문 퀸즈홈테라피입니다. {full_name} 어디서나 24시간 편안한 홈타이 서비스를 누려보세요.",
    "지친 하루의 완벽한 마무리, {full_name} {dong} 출장마사지 퀸즈홈테라피. 전문 관리사가 선사하는 1:1 맞춤 케어를 경험해 보세요.",
    "안심하고 이용할 수 있는 후불제 출장마사지! {dong} 및 {full_name} 전 지역 24시 신속 방문 퀸즈홈테라피가 함께합니다.",
    "일상의 활력을 되찾아주는 {full_name} {dong} 출장마사지·홈타이 서비스. 퀸즈홈테라피에서 차별화된 힐링 프로그램을 만나보세요.",
    "꼼꼼하고 섬세한 손길의 {dong} 출장마사지 퀸즈홈테라피. {full_name} 고객님의 편안한 휴식을 위해 24시간 언제나 열려있습니다.",
    "프라이빗한 공간에서 누리는 최고의 휴식, {full_name} {dong} 출장마사지 퀸즈홈테라피와 함께 피로를 말끔히 씻어내세요.",
    "언제나 고객 중심의 서비스, {dong} 출장마사지 퀸즈홈테라피가 {full_name} 지역에 24시간 대기 중입니다. 지금 바로 문의하세요.",
    "전문적인 테라피로 찾아가는 {full_name} {dong} 출장마사지·홈타이. 퀸즈홈테라피에서 편안하고 안전한 관리를 받아보세요.",
    "당신의 휴식을 책임지는 {dong} 출장마사지 퀸즈홈테라피. {full_name} 전 지역 신속한 방문으로 최상의 만족감을 드립니다.",
    "믿을 수 있는 후불제 홈케어, {full_name} {dong} 출장마사지 퀸즈홈테라피. 아로마, 스웨디시, VIP 코스로 피로를 회복하세요.",
    "머무시는 그 자리가 힐링 공간이 되는 곳, {dong} 출장마사지 퀸즈홈테라피. {full_name} 24시 언제든 편안하게 찾아갑니다.",
    "완벽한 휴식을 위한 24시 홈케어 파트너, {full_name} {dong} 출장마사지 퀸즈홈테라피. 지금 바로 전문 관리사를 만나보세요."
]

def get_html_content(title, desc, banner_path, main_title, sub_desc, bottom_selector_html, breadcrumb, canonical_url):
    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="index,follow">
<meta name="naver-site-verification" content="3f345e54f2dfbcb90e980d17cfe5c1febe5f14aa">
<!-- Open Graph 태그 추가 -->
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{canonical_url}">
<meta property="og:image" content="https://queenshometherapy.netlify.app/images/banner.jpg">
<link rel="canonical" href="{canonical_url}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;700&display=swap" rel="stylesheet">
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
:root{{--primary:#ff6b35;--font:'Noto Sans KR',sans-serif;--text-dark:#1f2430;--text-muted:#5b6472;--bg-section:#fff5f0}}
body{{font-family:var(--font);letter-spacing:-0.01em;color:var(--text-dark);line-height:1.7;background:var(--bg-section);min-height:100vh;padding-bottom:80px}}
.container{{max-width:1200px;margin:0 auto;padding:0 20px}}
.header{{position:fixed;top:0;left:0;right:0;z-index:1000;background:rgba(10,10,26,.9);border-bottom:1px solid rgba(255,255,255,.1);backdrop-filter:blur(10px)}}
.header-inner{{display:flex;align-items:center;justify-content:space-between;height:70px;max-width:1200px;margin:0 auto;padding:0 20px}}
.logo{{display:flex;align-items:center;gap:10px;text-decoration:none}}
.logo-icon{{width:40px;height:40px;background:var(--primary);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:20px;font-weight:700;color:#fff}}
.logo-text{{font-size:1.2rem;font-weight:700;color:#fff}}
.logo-sub{{font-size:.7rem;color:#b5b5c6;margin-top:-2px}}
.nav{{display:flex;gap:28px;align-items:center}}
.nav a{{color:#fff;font-size:.92rem;text-decoration:none}}
.nav-cta{{background:var(--primary);color:#fff!important;padding:10px 22px;border-radius:30px;font-weight:700;font-size:.88rem}}
.section{{padding:80px 0}}
.section-white{{background:#fff}}
.section-light{{background:#fff5f0}}
.section-title{{text-align:center;margin-bottom:50px}}
.section-title .bar{{width:40px;height:3px;background:var(--primary);margin:0 auto 12px;border-radius:2px}}
.section-title h2{{font-size:clamp(24px,3vw,36px);font-weight:700;color:var(--text-dark);margin-bottom:10px}}
.section-title p{{color:var(--text-muted);font-size:15px}}
.btn-primary{{background:var(--primary);color:#fff;padding:16px 38px;border-radius:14px;font-weight:700;font-size:1rem;display:inline-flex;align-items:center;gap:8px;text-decoration:none;box-shadow:0 4px 14px rgba(255,107,53,.28)}}
.banner-container{{max-width:1200px;margin:30px auto 0;padding:0 20px}}
.banner-container img{{width:100%;height:auto;border-radius:16px;box-shadow:0 4px 20px rgba(0,0,0,.15);object-fit:cover;max-height:400px}}
.region-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;margin-bottom:20px}}
.region-card{{background:#fff;padding:30px;border-radius:16px;text-align:center;border:1px solid rgba(255,107,53,.15);box-shadow:0 4px 12px rgba(0,0,0,.03);text-decoration:none;transition:all .3s}}
.region-card:hover{{transform:translateY(-5px);border-color:var(--primary);box-shadow:0 8px 20px rgba(255,107,53,.15)}}
.region-card h3{{font-size:1.4rem;color:var(--text-dark);margin-bottom:8px}}
.region-card p{{font-size:0.9rem;color:var(--text-muted)}}
.price-board{{display:grid;grid-template-columns:repeat(auto-fit,minmax(350px,1fr));gap:20px}}
.pt-row{{background:#fff;border-radius:16px;padding:24px;border:1px solid rgba(255,107,53,.15);box-shadow:0 4px 12px rgba(0,0,0,.03)}}
.pt-head{{display:flex;justify-content:space-between;align-items:center;margin-bottom:16px;padding-bottom:12px;border-bottom:1px solid #eee}}
.pt-cat{{font-size:12px;font-weight:700;color:var(--primary);background:rgba(255,107,53,.1);padding:4px 10px;border-radius:6px}}
.pt-name{{font-size:18px;font-weight:700;color:var(--text-dark)}}
.pt-tiers{{display:flex;flex-direction:column;gap:8px}}
.pt-tier{{display:flex;justify-content:space-between;font-size:15px;color:var(--text-muted)}}
.pt-tier b{{color:var(--text-dark)}}
.footer{{background:#15151f;color:#b5b5c6;padding:60px 0 30px;font-size:14px}}
.footer-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:30px;margin-bottom:40px}}
.footer h3{{color:#fff;font-size:16px;margin-bottom:16px}}
.business-info-footer{{border-top:1px solid rgba(255,255,255,.1);padding-top:20px;margin-top:20px;font-size:.85rem;line-height:1.6}}
.footer-bottom{{text-align:center;margin-top:30px;padding-top:20px;border-top:1px solid rgba(255,255,255,.05);font-size:.8rem}}

.floating-cta{{position:fixed;bottom:0;left:0;right:0;background:rgba(10,10,26,.95);backdrop-filter:blur(10px);border-top:1px solid rgba(255,107,53,.3);padding:12px 20px;z-index:9999;display:flex;gap:12px;max-width:600px;margin:0 auto;box-shadow:0 -4px 20px rgba(0,0,0,.3)}}
.floating-cta a{{flex:1;padding:14px 0;border-radius:12px;text-align:center;font-weight:700;font-size:1rem;text-decoration:none;display:flex;align-items:center;justify-content:center;gap:6px}}
.cta-call{{background:var(--primary);color:#fff;box-shadow:0 3px 10px rgba(255,107,53,.3)}}
.cta-sms{{background:#25d366;color:#fff;box-shadow:0 3px 10px rgba(37,211,102,.3)}}
@media(max-width:768px){{.floating-cta{{max-width:100%;border-radius:0;padding:10px 14px}}}}
</style>
</head>
<body>

<header class="header">
  <div class="header-inner">
    <a href="/" class="logo">
      <div class="logo-icon">Q</div>
      <div>
        <div class="logo-text">퀸즈홈테라피</div>
        <div class="logo-sub">{breadcrumb}</div>
      </div>
    </a>
    <nav class="nav">
      <a href="/">홈</a>
      <a href="tel:050712803296" class="nav-cta">전화 예약</a>
    </nav>
  </div>
</header>

<main role="main">
  <section style="background:#15151f;padding:140px 20px 50px;text-align:center;">
    <div class="container">
      <div style="color:var(--primary);font-size:14px;letter-spacing:2px;margin-bottom:16px;font-weight:700;">{sub_desc}</div>
      <h1 style="color:#fff;font-size:clamp(28px,4vw,44px);line-height:1.3;margin-bottom:18px">{main_title}</h1>
      <p style="color:#b5b5c6;font-size:16px;max-width:600px;margin:0 auto 30px">{sub_desc} 전문 관리사가 직접 찾아가 편안하고 품격 있는 케어를 제공합니다.</p>
      <div>
        <a href="tel:050712803296" class="btn-primary">0507-1280-3296 전화 예약하기</a>
      </div>
    </div>
  </section>

  <div class="banner-container">
    <img src="{banner_path}" alt="{main_title} 배너">
  </div>

  <section class="section section-white" id="price">
    <div class="container">
      <div class="section-title">
        <div class="bar"></div>
        <h2>퀸즈 프로그램 & 이용 요금</h2>
        <p>관리 스타일과 이용 시간을 비교해 나에게 맞는 프로그램을 살펴보세요.</p>
      </div>

      <div class="price-board">
        <div class="pt-row">
          <div class="pt-head"><span class="pt-cat">01 DRY</span><span class="pt-name">건식 힐링 코스</span></div>
          <p style="font-size:13px;color:var(--text-muted);margin-bottom:14px;">깔끔하고 부담 없는 관리 스타일을 선호하는 분을 위한 기본 프로그램입니다.</p>
          <div class="pt-tiers">
            <span class="pt-tier"><b>60분</b> 60,000원</span>
            <span class="pt-tier"><b>90분</b> 80,000원</span>
            <span class="pt-tier"><b>120분</b> 100,000원</span>
          </div>
        </div>
        <div class="pt-row">
          <div class="pt-head"><span class="pt-cat">02 AROMA</span><span class="pt-name">아로마 힐링 코스</span></div>
          <p style="font-size:13px;color:var(--text-muted);margin-bottom:14px;">은은한 아로마와 부드러운 관리 흐름을 조화롭게 구성한 프로그램입니다.</p>
          <div class="pt-tiers">
            <span class="pt-tier"><b>60분</b> 70,000원</span>
            <span class="pt-tier"><b>90분</b> 80,000원</span>
            <span class="pt-tier"><b>120분</b> 100,000원</span>
          </div>
        </div>
        <div class="pt-row">
          <div class="pt-head"><span class="pt-cat">03 SWEDISH</span><span class="pt-name">힐링스웨디시 코스</span></div>
          <p style="font-size:13px;color:var(--text-muted);margin-bottom:14px;">섬세하고 부드러운 관리감을 중심으로 여유 있는 분위기를 선호할 때 좋습니다.</p>
          <div class="pt-tiers">
            <span class="pt-tier"><b>60분</b> 80,000원</span>
            <span class="pt-tier"><b>90분</b> 100,000원</span>
            <span class="pt-tier"><b>120분</b> 120,000원</span>
          </div>
        </div>
        <div class="pt-row">
          <div class="pt-head"><span class="pt-cat">04 VIP</span><span class="pt-name">VIP 스페셜 코스</span></div>
          <p style="font-size:13px;color:var(--text-muted);margin-bottom:14px;">서로 다른 관리 구성을 한 코스 안에서 폭넓게 경험하는 프리미엄 프로그램입니다.</p>
          <div class="pt-tiers">
            <span class="pt-tier"><b>60분</b> 100,000원</span>
            <span class="pt-tier"><b>90분</b> 120,000원</span>
            <span class="pt-tier"><b>120분</b> 150,000원</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  {bottom_selector_html}
</main>

<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <h3>퀸즈홈테라피</h3>
        <p style="margin-top:12px"><strong>고객센터:</strong> <a href="tel:050712803296" style="color:#fff;text-decoration:none;">0507-1280-3296</a></p>
        <p><strong>운영시간:</strong> 365일 연중무휴</p>
      </div>
    </div>
    <div class="business-info-footer">
      <p><strong>퀸즈홈테라피</strong> | {breadcrumb} 출장마사지 안내 페이지</p>
    </div>
    <div class="footer-bottom">
      <p>&copy; 2026 퀸즈홈테라피. All rights reserved.</p>
    </div>
  </div>
</footer>

<div class="floating-cta">
  <a href="tel:050712803296" class="cta-call">📞 전화하기</a>
  <a href="sms:050712803296" class="cta-sms">💬 문자하기</a>
</div>

</body>
</html>
"""

count = 0
sitemap_urls = ["https://queenshometherapy.netlify.app/"]

# 1. 서울, 경기, 인천 대분류 허브 페이지 생성
for region_key, region_info in full_regions_data.items():
    full_name = region_info["name"]
    canonical_url = f"https://queenshometherapy.netlify.app/{region_key}.html"
    sitemap_urls.append(canonical_url)
    
    dist_cards_html = '<section class="section section-light"><div class="container"><div class="section-title"><div class="bar"></div><h2>세부 구·시·군 선택</h2><p>원하시는 구/시/군을 선택하여 세부 정보를 확인하세요.</p></div><div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:20px;">'
    for dist_key, dist_info in region_info["districts"].items():
        district_name = dist_info["name"]
        dist_cards_html += f'<a href="/{region_key}/{dist_key}/" style="background:#fff;padding:20px;border-radius:12px;text-align:center;text-decoration:none;color:var(--text-dark);border:1px solid rgba(255,107,53,.15);font-weight:700;box-shadow:0 4px 10px rgba(0,0,0,.02);">{full_name} {district_name}</a>'
    dist_cards_html += '</div></div></section>'
    
    hub_content = get_html_content(
        title=f"{full_name} 출장마사지 전 지역 안내 - 퀸즈홈테라피",
        desc=f"{full_name} 지역 전 구·시·군 24시 출장마사지 및 홈타이 서비스 안내.",
        banner_path="images/banner.jpg",
        main_title=f"{full_name} 출장마사지·홈타이 서비스",
        sub_desc=f"{full_name} 전 지역 연중무휴 24시",
        bottom_selector_html=dist_cards_html,
        breadcrumb=f"{full_name} 전체보기",
        canonical_url=canonical_url
    )
    with open(f"{region_key}.html", "w", encoding="utf-8") as f:
        f.write(hub_content)

    # 2. 구(District)별 하위 페이지 생성
    for dist_key, dist_info in region_info["districts"].items():
        district_name = dist_info["name"]
        dist_path = f"{region_key}/{dist_key}"
        canonical_url = f"https://queenshometherapy.netlify.app/{dist_path}/"
        sitemap_urls.append(canonical_url)
        
        dong_links_html = '<section class="section section-light"><div class="container"><div class="section-title"><div class="bar"></div><h2>세부 동 선택</h2><p>원하시는 동을 선택하여 맞춤 페이지로 이동하세요.</p></div><div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:center;">'
        for dong in dist_info["dongs"]:
            dong_path = f"{region_key}/{dist_key}/{dong}"
            sitemap_urls.append(f"https://queenshometherapy.netlify.app/{dong_path}/")
            dong_links_html += f'<a href="/{dong_path}/" style="background:#fff;color:var(--text-dark);padding:10px 18px;border-radius:10px;font-size:0.95rem;text-decoration:none;border:1px solid rgba(255,107,53,0.2);">{dong}</a>'
        dong_links_html += '</div></div></section>'

        dist_folder = os.path.join(region_key, dist_key)
        os.makedirs(dist_folder, exist_ok=True)
        
        dist_content = get_html_content(
            title=f"{full_name} {district_name} 출장마사지 - 24시 홈타이",
            desc=f"{full_name} {district_name} 출장마사지 및 홈타이 전문. 전 동 30분 내 방문.",
            banner_path="../../../images/banner.jpg",
            main_title=f"{district_name} 출장마사지·홈타이",
            sub_desc=f"{full_name} {district_name} 전 지역",
            bottom_selector_html=dong_links_html,
            breadcrumb=f"{full_name} {district_name}",
            canonical_url=canonical_url
        )
        with open(os.path.join(dist_folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(dist_content)

        # 3. 개별 동 페이지 생성
        for dong in dist_info["dongs"]:
            dong_path = f"{region_key}/{dist_key}/{dong}"
            canonical_url = f"https://queenshometherapy.netlify.app/{dong_path}/"
            folder_path = os.path.join(region_key, dist_key, dong)
            os.makedirs(folder_path, exist_ok=True)
            
            page_title = random.choice(title_templates).format(full_name=full_name, dong=dong)
            page_desc = random.choice(desc_templates).format(full_name=full_name, dong=dong)
            
            other_dongs_html = f'<section class="section section-light"><div class="container"><div class="section-title"><div class="bar"></div><h2>{district_name} 다른 동 둘러보기</h2><p>인근 지역의 다른 동도 확인해보세요.</p></div><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:center;">'
            for d in dist_info["dongs"]:
                if d != dong:
                    other_dongs_html += f'<a href="/{region_key}/{dist_key}/{d}/" style="background:#fff;color:var(--text-dark);padding:6px 12px;border-radius:8px;font-size:0.85rem;text-decoration:none;border:1px solid rgba(255,107,53,0.2);">{d}</a>'
            other_dongs_html += '</div></div></section>'
            
            dong_content = get_html_content(
                title=page_title,
                desc=page_desc,
                banner_path="../../../../images/banner.jpg",
                main_title=f"{dong} 출장마사지·홈타이",
                sub_desc=f"{full_name} {district_name} {dong}",
                bottom_selector_html=other_dongs_html,
                breadcrumb=f"{full_name} {district_name} {dong}",
                canonical_url=canonical_url
            )
            with open(os.path.join(folder_path, "index.html"), "w", encoding="utf-8") as f:
                f.write(dong_content)
            count += 1

# sitemap.xml 생성
sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
for url in sitemap_urls:
    sitemap_xml += f"  <url>\n    <loc>{url}</loc>\n    <changefreq>weekly</changefreq>\n    <priority>0.8</priority>\n  </url>\n"
sitemap_xml += '</urlset>'

with open("sitemap.xml", "w", encoding="utf-8") as f:
    f.write(sitemap_xml)

print(f"총 {count}개의 동 페이지 및 대분류/구별 허브 샵 페이지, 네이버 메타 태그, Open Graph 태그, 사이트맵 생성이 완료되었습니다!")