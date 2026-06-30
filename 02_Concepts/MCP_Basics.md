# MCP Basics

## One-Line Definition

MCP(Model Context Protocol)는 LLM 애플리케이션이 외부 도구와 데이터 소스를 표준 방식으로 연결하기 위한 프로토콜이다.

## Why MCP Exists

LLM은 텍스트를 생성하는 모델이다. 하지만 실제 작업에서는 파일 읽기, 코드 실행, 문서 검색, 데이터베이스 조회, 이슈 생성, 브라우저 조작 같은 외부 기능이 필요하다.

MCP는 이런 외부 기능을 매번 앱마다 새로 붙이는 대신, 공통 규격으로 연결하려는 구조다.

## Architecture

```text
User
  -> Host
      -> MCP Client
          -> MCP Server
              -> Tools
              -> Resources
              -> Prompts
```

## Terms

### Host

사용자가 직접 쓰는 AI 애플리케이션이다.

예:

```text
Claude Desktop
Codex
AI IDE
custom LLM app
```

Host는 사용자 인터페이스, 모델 호출, MCP server 연결 관리, 승인 흐름을 담당한다.

### Client

Host 내부에서 특정 MCP server와 통신하는 연결 주체다. 일반적으로 client-server 연결은 1:1로 생각하면 된다.

### Server

Tools, resources, prompts를 제공하는 외부 프로그램이다. MCP server는 모델이 아니라 기능 제공자다.

예:

```text
filesystem server
GitHub server
database server
documentation search server
browser automation server
```

### Tools

실행 가능한 행동이다. 외부 상태를 바꿀 수 있으므로 가장 위험도가 높다.

```text
read_file(path)
write_file(path, content)
run_sql(query)
create_github_issue(title, body)
send_email(to, subject, body)
```

### Resources

LLM이 읽을 수 있는 데이터나 문맥이다.

```text
project README
API documentation
database schema
LLM Wiki note
paper metadata
```

읽기 전용이어도 민감한 데이터가 포함될 수 있으므로 권한 검토가 필요하다.

### Prompts

재사용 가능한 지시 템플릿이다. 도구 실행이 아니라 작업 형식을 표준화한다.

```text
paper review template
bug triage template
weekly review template
experiment summary template
```

## Tool vs Resource vs Prompt

```text
Tool     = do something
Resource = read something
Prompt   = guide how to ask or perform a task
```

예:

```text
search_wiki(query)                 -> tool
06_LLM_Wiki/concepts/RAG.md        -> resource
summarize_paper_for_wiki_template  -> prompt
```

## Security Model

MCP의 장점은 LLM이 실제 작업 환경과 연결된다는 점이다. 위험도 같은 이유에서 생긴다.

점검할 항목:

```text
file read scope
file write scope
network access
API key/token/cookie access
cost-generating API calls
destructive tools
automatic approval settings
logging of sensitive content
```

권장 원칙:

```text
1. 최소 권한으로 시작한다.
2. 처음에는 읽기 전용 resource부터 연결한다.
3. write/delete/send/pay 같은 tool은 자동 실행하지 않는다.
4. project folder 단위로 범위를 제한한다.
5. 비용과 외부 전송 가능성이 있으면 사전 승인을 둔다.
```

## Relation To LLM Wiki

LLM Wiki를 MCP로 연결하면 host가 Wiki 노트를 검색하고 읽을 수 있다.

안전한 시작점:

```text
read-only access:
  F:\MyDesktop\AI_30Day_MasterPlan\06_LLM_Wiki
allowed tools:
  search_notes
  read_note
blocked initially:
  write_note
  delete_file
  network_send
```

나쁜 시작점:

```text
read/write access:
  C:\Users\<user>
network:
  allowed
approval:
  automatic
```

이 설정은 홈 디렉터리 전체 유출, 파일 변경, 외부 전송 위험을 만든다.

## Key Takeaway

MCP는 "AI가 무엇을 할 수 있는가"를 확장하는 연결 규격이다. 따라서 MCP를 배울 때는 기능보다 먼저 권한 경계를 봐야 한다.

## References

- Model Context Protocol official documentation: https://modelcontextprotocol.io/docs/getting-started/intro
- Model Context Protocol specification: https://modelcontextprotocol.io/specification/
