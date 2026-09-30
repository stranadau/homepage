# 학술대회 논문 올리는 곳

이 폴더에 파일을 올리면 홈페이지 **논문 > 학술대회 논문** 목록이 자동으로 갱신됩니다.
(GitHub에 올린 뒤 1~2분 안에 https://stranadau.github.io/homepage/publications/ 에 반영)

## 올리는 방법 (GitHub 웹)

1. 이 폴더(`conference_papers`)에서 **Add file > Upload files**를 누릅니다.
2. 논문 PDF와 정보 카드(.yaml)를 **같은 이름**으로 함께 올립니다.
   - 예: `2026-05-28_KSNVE_multi-crack.pdf` 와 `2026-05-28_KSNVE_multi-crack.yaml`
   - 카드는 `_template.yaml`을 복사해서 내용만 바꾸면 됩니다.
3. 아래쪽 **Commit changes**를 누르면 끝입니다.

## 파일 이름 규칙

`연도-월-일_학회약칭_짧은이름.pdf` (월·일은 생략 가능: `2026_ICSV32_scattering.pdf`)

- 공백 대신 `_`를 쓰세요.
- 카드 없이 PDF만 올려도 목록에 나오지만, 이때는 파일 이름에서 연도·학회·제목만 읽기 때문에
  **저자가 표시되지 않습니다.** 가능하면 카드를 함께 올려 주세요.
- PDF 없이 카드만 올리면 PDF 링크 없이 목록에만 추가됩니다.

## 카드 항목

| 항목 | 필수 | 내용 |
|---|---|---|
| authors | O | 저자 (예: `Jin Ho Hwang and Hyun Woo Park`) |
| title | O | 논문 제목 |
| venue | O | 학술대회 이름 (예: `Proceedings of the KSNVE Spring Conference 2026`) |
| year | O | 연도 |
| date | | 발표일 `YYYY-MM-DD` — 같은 해 안에서 순서를 정합니다 |
| details | | 쪽수·장소 등. 비우면 연도만 표시 |
| url | | DOI 등 링크 |

## 참고

- 목록은 연도 기준 최신순이며, 이 폴더에서 올린 논문이 같은 해의 기존 논문보다 앞에 옵니다.
- 수정은 카드 파일을 고치면 되고, 삭제는 PDF와 카드를 지우면 됩니다.
- 이 폴더의 논문은 `/legacy/` 옛 홈페이지 논문 목록(`publications*.htm`)에는 자동으로 들어가지 않습니다.
- 이름이 `_`로 시작하는 파일(`_template.yaml`)과 이 README는 목록에 나오지 않습니다.
