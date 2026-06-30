# Day 09 - MCP 입문

## Today's Goal

MCP(Model Context Protocol)가 LLM 앱을 외부 도구와 데이터에 연결하는 표준 방식임을 이해하고, host, client, server, tools, resources, prompts를 구분한다. 특히 MCP 서버를 설치하거나 연결할 때 권한과 보안 위험을 먼저 점검하는 습관을 만든다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 9를 따른다.

## Review From Day 08

- LLM Wiki는 AI가 자동으로 만든 요약 저장소가 아니라, source, AI summary, my understanding을 분리해서 관리하는 개인 연구 지식 시스템이다.
- Agent가 Wiki를 읽고 도와줄 수는 있지만, 최종 이해와 판단은 사람이 검증해야 한다.
- 오늘의 MCP는 Day 8의 Wiki와 자연스럽게 연결된다. MCP를 쓰면 LLM 앱이 파일, 문서, 데이터베이스, 검색 도구 같은 외부 맥락에 접근할 수 있기 때문이다.

## Work Log

- MCP를 "AI 앱용 USB-C 포트"처럼 이해했다. 모델 자체가 모든 도구를 직접 아는 것이 아니라, 표준 규격을 통해 외부 서버가 제공하는 기능을 발견하고 호출한다.
- host, client, server의 역할을 분리했다. host는 Claude Desktop, Codex, IDE 같은 전체 앱이고, client는 host 안에서 특정 MCP server와 1:1로 연결되는 통신 주체이며, server는 tools/resources/prompts를 노출하는 외부 프로그램이다.
- tools, resources, prompts의 차이를 정리했다. tool은 실행 가능한 행동, resource는 읽을 수 있는 맥락 데이터, prompt는 재사용 가능한 작업 템플릿이다.
- MCP가 편리한 이유와 위험한 이유가 같은 지점에서 나온다는 것을 확인했다. LLM이 파일 읽기, 명령 실행, API 호출 같은 실제 행동에 가까워질수록 권한 범위, 비용, 개인정보, 데이터 유출 위험도 커진다.
- 오늘은 실제 MCP 서버 설치까지 가지 않고, 연결 전 점검표와 개념 지도를 만드는 단계로 제한했다.

## Core Concept

MCP는 LLM이 외부 세계와 상호작용하는 방식을 표준화하려는 프로토콜이다. 핵심은 "모델이 모든 도구를 내장한다"가 아니라 "host 앱이 MCP server가 제공하는 기능을 발견하고, 필요할 때 정해진 방식으로 호출한다"이다.

```text
User
  -> Host app
      -> MCP client
          -> MCP server
              -> tools / resources / prompts
```

### Host

Host는 사용자가 실제로 사용하는 AI 애플리케이션이다.

예:

```text
Claude Desktop
Codex
AI 기능이 들어간 IDE
내가 만든 LLM 앱
```

Host의 책임은 사용자와 대화하고, 어떤 MCP server를 연결할지 관리하고, 위험한 행동에는 승인 절차를 두는 것이다.

### Client

Client는 host 안에서 MCP server 하나와 연결되는 통신 담당자다. 중요한 점은 보통 "client 하나가 server 하나와 연결된다"는 구조다. 여러 MCP server를 쓰면 host 안에 여러 client 연결이 생긴다고 보면 된다.

### Server

Server는 외부 기능을 제공하는 프로그램이다. 파일 시스템, GitHub, 데이터베이스, 논문 검색, 사내 문서, 브라우저 자동화 같은 기능을 MCP 형식으로 노출할 수 있다.

Server는 모델이 아니다. Server는 "모델이 사용할 수 있는 기능 목록과 실행 방법"을 제공하는 쪽이다.

### Tools

Tool은 실행 가능한 행동이다.

예:

```text
read_file(path)
search_docs(query)
run_sql(query)
create_issue(title, body)
send_slack_message(channel, text)
```

Tool은 외부 상태를 바꿀 수 있으므로 가장 조심해야 한다. 특히 파일 쓰기, 삭제, 네트워크 요청, 결제 API, 이메일/메신저 발송은 반드시 승인과 범위 제한이 필요하다.

### Resources

Resource는 LLM이 읽을 수 있는 맥락 데이터다.

예:

```text
project://README.md
docs://mcp/security
db-schema://lab_samples
wiki://concepts/RAG
```

Resource는 보통 "읽기" 중심이다. 하지만 읽기 전용이어도 개인정보, unpublished data, API key, 내부 문서가 포함될 수 있으므로 안전하다고 단정하면 안 된다.

### Prompts

Prompt는 재사용 가능한 작업 템플릿이다.

예:

```text
paper_review_prompt
bug_triage_prompt
experiment_summary_prompt
weekly_study_review_prompt
```

Prompt는 기능을 실행하는 것이 아니라, 특정 작업을 일관된 방식으로 수행하도록 입력 형식을 제공한다.

## Mental Model

MCP를 이렇게 구분하면 헷갈리지 않는다.

