# 1. HTTP 내용 정리
## 1-1. HTTP란?
**HTTP(HyperText Transfer Protocol)**는 웹에서 클라이언트(브라우저, 앱)와 서버가 데이터를 주고받기 위한 약속(프로토콜)이다. 손님(클라이언트)이 종업원(서버)에게 정해진 말투로 주문하고, 서버가 정해진 형식으로 답하는 규칙이라고 보면 된다.
특징:

- 비연결성(Connectionless): 요청-응답이 끝나면 연결을 끊는다.
- 무상태(Stateless): 서버는 이전 요청을 기억하지 않는다. 그래서 로그인 상태 유지를 위해 쿠키, 세션, 토큰(JWT)을 따로 쓴다.
- 요청(Request) - 응답(Response) 구조: 클라이언트가 요청하면 서버가 반드시 응답한다.

## 1-2. HTTP 요청 구조
POST /posts HTTP/1.1          ← 시작 줄 (메서드, 경로, 버전)
Host: example.com             ← 헤더 (메타 정보)
Content-Type: application/json
Authorization: Bearer xxx

{ "title": "안녕", "content": "첫 글" }   ← 바디 (실제 데이터)
구성: 시작 줄 / 헤더 / 바디.

## 1-3. HTTP 메서드 (CRUD와 매핑)
메서드의미CRUD예시GET자원 조회Read게시글 목록 보기POST자원 생성Create새 글 작성PUT자원 전체 수정Update글 통째로 교체PATCH자원 일부 수정Update제목만 수정DELETE자원 삭제Delete글 삭제

## 1-4. HTTP 상태 코드
코드 대역의미대표 예시1xx정보성100 Continue2xx성공200 OK, 201 Created, 204 No Content3xx리다이렉션301 Moved Permanently, 304 Not Modified4xx클라이언트 오류400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found5xx서버 오류500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable

## 1-5. 자주 쓰이는 헤더
- Content-Type: 보내는 데이터 형식 (예: application/json)
- Authorization: 인증 토큰
- Accept: 받고 싶은 응답 형식
- User-Agent: 클라이언트 정보 (브라우저 종류 등)

## 1-6. HTTPS
HTTP에 SSL/TLS 암호화를 추가한 것. 통신 내용을 도청·변조하지 못하게 한다. 요즘 서비스는 사실상 필수.
