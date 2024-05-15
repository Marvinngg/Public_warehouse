from crewai import Task
from textwrap import dedent


class MacroEconomicTasks:

    def collect_macroeconomic_task(self, agent, country):
        return Task(
            description=dedent("""
                Collect comprehensive macroeconomic data and information for analysis.
                This task involves gathering data related to GDP, inflation rate, unemployment rate, 
                interest rates, trade data, government fiscal data, and any other relevant macroeconomic indicators.

                Your final report should include a detailed analysis of macroeconomic trends and factors 
                influencing the economy.

                If you do your BEST WORK, I'll tip you $100!
            """),
            agent=agent
        )

    def analyze_task(self, agent, task):
        return Task(
            description=dedent("""
                Perform in-depth analysis of macroeconomic data and trends.
                This task includes:
                - Analyzing long-term trends and short-term fluctuations in key economic indicators.
                - Identifying causal relationships between different economic variables.
                - Comparing domestic economic data with international benchmarks.
                - Assessing the impact of economic policies on the economy.
                - Evaluating potential risks and uncertainties in the economic environment.
                - Forecasting future economic trends and providing strategic recommendations.

                Your analysis report should be thorough, insightful, and actionable.
                 Your final answer MUST be a Macroeconomic Analysis Report
                If you do your BEST WORK, I'll tip you $100!
            """),
            agent=agent,
            context=[task]
        )