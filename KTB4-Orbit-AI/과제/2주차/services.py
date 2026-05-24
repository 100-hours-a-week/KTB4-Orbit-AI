# 외부 LLM API 연동 레이어
# 참고 URL: https://github.com/google/generative-ai-python


from google import genai


def summarize_text(text: str) -> str:
    """Gemini 2.5 Flash 모델을 호출하여 본문이나 댓글을 요약합니다.

    [Google GenAI 공식 가이드 규칙]
    환경 변수 인식 오류를 방지하기 위해 Client 생성자에 api_key를 명시적으로 주입합니다.
    출처: https://github.com/google/generative-ai-python
    """
    try:
        # 아래 api키는 보안 이쓔로 인해 이렇게 해서 올렸슴다
        client = genai.Client()
        
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"다음 내용을 한 문장으로 핵심만 요약해줘:\n\n{text}",
        )
        
        if not response or not response.text:
            return "[LLM 요약 실패] 반환된 응답 결과가 비어있습니다."
            
        return response.text.strip()
    except Exception as e:
        return f"[LLM 요약 실패] API 키 연동 상태를 확인하세요. (사유: {str(e)})"