from crewai import Agent
from langchain_community.llms import OpenAI

from tools.browser_tools import BrowserTools
from tools.search_tools import SearchTools
from crewai_tools import WebsiteSearchTool
from dotenv import load_dotenv

load_dotenv()
# tool1 = WebsiteSearchTool(website='https://example.com')
# tool2 = WebsiteSearchTool(website='https://example.com')   # 预留权威网站地址，实现在网站内容中进行语义搜索
class CompanyAnalysisAgents:

    def company_information_collector(self):
        return Agent(
            role='Company Information Collector',
            goal='Collect comprehensive company information and data for analysis,The data is preferably cutting-edge,latest (2024), authoritative, and significant',
            backstory='Experienced in gathering and organizing company-related data for analysis',
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
            ],    #如果要加入设置权威网站地址，可以这里加入tool1,tool2。
            verbose=True
        )

    def company_analyst(self):
        return Agent(
            role='Company Analyst',
            goal='Based on the data obtained from the search, analyze the company condition and form an analysis report',
            backstory='Proficient in analyzing company profiles and assessing corporate health',
            tools=[
                BrowserTools.scrape_and_summarize_website,
                SearchTools.search_internet,
            ],
            verbose=True
        )


