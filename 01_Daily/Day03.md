# Day 03 - 파일, 폴더, 터미널, VS Code, 실행 환경

## Today's Goal

개발 작업에서 자주 나오는 파일 경로, 터미널, VS Code, 실행 위치 개념을 이해한다.

## MasterPlan Link

`00_MasterPlan.md`의 Day 3을 따른다.

## Work Log

- 파일은 하나의 문서나 데이터이고, 폴더는 파일을 담는 상자라고 이해했다.
- 경로는 파일이나 폴더의 주소다.
- 절대 경로는 처음부터 끝까지 모두 쓴 주소이고, 상대 경로는 현재 작업 위치를 기준으로 쓴 주소다.
- 명령어는 항상 현재 작업 위치를 기준으로 실행된다는 점을 배웠다.
- VS Code에서 폴더가 보인다고 해서 터미널도 항상 그 폴더에 있는 것은 아니므로, `Get-Location`으로 현재 위치를 확인해야 한다.
- Windows PowerShell과 Ubuntu/WSL은 같은 파일도 경로 표현 방식이 다르다는 점을 배웠다.

## Core Concepts

현재 프로젝트 폴더의 절대 경로:

```text
F:\MyDesktop\AI_30Day_MasterPlan
```

`Day03.md` 파일의 절대 경로:

```text
F:\MyDesktop\AI_30Day_MasterPlan\01_Daily\Day03.md
```

현재 위치가 `F:\MyDesktop\AI_30Day_MasterPlan`일 때 `Day03.md`의 상대 경로:

```text
01_Daily\Day03.md
```

## PowerShell Commands

현재 터미널이 어느 폴더를 기준으로 작업 중인지 확인한다.

```powershell
Get-Location
```

현재 작업 위치를 프로젝트 폴더로 옮긴다.

```powershell
Set-Location F:\MyDesktop\AI_30Day_MasterPlan
```

현재 작업 위치를 기준으로 `Day03.md` 파일 내용을 출력한다.

```powershell
Get-Content 01_Daily\Day03.md
```

## Relative Path Failure Example

현재 위치가 다음과 같다고 가정한다.

```text
C:\Users\un5567
```

이 상태에서 아래 명령어를 실행하면 실패할 수 있다.

```powershell
Get-Content 01_Daily\Day03.md
```

이유는 PowerShell이 실제로 다음 위치에서 파일을 찾으려 하기 때문이다.

```text
C:\Users\un5567\01_Daily\Day03.md
```

하지만 실제 파일은 다음 위치에 있다.

```text
F:\MyDesktop\AI_30Day_MasterPlan\01_Daily\Day03.md
```

해결 방법은 두 가지다.

1. 먼저 프로젝트 폴더로 이동한 뒤 상대 경로를 사용한다.

```powershell
Set-Location F:\MyDesktop\AI_30Day_MasterPlan
Get-Content 01_Daily\Day03.md
```

2. 현재 위치를 바꾸지 않고 절대 경로를 사용한다.

```powershell
Get-Content F:\MyDesktop\AI_30Day_MasterPlan\01_Daily\Day03.md
```

## Windows And WSL Paths

Windows PowerShell 경로:

```text
F:\MyDesktop\AI_30Day_MasterPlan
```

Ubuntu/WSL에서 보이는 경로:

```text
/mnt/f/MyDesktop/AI_30Day_MasterPlan
```

변환 규칙:

```text
C:\  ->  /mnt/c/
F:\  ->  /mnt/f/
```

주의:

- Windows는 보통 `\`를 사용한다.
- Ubuntu/WSL은 `/`를 사용한다.
- `F:\MyDesktop`은 WSL에서 `/mnt/f/MyDesktop`으로 보인다.

## LLM Wiki Note Candidate

Title: 파일 경로, 터미널, VS Code, 실행 위치

Tags: `PowerShell`, `Path`, `VS Code`, `WSL`, `Beginner`

Summary:

개발에서 명령어는 항상 현재 작업 위치를 기준으로 실행된다. 상대 경로는 현재 위치에 따라 의미가 달라지고, 절대 경로는 현재 위치와 상관없이 같은 파일을 가리킨다. VS Code에서 폴더를 열었더라도 터미널의 현재 위치를 확인해야 하며, Windows와 Ubuntu/WSL은 같은 파일도 경로 표현 방식이 다르다.

## Questions For Next Time

1. Git은 왜 필요한가?
2. Git과 GitHub는 어떻게 다른가?
3. commit은 어떤 순간에 해야 하는가?

## Review Plan

Day 4를 시작하기 전에 Day 1-3 핵심을 짧게 복습한다.
