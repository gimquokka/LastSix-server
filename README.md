# 개요

_Software Maestro_ 12기 공공데이터 활용 해커톤 LastSix 팀 (고동천, 김진영, 함초롬, 박효진, 진유진, 이종아)의 의약 폐기물 처리 안내 사이트 _"약! 그냥 버리게?"_ 웹 어플리케이션의 서버 프로젝트입니다.

# 기술 스택

```markdown
### 사용한 라이브러리

- flask
- mongoDB
- pymongo
- python

### 활용한 공공데이터

1. 서울특별시*양천구*폐의약품\_수거함위치
   (https://data.go.kr/data/15074902/fileData.do)
2. 서울특별시 용산구\_폐의약품 수거가능위치 현황
   (https://data.go.kr/data/15074891/fileData.do)
3. 서울특별시 동대문구\_폐의약품 수거함 위치 현황
   (https://data.go.kr/data/15074660/fileData.do)
4. 서울특별시 광진구\_폐의약품 수거함 및 수집 참여 약국 현황 (https://data.go.kr/data/15075017/fileData.do)
5. 서울특별시 동작구\_폐의약품 수거가능 약국현황
   (https://data.go.kr/data/15077702/fileData.do)
6. 서울특별시 강서구\_폐의약품 수거 약국 현황
   (https://data.go.kr/data/15074907/fileData.do)
7. 서울특별시 은평구\_폐의약품수거거점약국
   (https://data.go.kr/data/15077807/fileData.do)
8. 서울특별시 송파구\_폐의약품 수거 참여 약국 현황
   (https://data.go.kr/data/15077652/fileData.do)
9. 서울특별시 서대문구\_가정폐의약품 수거함 위치
   (https://data.go.kr/data/15074855/fileData.do)
10. 서울특별시 마포구\_불용의약품수거함
    (https://data.go.kr/data/15074773/fileData.do)
11. 국립중앙의료원\_전국 약국 정보 조회 서비스
    (https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000576)
```

# 프로젝트 구조

```python
├─ Readme.md
├─ modules
│  ├─ __init__.py
│  └─ garbege.py (will replaced)
├─ routes.py
├─ wsgi.py
└─ .gitignore
```

# API

## API DOCS

GET /?lat=''&lng=''

```swift
{
    "name": string, //dutyName
    "lat": number, //위도
    "lng": number, //경도
    "hpid": string, //고유 id 값
    "isOfficial": boolean //공공데이터 내 장소인지
}
```

https://medicine-server-gokzn.run.goorm.io/?lat=37.518379767474165&lng=126.91166094240059

```swift
{
    "msg": "success",
    "result": [
        {
            "hpid": "CIDSE123",
            "isOfficial": true,
            "lat": 37.51856697499053,
            "lng": 126.91216520641032,
            "name": "medicine"
        }
    ]
}
```

GET /:hpid

```swift
{
    "name": string, // 이름
    "addr": string, // 주소
    "tel" : string, // 전화번호
    "start": object {
        "mon": string, // 월요일 시작 시간 ex) "18:30"
        "tue": string, // 화요일 시작 시간
        "wed": string, // 수요일 시작 시간
        "thur": string, // 목요일 시작 시간
        "fri": string, // 금요일 시작 시간
        "sat": string, // 토요일 시작 시간
        "sun": string, // 일요일 시작 시간
    },
    "close" : {
        "mon": string, // 월요일 종료 시간 ex) "18:30"
        "tue": string, // 화요일 시작 시간
        "wed": string, // 수요일 시작 시간
        "thur": string, // 목요일 시작 시간
        "fri": string, // 금요일 시작 시간
        "sat": string, // 토요일 시작 시간
        "sun": string, // 일요일 시작 시간
    }
}
```

https://medicine-server-gokzn.run.goorm.io/CIDSE123

```swift
    {
    "msg": "success",
    "result": {
        "addr": "address",
        "close": {
            "fri": "09:30",
            "mon": "09:30",
            "sat": "09:30",
            "sun": "09:30",
            "thur": "09:30",
            "tue": "09:30",
            "wed": "09:30"
        },
        "name": "medicine",
        "start": {
            "fri": "09:30",
            "mon": "09:30",
            "sat": "09:30",
            "sun": "09:30",
            "thur": "09:30",
            "tue": "09:30",
            "wed": "09:30"
        },
        "tel": "02-123-1231"
    }
}
```

# 담당파트

**이종아** [@jong-a LEE](https://github.com/whddk4415)

- 팀장
- Mongo db 연결 쿼리 제작
- API 구현
- 데이터 전처리

**김진영** [@Jin Kim](https://github.com/gimquokka)

- API 구현
- 데이터 전처리
- 발표 및 README 작성

**고동천** [@cheon4050](https://github.com/cheon4050)

- 데이터 전처리
- README 작성
