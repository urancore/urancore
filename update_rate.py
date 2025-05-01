import requests
from datetime import datetime

response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
data = response.json()

# Extract and format data
usd_rate = data['Valute']['USD']['Value']
date = datetime.fromisoformat(data['Date']).strftime('%Y-%m-%d %H:%M')

# Format numbers
formatted_usd = f"{usd_rate:.2f}"
rub_example = f"{10 * usd_rate:.2f}"
usd_example = f"{1000 / usd_rate:.2f}"

readme_content = f"# USD Exchange Rate from CBR\n\n"
readme_content += f"**Last update:** {date} (MSK)\n"
readme_content += f"**1 USD → {formatted_usd} RUB**\n\n"
readme_content += "### Conversion examples:\n"
readme_content += f"- 10$ = {rub_example}RUB\n"
readme_content += f"- 1000RUB = {usd_example}$\n\n"
readme_content += "<sup>Data: [CBR](https://www.cbr.ru/development/SXML/) • "
readme_content += "Auto-updated on script run</sup>"


with open("README.md", "w", encoding="utf-8") as file:
	file.write(readme_content)
