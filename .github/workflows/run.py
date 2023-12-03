name: Telegram bot ⚡
on:
  push:
    branches:
      - master
    workflow_dispatch:
  schedule:
    - cron: "0 */5 * * *"
jobs:
  Learning-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout code
        uses: actions/checkout@v2

      - name: Set up Python environment
        uses: actions/setup-python@v2

      - name: Install dependencies
        run: |
          python3 -m pip install --upgrade pip
          pip3 install -r requirements.txt

      - name: Execute Python script
        run: python3 PunyaChael/__main__.py
        
