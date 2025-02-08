import os

class Config:
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "sk-svcacct-zAMfrDzUDkPBna14CfBI4StFmyV0RFjrrTqdUPhiJ3we8T0l07CB39X3vS11aujdLT3BlbkFJKtqa_oATFOvjrvocEooJQGTU6nF4o6JsWxAvetMF4DZgrS1W5deiZGYA3KyQfk-nQA")
    SECRET_KEY = os.urandom(24)
