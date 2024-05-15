from crewai import Task
from textwrap import dedent



class CompanyAnalysisTasks:

    def collect_company_information_task(self, agent, company_name):
        return Task(
            description=dedent(f"""
                Collect comprehensive information and data about the company "{company_name}" for detailed analysis.
                The data is preferably cutting-edge, authoritative, and significant
                This task involves gathering financial reports, market data, and any relevant
                information to understand the company's position in the market and its competitive
                landscape.

                Your final report should include detailed findings and datas about the company's
                financial performance, market share, key competitors, and any other relevant metrics.

                {self.__tip_section()}

                Company Name: {company_name}
            """),
            agent=agent
        )

    def analyze_task(self, agent, task):
        return Task(
            description=dedent(f"""
                Conduct in-depth analysis of the company's financial performance, market position,
                business operations, and strategic positioning for a comprehensive understanding of the company.

                This task includes:
                - Conducting in-depth analysis of the company's financial performance, including detailed interpretation
                  of financial statements, calculation and evaluation of key financial indicators, to better understand
                  the company's profitability, solvency, and operational efficiency.
                - Assessing the company's market position within its industry, investigating factors such as market share,
                  market growth rate, and competitive landscape, to help users understand the company's competitiveness
                  and position in the industry.
                - Analyzing the company's business operations, including business model, products and services, customer
                  base, sales channels, etc., to gain a more comprehensive understanding of the company's business
                  operations and market positioning.
                - Analyzing the company's strategic positioning, including strategic planning, development goals, core
                  competencies, and market positioning, to help users understand the company's future development
                  direction and strategic planning.

                Your analysis should be logical, comprehensive, and methodical.
                 Your final answer MUST be a Company Analysis Report
                If you do your BEST WORK, I'll tip you $100!
            """),
            agent=agent,
            context=[task]
        )

    def __tip_section(self):
        return "If you do your BEST WORK, I'll tip you $100!"