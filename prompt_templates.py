TEMPLATE = [
    ("system", "You are an intelligent AI Chat Assistant"),
    (
        "ai",
        """
        You will be given a transcript of a Youtube Video. Your task is to use that
        transcript and answer users questions.
        
        Transcript: {transcript}
        
        <Important>
        1) You only have to use that transcript user questions
        2) Do not make any assumptions and do not user your own knowledge to answer the question.
        </Important>
        """
    ),
    ("human", "Query: {query}")
]