# AI Crew for analyse_report
## Introduction
1.内置3个crew，分别完成行业分析、公司分析、宏观经济分析。

2.预留llm的选择，在llms.py中可以加入自己想用的llm，然后需要在对应的agent文件中导包，然后将agent的llm属性设置为LLMs(model_name="你想使用的llm").get_llm()

当然也可以直接from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model='gpt-3.5') # Loading GPT-3.5

3.预留搜索网页设置，在agent中，注释掉的tool1 = WebsiteSearchTool(website='https://example.com')语句可以设置想要检索网址。然后将tool1添加导agent的tool属性中

4.预留api，采用flask编写api，如果想运行为一个api，就将下面的运行指令改为poetry run python api_main.py


5.预留scraperGraph,作为search+broswer的平替（有版本冲突问题，后续解决）

## Running the Script
默认使用gpt4

***Disclaimer:** token需求量很大，估计用几次就会到api key的限制*

- **设置环境变量**: .env文件
- **安装依赖**: 运行 `poetry install --no-root`.
- **运行主函数**: 运行 `poetry run python main.py` .



## Using Local Models with Ollama
The CrewAI framework supports integration with local models, such as Ollama, for enhanced flexibility and customization. This allows you to utilize your own models, which can be particularly useful for specialized tasks or data privacy concerns.

### Setting Up Ollama
- **Install Ollama**: Ensure that Ollama is properly installed in your environment. Follow the installation guide provided by Ollama for detailed instructions.
- **Configure Ollama**: Set up Ollama to work with your local model. You will probably need to [tweak the model using a Modelfile](https://github.com/jmorganca/ollama/blob/main/docs/modelfile.md), I'd recommend adding `Observation` as a stop word and playing with `top_p` and `temperature`.

### Integrating Ollama with CrewAI
- Instantiate Ollama Model: Create an instance of the Ollama model. You can specify the model and the base URL during instantiation. For example:

```python
from langchain.llms import Ollama
ollama_openhermes = Ollama(model="agent")
# Pass Ollama Model to Agents: When creating your agents within the CrewAI framework, you can pass the Ollama model as an argument to the Agent constructor. For instance:

def local_expert(self):
	return Agent(
		role='Local Expert at this city',
		goal='Provide the BEST insights about the selected city',
		backstory="""A knowledgeable local guide with extensive information
		about the city, it's attractions and customs""",
		tools=[
			SearchTools.search_internet,
			BrowserTools.scrape_and_summarize_website,
		],
		llm=ollama_openhermes, # Ollama model passed here
		verbose=True
	)
```

### Advantages of Using Local Models
- **Privacy**: Local models allow processing of data within your own infrastructure, ensuring data privacy.
- **Customization**: You can customize the model to better suit the specific needs of your tasks.
- **Performance**: Depending on your setup, local models can offer performance benefits, especially in terms of latency.

## License
This project is released under the MIT License.
