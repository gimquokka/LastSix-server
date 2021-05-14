# 약! 그냥 버리게? Web

_Software Maestro_ 12기 공공데이터 활용 해커톤 _LastSix_ 팀 <small>(고동천, 김진영, 함초롬, 박효진, 진유진, 이종아)</small>의 

의약 폐기물 처리 안내 사이트 **_"약! 그냥 버리게?"_** 웹 어플리케이션의 서버 프로젝트입니다. 

#### Do you want know detail project information?

<small> (기획의도, 기능, 및 현황 정보 등 프로젝트 상세정보에 관한 링크입니다.) </small>

[문제의식 및 웹 기능](https://www.notion.so/98bdeab0972442b2a10d3159a90fa61e)

[의약 폐기물 환경오염 현황](https://www.notion.so/88fc34bcf5f94065904721c0f1bd08ec)



## Specification

### Library

- flask
- wsgi
- mongoDB
- pymongo
- nginx

### Dataset

1. [서울특별시 양천구 폐의약품 수거함위치](https://data.go.kr/data/15074902/fileData.do)
2. [서울특별시 용산구 폐의약품 수거가능위치 현황](https://data.go.kr/data/15074891/fileData.do)
3. [서울특별시 동대문구 폐의약품 수거함 위치 현황](https://data.go.kr/data/15074660/fileData.do)
4. [서울특별시 광진구 폐의약품 수거함 및 수집 참여 약국 현황](https://data.go.kr/data/15075017/fileData.do)
5. [서울특별시 동작구 폐의약품 수거가능 약국현황](https://data.go.kr/data/15077702/fileData.do)
6. [서울특별시 강서구 폐의약품 수거 약국 현황](https://data.go.kr/data/15074907/fileData.do)
7. [서울특별시 은평구 폐의약품수거거점약국](https://data.go.kr/data/15077807/fileData.do)
8. [서울특별시 송파구 폐의약품 수거 참여 약국 현황](https://data.go.kr/data/15077652/fileData.do)
9. [서울특별시 서대문구 가정폐의약품 수거함 위치](https://data.go.kr/data/15074855/fileData.do)
10. [서울특별시 마포구 불용의약품수거함](https://data.go.kr/data/15074773/fileData.do)
11. [국립중앙의료원 전국 약국 정보 조회 서비스](https://data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000576)



## Structures

```python
├─ README.md
├─ models
│  ├─ __init__.py
│  └─ garbage.py (will replaced)
├─ routes.py
├─ server_run.sh
├─ wsgi.py
├─ wsgi.ini
└─ .gitignore
```



## API documentation

### Table of contents

- 폐의약품 수거 약국 위치정보
  - [주변 약국 위치정보](#주변-약국-위치정보)
  - [특정 약국 영업정보](#특정-약국-영업정)



### 주변 약국 위치정보

#### Description

유저 반경 5km의 폐의약품 수거 약국정보를 가까운 순서대로 반환합니다.

#### METHOD

`GET`

#### URL

`/?lat=<float: latitude>&lng=<float: longitude>&limit=<int: 리스트로 받을 최대 개수 default=10`

#### URL EXAMPLE

`GET`  ` /?lat=37.5183&lng=126.9116&limit=10`

#### QUERY STRING

| name   | type   | require                   | description            |
| ------ | ------ | ------------------------- | ---------------------- |
| lat    | number | 필수 (default: 37.5666)   | 유저 현위치의 위도값    |
| lng    | number | 필수  (default: 126.9784) | 유저 현위치의 경도값    |
| limit  | number | 옵션  (default: 10)       | 리스트로 받을 최대 개수 |

> 리퀘스트의 url로 유저 현위치의 위도, 경도값을 전달합니다. 필요하다면 limit값도 전달합니다.

### RESPONSE

#### RESPONSE BODY

| name       | type    | require | description            |
| ---------- | ------- | ------- | ---------------------- |
| name       | string  | 필수    | 유저 현위치 지명       |
| lat        | number  | 필수    | 위도                   |
| lng        | number  | 필수    | 경도                   |
| hpid       | string  | 필수    | 고유 id 값             |
| isOfficial | boolean | 필수    | 공공데이터 내 장소인지 |

> 요청에 대한 반환으로 주변 약국의 정보들을 반환합니다.

#### success

**HTTP Status code : 200 success**

```json
{
  "msg":"success",
  "result":[
    {"hpid":"C1101142","isOfficial":false,"lat":37.518856184099995,"lng":126.9091119011,"name":"우신약국"},
    {"hpid":"C1104798","isOfficial":false,"lat":37.51927632914123,"lng":126.90715217610938,"name":"21세기신천지약국"},
    {"hpid":"C1102398","isOfficial":false,"lat":37.51972330525589,"lng":126.90726023739019,"name":"천우약국"},
    {"hpid":"C1108265","isOfficial":false,"lat":37.51688299656223,"lng":126.90681127166714,"name":"행복한수약국"},
    {"hpid":"C1106994","isOfficial":false,"lat":37.5169621597,"lng":126.906652812,"name":"더블유스토어아름다운약국"},
    {"hpid":"C1101980","isOfficial":false,"lat":37.51412251894385,"lng":126.91176898165945,"name":"공원온누리약국"},
    {"hpid":"C1101554","isOfficial":false,"lat":37.5173475954,"lng":126.9064080018,"name":"금강온누리약국"},
    {"hpid":"C1103199","isOfficial":false,"lat":37.5183625742201,"lng":126.90617948155399,"name":"나은약국"},
    {"hpid":"C1102073","isOfficial":false,"lat":37.5183455428,"lng":126.9059497617,"name":"동보약국"},
    {"hpid":"C1107905","isOfficial":false,"lat":37.522770652800006,"lng":126.9097813715,"name":"온누리정문약국"}
  ]
}
```

#### fail

**HTTP Status code : 400 Bad Request**

```json
{
    "status": 400,
    "msg": "failed",
    "detail": "lat and lng must be included in the query"
}
```

| name    | type   | description      |
| ------- | ------ | ---------------- |
| status  | number | HTTP status code |
| message | string | 에러 메시지      |
| detail  | string | 에러 원인 상세   |



---

### 특정 약국 영업정보

#### Description

특정 약국의 약국명, 연락처 및 요일별 운영시간 정보를 반환합니다.

#### METHOD

`GET`

#### URL

`/hpid = <string>`

#### URL EXAMPLE

`GET`  ` /C1108718`

#### QUERY STRING

| name | type   | require | description    |
| ---- | ------ | ------- | -------------- |
| hpid | string | 필수    | 약국의 hpid 값 |

> url로 특정 약국의 hpid 값을 보냅니다.

### RESPONSE

#### RESPONSE BODY

| name                     | type   | require | description                           |
| ------------------------ | ------ | ------- | ------------------------------------- |
| name                     | string | 필수    | 약국명                                |
| addr                     | string | 필수    | 상세 주소                             |
| tel                      | string | 필수    | 연락처                                |
| 'start': {'mon' ~ 'sun'} | string | 필수    | 약국의 월요일 ~ 일요일  영업시작 시각 |
| 'close': {'mon' ~ 'sun'} | string | 필수    | 약국의 월요일 ~ 일요일  영업종료 시각 |

> 요청에 대한 반환으로 hpid 해당 약국의 운영정보를 반환 합니다.

#### success

**HTTP Status code : 200 success**

```json
{
  "msg":"success",
  "result":{
    "name":"13층약국",
    "addr":"서울특별시 중구 서소문로 116, 유원빌딩 1304호 (서소문동)",
    "tel":"070-7718-1316",
    "start":{"mon":"09:00",
             "tue":"09:00",
             "wed":"09:00",
             "thur":"09:00",
             "fri":"09:00",
             "sat":"휴무일",
             "sun":"휴무일",
            },
    "close":{"mon":"18:30",
             "tue":"18:30",
             "wed":"18:30",
             "thur":"18:30",
             "fri":"18:30",
             "sat":"휴무일",
             "sun":"휴무일",
             "fri":"18:30",
            },
  }
```

#### fail

**HTTP Status code : 400 Bad Request**

```json
{
    "status": 500,
    "msg": "internal server error",
}
```

| name    | type   | description      |
| ------- | ------ | ---------------- |
| status  | number | HTTP status code |
| message | string | 에러 메시지      |



# 담당파트

**이종아** [@jong-a LEE](https://github.com/whddk4415)

- 팀장
- 프로젝트 기본 세팅
- Mongo db 연결 쿼리 제작
- API 구현
- 데이터 전처리

**고동천** [@cheon4050](https://github.com/cheon4050)

- 데이터 전처리
- README 작성

**김진영** [@Jin Kim](https://github.com/gimquokka)

- API 구현
- 데이터 전처리
- 발표 및 README 작성
