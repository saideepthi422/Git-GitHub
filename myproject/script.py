#yaml
name: Run Python Script
on: [push]
jobs:
  run:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v3
- name: Setup Python
        uses: actions/setup-python@v3
        with:
          python-version: '3.8'
- name: Run script
        run: python script.py

