from crewai import Task
from textwrap import dedent


class IndustryAnalysisTasks:

    def collect_industry_information_task(self, agent, industry_name):
        return Task(
            description=dedent(f"""
                Collect comprehensive information and data about the "{industry_name}" industry for analysis.
                The data is preferably cutting-edge, authoritative, and significant
                This task involves gathering market reports, industry trends, regulatory updates, and any other
                relevant information to understand the dynamics of the industry.

                Your final report should include detailed findings and insights about the industry's
                market size, growth trends, competitive landscape, regulatory environment, and any other
                significant factors influencing the industry.

                If you do your BEST WORK, I'll tip you $100!

                Industry Name: {industry_name}
            """),
            agent=agent
        )

    def analyze_industry_task(self, agent, task):
        return Task(
            description=dedent(f"""
                Perform in-depth analysis of the  industry using available data and information.
                This task includes:
                - Analyzing market trends, growth prospects, and competitive landscape.
                - Assessing industry dynamics, including supply-demand balance and regulatory influences.
                - Evaluating technological advancements and innovation trends within the industry.
                - Formulating strategic recommendations based on analysis findings.

                Your analysis report should be thorough, insightful, and actionable.
                 Your final answer MUST be a industry Analysis Report
                If you do your BEST WORK, I'll tip you $100!

    
            """),
            agent=agent,
            context=[task]
        )