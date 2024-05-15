from crewai import Crew
from textwrap import dedent
from company_agents import CompanyAnalysisAgents
from company_tasks import CompanyAnalysisTasks
from industry_agents import IndustryAnalysisAgents
from industry_tasks import IndustryAnalysisTasks
from macroeconomic_agents import MacroeconomicAnalysisAgents
from macroeconomic_tasks import MacroEconomicTasks
from dotenv import load_dotenv
from flask import Flask, request, jsonify
load_dotenv()
app = Flask(__name__)

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.json
    user_input = data.get('user_input')

    intent = identify_intent(user_input)
    if intent:
        result = create_crew_and_run(intent, user_input)
        return jsonify({'result': result})
    else:
        return jsonify({'error': '无法识别意图'})

def identify_intent(user_input):
    keyword = user_input.split()[0].lower()

    if keyword in ['company', '公司']:
        return 'company'
    elif keyword in ['industry', '行业']:
        return 'industry'
    elif keyword in ['macroeconomic', '宏观经济']:
        return 'macroeconomic'
    else:
        return None

def create_crew_and_run(intent, user_input):
    if intent == 'company':
        company_name = ' '.join(user_input.split()[1:])
        crew = CompanyCrew(company_name)
    elif intent == 'industry':
        industry_name = ' '.join(user_input.split()[1:])
        crew = IndustryCrew(industry_name)
    elif intent == 'macroeconomic':
        country = ' '.join(user_input.split()[1:])
        crew = MacroeconomicCrew(country)
    else:
        return "无法识别意图。"

    result = crew.run()
    return result


class CompanyCrew:

    def __init__(self, company_name):
        self.company_name = company_name

    def run(self):
        agents = CompanyAnalysisAgents()
        tasks = CompanyAnalysisTasks()

        company_information_agent = agents.company_information_collector()
        company_analyst_agent = agents.company_analyst()

        collect_company_task = tasks.collect_company_information_task(
            company_information_agent,
            self.company_name,
        )
        analyze_task = tasks.analyze_task(
            company_analyst_agent,
            collect_company_task
        )

        crew = Crew(
            agents=[company_information_agent, company_analyst_agent],
            tasks=[collect_company_task, analyze_task],
            verbose=True
        )

        result = crew.kickoff()
        return result


class IndustryCrew:

    def __init__(self, industry_name):
        self.industry_name = industry_name

    def run(self):
        agents = IndustryAnalysisAgents()
        tasks = IndustryAnalysisTasks()
        industry_information_collector_agent = agents.industy_information_collector()
        industry_analyst_agent = agents.industy_analyst()

        collect_industry_task = tasks.collect_industry_information_task(
            industry_information_collector_agent,
            self.industry_name,
        )
        analyze_task = tasks.analyze_industry_task(
            industry_analyst_agent,
            collect_industry_task
        )

        crew = Crew(
            agents=[industry_information_collector_agent, industry_analyst_agent],
            tasks=[collect_industry_task, analyze_task],
            verbose=True
        )

        result = crew.kickoff()
        return result


class MacroeconomicCrew:

    def __init__(self, country):
        self.country = country

    def run(self):
        agents = MacroeconomicAnalysisAgents()
        tasks = MacroEconomicTasks()
        macroeconomic_information_collector_agent = agents.macroeconomic_information_collector()
        macroeconomic_analyst_agent = agents.macroeconomic_analyst()

        collect_macroeconomic_task = tasks.collect_macroeconomic_task(
            macroeconomic_information_collector_agent,
            self.country,
        )
        analyze_task = tasks.analyze_task(
            macroeconomic_analyst_agent,
            collect_macroeconomic_task
        )

        crew = Crew(
            agents=[macroeconomic_information_collector_agent, macroeconomic_analyst_agent],
            tasks=[collect_macroeconomic_task, analyze_task],
            verbose=True
        )

        result = crew.kickoff()
        return result

if __name__ == "__main__":
    app.run(debug=True)
