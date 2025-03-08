**Task:**

Extracting the TRANSCRIPT  given YOUTUBE video ID and give a summary using GPT model. 

  

**Source for this task:**

https://www.youtube.com/watch?v=4y9ss33QWTY

  

  

**APIs used:**

SearchAPI.io

OpenAi

  

  

**_PROMPT to CLINE in VSC:_**

  

I want to create a python script that transforms Youtube videos into bullet point summaries.

  

**Step1:** To extract the YouTube video transcript with the following API:

  

Example api Request:

  

import requests

  

url = "https://www.searchapi.io/api/v1/search"

params = {

  "engine": "youtube\_transcripts",

  "video\_id": "0e3GPea1Tyg",

  "api\_key": "mtg3mRduLn4zU38wqrWdKu7i"

}

  

response = requests.get(url, params=params)

print(response.text)

  

  

Example API response :

  

{

  "search\_metadata": {

    "id": "search\_xRvzEGkNolVqF6MLpj4Q9WJb",

    "status": "Success",

    "created\_at": "2023-09-15T13:59:31Z",

    "request\_time\_taken": 1.79,

    "parsing\_time\_taken": 0.01,

    "total\_time\_taken": 1.8,

    "request\_url": "https://www.youtube.com/watch?v=0e3GPea1Tyg",

    "html\_url": "https://www.searchapi.io/api/v1/searches/search\_xRvzEGkNolVqF6MLpj4Q9WJb.html",

    "json\_url": "https://www.searchapi.io/api/v1/searches/search\_xRvzEGkNolVqF6MLpj4Q9WJb"

  },

  "search\_parameters": {

    "engine": "youtube\_transcripts",

    "video\_id": "0e3GPea1Tyg",

    "lang": "en"

  },

  "transcripts": \[

    {

      "text": "- \[Mr. Beast\] I've recreated every single set",

      "start": 0.15,

      "duration": 1.773

    },

    {

      "text": "from Squid Game in real life,",

      "start": 1.923,

      "duration": 1.857

    },

    ...

  \],

  "available\_languages": \[

    {

      "name": "Arabic",

      "lang": "ar"

    },

    {

      "name": "English",

      "lang": "en"

    },

    ...

  \],

}

  

  

**Step2:** Use OpenAI Api to summarize the transcript with “gpt-4o” model.

  

Then print the output in the console.

  

**Step3**: Paste the above prompt and hit the PLAN button. It generates the PYTHON code on its OWN and then will ask you to run the PY script

  

**Step4**: Once you run all it would ask for is the API keys for SearchAPI.io and OpenAi .For this you should have created an account with both OPENAI and SEARCH.io 

  

  

**step5**: ERRORS:

You will run into version issues with OPENAI and you can fix this by implementing the recommendation ===> pip install openai==0.28

  

An error occurred: 

  

You tried to access openai.ChatCompletion, but this is no longer supported in openai>=1.0.0 - see the README at https://github.com/openai/openai-python for the API.

  

You can run \`openai migrate\` to automatically upgrade your codebase to use the 1.0.0 interface. 

  

Alternatively, you can pin your installation to the old version, e.g. \`pip install openai==0.28\`

  

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

  

  

**Step6**:  

Summary:

  

\- AI agents are currently a hot market trend, presenting opportunities to sell them.

\- Contrary to popular belief, building AI agents doesn't require extensive technical skills.

\- The video provides a step-by-step guide to planning, building, and selling AI agents.

\- Key topics include finding profitable AI agent ideas and automating workflows for tasks like YouTube channel management and social media engagement.

\- Methods to discover AI agent opportunities include analyzing workflows and using websites like Future Pia and Agent.a.

\- The video emphasizes the use of AI to generate and automate scripts efficiently in platforms like VS Code.

\- Important tips include understanding the project, breaking it into small tasks, and reviewing AI-generated outputs.

\- Examples demonstrate creating an AI agent for summarizing YouTube videos using APIs
