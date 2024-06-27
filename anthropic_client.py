import anthropic

class AnthropicClient:
    _instance = None

    def __init__(self):
        self.client = anthropic.Anthropic()
        self.model = "claude-3-haiku-20240307"

    #A factory method to ensure that only a single instance of this class is created.  This function does this by
    #storing the single instance of the class in the class variable _instance.  When get_instance is called, the func
    #checks to see if _instance is None.  If it does not exist, it will set the class variable to the return from cls()
    #which triggers the __init__ function.  If it does exist, the function returns the already existing instance
    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            #Calling cls() triggers the __init__ function for the class
            cls._instance = cls()
            print("creating new instance of anthropic client")
        else:
            print("Instance already exists")
        return cls._instance
    
    def send_message(self, prompt:str):
        message = self.client.messages.create(
            model=self.model,
            max_tokens=2000, # The number of tokens claud will generate in its response before stopping (probably to restrict cost and usage)
            temperature=0.0,
            messages=[
                {"role":"user", "content": prompt}
            ]
        )
        return message.content[0].text


    def analyze_headlines(self, headlines:str):
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                temperature=0,
                #Provide context, instruction and guidelines to claud as to how it should formulate its response
                #Use this to set rules for how the system should respond.  In the first iteration of this project, I told
                #claud not to only summarize values and not to add any extra words or content.  That should have gone
                #here
                system="You are working as a blogger trying to summarize the AI news of the day.  When you answer, do not add any extra text.  Just respond with the summary.",
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": f"Here are some headlines realated to AI from todays news, can you write me a one paragraph summary of what is happening today?\n{headlines}"
                            }
                        ]
                    }
                ]
            )
            return message.content[0].text
        except anthropic.APIConnectionError as e:
            print("The server could not be reached")
            print(e.__cause__)  # an underlying Exception, likely raised within httpx.
        except anthropic.RateLimitError as e:
            print("A 429 status code was received; we should back off a bit.")
        except anthropic.APIStatusError as e:
            print("Another non-200-range status code was received")
            print(e.status_code)
            print(e.response)