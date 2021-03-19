from aiohttp.client import ClientSession


class KDCA:
    def __init__(self) -> None:
        self.ncv_root_url = "https://ncv.kdca.go.kr/"  # 질병관리청/중앙방역대본부 코로나 19 예방접종 현황 사이트 URL
        self.ncv_main_status_uri = "mainStatus.es?mid=a11702000000"  # 예방접종 상세 현황 (접종실적 총괄/시도별 접종 현황) 페이지 URI

    @staticmethod
    async def fetch_html(url: str, headers: dict) -> str:
        """Fetch HTML

        :param url: 가져올 웹 페이지 URL
        :param headers: User-Agent 포함한 HTTP header
        :return: UTF-8 encoded HTML
        """
        async with ClientSession(headers=headers) as session:
            async with session.get(url=url) as resp:
                HTTP_STATUS_CODE: int = resp.status

                # HTTP STATUS CODE 가 200이 아닐경우 ClientResponseError 반환
                if HTTP_STATUS_CODE != 200:
                    raise resp.raise_for_status()
                html_enc = await resp.text(encoding="utf-8")
        return html_enc

    async def ncv_status_classification(self):
        USER_AGENT = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.48 "
        }
        html = await self.fetch_html(url=self.ncv_root_url + self.ncv_main_status_uri, headers=USER_AGENT)