```text
Host      = 내가 쓰는 AI 앱
Client    = host 안의 server별 연결 담당자
Server    = 도구와 데이터를 제공하는 외부 프로그램
Tool      = 실행 가능한 행동
Resource  = 읽을 수 있는 데이터/문맥
Prompt    = 재사용 가능한 지시 템플릿
```

틀리기 쉬운 이해:

```text
MCP server = AI 모델
```

정확한 이해:

```text
MCP server = AI 앱이 사용할 수 있는 외부 기능 제공자
```

## Security Checklist Before Connecting An MCP Server

MCP 서버를 연결하기 전에 최소한 아래를 확인한다.

1. 이 서버가 읽을 수 있는 파일/폴더 범위는 어디까지인가?
2. 이 서버가 쓸 수 있는 파일/폴더 범위가 있는가?
3. 네트워크 요청을 보낼 수 있는가?
4. 외부 API key, token, cookie, 로그인 세션에 접근하는가?
5. 비용이 발생할 수 있는 API를 호출하는가?
6. 삭제, 전송, 게시, 이메일/메신저 발송처럼 되돌리기 어려운 tool이 있는가?
7. tool 호출 전에 host가 사용자 승인을 요구하는가?
8. 로그에 민감한 데이터가 남는가?

핵심 원칙:

```text
읽기 권한도 권한이다.
쓰기 권한은 더 큰 권한이다.
네트워크 권한은 데이터 유출 경로가 될 수 있다.
비용이 드는 API는 항상 사전 승인 대상이다.
```

## Practical Example: LLM Wiki + MCP

Day 8에서 만든 LLM Wiki를 MCP와 연결한다고 가정하면 다음 구조가 가능하다.

```text
Host: Codex 또는 Claude Desktop
MCP server: local filesystem/wiki search server
Resource: 06_LLM_Wiki/README.md, concept notes, paper notes
Tool: search_wiki(query), read_note(path)
Prompt: summarize_source_into_wiki_note
```

좋은 연결:

```text
LLM이 Wiki 노트를 검색하고, 관련 노트를 읽고, 답변에서 출처 파일을 언급한다.
```

위험한 연결:

```text
LLM이 전체 홈 디렉터리를 읽을 수 있고, API key나 개인 파일까지 접근할 수 있다.
```

따라서 처음에는 읽기 전용, 좁은 폴더 범위, 비용 없는 tool부터 시작하는 것이 맞다.

## Practice Questions

### Basic

1. Host, client, server를 각각 한 문장으로 설명하라.
2. Tool과 resource의 차이를 설명하라.
3. Prompt가 tool과 다른 점은 무엇인가?

### Intermediate

아래 기능을 tool, resource, prompt 중 하나로 분류하라.

```text
1. "프로젝트 README 파일 내용"
2. "GitHub issue를 생성하는 함수"
3. "논문을 정리하는 재사용 템플릿"
4. "SQLite 데이터베이스에서 query를 실행하는 함수"
5. "분석 프로젝트의 schema 문서"
```

정답:

```text
1. resource
2. tool
3. prompt
4. tool
5. resource
```

### Hard

다음 MCP server 설정은 왜 위험한가?

```text
filesystem server:
  read: C:\Users\<user>
  write: C:\Users\<user>
  network: allowed
approval:
  tool_calls: auto
```

해설:

홈 디렉터리 전체에 읽기/쓰기 권한이 있고, 네트워크 전송까지 가능하며, tool 호출이 자동 승인이다. 이 조합은 민감한 파일 유출, 실수로 인한 파일 변경, 외부 API 호출, 로그 유출 위험을 동시에 만든다. 최소 권한 원칙에 맞게 특정 프로젝트 폴더만 읽기 전용으로 열고, 쓰기/네트워크/tool 실행은 별도 승인으로 제한해야 한다.

## Files Updated Today

```text
01_Daily/Day09.md
02_Concepts/MCP_Basics.md
08_References/Source_Map.md
```

## LLM Wiki Note Candidate

Title: MCP 기본 구조와 보안 원칙

Tags: `MCP`, `Model Context Protocol`, `Agent`, `Tool Use`, `Security`, `LLM Wiki`

Summary:

MCP는 LLM host app이 외부 tools, resources, prompts를 표준 방식으로 발견하고 사용할 수 있게 하는 프로토콜이다. Host는 사용자가 쓰는 AI 앱이고, client는 host 안에서 MCP server와 연결되는 통신 주체이며, server는 실제 도구와 데이터를 제공한다. Tool은 실행 가능한 행동, resource는 읽을 수 있는 맥락 데이터, prompt는 재사용 가능한 지시 템플릿이다. MCP 서버를 연결할 때는 파일 접근 범위, 쓰기 권한, 네트워크 권한, 비용 발생 API, 자동 승인 여부를 먼저 점검해야 한다.

## Questions For Next Time

1. Day 10 미니 프로젝트에서 어떤 작은 데이터를 분석해서 Wiki 노트로 남길 것인가?
2. 분석 결과를 단순 출력이 아니라 "재사용 가능한 지식"으로 만들려면 어떤 구조가 필요한가?
3. 나중에 MCP로 LLM Wiki를 연결한다면, 처음에는 어떤 폴더를 읽기 전용으로 열어야 안전한가?
