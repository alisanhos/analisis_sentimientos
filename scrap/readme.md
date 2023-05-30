# Project Documentation
## To Scrape Tweets:
1. Create a virtual environment (venv) and activate it. You can use the following commands in PowerShell/CMD:

```bash
python -m venv myenv      # Create a virtual environment named "myenv"

myenv\Scripts\activate   # Activate the virtual environment
```
 2. Install the project dependencies by running the following command inside the activated virtual environment:

```bash
pip install -r requirements.txt
```
3. Once the dependencies are installed, the project is ready to run. Open the _main.py file and make the following modifications:

3.1.  Adjust the amount of tweets to scrape.
Specify the target users from whom you want to scrape the tweets.

```python
# Modify the following variables according to your requirements
scrape_tweets("username", amount)    # Change username and amount to scrap
```
4. Save the changes and run the _main.py script using the command:

```bash
python _main.py
```
The script will start scraping tweets from the specified users and store the data for further processing.